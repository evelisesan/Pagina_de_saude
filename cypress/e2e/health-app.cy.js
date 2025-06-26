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
    
    // Verifica links de navegação
    cy.get('a[href="/"]').should('be.visible')
    cy.get('a[href="/calorias"]').should('be.visible')
    cy.get('a[href="/receitas"]').should('be.visible')
    cy.get('a[href="/exercicios"]').should('be.visible')
    cy.get('a[href="/imc"]').should('be.visible')
  })

  it('Deve navegar para a página de calorias', () => {
    cy.get('a[href="/calorias"]').click()
    cy.url().should('include', '/calorias')
    cy.get('h1').should('contain', 'Calculadora de Calorias')
    
    // Verifica se o formulário está presente
    cy.get('form').should('be.visible')
    cy.get('input[type="number"]').should('have.length.at.least', 3)
  })

  it('Deve navegar para a página de receitas', () => {
    cy.get('a[href="/receitas"]').click()
    cy.url().should('include', '/receitas')
    cy.get('h1').should('contain', 'Receitas')
    
    // Verifica se há receitas listadas
    cy.get('.recipe-card').should('have.length.at.least', 1)
  })

  it('Deve navegar para a página de exercícios', () => {
    cy.get('a[href="/exercicios"]').click()
    cy.url().should('include', '/exercicios')
    cy.get('h1').should('contain', 'Exercícios')
    
    // Verifica se há exercícios listados
    cy.get('.exercise-card').should('have.length.at.least', 1)
  })

  it('Deve navegar para a página de IMC', () => {
    cy.get('a[href="/imc"]').click()
    cy.url().should('include', '/imc')
    cy.get('h1').should('contain', 'IMC')
    
    // Verifica se o formulário está presente
    cy.get('form').should('be.visible')
    cy.get('input[type="number"]').should('have.length.at.least', 2)
  })

  it('Deve calcular calorias corretamente', () => {
    cy.visit('/calorias')
    
    // Preenche o formulário
    cy.get('input[name="idade"]').type('30')
    cy.get('input[name="peso"]').type('70')
    cy.get('input[name="altura"]').type('1.70')
    cy.get('select[name="genero"]').select('masculino')
    cy.get('select[name="nivel_atividade"]').select('moderado')
    
    // Submete o formulário
    cy.get('button[type="submit"]').click()
    
    // Verifica se o resultado é exibido
    cy.get('.resultado-calorias').should('be.visible')
    cy.get('.calorias-diarias').should('contain.text', 'calorias')
  })

  it('Deve calcular IMC corretamente', () => {
    cy.visit('/imc')
    
    // Preenche o formulário
    cy.get('input[name="peso"]').type('70')
    cy.get('input[name="altura"]').type('1.70')
    
    // Submete o formulário
    cy.get('button[type="submit"]').click()
    
    // Verifica se o resultado é exibido
    cy.get('.resultado-imc').should('be.visible')
    cy.get('.imc-valor').should('contain.text', '24.22')
    cy.get('.imc-classificacao').should('contain.text', 'Peso Normal')
  })

  it('Deve buscar receitas', () => {
    cy.visit('/receitas')
    
    // Busca por "frango"
    cy.get('input[placeholder*="buscar"]').type('frango')
    cy.get('button[type="submit"]').click()
    
    // Verifica se os resultados são exibidos
    cy.get('.recipe-card').should('have.length.at.least', 1)
  })

  it('Deve filtrar exercícios por dificuldade', () => {
    cy.visit('/exercicios')
    
    // Filtra por exercícios iniciantes
    cy.get('select[name="dificuldade"]').select('iniciante')
    cy.get('button[type="submit"]').click()
    
    // Verifica se apenas exercícios iniciantes são exibidos
    cy.get('.exercise-card').each(($el) => {
      cy.wrap($el).should('contain.text', 'iniciante')
    })
  })

  it('Deve ser responsivo em dispositivos móveis', () => {
    // Define viewport mobile
    cy.viewport(375, 667)
    
    // Verifica se o menu mobile está presente
    cy.get('.mobile-menu-toggle').should('be.visible')
    
    // Abre o menu mobile
    cy.get('.mobile-menu-toggle').click()
    
    // Verifica se os links do menu mobile estão visíveis
    cy.get('.mobile-menu-content').should('be.visible')
    cy.get('.mobile-menu-content a[href="/calorias"]').should('be.visible')
  })

  it('Deve lidar com erros de formulário', () => {
    cy.visit('/calorias')
    
    // Tenta submeter formulário vazio
    cy.get('button[type="submit"]').click()
    
    // Verifica se mensagens de erro são exibidas
    cy.get('.alert-danger').should('be.visible')
  })
}) 