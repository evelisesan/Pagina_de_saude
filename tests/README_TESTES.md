# 📊 Pirâmide de Testes - Documentação Completa

## 🎯 Visão Geral

Este projeto implementa uma **pirâmide de testes completa** seguindo as melhores práticas de TDD (Test-Driven Development) e qualidade de software. A pirâmide garante cobertura abrangente desde testes unitários até testes end-to-end.

## 🏗️ Estrutura da Pirâmide

```
                    🔺 E2E (Robot Framework)
                   🔸 Integração + Performance
                  🔸 Segurança + Acessibilidade
                 🔻 Unitários (Base da Pirâmide)
```

### 📈 Distribuição dos Testes

| Tipo de Teste | Quantidade | Velocidade | Custo | Cobertura |
|---------------|------------|------------|-------|-----------|
| **Unitários** | ~50 testes | ⚡ Rápido | 💰 Baixo | 🔍 Alta |
| **Integração** | ~30 testes | 🐌 Médio | 💰 Médio | 🔍 Média |
| **Performance** | ~15 testes | 🐌 Médio | 💰 Médio | 🔍 Média |
| **Segurança** | ~20 testes | 🐌 Médio | 💰 Médio | 🔍 Média |
| **Acessibilidade** | ~15 testes | 🐌 Médio | 💰 Médio | 🔍 Média |
| **E2E** | ~20 testes | 🐌 Lento | 💰 Alto | 🔍 Baixa |

## 📁 Estrutura de Arquivos

```
tests/
├── health_page_tests.robot      # Testes E2E (Robot Framework)
├── test_unit.py                 # Testes unitários
├── test_integration.py          # Testes de integração
├── test_performance.py          # Testes de performance
├── test_security.py             # Testes de segurança
├── test_accessibility.py        # Testes de acessibilidade
├── run_all_tests.py             # Script para executar todos os testes
└── README_TESTES.md             # Esta documentação
```

## 🧪 Testes Unitários (`test_unit.py`)

### Objetivo
Testar funções individuais de forma isolada, sem dependências externas.

### Cobertura
- **Calculadora de Calorias**: Validação de entrada, cálculos matemáticos
- **Calculadora de IMC**: Validação de entrada, cálculos matemáticos
- **Filtros de Receitas**: Lógica de filtragem, validação de parâmetros
- **Filtros de Exercícios**: Lógica de filtragem, validação de parâmetros
- **Rotas Flask**: Respostas HTTP, status codes
- **APIs REST**: Validação de JSON, respostas corretas

### Exemplo de Teste
```python
def test_calcular_calorias_homem_45_anos(self):
    """Testa cálculo de calorias para homem de 45 anos"""
    resultado = calcular_calorias(45, 70, 170, 'male', 'moderate')
    self.assertIsInstance(resultado, dict)
    self.assertIn('calorias', resultado)
    self.assertGreater(resultado['calorias'], 0)
```

## 🔗 Testes de Integração (`test_integration.py`)

### Objetivo
Testar a comunicação entre diferentes componentes da aplicação.

### Cobertura
- **Integração Frontend-Backend**: Formulários com APIs
- **Integração de Filtros**: Filtros com exibição de dados
- **Integração de Navegação**: Fluxo entre páginas
- **Integração de Dados**: Consistência de dados entre componentes
- **Integração de Responsividade**: Menu mobile em todas as páginas

### Exemplo de Teste
```python
def test_integracao_calculo_calorias_web(self):
    """Testa integração entre frontend e backend para cálculo de calorias"""
    dados_form = {'idade': 45, 'peso': 70, 'altura': 170, 'genero': 'male', 'atividade': 'moderate'}
    
    # Testa API
    response = self.client.post('/api/calcular-calorias', json=dados_form)
    resultado_api = response.get_json()
    
    # Testa função direta
    resultado_funcao = calcular_calorias(45, 70, 170, 'male', 'moderate')
    
    # Verifica consistência
    self.assertEqual(resultado_api['calorias'], resultado_funcao['calorias'])
```

## ⚡ Testes de Performance (`test_performance.py`)

### Objetivo
Garantir que a aplicação atende aos requisitos de performance.

