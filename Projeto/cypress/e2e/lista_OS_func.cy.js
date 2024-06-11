describe('teste da visualiazação pelo funcionario da lista das OS’s', () => {
    it('Sem OS cadastrada no sistema', () => {
        cy.visit('/');
        cy.get('[href="/funcionario_login/"]').click();
        cy.get('a').click();
        cy.get('#id_nome').type('Larissa Magalhães');
        cy.get('#id_email').type('larissa@gmail.com');
        cy.get('#id_username').type('larissa');
        cy.get('#id_senha').type('123');
        cy.get('#id_confirmar_senha').type('123');
        cy.get('.btn').click();
    })
    it('Com OS cadastrada no sistema', () => {
        cy.visit('/');
        cy.get('[href="/funcionario_login/"]').click();
        cy.get('#username').type('lala');
        cy.get('#password').type('123')
        cy.get('.btn').click()
        cy.url().should('include', 'servicos')
    })
})