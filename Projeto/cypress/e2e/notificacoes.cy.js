describe('teste cadastro os usuário', () => {
    it('teste 1', () => {
        cy.visit('/');
        // Realizar o cadastro do cliente
        cy.wait(1000);
        cy.get('#cliente > .botao').click();
        cy.wait(2000);
        cy.get('a').click();
        cy.get('#id_nome').type('Mami Tomoe');
        cy.get('#id_username').type('tomoe');
        cy.get('#id_cpf').type('11122233304');
        cy.get('#id_data_nascimento').type('1970-03-21');
        cy.get('#id_contato').type('999998888');
        cy.get('#id_email').type('tomoe@gmail.com');
        cy.get('#id_senha').type('123');
        cy.get('#id_confirmar_senha').type('123');
        cy.wait(2000);
        cy.get('.btn').click();
        // Cadastrar uma nova ordem de serviço
        cy.get(':nth-child(2) > a > .img-fluid').click();
        cy.get('#aparelho').type('Geladeira');
        cy.get('#descricao_problema').type('Geladeira não gela');
        cy.get('#modelo').type('Eletrolux')
        cy.get('#garantia_sim').click();
        cy.get('.card > :nth-child(2) > .btn-primary').click();
        cy.wait(2000);
        // Simular a atribuição de um funcionário à ordem de serviço
        cy.get(':nth-child(4) > a > .img-fluid').click();
        cy.wait(1000);
        cy.get(':nth-child(5) > a > .img-fluid').click();
        cy.get('#funcionario').click();
        cy.get('a').click();
        cy.get('#id_nome').type('Camila de Lucas');
        cy.get('#id_email').type('camila@gmail.com');
        cy.get('#id_username').type('camila');
        cy.get('#id_senha').type('123');
        cy.get('#id_confirmar_senha').type('123');
        cy.get('.btn').type('123');
        cy.get('#lista_os > a > .img-fluid').click();
        cy.get('#ver-mais-lista-os').click();
        cy.get('.btn').click();
        cy.wait(2000);
        cy.get(':nth-child(1) > a > .img-fluid').click();
        cy.get(':nth-child(4) > a > .img-fluid').click();
        cy.get('#cliente').click();
        cy.get('#username').type('tomoe');
        cy.get('#senha').type('123');
        cy.get('.btn').click();
        cy.get(':nth-child(4) > a > .img-fluid').click();
        cy.get('.card').should('exist');
    })
})
