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
import Funtions.Funtions_Global as fg
import names
import builtins

saveMode = False 

@Given("the attachment of the program in Squish")
def step(context):
    attachToApplication(fg.TOOL_EXCEL)
    
@Given("the program is launched")
def step(context):
    startApplication(fg.TOOL_EXCEL)
    
@When("the doc is open")
def step(context):
    mouseClick(waitForObject(names.Hyperlink_Excel_Deck))

@Then("select the EcosimPro tab")
def step(context):
    mouseClick(waitForObject(names.ecosimPro_TabItem))
    
@Then("open the model")
def step(context):
    mouseClick(waitForObject(names.open_Button))
    snooze(2)
    
@Then("add report sheet")
def step(context):
    snooze(2)
    keyPress("<Alt>")
    keyRelease("<Alt>")
    snooze(2)
    keyPress("<y>")
    keyRelease("<y>")
    keyPress("<2>")
    keyRelease("<2>")
    snooze(2)
    keyPress("<y>")
    keyRelease("<y>")
    keyPress("<8>")
    keyRelease("<8>")
    snooze(2)
    
@Then("create the sheet report with h parameter")
def step(context):
    mouseClick(waitForObject(names.hOptionListView_ListViewItem))
    mouseClick(waitForObject(names.hOptionListView_ListViewItem))
    
@Then("play the model")
def step(context):
    snooze(2)
    keyPress("<Alt>")
    keyRelease("<Alt>")
    snooze(2)
    keyPress("<y>")
    keyRelease("<y>")
    keyPress("<2>")
    keyRelease("<2>")
    snooze(2)
    keyPress("<y>")
    keyRelease("<y>")
    keyPress("<A>")
    keyRelease("<A>")
    snooze(4)
    
@When("the recommended graph options is selected")
def step(context):
    snooze(2)
    keyPress("<Alt>")
    keyRelease("<Alt>")
    snooze(2)
    keyPress("<B>")
    keyRelease("<B>")
    snooze(2)
    keyPress("<L>")
    keyRelease("<L>")
    keyPress("<S>")
    keyRelease("<S>")
    snooze(4)
    
@When("create the default graph")
def step(context):
    mouseClick(waitForObject(names.Aceptar_Button))
    snooze(2)
    
@Then("the graph is correctly created")
def step(contex):
    #test.imagePresent("image")
    test.vp("VP1")

@Then("the '|any|' data values of the column '|any|' are the same that in '|any|'")
def step(contex, numberData, selectedColumn, selectedFile):
    dataList = []
    dataFile = []
    size = builtins.int(numberData)
    column = builtins.int(selectedColumn)
    if not saveMode:
        File = open(os.path.abspath(fg.INFO_PATH+"/"+selectedFile), "r")
        dataFile = File.read().split("\n")
    for i in range(size):
        selectedCell = findObject({"column": column, "container": names.deckGUI_Table, "row": i+2, "type": "TableCell"})
        dataItem = selectedCell.text
        if not saveMode:
            if dataItem not in dataFile[i]:
                test.fail("ERROR: Unexpected data at line "+str(i))
        else:
            dataList.append(dataItem)
    
    if saveMode:     
        fg.SaveFile(selectedFile, dataList) 
