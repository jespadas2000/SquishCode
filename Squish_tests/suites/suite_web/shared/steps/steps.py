
import names
import builtins

@Given("The web page is open")
def step(context):
    startBrowser("https://www.ucm.es/")


@When("the Universidad button is pressed")
def step(context):
    mouseClick(waitForObject(names.ucm_EstudiarTab))
        
@When("the Falcutad button is pressed")
def step(context):
    mouseClick(waitForObject(names.ucm_FacultadesTab))
    
@When("the Informatica option is selected")
def step(context):
    mouseClick(waitForObject(names.ucm_facultadInformatica))
    
@Then("search conferencias in the browser")
def step(context):
    typeText(waitForObject(names.ucm_informaticaSearch), "conferencias")
    clickButton(waitForObject(names.ucm_informaticaSearchSubmit))


@Then("the list of options is checked")
def step(context):
    snooze(1)
    numero = findObject("resultados")
    lista = findObject(names.Inform_BrowserTabDOCUMENT)
    numeroText = builtins.int(numero.simplifiedInnerText[0])
    if lista.numChildren != numeroText:
        test.fail("ERROR: los numeros no coinciden")
