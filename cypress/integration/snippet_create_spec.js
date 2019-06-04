/// <reference types="Cypress" />


describe('Create Snippet Test', function() {
  it('creates a public test snippet by testuser1', function() {
    cy.visit('/')
      .get('#id_username').type('testuser1')
      .get('#id_password').type('testing1234{enter}')
    //Should be on a new URL which includes '/snippets/'
    cy.url().should('include', '/snippets/')

    cy.get('#cy-keep').click()
    cy.get('#id_title').type('Cypress Test Snippet')
      .get('#id_content').type('test\ntest\ntest\ntest')
      .get('#id_language').select('Javascript').should('have.value', 'js')
      .get('#id_public').check()
    cy.pause()
    cy.get('#cy-keep-submit').click()

    cy.get('#cy-card div:first').should('have.')
    
  })
})