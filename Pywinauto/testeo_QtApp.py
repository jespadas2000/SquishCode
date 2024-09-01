from pywinauto.application import Application


app = Application(backend="uia").start('C:/Users/Jesus/Desktop/TFM/otros_test/Basic_App/x64/Release/Basic_App.exe')
dlgmain = app.top_window()
dlgmain["New Person"].click()

dlNewPerson= app.window(title='New Person')

dlNewPerson["OK"].click()
dlNewPerson["Cerrar"].click()
dlNewPerson["Cancel"].click()

dlgmain["New Person"].click()
dlNewPerson.print_control_identifiers()
dlNewPerson.Edit0.type_keys("1234", with_spaces=True)
if dlNewPerson.Edit0.window_text() != "":
	print("Error unexpected text, the text found was: "+dlNewPerson.Edit0.window_text())

dlNewPerson.Edit2.type_keys("1234", with_spaces=True)
if dlNewPerson.Edit2.window_text() != "":
	print("Error unexpected text, the text found was: "+dlNewPerson.Edit2.window_text())

dlNewPerson.Edit3.type_keys("abcd", with_spaces=True)
if dlNewPerson.Edit3.window_text() != "":
	print("Error unexpected text, the text found was: "+dlNewPerson.Edit3.window_text())

dlNewPerson.Edit0.type_keys("__a", with_spaces=True)
if dlNewPerson.Edit0.window_text() != "a":
	print("Error unexpected text, the text found was: "+dlNewPerson.Edit0.window_text())

dlNewPerson.Edit2.type_keys("__b", with_spaces=True)
if dlNewPerson.Edit2.window_text() != "b":
	print("Error unexpected text, the text found was: "+dlNewPerson.Edit2.window_text())

dlNewPerson.Edit3.type_keys("__1", with_spaces=True)
if dlNewPerson.Edit3.window_text() != "1":
	print("Error unexpected text, the text found was: "+dlNewPerson.Edit3.window_text())

dlNewPerson.Edit0.type_keys("[]+*`^:.;,<>!$%&/()=?¿¡", with_spaces=True)
if dlNewPerson.Edit0.window_text() != "a":
	print("Error unexpected text, the text found was: "+dlNewPerson.Edit0.window_text())

dlNewPerson.Edit2.type_keys("[]+*`^:.;,<>!$%&/()=?¿¡", with_spaces=True)
if dlNewPerson.Edit2.window_text() != "b":
	print("Error unexpected text, the text found was: "+dlNewPerson.Edit2.window_text())

dlNewPerson.Edit3.type_keys("[]+*`^:.;,<>!$%&/()=?¿¡", with_spaces=True)
if dlNewPerson.Edit3.window_text() != "1":
	print("Error unexpected text, the text found was: "+dlNewPerson.Edit3.window_text())

dlNewPerson["Cancel"].click()
dlgmain["Exit"].click()


#dlNewPerson.print_control_identifiers()

#dlNewPerson["m_sexComboBox"].Edit.type_keys("pywinauto works!", with_spaces=True)
#dlNewPerson.Edit0.type_keys("Hola", with_spaces=True)





#dlNewPerson.comboBox0.type_keys('{DOWN}{ENTER}')
#dlNewPerson.comboBox1.type_keys('{DOWN}{ENTER}')
#dlNewPerson.comboBox2.type_keys('{DOWN}{ENTER}')

#dlNewPerson.ComboBox.select(0)
#dir(dlNewPerson)
#dlNewPerson.print_control_identifiers()
#dlNewPerson.APP_newPersonClass.m_sexComboBox.select("Male")
#print(dlNewPerson.comboBox1.ListBox.texts())
#print(dlNewPerson.comboBox2.ListBox.texts())

#dlNewPerson.ListBox[0]['Pedro Gutierrez'].select()

#dlNewPerson['comboBox0'].type_keys('{DOWN}')
#dlNewPerson['comboBox0'].select("Male")
#dlNewPerson.comboBox1.select("Male")
#dlNewPerson.comboBox2.select("Male")

#dlNewPerson.comboBox0.select("Pedro Gutierrez")
#dlNewPerson.comboBox1.select("Pedro Gutierrez")
#dlNewPerson.comboBox2.select("Pedro Gutierrez")

#dlNewPerson.ListBox0.type_keys('{DOWN}{ENTER}')
#dlNewPerson.ListBox1.type_keys('{DOWN}{ENTER}')

#dlNewPerson.Properties.print_control_identifiers()

#dlNewPerson["m_nameQLine"].type("Hello", with_spaces=True, with_newlines=True, pause=0.5, with_tabs=True)
#dlNewPerson["Cancel"].click()

#dlg["Exit"].click()