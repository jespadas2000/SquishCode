from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:/Program Files/Mozilla Firefox/firefox.exe"
options = webdriver.FirefoxOptions()
options.binary_location = PATH
driver = webdriver.Firefox(options=options)

driver.get("https://www.ucm.es/")

time.sleep(10)

wait = WebDriverWait(driver, 10)

accept_botton = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Aceptar y cerrar')]")))

accept_botton.click()

time.sleep(1)



universidad_botton = driver.find_element(By.XPATH, "//a[text()='Universidad']")
universidad_botton.click()

time.sleep(1)

facultades_botton = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Facultades')]")))
facultades_botton.click()

time.sleep(1)

informatica_botton = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Informática')]")))
informatica_botton.click()

time.sleep(1)

search_editLine = wait.until(EC.presence_of_element_located((By.ID, "search")))
search_editLine.send_keys("conferencias")  

time.sleep(1)

search_editLine.send_keys(Keys.ENTER)

time.sleep(1)

found_total_text = driver.find_element(By.CLASS_NAME, "found_total").text

numero_texto = int(found_total_text[0])

lista_de_resultados = driver.find_element(By.CLASS_NAME, "found_list")

numero_hijos = lista_de_resultados.find_elements(By.XPATH, "./*")

numero_lista = len(numero_hijos)

if numero_texto == numero_lista:
    print("El número de elementos encontrados coincide con el número de hijos de la lista.")
else:
    print(f"Hay una discrepancia: elementos encontrados = {numero_texto}, hijos de la lista = {numero_lista}")

time.sleep(1)

driver.quit()