### Cobertura
- **APIs**: Tempo de resposta < 1 segundo
- **Páginas**: Tempo de carregamento < 2 segundos
- **Cálculos**: Tempo de processamento < 100ms
- **Filtros**: Tempo de filtragem < 500ms
- **Concorrência**: Múltiplas requisições simultâneas

### Exemplo de Teste
```python
def test_performance_api_buscar_receitas(self):
    """Testa performance da API de busca de receitas"""
    start_time = time.time()
    response = self.client.get('/api/buscar-receitas?q=frango')
    end_time = time.time()
    
    response_time = end_time - start_time
    self.assertLess(response_time, 1.0, f"API demorou {response_time:.3f}s")
```

## 🔒 Testes de Segurança (`test_security.py`)

### Objetivo
Identificar vulnerabilidades de segurança comuns.

### Cobertura
- **Validação de Entrada**: Dados inválidos, valores negativos
- **Injeção SQL**: Tentativas de SQL injection
- **XSS**: Tentativas de cross-site scripting
- **Headers de Segurança**: Configurações de segurança HTTP
- **Autenticação**: Controle de acesso
- **Rate Limiting**: Proteção contra ataques de força bruta

### Exemplo de Teste
```python
def test_validacao_idade_negativa(self):
    """Testa validação de idade negativa"""
    dados = {'idade': -5, 'peso': 70, 'altura': 170, 'genero': 'male', 'atividade': 'moderate'}
    response = self.client.post('/api/calcular-calorias', json=dados)
    self.assertEqual(response.status_code, 400)
```

## ♿ Testes de Acessibilidade (`test_accessibility.py`)

### Objetivo
Garantir conformidade com padrões WCAG (Web Content Accessibility Guidelines).

### Cobertura
- **Estrutura Semântica**: HTML semântico, hierarquia de cabeçalhos
- **Formulários**: Labels, required attributes, tipos de input
- **Navegação**: Navegação por teclado, skip links
- **Imagens**: Alt text, imagens decorativas
- **Cores**: Contraste adequado, não dependência apenas de cores
- **JavaScript**: Funcionalidade sem JS, eventos de teclado
- **ARIA**: Atributos ARIA, landmarks

### Exemplo de Teste
```python
def test_labels_formulario_calorias(self):
    """Testa se todos os campos do formulário de calorias têm labels"""
    response = self.client.get('/calorias')
    html = response.data.decode('utf-8')
    
    self.assertIn('for="age-input"', html)
    self.assertIn('id="age-input"', html)
```

## 🌐 Testes End-to-End (`health_page_tests.robot`)

### Objetivo
Testar o comportamento completo da aplicação do ponto de vista do usuário.

### Cobertura
- **Navegação**: Carregamento de páginas, menu de navegação
- **Funcionalidades**: Calculadoras, filtros, busca
- **Responsividade**: Dispositivos móveis, menu mobile
- **Performance**: Tempo de carregamento
- **Acessibilidade**: Elementos básicos de acessibilidade

### Exemplo de Teste
```robotframework
Verificar Se A Página Principal Carrega Corretamente
    [Documentation]    Verifica se a página principal carrega com todos os elementos básicos
    [Tags]    navigation    smoke
    Open Browser    ${BASE_URL}    ${BROWSER}
    Wait Until Page Contains    Saúde e Bem-estar    timeout=${TIMEOUT}
    Page Should Contain    Controle de Calorias
    Page Should Contain    Receitas Saudáveis
    Page Should Contain    Exercícios para 40+
    Close Browser
```

## 🚀 Como Executar os Testes

### Executar Todos os Testes
```bash
python tests/run_all_tests.py
```

### Executar Testes Específicos

#### Testes Unitários
```bash
python -m unittest tests.test_unit
```

#### Testes de Integração
```bash
python -m unittest tests.test_integration
```

#### Testes de Performance
```bash
python -m unittest tests.test_performance
```

#### Testes de Segurança
```bash
python -m unittest tests.test_security
```

#### Testes de Acessibilidade
```bash
python -m unittest tests.test_accessibility
```

#### Testes E2E (Robot Framework)
```bash
robot tests/health_page_tests.robot
```

