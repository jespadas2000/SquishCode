# encoding: UTF-8

from objectmaphelper import *

o_Window = "[Window]"

ucm_BrowserTab = {"title": "Universidad Complutense de Madrid", "type": "BrowserTab"}
o_Pane = {"occurrence": 4, "text": "", "type": "Pane"}
o_Toolbar = {"container": o_Pane, "type": "Toolbar"}
atr_s_ToolbarItem = {"container": o_Toolbar, "text": "Atrás", "type": "ToolbarItem"}
ucm_EstudiarTab = {"container": ucm_BrowserTab, "simplifiedInnerText": "Universidad", "tagName": "A", "visible": True}
ucm_FacultadesTab = {"container": ucm_BrowserTab, "simplifiedInnerText": "Facultades", "tagName": "A", "visible": True}
ucm_BrowserFacultadesTab = {"title": "Facultades | Universidad Complutense de Madrid", "type": "BrowserTab"}
ucm_facultadInformatica = {"container": ucm_BrowserFacultadesTab, "simplifiedInnerText": "Informática", "tagName": "A", "visible": True}
ucm_informaticaBrowser = {"title": "Facultad de Informática", "type": "BrowserTab"}
ucm_informaticaSearch = {"container": ucm_informaticaBrowser, "form": "formbuscador", "id": "search", "name": "search", "tagName": "INPUT", "type": "search", "visible": True}
ucm_informaticaSearchSubmit = {"container": ucm_informaticaBrowser, "form": "formbuscador", "id": "btsearch", "tagName": "BUTTON", "type": "submit", "visible": True}
Inform_BrowserTabDOCUMENT = "{title='Facultad de Informática' type='BrowserTab'}.DOCUMENT.HTML1.BODY1.MAIN1.DIV2.DIV2.DIV2.DIV1.UL1"
Inform_resultadosDIV = {"container": ucm_informaticaBrowser, "occurrence": 3, "tagName": "DIV", "visible": True}
