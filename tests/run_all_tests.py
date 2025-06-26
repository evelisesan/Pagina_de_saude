#!/usr/bin/env python3
"""
Script para executar todos os testes da pirâmide de testes
Inclui testes unitários, de integração, performance, segurança, acessibilidade e E2E
"""

import unittest
import sys
import os
import subprocess
import time
from pathlib import Path

# Adiciona o diretório pai ao path para importar a aplicação
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def executar_testes_unitarios():
    """Executa testes unitários"""
    print("🧪 Executando Testes Unitários...")
    print("=" * 50)
    
    # Carrega e executa testes unitários
    loader = unittest.TestLoader()
    suite = loader.discover('tests', pattern='test_unit.py')
    
    runner = unittest.TextTestRunner(verbosity=2)
    resultado = runner.run(suite)
    
    return resultado.wasSuccessful()

def executar_testes_integracao():
    """Executa testes de integração"""
    print("\n🔗 Executando Testes de Integração...")
    print("=" * 50)
    
    # Carrega e executa testes de integração
    loader = unittest.TestLoader()
    suite = loader.discover('tests', pattern='test_integration.py')
    
    runner = unittest.TextTestRunner(verbosity=2)
    resultado = runner.run(suite)
    
    return resultado.wasSuccessful()

def executar_testes_performance():
    """Executa testes de performance"""
    print("\n⚡ Executando Testes de Performance...")
    print("=" * 50)
    
    # Carrega e executa testes de performance
    loader = unittest.TestLoader()
    suite = loader.discover('tests', pattern='test_performance.py')
    
    runner = unittest.TextTestRunner(verbosity=2)
    resultado = runner.run(suite)
    
    return resultado.wasSuccessful()

def executar_testes_seguranca():
    """Executa testes de segurança"""
    print("\n🔒 Executando Testes de Segurança...")
    print("=" * 50)
    
    # Carrega e executa testes de segurança
    loader = unittest.TestLoader()
    suite = loader.discover('tests', pattern='test_security.py')
    
    runner = unittest.TextTestRunner(verbosity=2)
    resultado = runner.run(suite)
    
    return resultado.wasSuccessful()

def executar_testes_acessibilidade():
    """Executa testes de acessibilidade"""
    print("\n♿ Executando Testes de Acessibilidade...")
    print("=" * 50)
    
    # Carrega e executa testes de acessibilidade
    loader = unittest.TestLoader()
    suite = loader.discover('tests', pattern='test_accessibility.py')
    
    runner = unittest.TextTestRunner(verbosity=2)
    resultado = runner.run(suite)
    
    return resultado.wasSuccessful()

def executar_testes_e2e():
    """Executa testes end-to-end com Cypress"""
    print("\n🌐 Executando Testes End-to-End (Cypress)...")
    print("=" * 50)
    
    try:
        # Verifica se o Cypress está instalado
        resultado = subprocess.run(['npx', 'cypress', '--version'], 
                                 capture_output=True, text=True, timeout=10)
        if resultado.returncode == 0:
            print(f"Cypress versão: {resultado.stdout.strip()}")
        else:
            print("❌ Cypress não está instalado")
            print("Instale com: npm install cypress")
            return False
        
        # Executa os testes Cypress
        resultado = subprocess.run([
            'npx', 'cypress', 'run', '--headless'
        ], capture_output=True, text=True, timeout=120)
        
        print(resultado.stdout)
        if resultado.stderr:
            print("Erros:", resultado.stderr)
        
        return resultado.returncode == 0
        
    except subprocess.TimeoutExpired:
        print("❌ Timeout ao executar testes Cypress")
        return False
    except FileNotFoundError:
        print("❌ Node.js/npm não está instalado")
        print("Instale Node.js e depois: npm install cypress")
        return False
    except Exception as e:
        print(f"❌ Erro ao executar Cypress: {e}")
        return False

def verificar_dependencias():
    """Verifica se todas as dependências estão instaladas"""
    print("🔍 Verificando Dependências...")
    print("=" * 50)
    
    dependencias = [
        'flask',
        'selenium'
    ]
    
    faltando = []
    
    for dep in dependencias:
        try:
            __import__(dep.replace('-', '_'))
            print(f"✅ {dep}")
        except ImportError:
            print(f"❌ {dep} - NÃO INSTALADO")
            faltando.append(dep)
    
    # Verifica Robot Framework
    try:
        resultado = subprocess.run(['py', '-m', 'robot', '--version'], 
                                 capture_output=True, text=True, timeout=10)
        if resultado.returncode == 0:
            print(f"✅ robotframework")
        else:
            print(f"❌ robotframework - NÃO INSTALADO")
            faltando.append('robotframework')
    except Exception:
        print(f"❌ robotframework - NÃO INSTALADO")
        faltando.append('robotframework')
    
    # Verifica Robot Framework Selenium Library (assume que se robot funciona, selenium library também)
    try:
        resultado = subprocess.run(['py', '-m', 'robot', '--help'], 
                                 capture_output=True, text=True, timeout=10)
        if resultado.returncode == 0:
            print(f"✅ robotframework-seleniumlibrary")
        else:
            print(f"❌ robotframework-seleniumlibrary - NÃO INSTALADO")
            faltando.append('robotframework-seleniumlibrary')
    except Exception:
        print(f"❌ robotframework-seleniumlibrary - NÃO INSTALADO")
        faltando.append('robotframework-seleniumlibrary')
    
    if faltando:
        print(f"\n⚠️  Dependências faltando: {', '.join(faltando)}")
        print("Instale com: pip install " + " ".join(faltando))
        return False
    
    return True

