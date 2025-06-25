*** Settings ***
Documentation     Testes TDD para página de saúde e controle de calorias
Library           SeleniumLibrary
Library           RequestsLibrary
Suite Setup       Setup Test Environment
Suite Teardown    Close All Browsers

*** Variables ***
${BASE_URL}       http://localhost:5000
${BROWSER}        chrome
${TIMEOUT}        20s

*** Test Cases ***

# Testes de Navegação e Estrutura da Página
Verificar Se A Página Principal Carrega Corretamente
    [Documentation]    Verifica se a página principal carrega com todos os elementos básicos
    [Tags]    navigation    smoke
    Open Browser    ${BASE_URL}    ${BROWSER}
    Wait Until Page Contains    Saúde e Bem-estar    timeout=${TIMEOUT}
    Page Should Contain    Controle de Calorias
    Page Should Contain    Receitas Saudáveis
    Page Should Contain    Exercícios para 40+
    Close Browser

Verificar Menu De Navegação
    [Documentation]    Verifica se o menu de navegação está presente e funcional
    [Tags]    navigation
    Open Browser    ${BASE_URL}    ${BROWSER}
    Wait Until Element Is Visible    id=nav-menu    timeout=${TIMEOUT}
    Page Should Contain Element    link=Início
    Page Should Contain Element    link=Calorias
    Page Should Contain Element    link=Receitas
    Page Should Contain Element    link=Exercícios
    Page Should Contain Element    link=Contato
    Close Browser

# Testes de Calculadora de Calorias
Verificar Calculadora De Calorias
    [Documentation]    Verifica se a calculadora de calorias está presente e funcional
    [Tags]    calories    calculator
    Open Browser    ${BASE_URL}/calorias    ${BROWSER}
    Wait Until Page Contains    Calculadora de Calorias    timeout=${TIMEOUT}
    Wait Until Element Is Visible    id=age-input    timeout=${TIMEOUT}
    Page Should Contain Element    id=weight-input
    Page Should Contain Element    id=height-input
    Page Should Contain Element    id=activity-level
    Page Should Contain Element    id=calculate-btn
    Close Browser

Calcular Calorias Para Pessoa De 45 Anos
    [Documentation]    Testa o cálculo de calorias para uma pessoa de 45 anos
    [Tags]    calories    calculation
    Open Browser    ${BASE_URL}/calorias    ${BROWSER}
    Wait Until Element Is Visible    id=age-input    timeout=${TIMEOUT}
    Input Text    id=age-input    45
    Input Text    id=weight-input    70
    Input Text    id=height-input    170
    Select From List By Value    id=activity-level    moderate
    Wait Until Element Is Visible    id=calculate-btn    timeout=${TIMEOUT}
    Click Button    id=calculate-btn
    Wait Until Page Contains    Suas calorias diárias recomendadas    timeout=${TIMEOUT}
    Page Should Contain    aproximadamente
    Close Browser

# Testes de Receitas Saudáveis
Verificar Seção De Receitas
    [Documentation]    Verifica se a seção de receitas está presente
    [Tags]    recipes
    Open Browser    ${BASE_URL}/receitas    ${BROWSER}
    Wait Until Page Contains    Receitas Saudáveis e Baratas    timeout=${TIMEOUT}
    Wait Until Element Is Visible    class=recipe-card    timeout=${TIMEOUT}
    Page Should Contain    Filtros
    Wait Until Element Is Visible    id=filter-vegetarian    timeout=${TIMEOUT}
    Page Should Contain Element    id=filter-low-calorie
    Page Should Contain Element    id=filter-budget
    Close Browser

Filtrar Receitas Vegetarianas
    [Documentation]    Testa o filtro de receitas vegetarianas
    [Tags]    recipes    filters
    Open Browser    ${BASE_URL}/receitas    ${BROWSER}
    Wait Until Element Is Visible    id=filter-vegetarian    timeout=${TIMEOUT}
    Click Element    id=filter-vegetarian
    Wait Until Element Is Visible    class=vegetarian-recipe    timeout=${TIMEOUT}
    Page Should Contain Element    class=vegetarian-recipe
    Close Browser

Verificar Detalhes Da Receita
    [Documentation]    Verifica se os detalhes da receita são exibidos corretamente
    [Tags]    recipes    details
    Open Browser    ${BASE_URL}/receitas/1    ${BROWSER}
    Wait Until Page Contains    Ingredientes    timeout=${TIMEOUT}
    Page Should Contain    Modo de Preparo
    Page Should Contain    Informações Nutricionais
    Wait Until Element Is Visible    id=calories-per-serving    timeout=${TIMEOUT}
    Page Should Contain Element    id=cooking-time
    Page Should Contain Element    id=difficulty-level
    Close Browser

# Testes de Exercícios para 40+
Verificar Seção De Exercícios
    [Documentation]    Verifica se a seção de exercícios está presente
    [Tags]    exercises
    Open Browser    ${BASE_URL}/exercicios    ${BROWSER}
    Wait Until Page Contains    Exercícios para Pessoas Acima de 40 Anos    timeout=${TIMEOUT}
    Wait Until Element Is Visible    class=exercise-card    timeout=${TIMEOUT}
    Page Should Contain    Nível de Dificuldade
    Wait Until Element Is Visible    id=filter-beginner    timeout=${TIMEOUT}
    Page Should Contain Element    id=filter-intermediate
    Page Should Contain Element    id=filter-advanced
    Close Browser

