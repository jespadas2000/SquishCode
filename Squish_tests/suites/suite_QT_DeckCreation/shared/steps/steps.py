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


@Given("the program is launched")
def step(context):
    fg.launchExtTool("startaut.exe --port=5050 "+ fg.PROGRAM_PATH_ECOSIMPRO+"/"+fg.TOOL_Ecosimpro + " SQUISH_TESTING", True)
  
    
@Given("the program is ready for testing")
def step(context):
    snooze(1)
    attachToApplication(fg.TOOL_Ecosimpro)
    waitForObjectExists(names.kGI_dockWidgetContentsQWidget, 100000)
    
@Given("the attachment of the program in Squish")
def step(context):
    attachToApplication(fg.TOOL_Ecosimpro)
    
@Then("close the program")
def step(context):  
    fileExitWksAction = findObject("{objectName='fileExitAction' type='QAction'}")
    activateItem(fileExitWksAction)
    yesQPushButton = {"text": "Yes", "type": "QPushButton", "unnamed": 1, "visible": 1}
    clickButton(waitForObject(yesQPushButton))
    
@When("the library '|any|' is selected")
def step(context, libName):   
    waitForObjectExists(names.wksTreeWidget, 5000)
    wksTreeWidget = sq.findObject(names.wksTreeWidget)
    treeModel = wksTreeWidget.model()
   
    #Get library to select in the tree
    libItem = sq.QModelIndex()
    wksRootItemIndex = treeModel.index(0, 0, sq.QModelIndex())
    for row in range(treeModel.rowCount(wksRootItemIndex)):
        libIndex = treeModel.index(row, 0, wksRootItemIndex)
        itemName = libIndex.data(sq.Qt.DisplayRole).toString()
        if itemName == libName :
            libItem = libIndex
            break
         
    #Get a QModelIndex wrapped by Squish for this QModelIndex:
    if libItem != sq.QModelIndex():
        wksTreeWidget.setCurrentIndex(libItem)
        test.passes("Library %s is correctly selected" %libName)
        sq.snooze(1)
        
@Then("the file tree is visible")
def step(context):
    snooze(1)
    waitForObjectExists(names.treeView_lETtreeView, 100000)
    
@When("the tab '|any|' is selected")
def step(context, selectedTab):
    
    if selectedTab == "item":
        mouseClick(waitForObject(names.lbtWidgetTabBarExperiments), 15, 15, Qt.NoModifier, Qt.LeftButton)
    else :
        test.fail("Error: an unexpected tab was selected")
        
    snooze(1)
    
@When("the action '|any|' in the file '|any|' is selected")
def step(context, fileAction, fileName):
    
    letTreeView = findObject(names.treeView_lETtreeView)
    treeModel = letTreeView.model()
    
    listNames = fileName.split(">")
    
    #get library to select in the tree
    fileItem = QModelIndex()
    father = names.treeView_lETtreeView
    subItem = {}
    for file in listNames:
        for row in range(treeModel.rowCount(QModelIndex())):
            fileIndex = treeModel.index(row, 0, fileItem)
            itemName = fileIndex.data(Qt.DisplayRole).toString()
            if itemName == file:
                fileItem = fileIndex
                subItem = {"column": 0, "container": father, "text": itemName, "type": "QModelIndex"} 
                mouseClick(waitForObject(subItem), -1, 9, Qt.NoModifier, Qt.LeftButton)
                snooze(1)
                letTreeView = waitForObject(subItem)
                treeModel = letTreeView.model()
                father = subItem
                break

    #Name of item
    openContextMenu(waitForObject(subItem), 15, 15, Qt.NoModifier)
    
    objectAction = fg.LETContexMenuTextToObject(fileAction)

    if "" == objectAction:
        objectAction = {"type": "QMenu", "unnamed": 1, "visible": 1}
        activateItem(waitForObjectItem(objectAction, fileAction))
    else:
        activateItem(waitForObject(objectAction))
        
    if "Delete" == fileAction:
       okButton = {"text": "Ok", "type": "QPushButton"}
       clickButton(waitForObject(okButton))
    snooze(1)
    
