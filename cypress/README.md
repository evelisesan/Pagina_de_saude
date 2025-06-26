# Testes E2E com Cypress

Este diretório contém os testes end-to-end (E2E) da aplicação de Saúde e Bem-estar usando Cypress.

## Estrutura

```
cypress/
├── e2e/
│   └── health-app.cy.js    # Testes principais da aplicação
├── support/
│   ├── commands.js         # Comandos customizados
│   └── e2e.js             # Configurações globais
└── README.md              # Esta documentação
```

## Pré-requisitos

1. **Node.js** instalado (versão 14 ou superior)
2. **npm** ou **yarn** para gerenciar dependências
3. **Aplicação Flask** rodando em `http://localhost:5000`

## Instalação

```bash
# Instalar dependências
npm install

# Ou se preferir yarn
yarn install
```

## Executando os Testes

### Modo Headless (CI/CD)
```bash
npm run test:e2e
```

### Modo Interativo
```bash
npm run test:e2e:open
```

### Modo Headed (com navegador visível)
```bash
npm run test:e2e:headed
```

## Testes Disponíveis

### 1. Navegação Básica
- Carregamento da página inicial
- Navegação entre páginas (calorias, receitas, exercícios, IMC)

### 2. Funcionalidades Principais
- Cálculo de calorias
- Cálculo de IMC
- Busca de receitas
- Filtros de exercícios

### 3. Responsividade
- Testes em dispositivos móveis
- Menu mobile

### 4. Validação de Formulários
- Tratamento de erros
- Validação de campos obrigatórios

## Comandos Customizados

### `preencherFormularioCalorias(dados)`
Preenche o formulário de cálculo de calorias.

```javascript
cy.preencherFormularioCalorias({
  idade: 30,
  peso: 70,
  altura: 1.70,
  genero: 'masculino',
  nivel_atividade: 'moderado'
})
```

### `preencherFormularioIMC(dados)`
Preenche o formulário de cálculo de IMC.

```javascript
cy.preencherFormularioIMC({
  peso: 70,
  altura: 1.70
})
```

### `verificarAplicacaoRodando()`
Verifica se a aplicação está respondendo.

### `aguardarCarregamento()`
Aguarda o carregamento completo da página.

### `verificarResponsividade(viewport)`
Testa responsividade em diferentes resoluções.

```javascript
cy.verificarResponsividade({
  width: 375,
  height: 667
})
```

## Configuração

O Cypress está configurado em `cypress.config.js` com:

- **Base URL**: `http://localhost:5000`
- **Viewport**: 1280x720
- **Timeout**: 10 segundos
- **Vídeos**: Desabilitados
- **Screenshots**: Habilitados em caso de falha

## Integração com CI/CD

Para integrar com pipelines de CI/CD, use:

```bash
# Instalar dependências
npm ci

# Executar testes
npm run test:e2e
```

## Troubleshooting

### Aplicação não está rodando
Certifique-se de que o Flask está rodando:
```bash
python app.py
```

### Erros de timeout
Aumente o timeout no `cypress.config.js`:
```javascript
defaultCommandTimeout: 15000
```

### Problemas de responsividade
Verifique se os elementos estão visíveis no viewport correto:
```javascript
cy.viewport(375, 667)
cy.get('.mobile-menu-toggle').should('be.visible')
``` 