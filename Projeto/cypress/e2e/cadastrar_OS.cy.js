describe('teste cadastro os funcionario', () => {
    it('teste 1', () => {
        cy.visit('/');
        cy.wait(1000);
        cy.get('#cliente > .botao').click();
        cy.wait(2000);
        cy.get('a').click();
        cy.get('#id_nome').type('bob');
        cy.get('#id_username').type('bob');
        cy.get('#id_cpf').type('11122233304');
        cy.get('#id_data_nascimento').type('1970-03-21');
        cy.get('#id_contato').type('999998888');
        cy.get('#id_email').type('bob@gmail.com');
        cy.get('#id_senha').type('123');
        cy.get('#id_confirmar_senha').type('123');
        cy.get('.btn').click();
        cy.wait(2000);
        cy.get('.btn').click();
        cy.get('#aparelho').type('microondas');
        cy.get('#descricao_problema').type('aparelho não quer ligar');
        cy.get('#modelo').type('lg 1234')
        cy.get('#garantia_sim').click();
        cy.get('.btn-primary').click();
        cy.wait(2000)
        cy.get(':nth-child(5) > a > .img-fluid').click();
        cy.get('#funcionario > .botao').click();
        cy.get('a').click();
        cy.get('#id_nome').type('rob');
        cy.get('#id_email').type('rob@tech.com')
        cy.get('#id_username').type('rob');
        cy.get('#id_senha').type('123')
        cy.get('#id_confirmar_senha').type('123')
        cy.get('.btn').click();
        cy.wait(1500)
        cy.get(':nth-child(2) > a > .img-fluid').click()
        cy.wait(1500)
        cy.get('#ver-mais-lista-os').click()
        cy.wait(1500)
        cy.get('.btn').click()
        cy.wait(1500)
        cy.get(':nth-child(1) > a > .img-fluid').click()
        cy.get('.card').should('exist')
    })
})