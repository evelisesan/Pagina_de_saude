// ***********************************************
// This example commands.js shows you how to
// create various custom commands and overwrite
// existing commands.
//
// For more comprehensive examples of custom
// commands please read more here:
// https://on.cypress.io/custom-commands
// ***********************************************

// Comando para preencher formulário de calorias
Cypress.Commands.add('preencherFormularioCalorias', (dados) => {
  cy.get('input[name="idade"]').clear().type(dados.idade)
  cy.get('input[name="peso"]').clear().type(dados.peso)
  cy.get('input[name="altura"]').clear().type(dados.altura)
  cy.get('select[name="genero"]').select(dados.genero)
  cy.get('select[name="nivel_atividade"]').select(dados.nivel_atividade)
})

// Comando para preencher formulário de IMC
Cypress.Commands.add('preencherFormularioIMC', (dados) => {
  cy.get('input[name="peso"]').clear().type(dados.peso)
  cy.get('input[name="altura"]').clear().type(dados.altura)
})

// Comando para verificar se a aplicação está rodando
Cypress.Commands.add('verificarAplicacaoRodando', () => {
  cy.request({
    url: '/',
    failOnStatusCode: false
  }).then((response) => {
    expect(response.status).to.be.oneOf([200, 404])
  })
})

// Comando para aguardar carregamento da página
Cypress.Commands.add('aguardarCarregamento', () => {
  cy.get('body').should('be.visible')
  cy.get('.loading', { timeout: 10000 }).should('not.exist')
})

// Comando para verificar responsividade
Cypress.Commands.add('verificarResponsividade', (viewport) => {
  cy.viewport(viewport.width, viewport.height)
  cy.get('body').should('be.visible')
}) 