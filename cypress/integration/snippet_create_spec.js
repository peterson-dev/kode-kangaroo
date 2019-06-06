/// <reference types="Cypress" />


describe('Create Snippet Test', function() {
  function makeid(length) {
    var result           = '';
    var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var charactersLength = characters.length;
    for ( var i = 0; i < length; i++ ) {
       result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
  }
  it('creates a public test snippet by testuser1', function() {
    cy.visit('/')
      .get('#id_username').type('testuser1')
      .get('#id_password').type('testing1234{enter}')
    //Should be on a new URL which includes '/snippets/'
    cy.url().should('include', '/snippets/')

    cy.get('#cy-keep').click()
    var randomTitle = makeid(9)

    //check that modal is shown
    cy.get('.modal-content').should('be.visible')
    cy.get('option:first').should('be.selected').then(($option) => {
      expect($option).to.contain('Bash')
    })
    cy.get('form').find('input[type=checkbox]').should('not.be.checked')

    cy.get('#id_title').type(randomTitle)
      .get('#id_content').type('This\nIs\nA\nCypress\nTest\nSnippet')
      .get('#id_language').select('Javascript').should('have.value', 'js')
      .get('#id_public').check()
    cy.pause()
    cy.get('#cy-keep-submit').click()

    cy.get('#cy-card div:first')
      .find('.card-header')
      .should('contain', randomTitle)    
  })
})