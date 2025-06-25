#!/usr/bin/env python3
"""
Script para manter o README sempre atualizado
Atualiza automaticamente informações do projeto no README.md
"""

import os
import re
import subprocess
import json
from datetime import datetime
from pathlib import Path

class ReadmeUpdater:
    def __init__(self):
        self.project_root = Path(".")
        self.readme_path = self.project_root / "README.md"
        self.requirements_path = self.project_root / "requirements.txt"
        self.app_path = self.project_root / "app.py"
        self.tests_path = self.project_root / "tests"
        self.templates_path = self.project_root / "templates"
        
    def get_project_stats(self):
        """Coleta estatísticas do projeto"""
        stats = {
            "files_count": 0,
            "lines_of_code": 0,
            "test_cases": 0,
            "templates": 0,
            "last_modified": None
        }
        
        # Conta arquivos Python
        for py_file in self.project_root.rglob("*.py"):
            if "venv" not in str(py_file) and "__pycache__" not in str(py_file):
                stats["files_count"] += 1
                try:
                    with open(py_file, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        stats["lines_of_code"] += len(lines)
                except:
                    pass
        
        # Conta templates HTML
        for html_file in self.templates_path.rglob("*.html"):
            stats["templates"] += 1
        
        # Conta casos de teste no Robot Framework
        robot_file = self.tests_path / "health_page_tests.robot"
        if robot_file.exists():
            try:
                with open(robot_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Conta Test Cases
                    test_cases = re.findall(r'^\*\* Test Cases \*\*', content, re.MULTILINE)
                    stats["test_cases"] = len(test_cases)
            except:
                pass
        
        # Data de última modificação
        latest_time = 0
        for file_path in self.project_root.rglob("*"):
            if file_path.is_file() and "venv" not in str(file_path):
                mtime = file_path.stat().st_mtime
                if mtime > latest_time:
                    latest_time = mtime
        
        if latest_time > 0:
            stats["last_modified"] = datetime.fromtimestamp(latest_time).strftime("%d/%m/%Y %H:%M")
        
        return stats
    
    def get_dependencies_info(self):
        """Obtém informações das dependências"""
        deps = {}
        if self.requirements_path.exists():
            try:
                with open(self.requirements_path, 'r') as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith('#'):
                            if '==' in line:
                                name, version = line.split('==')
                                deps[name] = version
                            else:
                                deps[line] = "latest"
            except:
                pass
        return deps
    
    def get_git_info(self):
        """Obtém informações do Git"""
        git_info = {
            "branch": "main",
            "last_commit": "N/A",
            "commit_count": 0
        }
        
        try:
            # Branch atual
            result = subprocess.run(['git', 'branch', '--show-current'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                git_info["branch"] = result.stdout.strip()
            
            # Último commit
            result = subprocess.run(['git', 'log', '-1', '--format=%h - %s (%cr)'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                git_info["last_commit"] = result.stdout.strip()
            
            # Número de commits
            result = subprocess.run(['git', 'rev-list', '--count', 'HEAD'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                git_info["commit_count"] = int(result.stdout.strip())
                
        except:
            pass
        
        return git_info
    
    def update_version_info(self, content):
        """Atualiza informações de versão"""
        stats = self.get_project_stats()
        deps = self.get_dependencies_info()
        git_info = self.get_git_info()
        
        # Atualiza data de última modificação
        if stats["last_modified"]:
            content = re.sub(
                r'- \*\*Última atualização\*\*: .*',
                f'- **Última atualização**: {stats["last_modified"]}',
                content
            )
        
        # Atualiza estatísticas do projeto
        content = re.sub(
            r'### Versão 1\.0\.0 \(Atual\)',
            f'### Versão 1.0.0 (Atual) - {stats["last_modified"] or "N/A"}',
            content
        )
        
        # Atualiza informações de dependências
        if 'Flask' in deps:
            content = re.sub(
                r'- \*\*Flask\*\*: Framework web Python',
                f'- **Flask {deps.get("flask", "3.0.0")}**: Framework web Python',
                content
            )
        
        if 'robotframework' in deps:
            content = re.sub(
                r'- \*\*Robot Framework\*\*: Framework de automação',
                f'- **Robot Framework {deps.get("robotframework", "6.1.1")}**: Framework de automação',
                content
            )
        
        return content
    
    def update_project_stats(self, content):
        """Atualiza estatísticas do projeto"""
        stats = self.get_project_stats()
        
        # Adiciona seção de estatísticas se não existir
        if "## 📊 Estatísticas do Projeto" not in content:
            stats_section = f"""
## 📊 Estatísticas do Projeto

- 📁 **Arquivos Python**: {stats['files_count']}
- 📝 **Linhas de Código**: {stats['lines_of_code']:,}
- 🧪 **Casos de Teste**: {stats['test_cases']}
- 🎨 **Templates HTML**: {stats['templates']}
- 📅 **Última Modificação**: {stats['last_modified'] or 'N/A'}

"""
            # Insere após a seção de arquitetura
            content = re.sub(
                r'(## 🚀 Instalação e Execução)',
                f'{stats_section}\\1',
                content
            )
        else:
            # Atualiza estatísticas existentes
            content = re.sub(
                r'- 📁 \*\*Arquivos Python\*\*: \d+',
                f'- 📁 **Arquivos Python**: {stats["files_count"]}',
                content
            )
            content = re.sub(
                r'- 📝 \*\*Linhas de Código\*\*: [\d,]+',
                f'- 📝 **Linhas de Código**: {stats["lines_of_code"]:,}',
                content
            )
            content = re.sub(
                r'- 🧪 \*\*Casos de Teste\*\*: \d+',
                f'- 🧪 **Casos de Teste**: {stats["test_cases"]}',
                content
            )
            content = re.sub(
                r'- 🎨 \*\*Templates HTML\*\*: \d+',
                f'- 🎨 **Templates HTML**: {stats["templates"]}',
                content
            )
            content = re.sub(
                r'- 📅 \*\*Última Modificação\*\*: .*',
                f'- 📅 **Última Modificação**: {stats["last_modified"] or "N/A"}',
                content
            )
        
        return content
    
    def update_test_coverage(self, content):
        """Atualiza informações de cobertura de testes"""
        test_file = self.tests_path / "health_page_tests.robot"
        if test_file.exists():
            try:
                with open(test_file, 'r', encoding='utf-8') as f:
                    test_content = f.read()
                
                # Conta diferentes tipos de teste
                navigation_tests = len(re.findall(r'\[Tags\]\s+.*navigation', test_content))
                calories_tests = len(re.findall(r'\[Tags\]\s+.*calories', test_content))
                recipes_tests = len(re.findall(r'\[Tags\]\s+.*recipes', test_content))
                exercises_tests = len(re.findall(r'\[Tags\]\s+.*exercises', test_content))
                performance_tests = len(re.findall(r'\[Tags\]\s+.*performance', test_content))
                accessibility_tests = len(re.findall(r'\[Tags\]\s+.*accessibility', test_content))
                
                total_tests = navigation_tests + calories_tests + recipes_tests + exercises_tests + performance_tests + accessibility_tests
                
                # Atualiza seção de cobertura de testes
                coverage_section = f"""
### Cobertura de Testes
- ✅ Navegação: {navigation_tests} testes
- ✅ Funcionalidades principais: {calories_tests + recipes_tests + exercises_tests} testes
- ✅ Responsividade: {navigation_tests} testes
- ✅ Performance: {performance_tests} testes
- ✅ Acessibilidade: {accessibility_tests} testes
- 📊 **Total**: {total_tests} testes implementados
"""
                
                # Substitui seção existente ou adiciona nova
                if "### Cobertura de Testes" in content:
                    content = re.sub(
                        r'### Cobertura de Testes\n.*?\n\n',
                        f'{coverage_section}\n\n',
                        content,
                        flags=re.DOTALL
                    )
                else:
                    # Adiciona após Métricas de Qualidade
                    content = re.sub(
                        r'(## 📈 Métricas de Qualidade)',
                        f'\\1{coverage_section}',
                        content
                    )
                    
            except Exception as e:
                print(f"Erro ao atualizar cobertura de testes: {e}")
        
        return content
    
    def update_readme(self):
        """Atualiza o README com informações mais recentes"""
        if not self.readme_path.exists():
            print("❌ README.md não encontrado!")
            return False
        
        try:
            # Lê o conteúdo atual
            with open(self.readme_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            print("🔄 Atualizando README.md...")
            
            # Atualiza informações
            content = self.update_version_info(content)
            content = self.update_project_stats(content)
            content = self.update_test_coverage(content)
            
            # Adiciona timestamp de atualização automática
            timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            content = re.sub(
                r'\*Este README é mantido sempre atualizado.*\*',
                f'*Este README é mantido sempre atualizado. Última atualização automática: {timestamp}*',
                content
            )
            
            # Salva o arquivo atualizado
            with open(self.readme_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print("✅ README.md atualizado com sucesso!")
            return True
            
        except Exception as e:
            print(f"❌ Erro ao atualizar README: {e}")
            return False
    
    def create_update_script(self):
        """Cria script para atualização automática"""
        script_content = '''#!/bin/bash
# Script para atualização automática do README
# Adicione este script ao seu cron job ou GitHub Actions

cd "$(dirname "$0")"
python update_readme.py

# Se estiver usando Git, commit das mudanças
if git diff --quiet README.md; then
    echo "README.md não foi modificado"
else
    git add README.md
    git commit -m "docs: atualização automática do README"
    echo "README.md atualizado e commitado"
fi
'''
        
        script_path = self.project_root / "update_readme.sh"
        with open(script_path, 'w') as f:
            f.write(script_content)
        
        # Torna executável (Linux/Mac)
        try:
            os.chmod(script_path, 0o755)
        except:
            pass
        
        print("📝 Script de atualização automática criado: update_readme.sh")

def main():
    """Função principal"""
    print("📝 Atualizador de README - Saúde e Bem-estar")
    print("=" * 50)
    
    updater = ReadmeUpdater()
    
    # Atualiza o README
    success = updater.update_readme()
    
    if success:
        # Cria script de atualização automática
        updater.create_update_script()
        
        print("\n🎉 Processo concluído!")
        print("\n💡 Dicas para manter o README sempre atualizado:")
        print("1. Execute este script regularmente: python update_readme.py")
        print("2. Configure um cron job para execução automática")
        print("3. Use o script update_readme.sh para atualizações automáticas")
        print("4. Mantenha as tags nos testes organizadas")
    else:
        print("\n❌ Falha na atualização do README")

if __name__ == "__main__":
    main() 