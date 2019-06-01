/// <reference types="Cypress" />

//my first cypress test
describe('Log in Admin', function() {
  it('should log in existing user and travel to index', function() {
    cy.visit('http://localhost:8000/')
    //cy.visit('http://kode-kangaroo.herokuapp.com')
    cy.get('#id_username')
      .type('admin')
      .get('#id_password')
      .type('1234')
      .get('#cy-login').click()

    //Should be on a new URL which includes '/snippets/'
    cy.url().should('include', '/snippets/')
  })
})