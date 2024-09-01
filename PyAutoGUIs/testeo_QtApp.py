import pyautogui
import time

time.sleep(5)
print(pyautogui.position()) 

pyautogui.click(1148, 755)#New person posicion
time.sleep(0.1)
pyautogui.click(960, 592)#OK del new person
time.sleep(0.1)
pyautogui.click(1070, 546)#OK de warnning
time.sleep(0.1)
pyautogui.click(980, 449)#name QLine
time.sleep(0.1)
pyautogui.write('Tomas', interval=0.25)
pyautogui.click(987, 476)#surName QLine
time.sleep(0.1)
pyautogui.write('Gimenez', interval=0.25)
pyautogui.click(980, 506)#Age QLine
time.sleep(0.1)
pyautogui.write('24', interval=0.25)
pyautogui.click(998, 536)#Sex QCombobox
time.sleep(0.1)
pyautogui.click(960, 567)#Sex QCombobox Male
time.sleep(0.1)
pyautogui.click(994, 559)#Parent QCombobox
time.sleep(0.1)
pyautogui.click(993, 583)#Parent QCombobox No parent
time.sleep(0.1)
pyautogui.click(960, 592)#OK del new person
time.sleep(0.1)

print(pyautogui.position()) 


#pyautogui.click('./QtPNG/newPerson.png')