describe('acompanhamento status da os pelo cliente', () => {
    it('teste 1', () => {
        cy.visit('/');
        cy.wait(1000);
        cy.get('#cliente').click();
        cy.wait(2000);
        cy.get('a').click();
        cy.wait(1000);
        cy.get('#id_nome').type('Jonatas Joel');
        cy.get('#id_username').type('jonatas');
        cy.get('#id_cpf').type('45490900089');
        cy.get('#id_data_nascimento').type('2003-05-05');
        cy.get('#id_contato').type('81990909090');
        cy.get('#id_email').type('jj@gmail.com');
        cy.get('#id_senha').type('123');
        cy.get('#id_confirmar_senha').type('123');
        cy.get('.btn').click();
        cy.wait(1000); // Espera após clicar no botão
        // home cliente
        cy.get('.btn').click();
        cy.wait(1000); // Espera após clicar no botão

        // cadastra os cliente
        cy.get('.picture').attachFile('imgs/maquina_de_lavar.jpg');
        cy.get('#aparelho').type('Maquina de Lavar');
        cy.get('#modelo').type('Electrolux');
        cy.get('#descricao_problema').type('Maquina de Lavar não está funcionando');
        cy.get('#garantia_sim').click();
        cy.wait(500); // Espera após clicar na garantia
        cy.get('.btn-primary').click();
        cy.wait(1000); // Espera após clicar no botão
        cy.get(':nth-child(5) > a > .img-fluid').click();
        cy.wait(1000); // Espera após clicar no item

        // login funcionario
        cy.get('#funcionario').click();
        cy.wait(1000); // Espera após clicar no botão
        cy.get('a').click();
        cy.wait(1000); // Espera após clicar no link
        cy.get('#id_nome').type('Joana Bueno');
        cy.get('#id_email').type('jb@gmail.com');
        cy.get('#id_username').type('joana');
        cy.get('#id_senha').type('123');
        cy.get('#id_confirmar_senha').type('123');
        cy.wait(1000); // Espera após digitar as informações
        cy.get('.btn').click();
        cy.wait(1000); // Espera após clicar no botão
        cy.get(':nth-child(2) > a > .img-fluid').click();
        cy.wait(1000); // Espera após clicar no item

        // home funcionario
        cy.get('#lista_os').click();
        cy.wait(1000); // Espera após clicar no botão
        cy.get('#ver-mais-lista-os').click();
        cy.wait(1000); // Espera após clicar no link
        cy.get('.btn').click();
        cy.wait(1000); // Espera após clicar no botão
        cy.get('.btn').click();
        cy.wait(1000); // Espera após clicar no botão
        cy.get('#status').should('be.visible').select('Aguardando peça');
        cy.wait(1000); // Espera após selecionar o status
        cy.get('#status').should('have.value', 'Aguardando_peca');
        cy.get('#tipo_atendimento').should('be.visible').select('Garantia on site');
        cy.wait(1000); // Espera após selecionar o tipo de atendimento
        cy.get('#tipo_atendimento').should('have.value', 'GON');
        cy.get('.btn').click();
        cy.wait(1000); // Espera após clicar no botão
        cy.get(':nth-child(4) > a > .img-fluid').click();
        cy.wait(1000); // Espera após clicar no item

        // verifica status
        cy.get('#cliente').click();
        cy.wait(1000); // Espera após clicar no botão
        cy.get('#username').type('jonatas');
        cy.get('#senha').type('123');
        cy.wait(1000); // Espera após digitar as credenciais
        cy.get('.btn').click();
        cy.wait(1000); // Espera após clicar no botão
        cy.get('.col-lg-3.col-md-4.col-sm-6.mb-4').click();
        cy.wait(1000); // Espera após clicar no item
        
        // Adding logs to help with debugging
        cy.get('#status_os_detalhes_cliente').then(($el) => {
            cy.log('Status Text:', $el.text());
        });

        cy.get('#status_aguardando_peca > .progress-count').should('exist');
    });
});