Filtrar Exercícios Para Iniciantes
    [Documentation]    Testa o filtro de exercícios para iniciantes
    [Tags]    exercises    filters
    Open Browser    ${BASE_URL}/exercicios    ${BROWSER}
    Wait Until Element Is Visible    id=filter-beginner    timeout=${TIMEOUT}
    Click Element    id=filter-beginner
    Wait Until Element Is Visible    class=beginner-exercise    timeout=${TIMEOUT}
    Page Should Contain Element    class=beginner-exercise
    Close Browser

Verificar Detalhes Do Exercício
    [Documentation]    Verifica se os detalhes do exercício são exibidos corretamente
    [Tags]    exercises    details
    Open Browser    ${BASE_URL}/exercicios/1    ${BROWSER}
    Wait Until Page Contains    Como Fazer    timeout=${TIMEOUT}
    Page Should Contain    Benefícios
    Page Should Contain    Precauções
    Wait Until Element Is Visible    id=exercise-video    timeout=${TIMEOUT}
    Page Should Contain Element    id=duration
    Page Should Contain Element    id=sets-reps
    Close Browser

# Testes de Responsividade
Verificar Responsividade Em Dispositivo Móvel
    [Documentation]    Verifica se a página é responsiva em dispositivos móveis
    [Tags]    responsive    mobile
    Open Browser    ${BASE_URL}    ${BROWSER}
    Set Window Size    375    667
    Wait Until Element Is Visible    id=mobile-menu-toggle    timeout=${TIMEOUT}
    Page Should Be Visible    id=nav-menu
    Close Browser

# Testes de Performance
Verificar Tempo De Carregamento Da Página
    [Documentation]    Verifica se a página carrega em tempo aceitável
    [Tags]    performance
    ${start_time}=    Get Time    epoch
    Open Browser    ${BASE_URL}    ${BROWSER}
    Wait Until Page Contains    Saúde e Bem-estar    timeout=${TIMEOUT}
    ${end_time}=    Get Time    epoch
    ${load_time}=    Evaluate    ${end_time} - ${start_time}
    Should Be True    ${load_time} < 10
    Close Browser

# Testes de Acessibilidade
Verificar Acessibilidade Básica
    [Documentation]    Verifica elementos básicos de acessibilidade
    [Tags]    accessibility
    Open Browser    ${BASE_URL}    ${BROWSER}
    Wait Until Element Is Visible    tag=main    timeout=${TIMEOUT}
    Page Should Contain Element    tag=nav
    Page Should Contain Element    tag=footer
    Page Should Contain Element    tag=h1
    Close Browser

# Testes de Funcionalidades Específicas
Verificar Busca De Receitas
    [Documentation]    Testa a funcionalidade de busca de receitas
    [Tags]    search    recipes
    Open Browser    ${BASE_URL}/receitas    ${BROWSER}
    Wait Until Element Is Visible    id=search-input    timeout=${TIMEOUT}
    Input Text    id=search-input    frango
    Wait Until Element Is Visible    id=search-btn    timeout=${TIMEOUT}
    Click Button    id=search-btn
    Wait Until Page Contains    Resultados para "frango"    timeout=${TIMEOUT}
    Wait Until Element Is Visible    class=search-result    timeout=${TIMEOUT}
    Page Should Contain Element    class=search-result
    Close Browser

Verificar Calculadora De IMC
    [Documentation]    Testa a calculadora de IMC
    [Tags]    bmi    calculator
    Open Browser    ${BASE_URL}/imc    ${BROWSER}
    Wait Until Element Is Visible    id=weight-input    timeout=${TIMEOUT}
    Input Text    id=weight-input    70
    Input Text    id=height-input    1.70
    Wait Until Element Is Visible    id=calculate-bmi-btn    timeout=${TIMEOUT}
    Click Button    id=calculate-bmi-btn
    Wait Until Page Contains    Seu IMC é    timeout=${TIMEOUT}
    Page Should Contain    Peso Normal
    Close Browser

# Testes de Menu Mobile
Verificar Menu Mobile
    [Documentation]    Testa a funcionalidade do menu mobile
    [Tags]    mobile    menu
    Open Browser    ${BASE_URL}    ${BROWSER}
    Set Window Size    375    667
    Wait Until Element Is Visible    id=mobile-menu-toggle    timeout=${TIMEOUT}
    Click Element    id=mobile-menu-toggle
    Wait Until Element Is Visible    id=mobile-menu-content    timeout=${TIMEOUT}
    Page Should Contain Element    id=mobile-menu-overlay
    Click Element    id=mobile-menu-close
    Wait Until Element Is Not Visible    id=mobile-menu-content    timeout=${TIMEOUT}
    Close Browser

*** Keywords ***
Setup Test Environment
    [Documentation]    Configura o ambiente de teste
    Set Selenium Speed    0.5s
    Set Selenium Timeout    ${TIMEOUT} 