# encoding: UTF-8

from objectmaphelper import *

import Names.Names_Global as Global_names

app_newPersonButton = {"name": "m_newPersonButton", "type": "QPushButton", "visible": 1, "window": Global_names.main_APP_window}
app_personDataWidget = {"name": "m_personListWidget", "type": "QListWidget", "visible": 1, "window": Global_names.main_APP_window}

app_newPersonDialog = {"name": "APP_newPersonClass", "type": "APP_newPerson", "visible": 1}
app_nameQLine = {"name": "m_nameQLine", "type": "QLineEdit", "visible": 1, "window": app_newPersonDialog}
app_surNameQLine = {"name": "m_surnameQLine", "type": "QLineEdit", "visible": 1, "window": app_newPersonDialog}
app_ageQLine = {"name": "m_ageQLine", "type": "QLineEdit", "visible": 1, "window": app_newPersonDialog}
app_sexComboBox = {"name": "m_sexComboBox", "type": "QComboBox", "visible": 1, "window": app_newPersonDialog}
app_parentComboBox = {"name": "m_parentComboBox", "type": "QComboBox", "visible": 1, "window": app_newPersonDialog}
app_okButton = {"name": "m_okButton", "type": "QPushButton", "visible": 1, "window": app_newPersonDialog}
app_cancelButton = {"name": "m_cancelButton", "type": "QPushButton", "visible": 1, "window": app_newPersonDialog}

app_QMessage = {"type": "QMessageBox", "unnamed": 1, "visible": 1, "windowTitle": "Error"}
aPP_windowClass_APP_window = {"name": "APP_windowClass", "type": "APP_window", "visible": 1}

tree_qt = {"name": "m_personTreeView", "type": "QTreeView", "visible": 1, "window": aPP_windowClass_APP_window}
