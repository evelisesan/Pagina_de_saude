#!/usr/bin/env python3
"""
Script para testar se a aplicação está funcionando após deploy
Execute: python test_deploy.py
"""

import requests
import sys
import time

def test_url(url, description):
    """Testa uma URL e retorna o status"""
    try:
        print(f"🔍 Testando: {description}")
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            print(f"✅ {description}: OK (Status {response.status_code})")
            return True
        else:
            print(f"❌ {description}: ERRO (Status {response.status_code})")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ {description}: ERRO - {e}")
        return False

def main():
    # Substitua pela URL do seu Render
    base_url = input("Digite a URL do seu Render (ex: https://saude-bemestar.onrender.com): ").strip()
    
    if not base_url:
        print("❌ URL não fornecida!")
        return
    
    # Remove barra final se existir
    base_url = base_url.rstrip('/')
    
    print(f"\n🚀 Testando aplicação em: {base_url}")
    print("=" * 50)
    
    # Lista de páginas para testar
    pages = [
        ("/", "Página Principal"),
        ("/calorias", "Calculadora de Calorias"),
        ("/receitas", "Página de Receitas"),
        ("/exercicios", "Página de Exercícios"),
        ("/imc", "Calculadora de IMC"),
        ("/api/receitas", "API de Receitas"),
        ("/api/exercicios", "API de Exercícios"),
    ]
    
    success_count = 0
    total_pages = len(pages)
    
    for path, description in pages:
        url = f"{base_url}{path}"
        if test_url(url, description):
            success_count += 1
        print()  # Linha em branco
    
    # Resultado final
    print("=" * 50)
    print(f"📊 RESULTADO: {success_count}/{total_pages} páginas funcionando")
    
    if success_count == total_pages:
        print("🎉 PARABÉNS! Sua aplicação está funcionando perfeitamente!")
        print(f"🌐 Acesse: {base_url}")
    else:
        print("⚠️  Algumas páginas não estão funcionando. Verifique os logs no Render.")
    
    # Teste de funcionalidade específica
    print("\n🔧 Testando funcionalidades específicas...")
    
    # Teste da API de busca de receitas
    try:
        search_url = f"{base_url}/api/buscar-receitas?q=frango"
        response = requests.get(search_url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list):
                print(f"✅ API de busca: OK (encontrou {len(data)} receitas)")
            else:
                print("⚠️  API de busca: retornou formato inesperado")
        else:
            print(f"❌ API de busca: ERRO (Status {response.status_code})")
    except Exception as e:
        print(f"❌ API de busca: ERRO - {e}")

if __name__ == "__main__":
    main() 