# encoding: UTF-8

from objectmaphelper import *

kGI_menu = {"name": "KGI_menu", "type": "KGI_menu", "visible": 1}
kGI_menu_ECWdockWidget = {"name": "m_workspaceDockWidget", "type": "ECW_dockWidget", "visible": 1, "window": kGI_menu}
kGI_dockWidgetContentsQWidget = {"container": kGI_menu_ECWdockWidget, "name": "dockWidgetContents", "type": "QWidget", "visible": 1}

wksDockWidget = {"name": "m_workspaceDockWidget", "type": "ECW_dockWidget", "visible": 1, "window": kGI_menu}
wksDockWidgetSplitter = {"container": wksDockWidget, "name": "m_dockSplitter", "type": "QSplitter", "visible": 1}
wksTreeWidget = {"container": wksDockWidgetSplitter, "name": "m_workspaceTreeWidget", "type": "WKS_treeWidget", "visible": 1}

dockSplitter_QStackedWidget = {"container": wksDockWidgetSplitter, "name": "m_librariesStack", "type": "QStackedWidget", "visible": 1}
librariesStack_QStackedWidget = {"container": dockSplitter_QStackedWidget, "name": "qt_tabwidget_stackedwidget", "type": "QStackedWidget", "visible": 1}
tabWork_QWidget = {"container": librariesStack_QStackedWidget, "name": "tabWork", "type": "QWidget", "visible": 1}
treeView_lFTtreeView = {"container": tabWork_QWidget, "name": "m_treeView", "type": "LFT_treeView", "visible": 1}

lbtWidget = {"container": wksDockWidgetSplitter, "name": "m_librariesStack", "type": "QStackedWidget", "visible": 1}
lbtWidgetTabBar = {"container": lbtWidget, "name": "qt_tabwidget_tabbar", "type": "QTabBar", "visible": 1}
lbtWidgetTabBarExperiments = {"container": lbtWidgetTabBar, "index": 2, "type": "TabItem"}

dKA_assistant = {"name": "DKA_assistant", "type": "DKA_assistant", "visible": 1}
dKA_assistant_splitter2 = {"name": "splitter_2", "type": "QSplitter", "visible": 1, "window": dKA_assistant}
dKA_assistant_QStackedWidget = {"container": dKA_assistant_splitter2, "name": "m_QStackedWidget", "type": "QStackedWidget", "visible": 1}
dKA_assistant_stackedwidgetQStackedWidget = {"container": dKA_assistant_QStackedWidget, "name": "qt_tabwidget_stackedwidget", "type": "QStackedWidget", "visible": 1}
dKA_assistant_tabHelpQWidget = {"container": dKA_assistant_stackedwidgetQStackedWidget, "name": "tabHelp", "type": "QWidget", "visible": 1}
dKA_assistant_scrollArea2 = {"container": dKA_assistant_tabHelpQWidget, "name": "scrollArea_2", "type": "QScrollArea", "visible": 1}
dKA_assistant_groupBox2 = {"container": dKA_assistant_scrollArea2, "name": "groupBox_2", "type": "QGroupBox", "visible": 1}
dKA_assistant_deckNameLineEdit = {"container": dKA_assistant_groupBox2, "name": "m_infoNameText", "type": "ECW_lineEdit", "visible": 1}
dKA_assistant_groupBoxType = {"container": dKA_assistant_scrollArea2, "name": "m_groupBoxType", "type": "QGroupBox", "visible": 1}
dKA_assistant_comboBoxType = {"container": dKA_assistant_groupBoxType, "name": "m_comboBoxType", "type": "QComboBox", "visible": 1}
dKA_assistant_generateButton = {"name": "m_QPushButton_generate", "type": "QPushButton", "visible": 1, "window": dKA_assistant}
dKA_assistant_nameLineEdit = {"container": dKA_assistant_groupBox2, "name": "m_infoNameText", "type": "ECW_lineEdit", "visible": 1}

