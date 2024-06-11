# -*- coding: utf-8 -*-

import names
import Names.Names_Global as Global_names


@Then("open the new person dialog")
def step(context):
    clickButton(waitForObject(names.app_newPersonButton))
    
@Then("the ok button is pressed")
def step(contex):
    clickButton(waitForObject(names.app_okButton))
    
@Then("the cancel button is pressed")
def step(contex):
    clickButton(waitForObject(names.app_cancelButton))

@Then("a QMessage appears")
def step(context):
    okMessageButton = {"text": "OK", "type": "QPushButton", "container": names.app_QMessage}
    clickButton(waitForObject(okMessageButton))
    
@When("'|any|' has been written in the name parameter")
def step(contex, selectedName):
    type(waitForObject(names.app_nameQLine), selectedName)
    
@When("'|any|' has been written in the surname parameter")
def step(contex, selectedSurName):
    type(waitForObject(names.app_surNameQLine), selectedSurName)
    
@When("'|any|' has been written in the age parameter")
def step(context, selectedAge):
    type(waitForObject(names.app_ageQLine), selectedAge)
    
@When("'|any|' has been written in the sex parameter")
def step(context, selectedSex):
    waitForObject(names.app_sexComboBox)
    comboBox = findObject(names.app_sexComboBox)
    
    for n in range(comboBox.count):
        if comboBox.itemText(n) == selectedSex:
            comboBox.setCurrentIndex(n)
            
@When("'|any|' has been written in the parent parameter")
def step(context, selectedParent):
    waitForObject(names.app_parentComboBox)
    comboBox = findObject(names.app_parentComboBox)
    
    for n in range(comboBox.count):
        if comboBox.itemText(n) == selectedParent:
            comboBox.setCurrentIndex(n)
            
@Then("'|any|' with age '|any|' sex '|any|' and '|any|' as parent")
def step(context, selectedPersons, selectedAge, selectedSex, selectedParent):
    snooze(1)
    
    personTreeView = findObject(Global_names.treeView_person)
    treeModel = personTreeView.model()
    
    listNames = selectedPersons.split(">")
    
    personItem = QModelIndex()
    father = Global_names.treeView_person
    subItem = {}
    itemName = ""
    itemSurName= ""
    
    for person in listNames:
        for row in range(treeModel.rowCount(QModelIndex())):
            PersonIndex = treeModel.index(row, 1, personItem)
            itemSurName = PersonIndex.data(Qt.DisplayRole).toString()
            PersonIndex = treeModel.index(row, 0, personItem)
            itemName = PersonIndex.data(Qt.DisplayRole).toString()  
            if str(itemName)+" "+str(itemSurName) == person:
                personItem = PersonIndex
                subItem = {"column": 0, "container": father, "text": itemName, "type": "QModelIndex"} 
                mouseClick(waitForObject(subItem), -1, 9, Qt.NoModifier, Qt.LeftButton)
                snooze(1)
                personTreeView = waitForObject(subItem)
                treeModel = personTreeView.model()
                father = subItem
                break
    
    treePerson = waitForObject(subItem)
    mouseClick(treePerson, 0, 0, Qt.NoModifier, Qt.LeftButton)

    personData = findObject(names.app_personDataWidget)
    
    if(str(personData.item(0).data(Qt.DisplayRole).toString()) == "Name: "+ str(itemName) and 
       str(personData.item(1).data(Qt.DisplayRole).toString()) == "Sur name: "+ str(itemSurName) and 
       str(personData.item(2).data(Qt.DisplayRole).toString()) == "Age: "+ str(selectedAge) and 
       str(personData.item(3).data(Qt.DisplayRole).toString()) == "Sex: "+ str(selectedSex) and
       str(personData.item(4).data(Qt.DisplayRole).toString()) == "Parent: "+ str(selectedParent)):
        test.passes("PASS: The person "+str(itemName)+" "+str(itemSurName)+" was found in the tree")
    else:
        test.fail("ERROR: The person "+str(itemName)+" "+str(itemSurName)+" was not found in the tree")
    

@Then("the name parameter contains '|any|'")
def step(context, textName):
    
    waitForObject(names.app_nameQLine)
    LineName = findObject(names.app_nameQLine)
    
    usedText = ""
    if textName != "NO TEXT":
        usedText = textName
    
    try:
        if LineName.text != usedText:
            test.fail("ERROR: Unexpected text in the name parameter")
        else:    
            test.passes("PASS: Same text detected in the name parameter")   
            
    except Exception:
        None  
        
    LineName.clear() 
    
@Then("the surname parameter contains '|any|'")
def step(context, textSurName):
    
    waitForObject(names.app_surNameQLine)
    LineSurName = findObject(names.app_surNameQLine)
    
    usedText = ""
    if textSurName != "NO TEXT":
        usedText = textSurName
    
    try:
        if LineSurName.text == usedText:
            test.passes("PASS: Same text detected in the name parameter")
        else:
            test.fail("ERROR: Unexpected text in the surname parameter")
            
    except Exception:
        None        

    LineSurName.clear() 
        
@Then("the age parameter contains '|any|'")
def step(context, textAge):
    
    waitForObject(names.app_ageQLine)
    LineAge = findObject(names.app_ageQLine)
    
    usedText = ""
    if textAge != "NO TEXT":
        usedText = textAge
    
    try:
        if LineAge.text == usedText:
            test.passes("PASS: Same text detected in the age parameter")
        else:
            test.fail("ERROR: Unexpected text in the age parameter")
            
    except Exception:
        None 
        
    LineAge.clear() 