def gerar_relatorio(resultados):
    """Gera relatório final dos testes"""
    print("\n" + "=" * 60)
    print("📊 RELATÓRIO FINAL DOS TESTES")
    print("=" * 60)
    
    total_testes = len(resultados)
    testes_passaram = sum(1 for sucesso in resultados.values() if sucesso)
    testes_falharam = total_testes - testes_passaram
    
    print(f"Total de Suítes de Teste: {total_testes}")
    print(f"✅ Passaram: {testes_passaram}")
    print(f"❌ Falharam: {testes_falharam}")
    print(f"📈 Taxa de Sucesso: {(testes_passaram/total_testes)*100:.1f}%")
    
    print("\nDetalhes por Categoria:")
    for categoria, sucesso in resultados.items():
        status = "✅ PASSOU" if sucesso else "❌ FALHOU"
        print(f"  {categoria}: {status}")
    
    if testes_falharam == 0:
        print("\n🎉 TODOS OS TESTES PASSARAM!")
        return True
    else:
        print(f"\n⚠️  {testes_falharam} suíte(s) de teste falharam")
        return False

def main():
    """Função principal que executa todos os testes"""
    print("🚀 INICIANDO EXECUÇÃO COMPLETA DOS TESTES")
    print("=" * 60)
    print("Pirâmide de Testes:")
    print("  🔺 E2E (Cypress) - Menos testes")
    print("  🔸 Integração - Testes médios")
    print("  🔻 Unitários - Mais testes")
    print("  🔸 Performance - Testes de velocidade")
    print("  🔸 Segurança - Testes de vulnerabilidades")
    print("  🔸 Acessibilidade - Testes WCAG")
    print("=" * 60)
    
    # Verifica dependências básicas apenas
    print("\n🔍 Verificando Dependências Básicas...")
    print("=" * 50)
    
    dependencias_basicas = ['flask', 'selenium']
    for dep in dependencias_basicas:
        try:
            __import__(dep.replace('-', '_'))
            print(f"✅ {dep}")
        except ImportError:
            print(f"❌ {dep} - NÃO INSTALADO")
    
    # Inicia aplicação Flask em background (se necessário)
    print("\n🌐 Iniciando aplicação Flask...")
    try:
        from app import app
        app.config['TESTING'] = True
        print("✅ Aplicação Flask carregada para testes")
    except Exception as e:
        print(f"❌ Erro ao carregar aplicação Flask: {e}")
        return False
    
    # Executa todos os tipos de teste
    resultados = {}
    
    # 1. Testes Unitários (base da pirâmide)
    resultados['Unitários'] = executar_testes_unitarios()
    
    # 2. Testes de Integração (meio da pirâmide)
    resultados['Integração'] = executar_testes_integracao()
    
    # 3. Testes de Performance
    resultados['Performance'] = executar_testes_performance()
    
    # 4. Testes de Segurança
    resultados['Segurança'] = executar_testes_seguranca()
    
    # 5. Testes de Acessibilidade
    resultados['Acessibilidade'] = executar_testes_acessibilidade()
    
    # 6. Testes E2E (topo da pirâmide)
    resultados['E2E (Cypress)'] = executar_testes_e2e()
    
    # Gera relatório final
    sucesso_geral = gerar_relatorio(resultados)
    
    # Cria diretório de resultados se não existir
    Path('test_results').mkdir(exist_ok=True)
    
    # Salva relatório em arquivo
    with open('test_results/relatorio_teste.txt', 'w', encoding='utf-8') as f:
        f.write("RELATÓRIO DE TESTES - " + time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        f.write("=" * 60 + "\n")
        for categoria, sucesso in resultados.items():
            status = "PASSOU" if sucesso else "FALHOU"
            f.write(f"{categoria}: {status}\n")
    
    print(f"\n📄 Relatório salvo em: test_results/relatorio_teste.txt")
    
    return sucesso_geral

if __name__ == '__main__':
    sucesso = main()
    sys.exit(0 if sucesso else 1) 