dKA_assistant_splitter2 = {"container": dKA_assistant_splitter2, "name": "m_listWidgetWorkflow", "type": "QListWidget", "visible": 1}
dKA_assistant_splitterVariableSection = {"container": dKA_assistant_splitter2, "text": "Variable Selection", "type": "QModelIndex"}
dKA_assistant_tabVarsQWidget = {"container": dKA_assistant_stackedwidgetQStackedWidget, "name": "tabVars", "type": "QWidget", "visible": 1}
dKA_assistant_dataTreewidget = {"container": dKA_assistant_tabVarsQWidget, "name": "m_treeVars", "type": "QTreeWidget", "visible": 1}

tabwidget_QWidget = {"container": librariesStack_QStackedWidget, "name": "tabCompiledItems", "type": "QWidget", "visible": 1}
treeView_lETtreeView = {"container": tabwidget_QWidget, "name": "m_treeView", "type": "LET_treeView", "visible": 1}

kGI_menu_mdi_main_WND_mdiArea = {"name": "mdi_main", "type": "WND_mdiArea", "visible": 1, "window": kGI_menu}
mdi_main_m_graphicsView_GCV_view = {"container": kGI_menu_mdi_main_WND_mdiArea, "name": "m_graphicsView", "type": "GCV_view", "visible": 1}
m_graphicsView_QGraphicsItem = {"acceptDrops": "no", "container": mdi_main_m_graphicsView_GCV_view, "enabled": "yes", "focusable": "no", "lineColor": "#000000", "movable": "no", "selectable": "no", "type": "QGraphicsItem", "userType": 109, "visible": "yes"}
o_QGraphicsItemGroup = {"acceptDrops": "no", "container": m_graphicsView_QGraphicsItem, "enabled": "yes", "focusable": "no", "lineColor": "#000000", "movable": "no", "selectable": "no", "type": "QGraphicsItemGroup", "visible": "yes"}
o_QGraphicsItem = {"acceptDrops": "no", "container": o_QGraphicsItemGroup, "enabled": "yes", "focusable": "no", "lineColor": "#000000", "movable": "no", "selectable": "no", "type": "QGraphicsItem", "userType": 111, "visible": "yes"}
o_QGraphicsItemGroup_2 = {"acceptDrops": "no", "container": o_QGraphicsItem, "enabled": "yes", "focusable": "no", "lineColor": "#000000", "movable": "no", "selectable": "no", "type": "QGraphicsItemGroup", "visible": "yes"}
o_b_Port_b_e_n_br_b_Type_b_PORTS_LIB_elec_br_b_Direction_b_IN_br_b_Current_cardinality_b_1_br_b_Minimum_cardinality_b_0_br_b_Maximum_cardinality_b_INT_MAX_QGraphicsItem = {"acceptDrops": "no", "container": o_QGraphicsItemGroup_2, "enabled": "yes", "focusable": "no", "lineColor": "#000000", "movable": "no", "selectable": "no", "toolTip": "<b>Port:</b> e_n<br><b>Type:</b> PORTS_LIB.elec<br><b>Direction:</b> IN<br><b>Current cardinality:</b> 1<br><b>Minimum cardinality:</b> 0<br><b>Maximum cardinality:</b> INT_MAX", "type": "QGraphicsItem", "userType": 112, "visible": "yes"}
m_graphicsView_QGraphicsItem_2 = {"acceptDrops": "no", "container": mdi_main_m_graphicsView_GCV_view, "enabled": "yes", "focusable": "no", "lineColor": "#000000", "movable": "no", "selectable": "no", "type": "QGraphicsItem", "userType": 122, "visible": "yes"}
m_attDock_1_ATT_dockWidget = {"name": "m_attDock_1", "type": "ATT_dockWidget", "visible": 1}
m_attDock_1_m_webSplitter_QSplitter = {"container": m_attDock_1_ATT_dockWidget, "name": "m_webSplitter", "type": "QSplitter", "visible": 1}
m_webSplitter_m_splitterTree_QSplitter = {"container": m_attDock_1_m_webSplitter_QSplitter, "name": "m_splitterTree", "type": "QSplitter", "visible": 1}
m_splitterTree_m_tableView_ATT_edsTableView = {"container": m_webSplitter_m_splitterTree_QSplitter, "name": "m_tableView", "type": "ATT_edsTableView", "visible": 1}
