describe('teste da visualiazação pelo funcionario da lista das OS’s', () => {
    it('Com OS cadastrada no sistema', () => {
        cy.visit('/');
        cy.get('#cliente > .botao').click();
        cy.get('a').click();
        cy.get('#id_nome').type('Gabi Lima');
        cy.get('#id_username').type('gabi');
        cy.get('#id_cpf').type('18851022628');
        cy.get('#id_data_nascimento').type('2005-03-01');
        cy.get('#id_contato').type('81923456789');
        cy.get('#id_email').type('gabi@gmail.com');
        cy.get('#id_senha').type('123');
        cy.get('#id_confirmar_senha').type('123');
        cy.wait(2000);
        cy.get('.btn').click();
        cy.get('.btn').click();
        cy.get('#aparelho').type('Maquina de Lavar');
        cy.get('#modelo').type('Electrolux');
        cy.get('#descricao_problema').type('Maquina de Lavar não está funcionando');
        cy.get('#garantia_sim').click();
        cy.wait(1000);
        cy.get('.btn-primary').click();
        cy.get(':nth-child(5) > a > .img-fluid').click();
        cy.get('[href="/funcionario_login/"]').click();
        cy.get('a').click();
        cy.get('#id_nome').type('Nanga Gueiros');
        cy.get('#id_email').type('nanda@gmail.com');
        cy.get('#id_username').type('nanda');
        cy.get('#id_senha').type('123');
        cy.get('#id_confirmar_senha').type('123');
        cy.wait(1000);
        cy.get('.btn').click();
        cy.get(':nth-child(2) > a > .img-fluid').click();
        cy.wait(1000);
        cy.get('thead > tr > :nth-child(1)').should('exist');
    })
})