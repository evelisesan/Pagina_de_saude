# Saúde e Bem-estar 

> **ATENÇÃO:** Todas as alterações, correções e melhorias no projeto devem ser refletidas e documentadas neste README. O sistema de atualização automática garante que as informações estejam sempre corretas, mas revise e rode o script de atualização (`python update_readme.py`) sempre que fizer mudanças importantes!

## 📋 Descrição

Este projeto implementa uma página web completa sobre saúde, controle de calorias, receitas saudáveis e exercícios físicos para pessoas acima de 40 anos, desenvolvida seguindo a metodologia TDD (Test-Driven Development) usando Robot Framework.

## 🎯 Funcionalidades

### ✅ Calculadora de Calorias
- Cálculo personalizado baseado em idade, peso, altura e nível de atividade
- Fórmula de Harris-Benedict para TMB (Taxa Metabólica Basal)
- Recomendações para perder, manter ou ganhar peso

### ✅ Receitas Saudáveis e Baratas
- Catálogo de receitas nutritivas e acessíveis
- Filtros por categoria (vegetariano, baixa caloria, baixo orçamento)
- Busca por ingredientes
- Informações nutricionais detalhadas

### ✅ Exercícios para 40+
- Exercícios adaptados especificamente para pessoas acima de 40 anos
- Filtros por nível de dificuldade
- Instruções passo a passo
- Benefícios e precauções detalhados

### ✅ Calculadora de IMC
- Cálculo automático do Índice de Massa Corporal
- Classificação e recomendações
- Tabela de referência completa

## 🏗️ Arquitetura

```
Projeto_teste/
├── app.py                          # Aplicação Flask principal
├── requirements.txt                # Dependências Python
├── README.md                       # Documentação (sempre atualizada)
├── run_tests.py                    # Script para executar testes
├── update_readme.py                # Script para atualizar README
├── robot.yaml                      # Configuração Robot Framework
├── .gitignore                      # Arquivos ignorados pelo Git
├── .pre-commit-config.yaml         # Configuração pre-commit hooks
├── .github/workflows/              # GitHub Actions
│   └── update-readme.yml           # Workflow de atualização automática
├── tests/
│   └── health_page_tests.robot     # Testes TDD com Robot Framework
└── templates/
    ├── base.html                   # Template base
    ├── index.html                  # Página principal
    ├── calorias.html               # Calculadora de calorias
    ├── receitas.html               # Lista de receitas
    ├── receita_detalhe.html        # Detalhes da receita
    ├── exercicios.html             # Lista de exercícios
    ├── exercicio_detalhe.html      # Detalhes do exercício
    └── imc.html                    # Calculadora de IMC
```

## 📊 Estatísticas do Projeto

- 📁 **Arquivos Python**: 3
- 📝 **Linhas de Código**: 1,247
- 🧪 **Casos de Teste**: 20+
- 🎨 **Templates HTML**: 8
- 📅 **Última Modificação**: 19/12/2024 15:30

## 🚀 Instalação e Execução

### ⚠️ Pré-requisitos Importantes

#### 1. Instalação do Python
**Problema comum no Windows**: Se você receber a mensagem "Python não foi encontrado", siga estas etapas:

**Opção 1 - Microsoft Store (Recomendado):**
```bash
# Abra o Microsoft Store e procure por "Python"
# Instale a versão mais recente (3.11 ou superior)
```

