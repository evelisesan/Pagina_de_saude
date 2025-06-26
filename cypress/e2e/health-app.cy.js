describe('Aplicação de Saúde e Bem-estar', () => {
  beforeEach(() => {
    // Visita a página inicial antes de cada teste
    cy.visit('/')
  })

  it('Deve carregar a página inicial corretamente', () => {
    // Verifica se a página carrega
    cy.get('body').should('be.visible')
    
    // Verifica elementos principais
    cy.get('h1').should('contain', 'Saúde')
    cy.get('.navbar-brand').should('be.visible')
    
    // Verifica links de navegação na navbar
    cy.get('.navbar-nav .nav-link[href="/"]').should('be.visible')
    cy.get('.navbar-nav .nav-link[href="/calorias"]').should('be.visible')
    cy.get('.navbar-nav .nav-link[href="/receitas"]').should('be.visible')
    cy.get('.navbar-nav .nav-link[href="/exercicios"]').should('be.visible')
    cy.get('.navbar-nav .nav-link[href="/imc"]').should('be.visible')
  })

  it('Deve navegar para a página de calorias', () => {
    // Usa seletor mais específico para o link de calorias na navbar
    cy.get('.navbar-nav .nav-link[href="/calorias"]').first().click()
    cy.url().should('include', '/calorias')
    cy.get('h1').should('contain', 'Calculadora de Calorias')
    
    // Verifica se o formulário está presente
    cy.get('#calorias-form').should('be.visible')
    cy.get('#calorias-form input[type="number"]').should('have.length.at.least', 3)
  })

  it('Deve navegar para a página de receitas', () => {
    // Usa seletor mais específico para o link de receitas na navbar
    cy.get('.navbar-nav .nav-link[href="/receitas"]').first().click()
    cy.url().should('include', '/receitas')
    cy.get('h1').should('contain', 'Receitas')
    
    // Verifica se há receitas listadas
    cy.get('.recipe-card').should('have.length.at.least', 1)
  })

  it('Deve navegar para a página de exercícios', () => {
    // Usa seletor mais específico para o link de exercícios na navbar
    cy.get('.navbar-nav .nav-link[href="/exercicios"]').first().click()
    cy.url().should('include', '/exercicios')
    cy.get('h1').should('contain', 'Exercícios')
    
    // Verifica se há exercícios listados
    cy.get('.exercise-card').should('have.length.at.least', 1)
  })

  it('Deve navegar para a página de IMC', () => {
    // Usa seletor mais específico para o link de IMC na navbar
    cy.get('.navbar-nav .nav-link[href="/imc"]').first().click()
    cy.url().should('include', '/imc')
    cy.get('h1').should('contain', 'IMC')
    
    // Verifica se o formulário está presente
    cy.get('#imc-form').should('be.visible')
    cy.get('#imc-form input[type="number"]').should('have.length.at.least', 2)
  })

  it('Deve calcular calorias corretamente', () => {
    cy.visit('/calorias')
    
    // Preenche o formulário
    cy.get('#age-input').type('30')
    cy.get('#weight-input').type('70')
    cy.get('#height-input').type('170')
    cy.get('#gender-select').select('masculino')
    cy.get('#activity-level').select('moderado')
    
    // Submete o formulário
    cy.get('#calculate-btn').click()
    
    // Verifica se o resultado é exibido
    cy.get('#resultado').should('be.visible')
    cy.get('#calorias-diarias').invoke('text').then((text) => {
      const valor = Number(text.replace(/\D/g, ''));
      expect(valor).to.be.greaterThan(0)
    })
  })

  it('Deve calcular IMC corretamente', () => {
    cy.visit('/imc')
    
    // Preenche o formulário
    cy.get('#weight-input').type('70')
    cy.get('#height-input').type('1.70')
    
    // Submete o formulário
    cy.get('#calculate-bmi-btn').click()
    
    // Verifica se o resultado é exibido
    cy.get('#resultado-imc').should('be.visible')
    cy.get('#imc-valor').should('contain.text', '24.22')
    cy.get('#imc-classificacao').should('contain.text', 'Peso Normal')
  })

  it('Deve buscar receitas', () => {
    cy.visit('/receitas')
    
    // Busca por "frango"
    cy.get('#search-input').type('frango')
    cy.get('#search-btn').click()
    
    // Verifica se os resultados são exibidos
    cy.get('#search-results').should('be.visible')
    cy.get('#search-grid .recipe-card').should('have.length.at.least', 1)
  })

  it('Deve filtrar exercícios por dificuldade', () => {
    cy.visit('/exercicios')
    
    // Filtra por exercícios iniciantes
    cy.get('#filter-beginner').check()
    cy.get('#apply-filters').click()
    
    // Verifica se apenas exercícios iniciantes são exibidos
    cy.get('.exercise-card').each(($el) => {
      cy.wrap($el).find('.badge').should('contain.text', 'Iniciante')
    })
  })

  it('Deve ser responsivo em dispositivos móveis', () => {
    // Define viewport mobile
    cy.viewport(375, 667)
    
    // Verifica se o menu mobile está presente
    cy.get('#mobile-menu-toggle').should('be.visible')
    
    // Abre o menu mobile
    cy.get('#mobile-menu-toggle').click()
    
    // Verifica se os links do menu mobile estão visíveis
    cy.get('#mobile-menu-content').should('be.visible')
    cy.get('#mobile-menu-content .nav-link[href="/calorias"]').should('be.visible')
  })

  it('Deve lidar com erros de formulário', () => {
    cy.visit('/calorias')
    
    // Tenta submeter formulário vazio
    cy.get('#calculate-btn').click()
    
    // Verifica se mensagens de erro são exibidas (validação HTML5)
    cy.get('#age-input').should('have.attr', 'required')
    cy.get('#weight-input').should('have.attr', 'required')
    cy.get('#height-input').should('have.attr', 'required')
  })

  it('Deve navegar usando links da página inicial', () => {
    // Testa navegação pelos botões da página inicial
    cy.get('.btn[href="/calorias"]').first().click()
    cy.url().should('include', '/calorias')
    
    cy.visit('/')
    cy.get('.btn[href="/receitas"]').first().click()
    cy.url().should('include', '/receitas')
    
    cy.visit('/')
    cy.get('.btn[href="/exercicios"]').first().click()
    cy.url().should('include', '/exercicios')
  })

  it('Deve verificar funcionalidade de filtros de receitas', () => {
    cy.visit('/receitas')
    
    // Testa filtro vegetariano
    cy.get('#filter-vegetarian').check()
    cy.get('#apply-filters').click()
    
    // Verifica se as receitas vegetarianas são exibidas
    cy.get('.vegetarian-recipe').should('have.length.at.least', 1)
  })

  it('Deve verificar estrutura de cards de receitas', () => {
    cy.visit('/receitas')
    
    // Verifica se os cards têm a estrutura correta
    cy.get('.recipe-card').first().within(() => {
      cy.get('.card-title').should('be.visible')
      cy.get('.badge').should('exist')
      cy.get('.btn').should('contain.text', 'Ver Receita')
    })
  })

  it('Deve verificar estrutura de cards de exercícios', () => {
    cy.visit('/exercicios')
    
    // Verifica se os cards têm a estrutura correta
    cy.get('.exercise-card').first().within(() => {
      cy.get('.card-title').should('be.visible')
      cy.get('.badge').should('exist')
      cy.get('.btn').should('contain.text', 'Ver Exercício')
    })
  })
}) 