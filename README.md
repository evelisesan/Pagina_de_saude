# Aplicação de Saúde e Bem-estar

Uma aplicação web completa para saúde e bem-estar, desenvolvida com Flask e testada com uma pirâmide de testes abrangente.

## 🏗️ Arquitetura

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Testes**: Pirâmide completa de testes (Unitários, Integração, Performance, Segurança, Acessibilidade, E2E)

## 🧪 Pirâmide de Testes

```
🔺 E2E (Cypress) - Menos testes, mais complexos
🔸 Integração - Testes de componentes
🔻 Unitários - Mais testes, mais simples
🔸 Performance - Testes de velocidade
🔸 Segurança - Testes de vulnerabilidades
🔸 Acessibilidade - Testes WCAG
```

### Tipos de Teste

1. **Unitários** (`tests/test_unit.py`)
   - Testes de funções individuais
   - APIs e cálculos
   - Estrutura de dados

2. **Integração** (`tests/test_integration.py`)
   - Testes de fluxo completo
   - Integração entre componentes
   - Formulários e navegação

3. **Performance** (`tests/test_performance.py`)
   - Testes de velocidade de resposta
   - Carga e concorrência

4. **Segurança** (`tests/test_security.py`)
   - Validação de entrada
   - Headers de segurança
   - Proteção contra injeções

5. **Acessibilidade** (`tests/test_accessibility.py`)
   - Conformidade WCAG
   - Navegação por teclado
   - Estrutura semântica

6. **E2E** (`cypress/e2e/health-app.cy.js`)
   - Testes end-to-end com Cypress
   - Fluxos completos do usuário
   - Responsividade

## 🚀 Instalação e Execução

### Pré-requisitos

- Python 3.8+
- Node.js 14+
- npm ou yarn

### Backend (Flask)

```bash
# Instalar dependências Python
pip install -r requirements.txt

# Executar aplicação
python app.py
```

### Frontend e Testes E2E

```bash
# Instalar dependências Node.js
npm install

# Executar testes E2E
npm run test:e2e
```

## 🧪 Executando os Testes

### Todos os Testes

```bash
# Executar toda a pirâmide de testes
python tests/run_all_tests.py

# Ou executar tudo incluindo E2E
npm run test:all
```

### Testes Específicos

```bash
# Testes unitários
python -m pytest tests/test_unit.py -v

# Testes de integração
python -m pytest tests/test_integration.py -v

# Testes de segurança
python -m pytest tests/test_security.py -v

# Testes de acessibilidade
python -m pytest tests/test_accessibility.py -v

# Testes E2E (Cypress)
npm run test:e2e
```

### Testes E2E Interativos

```bash
# Abrir interface do Cypress
npm run test:e2e:open

# Executar com navegador visível
npm run test:e2e:headed
```

## 📊 Funcionalidades

### Calculadora de Calorias
- Cálculo baseado na fórmula de Harris-Benedict
- Suporte a diferentes níveis de atividade
- Validação robusta de entrada

### Calculadora de IMC
- Cálculo automático de IMC
- Classificação automática
- Validação de dados

### Receitas Saudáveis
- Catálogo de receitas nutritivas
- Filtros por categoria, dieta e orçamento
- Busca por ingredientes

### Exercícios
- Exercícios adaptados para iniciantes
- Instruções detalhadas
- Filtros por dificuldade

## 🔒 Segurança

- Validação rigorosa de entrada
- Proteção contra injeção SQL e XSS
- Headers de segurança configurados
- Rate limiting implementado

## ♿ Acessibilidade

- Conformidade com WCAG 2.1
- Navegação por teclado
- Estrutura semântica
- Responsividade completa

## 📈 Performance

- Otimização de consultas
- Cache de dados
- Compressão de assets
- Lazy loading

## 🛠️ Tecnologias

### Backend
- **Flask**: Framework web
- **Jinja2**: Template engine
- **Flask-CORS**: Cross-origin resource sharing

### Frontend
- **Bootstrap 5**: Framework CSS
- **Font Awesome**: Ícones
- **JavaScript**: Interatividade

### Testes
- **pytest**: Framework de testes Python
- **Cypress**: Testes E2E
- **unittest**: Testes unitários e integração

## 📁 Estrutura do Projeto

```
Projeto_teste/
├── app.py                 # Aplicação Flask principal
├── requirements.txt       # Dependências Python
├── package.json          # Dependências Node.js
├── cypress.config.js     # Configuração Cypress
├── templates/            # Templates HTML
├── cypress/              # Testes E2E
│   ├── e2e/
│   │   └── health-app.cy.js
│   └── support/
│       ├── commands.js
│       └── e2e.js
├── tests/                # Testes Python
│   ├── test_unit.py
│   ├── test_integration.py
│   ├── test_security.py
│   ├── test_accessibility.py
│   └── run_all_tests.py
└── test_results/         # Resultados dos testes
```

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature
3. Adicione testes para novas funcionalidades
4. Execute todos os testes
5. Faça commit das mudanças
6. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 📞 Suporte

Para dúvidas ou problemas:
- Abra uma issue no GitHub
- Consulte a documentação dos testes
- Verifique os logs de erro