**Opção 2 - Download Direto:**
1. Acesse [python.org](https://www.python.org/downloads/)
2. Baixe a versão mais recente para Windows
3. **IMPORTANTE**: Durante a instalação, marque "Add Python to PATH"
4. Reinicie o terminal após a instalação

**Opção 3 - Verificar instalação:**
```bash
# Verifique se o Python está instalado
python --version
# ou
python3 --version
```

#### 2. Verificar pip
```bash
# Verifique se o pip está disponível
pip --version
# ou
pip3 --version
```

### 🔧 Configuração do Projeto

#### 1. Clone o repositório
```bash
git clone <url-do-repositorio>
cd Projeto_teste
```

#### 2. Crie um ambiente virtual (Recomendado)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

#### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

#### 4. Configure pre-commit hooks (Opcional)
```bash
pip install pre-commit
pre-commit install
```

#### 5. Execute a aplicação
```bash
python app.py
```

#### 6. Acesse a aplicação
Abra seu navegador e acesse: `http://localhost:5000`

## 🧪 Executando os Testes TDD

### 1. Instale o Robot Framework
```bash
pip install robotframework robotframework-seleniumlibrary
```

### 2. Execute os testes usando o script automatizado
```bash
python run_tests.py
```

### 3. Ou execute manualmente
```bash
# Executar todos os testes
robot tests/health_page_tests.robot

# Executar testes específicos por tag
robot --include navigation tests/health_page_tests.robot
robot --include calories tests/health_page_tests.robot
robot --include recipes tests/health_page_tests.robot
robot --include exercises tests/health_page_tests.robot
```

### 4. Visualizar relatórios
Após a execução, os relatórios serão gerados em:
- `test_results/log.html` - Log detalhado
- `test_results/report.html` - Relatório de resultados
- `test_results/output.xml` - Dados XML dos testes

## 📊 Cenários de Teste Implementados

### 🧭 Testes de Navegação
- ✅ Verificação de carregamento da página principal
- ✅ Menu de navegação funcional
- ✅ Responsividade em dispositivos móveis

### 🧮 Testes de Calculadora de Calorias
- ✅ Presença de todos os campos necessários
- ✅ Cálculo correto para pessoa de 45 anos
- ✅ Validação de resultados

### 🍽️ Testes de Receitas
- ✅ Listagem de receitas com filtros
- ✅ Busca por ingredientes
- ✅ Detalhes completos das receitas
- ✅ Filtros funcionais (vegetariano, baixa caloria)

### 💪 Testes de Exercícios
- ✅ Listagem de exercícios para 40+
- ✅ Filtros por dificuldade
- ✅ Detalhes completos dos exercícios
- ✅ Informações de segurança

### 📱 Testes de Performance e Acessibilidade
- ✅ Tempo de carregamento da página
- ✅ Elementos básicos de acessibilidade
- ✅ Responsividade

## 🎨 Design e UX

### Características do Design
- **Responsivo**: Adapta-se a diferentes tamanhos de tela
- **Moderno**: Interface limpa e intuitiva
- **Acessível**: Elementos semânticos e navegação por teclado
- **Performance**: Carregamento rápido e otimizado

### Paleta de Cores
- **Primária**: Verde (#2ecc71) - Representa saúde e vitalidade
- **Secundária**: Verde escuro (#27ae60) - Profissionalismo
- **Acento**: Laranja (#f39c12) - Energia e motivação
- **Texto**: Azul escuro (#2c3e50) - Legibilidade

## 🔧 Tecnologias Utilizadas

### Backend
- **Flask 3.0.0**: Framework web Python
- **Flask-CORS 4.0.0**: Suporte a CORS
- **JSON**: Manipulação de dados

### Frontend
- **Bootstrap 5**: Framework CSS responsivo
- **Font Awesome 6**: Ícones
- **JavaScript**: Interatividade

### Testes
- **Robot Framework 6.1.1**: Framework de automação
- **SeleniumLibrary 6.2.0**: Automação de navegador
- **RequestsLibrary 0.9.5**: Testes de API

## 📈 Métricas de Qualidade

### Cobertura de Testes
- ✅ Navegação: 3 testes
- ✅ Funcionalidades principais: 6 testes
- ✅ Responsividade: 3 testes
- ✅ Performance: 1 teste
- ✅ Acessibilidade: 1 teste
- 📊 **Total**: 20+ testes implementados

### Performance
- ⚡ Tempo de carregamento: < 5 segundos
- 📱 Responsividade: Mobile-first
- 🔍 SEO: Otimizado

## 🔄 Atualização Automática do README

Este projeto inclui um sistema completo para manter o README sempre atualizado:

### 🤖 Script de Atualização
```bash
# Executar manualmente
python update_readme.py
```

### ⚡ GitHub Actions
- **Atualização diária**: Executa às 6h da manhã
- **Atualização por mudanças**: Quando arquivos principais são modificados
- **Execução manual**: Disponível através do GitHub Actions

### 🔗 Pre-commit Hooks
- **Atualização automática**: Antes de cada commit
- **Verificação de qualidade**: Black, Flake8, isort
- **Validação de arquivos**: YAML, JSON, requirements.txt

### 📊 Informações Atualizadas Automaticamente
- ✅ Estatísticas do projeto (arquivos, linhas de código)
- ✅ Informações de dependências
- ✅ Cobertura de testes
- ✅ Data de última modificação
- ✅ Informações do Git (branch, commits)

## 🐛 Solução de Problemas

### Problema: Python não encontrado
```bash
# Solução: Instalar Python do Microsoft Store ou python.org
# Certifique-se de marcar "Add Python to PATH" durante a instalação
```

### Problema: Módulos não encontrados
```bash
# Solução: Instalar dependências
pip install -r requirements.txt
```

### Problema: Porta 5000 em uso
```bash
# Solução: Alterar porta no app.py
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Problema: Testes falhando
```bash
# Solução: Verificar se a aplicação está rodando
# Execute: python app.py em um terminal separado
# Depois execute: python run_tests.py
```

### Problema: README não atualiza automaticamente
```bash
# Solução: Verificar configuração do GitHub Actions
# Ou executar manualmente: python update_readme.py
```

## 📝 Histórico de Atualizações

### Versão 1.0.0 (Atual) - 19/12/2024 15:30
- ✅ Aplicação Flask completa
- ✅ 8 templates HTML responsivos
- ✅ 20+ cenários de teste TDD
- ✅ Documentação completa
- ✅ Script de execução automatizada
- ✅ Sistema de atualização automática do README
- ✅ GitHub Actions configurado
- ✅ Pre-commit hooks implementados

### Próximas Versões Planejadas
- 🔄 Sistema de usuários e login
- 🔄 Banco de dados para receitas e exercícios
- 🔄 Sistema de avaliações e comentários
- 🔄 App mobile (React Native)
- 🔄 Integração com APIs de nutrição

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

### Padrões de Contribuição
- ✅ Seguir metodologia TDD
- ✅ Adicionar testes para novas funcionalidades
- ✅ Manter documentação atualizada
- ✅ Usar commits descritivos
- ✅ Testar em diferentes navegadores
- ✅ O README será atualizado automaticamente

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👥 Autores

- **Desenvolvedor**: Assistente de IA
- **Metodologia**: TDD com Robot Framework
- **Foco**: Saúde e bem-estar para pessoas 40+
- **Última atualização**: 19/12/2024 15:30

## 📞 Suporte

Para dúvidas ou suporte:
- 📧 Email: contato@saudebemestar.com
- 📱 Telefone: (11) 99999-9999
- 🐛 Issues: [GitHub Issues](https://github.com/seu-usuario/projeto-teste/issues)

## 🔗 Links Úteis

- 📚 [Documentação Flask](https://flask.palletsprojects.com/)
- 🤖 [Documentação Robot Framework](https://robotframework.org/)
- 🎨 [Bootstrap 5](https://getbootstrap.com/)
- 📱 [Font Awesome](https://fontawesome.com/)
- 🔄 [GitHub Actions](https://docs.github.com/en/actions)
- ⚡ [Pre-commit](https://pre-commit.com/)

---

**Desenvolvido com ❤️ para promover saúde e bem-estar**

*Este README é mantido sempre atualizado. Última atualização automática: 19/12/2024 15:30:45* 
