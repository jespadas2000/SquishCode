# encoding: UTF-8

from objectmaphelper import *

dKG_mainWndManaged = {"name": "DKG_mainWndManaged", "type": "DKG_mainWndManaged", "visible": 1}
dKG_mainWndManagedQSplitter = {"name": "m_splitter", "type": "QSplitter", "visible": 1, "window": dKG_mainWndManaged}
dKG_stackedwidgetQStackedWidget = {"container": dKG_mainWndManagedQSplitter, "name": "qt_tabwidget_stackedwidget", "type": "QStackedWidget", "visible": 1}
dKG_tabSimulationQWidget = {"container": dKG_stackedwidgetQStackedWidget, "name": "tabSimulation", "type": "QWidget", "visible": 1}
dKG_tabSimulationQSplitter = {"container": dKG_tabSimulationQWidget, "name": "splitter_2", "type": "QSplitter", "visible": 1}
dKG_groupBoxOutputQGroupBox = {"container": dKG_tabSimulationQSplitter, "name": "m_groupBoxOutput", "type": "QGroupBox", "visible": 1}
dKG_groupBox = {"container": dKG_tabSimulationQSplitter, "name": "groupBox", "type": "QGroupBox", "visible": 1}

dKG_DeleteCaseQPushButton = {"container": dKG_groupBox, "name": "m_pushButtonDeleteCase", "type": "QPushButton", "visible": 1}
dKG_AddCaseCustomQPushButton = {"container": dKG_groupBox, "name": "m_pushButtonAddCaseCustom", "type": "QPushButton", "visible": 1}

dKG_groupBox_stackedwidgetQStackedWidget = {"container": dKG_groupBox, "name": "qt_tabwidget_stackedwidget", "type": "QStackedWidget", "visible": 1}
dKG_QstackedwidgetDKGcalc = {"container": dKG_groupBox_stackedwidgetQStackedWidget, "name": "DKG_calc", "type": "DKG_calc", "visible": 1}
dKG_calcsplitterQSplitter = {"container": dKG_QstackedwidgetDKGcalc, "name": "splitter", "type": "QSplitter", "visible": 1}
dKG_inputDataQTableWidget = {"container": dKG_calcsplitterQSplitter, "name": "m_tableWidgetInputs", "type": "QTableWidget", "visible": 1}
dKG_hDataInput = {"container": dKG_inputDataQTableWidget, "type": "QLineEdit", "unnamed": 1, "visible": 1}
dKG_HzDataInput = {"container": dKG_inputDataQTableWidget, "occurrence": 3, "type": "QLineEdit", "unnamed": 1, "visible": 1}
dKG_outputDataQTableWidget = {"container": dKG_groupBoxOutputQGroupBox, "name": "m_tableWidgetStatus", "type": "QTableWidget", "visible": 1}

delete_QMessageBox = {"type": "QMessageBox", "unnamed": 1, "visible": 1, "windowTitle": "Delete calculation"}
dKG_playButton = {"text": "Play", "type": "QToolButton", "unnamed": 1, "visible": 1, "window": dKG_mainWndManaged}
dKG_timeQLine = {"container": dKG_groupBoxOutputQGroupBox, "name": "m_lcdTime", "type": "QLineEdit", "visible": 1}

delete_QMessageBox = {"type": "QMessageBox", "unnamed": 1, "visible": 1, "windowTitle": "Delete calculation"}
yes_deleteQMessageBox = {"text": "Yes", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": delete_QMessageBox}