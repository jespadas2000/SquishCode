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
    fg.launchExtTool("startaut.exe --port=5050 "+ fg.PROGRAM_PATH_QT_DECKS_Circuit+"/"+fg.TOOL_QTDECKS + " SQUISH_TESTING", True)
    
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
        
@Then("the h input is set to '|any|'")
def step(context, setData):
    waitForObject(names.dKG_inputDataQTableWidget)
    inputTable = waitForObject(names.dKG_HzDataInput)
    inputTable.selectAll()
    inputTable.backspace()
    type(inputTable, setData)
    type(inputTable, "<Return>")        
        
@Then("create a new custom deck")
def step(context):
    clickButton(waitForObject(names.dKG_AddCaseCustomQPushButton))
    
@When("the deck is play")
def step(context):
    clickButton(waitForObject(names.dKG_playButton))
    
@When("the deck finish")
def step(context):
    fg.waitForPropertyValue(names.dKG_timeQLine, "text", "14.6778815", 10000)
    
@Then("the output data is the same of the file '|any|' of the colunm C.e_n.v(V)")
def step(context, selectedFile):
    tableStatus = findObject(names.dKG_outputDataQTableWidget)
    dataList = []
    dataFile = []
    if not saveMode:
        File = open(os.path.abspath(INFO_PATH+"/"+selectedFile), "r")
        dataFile = File.read().split("\n")
    for i in range(200):
        dataItem = tableStatus.item(i,5).data(0)  
        if not saveMode:
            if str(dataItem) not in dataFile:
                test.fail("ERROR: Unexpected data at line "+str(i))
        else:
            dataList.append(dataItem)
    
    if saveMode:     
        SaveFile(selectedFile, dataList) 
        
@Then("the output data is the same of the file '|any|' of the colunm VAC.v(V)")
def step(context, selectedFile):
    tableStatus = findObject(names.dKG_outputDataQTableWidget)
    dataList = []
    dataFile = []
    if not saveMode:
        File = open(os.path.abspath(INFO_PATH+"/"+selectedFile), "r")
        dataFile = File.read().split("\n")
    for i in range(200):
        dataItem = tableStatus.item(i,6).data(0)  
        if not saveMode:
            if str(dataItem) not in dataFile:
                test.fail("ERROR: Unexpected data at line "+str(i))
        else:
            dataList.append(dataItem)
    
    if saveMode:     
        SaveFile(selectedFile, dataList) 