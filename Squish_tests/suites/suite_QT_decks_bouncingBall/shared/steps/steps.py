# -*- coding: utf-8 -*-

# A quick introduction to implementing scripts for BDD tests:
#
# This file contains snippets of script code to be executed as the .feature
# file is processed. See the section 'Behaviour Driven Testing' in the 'API
# Reference Manual' chapter of the Squish manual for a comprehensive reference.
#
# The decorators Given/When/Then/Step can be used to associate a script snippet
# with a pattern which is matched against the steps being executed. Optional
# table/multi-line string arguments of the step are passed via a mandatory
# 'context' parameter:
#
#   @When("I enter the text")
#   def whenTextEntered(context):
#      <code here>
#
# The pattern is a plain string without the leading keyword, but a couple of
# placeholders including |any|, |word| and |integer| are supported which can be
# used to extract arbitrary, alphanumeric and integer values resp. from the
# pattern; the extracted values are passed as additional arguments:
#
#   @Then("I get |integer| different names")
#   def namesReceived(context, numNames):
#      <code here>
#
# Instead of using a string with placeholders, a regular expression can be
# specified. In that case, make sure to set the (optional) 'regexp' argument
# to True.

import names
import Funtions.Funtions_Global as fg
import Names.Names_Global as Global_names
import builtins

saveMode = False

@Given("the attachment of the program in Squish")
def step(context):
    attachToApplication(fg.TOOL_QTDECKS)
    
@Given("the program is launched")
def step(context):
    fg.launchExtTool("startaut.exe --port=5050 "+ fg.PROGRAM_PATH_QT_DECKS+"/"+fg.TOOL_QTDECKS + " SQUISH_TESTING", True)
    
@Given("the program is ready for testing")
def step(context):
    snooze(1)
    attachToApplication(fg.TOOL_QTDECKS)
    waitForObjectExists(names.dKG_groupBox, 50000)

@Then("close the program")
def step(context):
    keyPress("<Alt>")
    keyPress("<F4>")
    keyRelease("<Alt>")
    keyRelease("<F4>")
    
           
@When("no custom deck is created")
def step(context):
    clickButton(waitForObject(names.dKG_DeleteCaseQPushButton))
    snooze(2)
    if object.exists(names.delete_QMessageBox):
        clickButton(waitForObject(names.yes_deleteQMessageBox))
    
@Then("create a new custom deck")
def step(context):
    clickButton(waitForObject(names.dKG_AddCaseCustomQPushButton))
    
@Then("the h input is set to '|any|'")
def step(context, setData):
    waitForObject(names.dKG_inputDataQTableWidget)
    inputTable = waitForObject(names.dKG_hDataInput)
    inputTable.selectAll()
    inputTable.backspace()
    type(inputTable, setData)
    type(inputTable, "<Return>")
    
@When("the deck is play")
def step(context):
    clickButton(waitForObject(names.dKG_playButton))
    
@When("the deck finish")
def step(context):
    fg.waitForPropertyValue(names.dKG_timeQLine, "text", "14.6778815", 60000)
    
@Then("the output data is the same of the file '|any|'")
def step(context, selectedFile):
    tableStatus = findObject(names.dKG_outputDataQTableWidget)
    dataList = []
    dataFile = []
    if not saveMode:
        File = open(os.path.abspath(INFO_PATH+"/"+selectedFile), "r")
        dataFile = File.read().split("\n")
    for i in range(233):
        dataItem = tableStatus.item(i,5).data(0) 
        if not saveMode:
            if str(dataItem) not in dataFile:
                test.fail("ERROR: Unexpected data at line "+str(i))
        else:
            dataList.append(dataItem)
    
    if saveMode:     
        SaveFile(selectedFile, dataList) 