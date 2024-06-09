describe('test login_funcionario', () => {
    it('Login com sucesso', () => {
        cy.visit('/');
        cy.get('[href="/funcionario_login/"]').click();
        cy.get('#username').type('lala');
        cy.get('#password').type('123')
        cy.get('.btn').click()
        cy.url().should('include', 'servicos')
    })
})