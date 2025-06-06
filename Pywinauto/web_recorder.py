# encoding: utf-8

from pywinauto_recorder.player import *


with UIPath(u"Barra de tareas||Pane"):
	with UIPath(u"Aplicaciones en ejecución||ToolBar"):
		click(u"Firefox||Button")

with UIPath(u"Mozilla Firefox||Window"):
	click(u"||Custom->||Pane->¿Hacer de Firefox su navegador principal?||Custom->Ahora no||Button")
	click(u"Área de navegación||ToolBar")
	send_keys("ucm.es""{ENTER}")

with UIPath(u"Universidad Complutense de Madrid — Mozilla Firefox||Window"):
	with UIPath(u"||Custom->||Pane->Universidad Complutense de Madrid||Document->||Group->||Group->||Menu"):
		click(u"Universidad||MenuItem")
		click(u"Universidad||MenuItem")

with UIPath(u"Facultades | Universidad Complutense de Madrid — Mozilla Firefox||Window"):
	with UIPath(u"||Custom->||Pane->Facultades | Universidad Complutense de Madrid||Document->||Group->||List"):
		drag_and_drop(u" Informática||ListItem", u" Informática||ListItem")

with UIPath(u"Facultad de Informática — Mozilla Firefox||Window"):
	with UIPath(u"||Custom->||Pane->Facultad de Informática||Document"):
		click(u"||Group#[0,0]")
		send_keys("conferencias""{ENTER}")
