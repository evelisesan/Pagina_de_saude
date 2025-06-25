# 📝 Guia para Manter o README Sempre Atualizado

Este documento explica como o sistema de atualização automática do README funciona e como contribuir para mantê-lo sempre atualizado.

## 🤖 Sistema de Atualização Automática

### Arquivos do Sistema
- `update_readme.py` - Script principal de atualização
- `.github/workflows/update-readme.yml` - GitHub Actions
- `.pre-commit-config.yaml` - Pre-commit hooks
- `MAINTAIN_README.md` - Este guia

## 🔄 Como Funciona

### 1. Atualização Manual
```bash
# Execute o script manualmente
python update_readme.py
```

### 2. Atualização Automática via GitHub Actions
- **Diária**: Executa às 6h da manhã
- **Por mudanças**: Quando arquivos principais são modificados
- **Manual**: Disponível no GitHub Actions

### 3. Atualização via Pre-commit Hooks
- **Automática**: Antes de cada commit
- **Verificação**: Qualidade do código e documentação

## 📊 Informações Atualizadas Automaticamente

### Estatísticas do Projeto
- 📁 Número de arquivos Python
- 📝 Linhas de código
- 🧪 Casos de teste
- 🎨 Templates HTML
- 📅 Data de última modificação

### Dependências
- Versões das bibliotecas Python
- Compatibilidade de versões
- Novas dependências adicionadas

### Testes
- Cobertura de testes por categoria
- Total de testes implementados
- Status dos testes (passando/falhando)

### Git
- Branch atual
- Último commit
- Número total de commits

## 🛠️ Como Contribuir

### 1. Adicionar Novos Testes
Ao adicionar novos testes, use tags organizadas:

```robotframework
*** Test Cases ***
Novo Teste De Funcionalidade
    [Documentation]    Descrição do teste
    [Tags]    nova-funcionalidade    smoke
    # ... implementação do teste
```

### 2. Atualizar Dependências
Ao atualizar `requirements.txt`:
```bash
# O script detectará automaticamente as mudanças
# e atualizará as versões no README
```

### 3. Adicionar Novos Templates
Ao adicionar novos templates HTML:
```bash
# O script contará automaticamente os novos arquivos
# e atualizará as estatísticas
```

### 4. Modificar Funcionalidades
Ao modificar `app.py`:
```bash
# O script detectará as mudanças
# e atualizará a data de última modificação
```

## 🔧 Configuração Local

### Instalar Pre-commit Hooks
```bash
pip install pre-commit
pre-commit install
```

### Configurar Git Hooks
```bash
# Os hooks serão instalados automaticamente
# quando você executar pre-commit install
```

### Verificar Configuração
```bash
# Verificar se os hooks estão funcionando
pre-commit run --all-files
```

## 📋 Checklist de Manutenção

### Antes de Fazer Commit
- [ ] Execute `python update_readme.py`
- [ ] Verifique se as estatísticas estão corretas
- [ ] Confirme que a data foi atualizada
- [ ] Teste se os links funcionam

### Semanalmente
- [ ] Verifique se o GitHub Actions está funcionando
- [ ] Revise as estatísticas do projeto
- [ ] Atualize informações de versão se necessário

### Mensalmente
- [ ] Revise a seção de próximas versões
- [ ] Atualize links e referências
- [ ] Verifique se todas as funcionalidades estão documentadas

## 🐛 Solução de Problemas

### Problema: Script não executa
```bash
# Verificar se o Python está instalado
python --version

# Verificar se as dependências estão instaladas
pip install -r requirements.txt
```

### Problema: GitHub Actions falha
```bash
# Verificar logs no GitHub
# Verificar se o arquivo .github/workflows/update-readme.yml existe
# Verificar permissões do repositório
```

### Problema: Pre-commit não funciona
```bash
# Reinstalar hooks
pre-commit uninstall
pre-commit install

# Verificar configuração
pre-commit run --all-files
```

### Problema: Estatísticas incorretas
```bash
# Verificar se os arquivos estão sendo contados corretamente
# Verificar se há arquivos em .gitignore que deveriam ser contados
# Executar script manualmente para debug
python update_readme.py --debug
```

## 📈 Métricas de Qualidade do README

### Indicadores de Qualidade
- ✅ **Atualização**: README atualizado nas últimas 24h
- ✅ **Completude**: Todas as seções preenchidas
- ✅ **Precisão**: Estatísticas corretas
- ✅ **Links**: Todos os links funcionando
- ✅ **Formatação**: Markdown bem formatado

### Relatórios Automáticos
- 📊 Estatísticas atualizadas diariamente
- 🔄 Data de última modificação
- 📝 Contagem de linhas de código
- 🧪 Cobertura de testes

## 🎯 Boas Práticas

### Para Desenvolvedores
1. **Sempre execute** o script de atualização antes de commitar
2. **Mantenha as tags** dos testes organizadas
3. **Documente mudanças** importantes
4. **Teste links** antes de commitar

### Para Mantenedores
1. **Revise semanalmente** as estatísticas
2. **Atualize roadmap** conforme necessário
3. **Monitore GitHub Actions** para falhas
4. **Mantenha documentação** de configuração

### Para Contribuidores
1. **Siga o padrão** de commits
2. **Adicione testes** para novas funcionalidades
3. **Atualize documentação** quando necessário
4. **Use pre-commit hooks** localmente

## 📞 Suporte

Se você encontrar problemas com o sistema de atualização:

1. **Verifique logs** do GitHub Actions
2. **Execute manualmente** o script de atualização
3. **Abra uma issue** no repositório
4. **Consulte** este guia de manutenção

## 🔗 Links Úteis

- 📚 [Documentação do Robot Framework](https://robotframework.org/)
- 🔄 [GitHub Actions Documentation](https://docs.github.com/en/actions)
- ⚡ [Pre-commit Documentation](https://pre-commit.com/)
- 📝 [Markdown Guide](https://www.markdownguide.org/)

---

**Este guia é parte do sistema de manutenção automática do README. Mantenha-o atualizado conforme necessário.** 