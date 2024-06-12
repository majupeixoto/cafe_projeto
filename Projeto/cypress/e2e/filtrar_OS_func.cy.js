describe('teste de filtrar a visualização das OS’s', () => {
    it('Todos', () => {
        cy.visit('/');
        cy.get('#cliente > .botao').click();
        cy.get('a').click();
        cy.get('#id_nome').type('Mari Lima');
        cy.get('#id_username').type('mari');
        cy.get('#id_cpf').type('18851022628');
        cy.get('#id_data_nascimento').type('2005-03-01');
        cy.get('#id_contato').type('81923456789');
        cy.get('#id_email').type('mari@gmail.com');
        cy.get('#id_senha').type('123');
        cy.get('#id_confirmar_senha').type('123');
        cy.wait(1000);
        cy.get('.btn').click();
        cy.get('.btn').click();
        cy.get('#aparelho').type('Ar condicionado');
        cy.get('#modelo').type('Electrolux');
        cy.get('#descricao_problema').type('Ar condicionado não está funcionando');
        cy.get('#garantia_sim').click();
        cy.wait(1000);
        cy.get('.btn-primary').click();
        cy.get(':nth-child(5) > a > .img-fluid').click();
        cy.get('[href="/funcionario_login/"]').click();
        cy.get('a').click();
        cy.get('#id_nome').type('Camila Magalhães');
        cy.get('#id_email').type('camila@gmail.com');
        cy.get('#id_username').type('camila');
        cy.get('#id_senha').type('123');
        cy.get('#id_confirmar_senha').type('123');
        cy.wait(1000);
        cy.get('.btn').click();
        cy.get(':nth-child(2) > a > .img-fluid').click();
        cy.wait(1000);
        cy.get(':nth-child(1) > :nth-child(7) > .btn-group > #ver-mais-lista-os').click();
        cy.get('.btn').click();
        cy.get('#lista_os > a > .img-fluid').click();
        cy.get('#status').should('have.value', '');
    })
    it('Ordem de serviço enviada', () => {
        cy.visit('/');
        cy.get('#cliente > .botao').click();
        cy.get('a').click();
        cy.get('#id_nome').type('Lari Lima');
        cy.get('#id_username').type('lari');
        cy.get('#id_cpf').type('18851022628');
        cy.get('#id_data_nascimento').type('2005-03-01');
        cy.get('#id_contato').type('81923456789');
        cy.get('#id_email').type('lari@gmail.com');
        cy.get('#id_senha').type('123');
        cy.get('#id_confirmar_senha').type('123');
        cy.wait(1000);
        cy.get('.btn').click();
        cy.get('.btn').click();
        cy.get('#aparelho').type('Liquidificador');
        cy.get('#modelo').type('Electrolux');
        cy.get('#descricao_problema').type('Liquidificador não está funcionando');
        cy.get('#garantia_sim').click();
        cy.wait(1000);
        cy.get('.btn-primary').click();
        cy.get(':nth-child(5) > a > .img-fluid').click();
        cy.get('[href="/funcionario_login/"]').click();
        cy.get('a').click();
        cy.get('#id_nome').type('Manu Magalhães');
        cy.get('#id_email').type('manu@gmail.com');
        cy.get('#id_username').type('manu');
        cy.get('#id_senha').type('123');
        cy.get('#id_confirmar_senha').type('123');
        cy.wait(1000);
        cy.get('.btn').click();
        cy.get(':nth-child(2) > a > .img-fluid').click();
        cy.wait(1000);
        cy.get(':nth-child(1) > :nth-child(7) > .btn-group > #ver-mais-lista-os').click();
        cy.get('.btn').click();
        cy.get('#lista_os > a > .img-fluid').click();
        cy.get('#status').select('Ordem de serviço enviada')
        cy.get('#status').should('have.value', 'Enviada');
    })
})