@Then("the type of the deck '|any|' is '|any|'")
def step(context, deckName, deckType):
    waitForObject(names.dKA_assistant_deckNameLineEdit)
    lineEdit = findObject(names.dKA_assistant_deckNameLineEdit)
    lineEdit.setText(deckName)
    
    comboBox = findObject(names.dKA_assistant_comboBoxType)
     
    for n in range(comboBox.count):
        if comboBox.itemText(n) == deckType:
            comboBox.setCurrentIndex(n)
            
@Then("press the Generate button")
def step(context):
    clickButton(waitForObject(names.dKA_assistant_generateButton))
    snooze(1)
    
@Then("press the Finish button")
def step(context):
    clickButton(waitForObject(names.dKA_assistant_generateButton))
       
@Then("the name of the deck is '|any|'")
def step(context, deckName):
    
    LineName = findObject(names.dKA_assistant_nameLineEdit)
    LineName.clear()
    type(waitForObject(names.dKA_assistant_nameLineEdit),deckName)

@When("the tab '|any|' is selected in deck creator")
def step(context, selectedTab):
    if selectedTab == "Variable Selection":
        mouseClick(waitForObject(names.dKA_assistant_splitterVariableSection))
    else :
        test.fail("Error: an unexpected tab was selected")
    
@Then("the variable '|any|' is '|any|'")
def step(context, selectedVariable, selectedOption ):
    
    waitForObject(names.dKA_assistant_dataTreewidget)
    tableTreeView = findObject(names.dKA_assistant_dataTreewidget)
    treeModel = tableTreeView.model()
    father = names.dKA_assistant_dataTreewidget
    
    for row in range(treeModel.rowCount(QModelIndex())):
        VaraibleIndex = treeModel.index(row, 0, QModelIndex())
        itemSurName = VaraibleIndex.data(Qt.DisplayRole).toString()
        if itemSurName == selectedVariable:
            if selectedOption == "Deck-In":
                itemName = treeModel.index(row, 1, QModelIndex()).data(sq.Qt.DisplayRole).toString()
                subItem = {"row": row, "column": 1, "container": father, "text": itemName, "type": "QModelIndex"}
                openContextMenu(waitForObject(subItem), 15, 15, Qt.NoModifier)
                snooze(1)
                menuAction = findObject("{objectName='qmenu_DeckVarSelectorContextualMain'  type= 'QMenu'}")
                activateItem(waitForObjectItem(menuAction, "Change Deck-In to"))
                objectAction = {"objectName":"action_DECKIN_PUBLIC",  "type": "QAction", "visible": 1}  
                activateItem(waitForObject(objectAction))
            elif selectedOption == "Deck-Out":
                itemName = treeModel.index(row, 2, QModelIndex()).data(sq.Qt.DisplayRole).toString()
                subItem = {"row": row, "column": 2, "container": father, "text": itemName, "type": "QModelIndex"}
                openContextMenu(waitForObject(subItem), 15, 15, Qt.NoModifier)
                snooze(1)
                menuAction = findObject("{objectName='qmenu_DeckVarSelectorContextualMain'  type= 'QMenu'}")
                activateItem(waitForObjectItem(menuAction, "Change Deck-Out to"))
                objectAction = {"objectName":"action_DECKOUT_PUBLIC",  "type": "QAction", "visible": 1}  
                activateItem(waitForObject(objectAction))
            else:
                test.fail("Error: an unexpected option was selected")
            


@Given("step test")
def step(context):
    mouseClick(waitForObject(names.o_b_Port_b_e_n_br_b_Type_b_PORTS_LIB_elec_br_b_Direction_b_IN_br_b_Current_cardinality_b_1_br_b_Minimum_cardinality_b_0_br_b_Maximum_cardinality_b_INT_MAX_QGraphicsItem), 0, 3, Qt.NoModifier, Qt.LeftButton)
    doubleClick(waitForObject(names.m_graphicsView_QGraphicsItem_2), 276, 306, Qt.NoModifier, Qt.LeftButton)
    test.vp("VP1")
