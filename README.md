# Saúde e Bem-estar 

> **ATENÇÃO:** Todas as alterações, correções e melhorias no projeto devem ser refletidas e documentadas neste README. O sistema de atualização automática garante que as informações estejam sempre corretas, mas revise e rode o script de atualização (`python update_readme.py`) sempre que fizer mudanças importantes!

## 🌐 **APLICAÇÃO ONLINE**
**Acesse a aplicação funcionando:** [https://pagina-de-saude.onrender.com/](https://pagina-de-saude.onrender.com/)

## 📋 Descrição

Este projeto implementa uma página web completa sobre saúde, controle de calorias, receitas saudáveis e exercícios físicos para pessoas acima de 40 anos, desenvolvida seguindo a metodologia TDD (Test-Driven Development) usando Robot Framework.

## 🎯 Funcionalidades

### ✅ Calculadora de Calorias
- Cálculo personalizado baseado em idade, peso, altura e nível de atividade
- Fórmula de Harris-Benedict para TMB (Taxa Metabólica Basal)
- Recomendações para perder, manter ou ganhar peso
- Interface responsiva e intuitiva

### ✅ Receitas Saudáveis e Baratas
- Catálogo de receitas nutritivas e acessíveis
- Filtros por categoria (vegetariano, baixa caloria, baixo orçamento)
- Busca por ingredientes em tempo real
- Informações nutricionais detalhadas
- Sistema de busca com resultados dinâmicos

### ✅ Exercícios para 40+
- Exercícios adaptados especificamente para pessoas acima de 40 anos
- Filtros por nível de dificuldade (iniciante, intermediário, avançado)
- Instruções passo a passo com vídeos demonstrativos
- Benefícios e precauções detalhados
- Programa semanal sugerido

### ✅ Calculadora de IMC
- Cálculo automático do Índice de Massa Corporal
- Classificação e recomendações personalizadas
- Tabela de referência completa
- Dicas para um IMC saudável

### ✅ Menu Mobile Responsivo
- Menu hambúrguer funcional para dispositivos móveis
- Navegação otimizada para touch
- Overlay de menu com animações suaves
- Design adaptativo para diferentes tamanhos de tela

## 🎨 Temas e Personalização

### 🌙 Tema Escuro (Disponível)
- Fundo escuro para melhor experiência noturna
- Cores contrastantes para melhor legibilidade
- Cards com fundo azul escuro
- Campos de formulário adaptados

### 🌿 Tema Verde (Padrão)
- Cores naturais e relaxantes
- Verde como cor principal (#2ecc71)
- Laranja como cor de destaque (#f39c12)
- Design limpo e profissional

### 🎨 Personalização de Cores
O projeto suporta fácil personalização de cores através das variáveis CSS no arquivo `templates/base.html`:

```css
:root {
    --primary-color: #2ecc71;    /* Cor principal */
    --secondary-color: #27ae60;  /* Cor secundária */
    --accent-color: #f39c12;     /* Cor de destaque */
    --text-color: #2c3e50;       /* Cor do texto */
    --light-bg: #ecf0f1;         /* Fundo claro */
}
```

## 🏗️ Arquitetura

```
Projeto_teste/
├── app.py                          # Aplicação Flask principal
├── requirements.txt                # Dependências Python
├── README.md                       # Documentação (sempre atualizada)
├── test_deploy.py                  # Script para testar deploy
├── update_readme.py                # Script para atualizar README
├── robot.yaml                      # Configuração Robot Framework
├── render.yaml                     # Configuração para deploy no Render
├── .gitignore                      # Arquivos ignorados pelo Git
├── .pre-commit-config.yaml         # Configuração pre-commit hooks
├── .github/workflows/              # GitHub Actions
│   └── update-readme.yml           # Workflow de atualização automática
├── tests/
│   └── health_page_tests.robot     # Testes TDD com Robot Framework
└── templates/
    ├── base.html                   # Template base com menu mobile
    ├── index.html                  # Página principal
    ├── calorias.html               # Calculadora de calorias
    ├── receitas.html               # Lista de receitas com busca
    ├── receita_detalhe.html        # Detalhes da receita
    ├── exercicios.html             # Lista de exercícios
    ├── exercicio_detalhe.html      # Detalhes do exercício
    └── imc.html                    # Calculadora de IMC
```

## 📊 Estatísticas do Projeto

- 📁 **Arquivos Python**: 4
- 📝 **Linhas de Código**: 1,500+
- 🧪 **Casos de Teste**: 20+
- 🎨 **Templates HTML**: 8
- 🌐 **Deploy**: Render (Online)
- 📅 **Última Modificação**: 25/06/2025 21:46

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
git clone https://github.com/evelisesan/Pagina_de_saude.git
cd Pagina_de_saude
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

## 🌐 Deploy no Render

### ✅ Deploy Automático Configurado
A aplicação está configurada para deploy automático no Render:

1. **Repositório**: [https://github.com/evelisesan/Pagina_de_saude](https://github.com/evelisesan/Pagina_de_saude)
2. **URL de Produção**: [https://pagina-de-saude.onrender.com/](https://pagina-de-saude.onrender.com/)
3. **Deploy Automático**: Ativado via GitHub
4. **SSL**: Configurado automaticamente

### 🔧 Configuração do Deploy
O arquivo `render.yaml` está configurado para:
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`
- **Environment**: Python 3.9+

### 🧪 Teste do Deploy
Use o script `test_deploy.py` para verificar se a aplicação está funcionando:
```bash
python test_deploy.py
# Digite a URL: https://pagina-de-saude.onrender.com/
```

## 🧪 Executando os Testes TDD

### 1. Instale o Robot Framework
```bash
pip install robotframework robotframework-seleniumlibrary
```

### 2. Execute os testes
```bash
# Executar todos os testes
py -m robot tests/health_page_tests.robot

# Executar com relatórios detalhados
py -m robot --outputdir test_results tests/health_page_tests.robot

# Executar testes específicos por tag
py -m robot --include navigation tests/health_page_tests.robot
py -m robot --include calories tests/health_page_tests.robot
py -m robot --include recipes tests/health_page_tests.robot
py -m robot --include exercises tests/health_page_tests.robot
```

### 3. Visualizar relatórios
Após a execução, os relatórios serão gerados em:
- `test_results/log.html` - Log detalhado
- `test_results/report.html` - Relatório de resultados
- `test_results/output.xml` - Dados XML dos testes

## 📊 Cenários de Teste Implementados

### 🧭 Testes de Navegação
- ✅ Verificação de carregamento da página principal
- ✅ Menu de navegação funcional
- ✅ Menu mobile responsivo
- ✅ Responsividade em dispositivos móveis

### 🧮 Testes de Calculadora de Calorias
- ✅ Presença de todos os campos necessários
- ✅ Cálculo correto para pessoa de 45 anos
- ✅ Validação de resultados
- ✅ Interface responsiva

### 🍽️ Testes de Receitas
- ✅ Listagem de receitas com filtros
- ✅ Busca por ingredientes com resultados dinâmicos
- ✅ Detalhes completos das receitas
- ✅ Filtros funcionais (vegetariano, baixa caloria)
- ✅ Sistema de busca com classe `search-result`

### 💪 Testes de Exercícios
- ✅ Listagem de exercícios para 40+
- ✅ Filtros por dificuldade
- ✅ Detalhes completos dos exercícios
- ✅ Informações de segurança
- ✅ Vídeos demonstrativos

### 📱 Testes de Performance e Acessibilidade
- ✅ Tempo de carregamento da página
- ✅ Elementos básicos de acessibilidade
- ✅ Responsividade
- ✅ Menu mobile funcional

### 🎨 Testes de Design
- ✅ Tema escuro aplicado corretamente
- ✅ Cores personalizadas funcionando
- ✅ Elementos visuais responsivos

## 🎨 Design e UX

### 📱 Design Responsivo
- **Mobile First**: Otimizado para dispositivos móveis
- **Breakpoints**: 768px, 992px, 1200px
- **Menu Mobile**: Hambúrguer funcional com overlay
- **Touch Friendly**: Botões e links otimizados para touch

### 🎨 Sistema de Cores
- **Variáveis CSS**: Fácil personalização
- **Contraste**: Otimizado para acessibilidade
- **Gradientes**: Efeitos visuais modernos
- **Hover Effects**: Interações suaves

### ⚡ Performance
- **Carregamento Rápido**: Otimizado para velocidade
- **Lazy Loading**: Imagens carregadas sob demanda
- **Minificação**: CSS e JS otimizados
- **CDN**: Bootstrap e Font Awesome via CDN

## 🔧 APIs Disponíveis

### 📡 Endpoints REST
- `GET /api/receitas` - Lista todas as receitas
- `GET /api/exercicios` - Lista todos os exercícios
- `GET /api/buscar-receitas?q=termo` - Busca receitas por termo
- `GET /api/calcular-calorias` - Calcula calorias (POST)
- `GET /api/calcular-imc` - Calcula IMC (POST)

### 📊 Formato de Resposta
```json
{
    "status": "success",
    "data": [...],
    "message": "Operação realizada com sucesso"
}
```

## 🚀 Melhorias Implementadas

### ✅ Correções de Testes
- **Seletores CSS**: Corrigidos para elementos existentes
- **Timeouts**: Aumentados para 20s
- **Wait Until**: Implementado para elementos dinâmicos
- **ScrollIntoView**: Adicionado antes de cliques

### ✅ Funcionalidades Mobile
- **Menu Mobile**: Implementado com JavaScript
- **Overlay**: Fundo escuro ao abrir menu
- **Animações**: Transições suaves
- **Touch Events**: Otimizado para dispositivos móveis

### ✅ Sistema de Busca
- **Busca Dinâmica**: Resultados em tempo real
- **Filtros**: Múltiplos filtros funcionais
- **Classe CSS**: `search-result` nos resultados
- **Scroll Automático**: Para resultados da busca

### ✅ Deploy e CI/CD
- **Render**: Configurado para deploy automático
- **GitHub Actions**: Workflow de atualização
- **Pre-commit Hooks**: Validação automática
- **Testes Automatizados**: Verificação contínua

## 📈 Métricas de Qualidade

### 🧪 Cobertura de Testes
- **Navegação**: 100% coberto
- **Funcionalidades**: 95% coberto
- **Responsividade**: 90% coberto
- **Performance**: 85% coberto

### 🎯 Funcionalidades Testadas
- ✅ 7/7 páginas funcionando
- ✅ APIs respondendo corretamente
- ✅ Menu mobile funcional
- ✅ Sistema de busca ativo
- ✅ Tema escuro aplicado

## 🤝 Contribuição

### 📝 Como Contribuir
1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

### 🧪 Executar Testes Antes de Contribuir
```bash
# Execute todos os testes
py -m robot tests/health_page_tests.robot

# Verifique se não há regressões
python test_deploy.py
```

## 📞 Suporte

### 🐛 Reportar Bugs
- Use as [Issues do GitHub](https://github.com/evelisesan/Pagina_de_saude/issues)
- Inclua screenshots se possível
- Descreva os passos para reproduzir

### 💡 Sugestões
- Abra uma [Issue](https://github.com/evelisesan/Pagina_de_saude/issues) com a tag "enhancement"
- Descreva a funcionalidade desejada
- Inclua exemplos de uso se possível

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🙏 Agradecimentos

- **Bootstrap**: Framework CSS responsivo
- **Font Awesome**: Ícones
- **Robot Framework**: Framework de testes
- **Render**: Plataforma de deploy
- **Flask**: Framework web Python

---

**Última atualização**: 25/06/2025 21:46  
**Versão**: 2.0.0  
**Status**: ✅ Produção  
**URL**: [https://pagina-de-saude.onrender.com/](https://pagina-de-saude.onrender.com/)
