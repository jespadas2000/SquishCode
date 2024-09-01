from pywinauto.application import Application


app = Application(backend="uia").start('C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE')
dlgmain = app.top_window()
#dlgmain.print_control_identifiers()
dlgmain["Libro en blanco"].click()
