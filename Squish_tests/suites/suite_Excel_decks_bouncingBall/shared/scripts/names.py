# encoding: UTF-8

from objectmaphelper import *

Hyperlink_Excel_Deck = {"text": "Deck_Excell.xlsx", "type": "Hyperlink"}
ecosimPro_TabItem = {"text": "EcosimPro", "type": "TabItem"}
open_Button = {"text": "Open", "type": "Button"}
addReportSheet_Button = {"text": "Add report sheet", "type": "Button"}
play_Button = {"text": "Play", "type": "Button"}
Aceptar_Button = {"text": "Aceptar", "type": "Button"}

createReportSheet_Dialog = {"text": "Create report sheet...", "type": "Dialog"}
createReportSheet_ListView = {"container": createReportSheet_Dialog, "type": "ListView"}
hOptionListView_ListViewItem = {"container": createReportSheet_ListView, "text": "h", "type": "ListViewItem"}

deckGUI_excelWindow = {"text": "Deck_Excell.xlsx - Excel", "type": "Window"}
deckGUI_excelWorkbook = {"container": deckGUI_excelWindow, "type": "Workbook"}
deckGUI_Table = {"container": deckGUI_excelWorkbook, "occurrence": 3, "type": "Table"}
example_cloumn = {"column": 1, "container": deckGUI_Table, "row": 2, "type": "TableCell"}
deck_Excell_xlsx_Excel_Window = {"text": "Deck_Excell.xlsx - Excel", "type": "Window"}
deck_Excell_xlsx_Excel_Workbook = {"container": deck_Excell_xlsx_Excel_Window, "type": "Workbook"}

