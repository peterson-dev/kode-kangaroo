/// <reference types="Cypress" />


describe('Create Snippet', function() {

  const user = 'testuser1'
  const pass = 'testing1234'

  function makeid(length) {
    var result           = '';
    var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var charactersLength = characters.length;
    for ( var i = 0; i < length; i++ ) {
       result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
  }

  it('logs in an existing user', function() {
    cy.login(user, pass)
    cy.url().should('include', '/snippets/')
    cy.get('nav').contains(user)
  })

  it('tests if create snippet modal disappears on desktop upon esc key press', function() {
    cy.get('nav').contains('Keep').click()
    cy.get('.modal-content').should('be.visible')

    cy.wait(500)
    cy.get('span > .fas').click()
    cy.get('.modal-content').should('not.be.visible')
  })

  it('creates a public test snippet by testuser1', function() {
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
      .get(':nth-child(4) > #id_language').select('Javascript').should('have.value', 'js')
      .get('#id_public').check()
    cy.pause()
    cy.get('#cy-keep-submit').click()
    cy.log('Snippet Created')

    cy.get('#cy-card div:first')
      .find('.card-header')
      .should('contain', randomTitle)    
  })
})