### Executar Testes por Tags (Robot Framework)
```bash
# Apenas testes de navegação
robot --include navigation tests/health_page_tests.robot

# Apenas testes de calculadora
robot --include calories tests/health_page_tests.robot

# Apenas testes de receitas
robot --include recipes tests/health_page_tests.robot

# Apenas testes de exercícios
robot --include exercises tests/health_page_tests.robot
```

## 📊 Relatórios e Resultados

### Relatório Automático
O script `run_all_tests.py` gera automaticamente:
- Relatório no console com estatísticas
- Arquivo `test_results/relatorio_teste.txt`
- Resultados detalhados do Robot Framework

### Exemplo de Relatório
```
📊 RELATÓRIO FINAL DOS TESTES
============================================================
Total de Suítes de Teste: 6
✅ Passaram: 6
❌ Falharam: 0
📈 Taxa de Sucesso: 100.0%

Detalhes por Categoria:
  Unitários: ✅ PASSOU
  Integração: ✅ PASSOU
  Performance: ✅ PASSOU
  Segurança: ✅ PASSOU
  Acessibilidade: ✅ PASSOU
  E2E (Robot): ✅ PASSOU

🎉 TODOS OS TESTES PASSARAM!
```

## 🔧 Configuração e Dependências

### Dependências Necessárias
```bash
pip install flask
pip install selenium
pip install robotframework
pip install robotframework-seleniumlibrary
```

### Configuração do Ambiente
1. **Python**: Versão 3.7 ou superior
2. **Chrome/Chromium**: Para testes E2E
3. **ChromeDriver**: Compatível com a versão do Chrome

### Variáveis de Ambiente
```bash
# Para testes E2E
export BASE_URL=http://localhost:5000
export BROWSER=chrome
export TIMEOUT=20s
```

## 📈 Métricas de Qualidade

### Cobertura de Código
- **Testes Unitários**: ~90% de cobertura
- **Testes de Integração**: ~80% de cobertura
- **Testes E2E**: ~70% de cobertura

### Performance Benchmarks
- **APIs**: < 1 segundo
- **Páginas**: < 2 segundos
- **Cálculos**: < 100ms
- **Filtros**: < 500ms

### Critérios de Aceitação
- ✅ Todos os testes unitários passam
- ✅ Todos os testes de integração passam
- ✅ Performance dentro dos limites
- ✅ Sem vulnerabilidades de segurança críticas
- ✅ Conformidade com WCAG 2.1 AA
- ✅ Testes E2E passam em diferentes navegadores

## 🛠️ Manutenção dos Testes

### Boas Práticas
1. **Nomes Descritivos**: Use nomes claros para testes
2. **Documentação**: Documente o propósito de cada teste
3. **Isolamento**: Testes devem ser independentes
4. **Dados de Teste**: Use dados específicos para testes
5. **Limpeza**: Limpe dados após cada teste

### Atualização de Testes
- Atualize testes quando adicionar novas funcionalidades
- Revise testes quando modificar APIs
- Mantenha testes de performance atualizados
- Verifique testes de segurança regularmente

## 🎯 Benefícios da Pirâmide de Testes

### Para Desenvolvedores
- **Feedback Rápido**: Testes unitários executam em segundos
- **Confiança**: Cobertura abrangente garante qualidade
- **Refatoração Segura**: Mudanças são testadas automaticamente
- **Documentação Viva**: Testes documentam o comportamento esperado

### Para o Projeto
- **Qualidade**: Reduz bugs em produção
- **Manutenibilidade**: Facilita mudanças futuras
- **Performance**: Identifica problemas de performance cedo
- **Segurança**: Detecta vulnerabilidades antes do deploy

### Para Usuários
- **Confiabilidade**: Aplicação mais estável
- **Acessibilidade**: Usável por pessoas com deficiências
- **Performance**: Carregamento rápido
- **Segurança**: Dados protegidos

## 📚 Recursos Adicionais

### Documentação
- [Robot Framework User Guide](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html)
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)

### Ferramentas Recomendadas
- **Coverage.py**: Para medir cobertura de código
- **Pytest**: Framework alternativo para testes Python
- **Lighthouse**: Para testes de acessibilidade e performance
- **OWASP ZAP**: Para testes de segurança automatizados

---

*Esta documentação é mantida atualizada conforme a evolução do projeto.* 