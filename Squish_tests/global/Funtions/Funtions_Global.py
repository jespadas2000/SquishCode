import os
import squish as sq

TOOL_NAME = "Basic_App"
TOOL_QTDECKS = "dkg_win64_vcr1.exe"
TOOL_Ecosimpro = "EcosimPro.exe"
TOOL_EXCEL = "EXCEL"
#"Deck_GUI"

TMP_PATH = "../../../tmp"
INFO_PATH = "../../../SavedInfo"

PROGRAM_PATH_INSTALL = "Path/to/QtProgram"
PROGRAM_PATH_QT_DECKS = "Path/to/QtDeck"
PROGRAM_PATH_ECOSIMPRO = "Path/to/EcosimPro"
PROGRAM_PATH_EXCEL_BOUNCINGBALL = "Path/to/excel"

def regAppInServer(appName : str, path : str, add : bool):
    option = ""
    
    if add:
        option = "addAUT"
    else:
        option = "removeAUT"

    system_call = "squishserver --config " + option + " \"" + appName + "\" \"" +  path + "\""
    os.system( system_call )
    
def regAttachableAppInServer(appName : str, port : str, add : bool):
    option = ""
    
    if add:
        option = "addAttachableAUT"
    else:
        option = "removeAttachableAUT"

    system_call = "squishserver --config " + option + " " + appName + " localhost:" + port
    os.system( system_call )
    
def launchExtTool(system_call : str, unattended : bool = False):
    
    if unattended:
        system_call = "start /b " + system_call 
    
    os.system( system_call )
    
    
def waitForPropertyValue(objectName, propertyName, expectedValue, timeoutInMilliseconds):
    """Waits for property value of an already existing object"""
    condition = "sq.findObject({}).".format(objectName) + propertyName + " == expectedValue";
    return sq.waitFor(condition, timeoutInMilliseconds);

def SaveFile(fileName, datalist):   
    
    newpath = os.path.abspath(INFO_PATH)
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        
    f = open(os.path.abspath(INFO_PATH+"/"+fileName), "w")
    
    for data in datalist:
        f.write(str(data)+"\n")
        
def LETContexMenuTextToObject(contexOptionText): #Pensar en generalizar para  mas menus contextuales y cambiarle el nombre.
    
    contextualMenu = {"type": "QMenu", "visible":1}
    if contexOptionText =="Simulate":
        return {"container":contextualMenu ,"objectName":"experimentItemSimulateAction",  "type": "QAction"}
    elif contexOptionText =="Simulate in Monitor":
        return {"container":contextualMenu ,"text":"Simulate in Monitor",  "type": "QAction"}
    elif contexOptionText == "Export Experiment to C++ for Debugging ...":
        return {"objectName":"action_CPGDebuggingNewContextual",  "type": "QAction"}  
    elif contexOptionText == "Export Experiment to Create a C++ Program ...":
        return {"objectName":"action_CPGExampleNewContextual",  "type": "QAction"}  
    return ""
        
