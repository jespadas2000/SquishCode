describe('template spec', () => {

  it('acceder a fracultades', () => {
    cy.visit('https://www.ucm.es/')
    cy.contains("Aceptar y cerrar").click()

    cy.get('[class="dropdown-toggle"]').contains("Universidad").click()
    cy.contains("Facultades").click()
    cy.get('[href="http://informatica.ucm.es"]') //no funciona el click sobre informatica
  })

  it('el buscador deja escribir y probar lista de elementos', () => {
    cy.visit('http://informatica.ucm.es/')
    cy.contains("Aceptar y cerrar").click()

    cy.get('[placeholder="Buscar en la web"]').type("conferencias")
    cy.get('[placeholder="Buscar en la web"]').should('have.value', 'conferencias')
    cy.get('[id="btsearch"]').click()

    cy.get('[class="found_total"]').should('contain', '6 resultados')
  })

  

})