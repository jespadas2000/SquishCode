import Funtions.Funtions_Global as fg
import Names.Names_Global as Global_names

@Given("the attachment of the program in Squish")
def step(context):
    attachToApplication(fg.TOOL_NAME)
    
@Given("the program is launched")
def step(context):
    fg.launchExtTool("startaut.exe --port=5050 "+ fg.PROGRAM_PATH_INSTALL+"/"+fg.TOOL_NAME + " SQUISH_TESTING", True)
    
@Given("the program is ready for testing")
def step(context):
    snooze(1)
    attachToApplication(fg.TOOL_NAME)
    waitForObjectExists(Global_names.treeView_person, 100000)
    
@Given("the deletion of the tmp directory with the aim of emptying the previous contents") 
def step(context): 
    if os.path.exists(os.path.abspath(fg.TMP_PATH)):
        if fg.PROGRAM_PATH_QT_DECKS[len(fg.TMP_PATH) - 3:]=="tmp":
            os.system("rmdir /s /q "+os.path.abspath(fg.TMP_PATH))
            
@Then("close the program")
def step(context):
    clickButton(waitForObject(Global_names.app_exitButton))
    
@Given("the creation of a new tmp directory")
def step(context):
    if fg.TMP_PATH[len(fg.TMP_PATH) - 3:] == "tmp" :
        if not os.path.exists(os.path.abspath(fg.TMP_PATH)):
           os.mkdir(fg.TMP_PATH, 0o777)
           
@Given("the creation of a new info path directory")
def step(context):
    if fg.INFO_PATH[len(fg.INFO_PATH) - 3:] == "tmp" :
        if not os.path.exists(os.path.abspath(fg.INFO_PATH)):
           os.mkdir(fg.INFO_PATH, 0o777)