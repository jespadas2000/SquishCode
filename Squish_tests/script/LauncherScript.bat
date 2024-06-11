start /b path\to\LaunchSquishserver.bat
timeout 5
Rem GUI testing for EcosimPro
"path\to\squishrunner.exe" --testsuite path\to\suite_QT_DeckCreation --reportgen html,path\to\data_creation.html
timeout 5
"path\to\squishrunner.exe" --testsuite path\to\suite_QT_decks_bouncingBall --reportgen html,path\to\data_Qt.html
timeout 5
start /b path\to\stop_LauncherScript.bat
timeout 3
start /b path\to\LauncherWindowsServer.bat
timeout 3
"path\to\squishrunner.exe" --testsuite path\to\suite_Excel_decks_bouncingBall --reportgen html,path\to\data_excel.html