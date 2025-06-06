from pywinauto import Desktop, Application
#from pywinauto.application import Application
#from pywinauto.Desktop import Desktop

path_firefox = "C:/Program Files/Mozilla Firefox/firefox.exe"

firefox = Application(backend='uia')

firefox.start(path_firefox + '--force-renderer-accessibility --incognito --start-maximized '
			  'https://www.ucm.es/')

