import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, RECEITAS, EXERCICIOS

class TestAcessibilidadeBasica(unittest.TestCase):
    """Testes básicos de acessibilidade"""
    
    def setUp(self):
        """Configura o cliente de teste Flask"""
        app.config['TESTING'] = True
        self.client = app.test_client()
    
    def test_pagina_inicial_carrega(self):
        """Testa se a página inicial carrega corretamente"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
        html = response.data.decode('utf-8')
        
        # Verifica elementos básicos de acessibilidade
        self.assertIn('<html', html)
        self.assertIn('<head', html)
        self.assertIn('<body', html)
        self.assertIn('<main', html)
    
    def test_pagina_calorias_carrega(self):
        """Testa se a página de calorias carrega corretamente"""
        response = self.client.get('/calorias')
        self.assertEqual(response.status_code, 200)
        
        html = response.data.decode('utf-8')
        
        # Verifica elementos básicos
        self.assertIn('<main', html)
        self.assertIn('<form', html)
    
    def test_pagina_receitas_carrega(self):
        """Testa se a página de receitas carrega corretamente"""
        response = self.client.get('/receitas')
        self.assertEqual(response.status_code, 200)
        
        html = response.data.decode('utf-8')
        
        # Verifica elementos básicos
        self.assertIn('<main', html)
    
    def test_pagina_exercicios_carrega(self):
        """Testa se a página de exercícios carrega corretamente"""
        response = self.client.get('/exercicios')
        self.assertEqual(response.status_code, 200)
        
        html = response.data.decode('utf-8')
        
        # Verifica elementos básicos
        self.assertIn('<main', html)
    
    def test_pagina_imc_carrega(self):
        """Testa se a página de IMC carrega corretamente"""
        response = self.client.get('/imc')
        self.assertEqual(response.status_code, 200)
        
        html = response.data.decode('utf-8')
        
        # Verifica elementos básicos
        self.assertIn('<main', html)
        self.assertIn('<form', html)

class TestAcessibilidadeFormularios(unittest.TestCase):
    """Testes de acessibilidade para formulários"""
    
    def setUp(self):
        """Configura o cliente de teste Flask"""
        app.config['TESTING'] = True
        self.client = app.test_client()
    
    def test_formulario_calorias_tem_campos(self):
        """Testa se o formulário de calorias tem campos básicos"""
        response = self.client.get('/calorias')
        self.assertEqual(response.status_code, 200)
        
        html = response.data.decode('utf-8')
        
        # Verifica se há campos de input
        self.assertIn('input', html)
        self.assertIn('type="number"', html)
        self.assertIn('type="submit"', html)
    
    def test_formulario_imc_tem_campos(self):
        """Testa se o formulário de IMC tem campos básicos"""
        response = self.client.get('/imc')
        self.assertEqual(response.status_code, 200)
        
        html = response.data.decode('utf-8')
        
        # Verifica se há campos de input
        self.assertIn('input', html)
        self.assertIn('type="number"', html)
        self.assertIn('type="submit"', html)

class TestAcessibilidadeNavegacao(unittest.TestCase):
    """Testes de acessibilidade para navegação"""
    
    def setUp(self):
        """Configura o cliente de teste Flask"""
        app.config['TESTING'] = True
        self.client = app.test_client()
    
    def test_navegacao_links_existem(self):
        """Testa se os links de navegação existem"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
        html = response.data.decode('utf-8')
        
        # Verifica se há links de navegação
        self.assertIn('href="/"', html)
        self.assertIn('href="/calorias"', html)
        self.assertIn('href="/receitas"', html)
        self.assertIn('href="/exercicios"', html)
        self.assertIn('href="/imc"', html)
    
    def test_menu_mobile_existe(self):
        """Testa se o menu mobile existe"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
        html = response.data.decode('utf-8')
        
        # Verifica se há elementos do menu mobile
        self.assertIn('mobile-menu-toggle', html)

class TestAcessibilidadeConteudo(unittest.TestCase):
    """Testes de acessibilidade para conteúdo"""
    
    def setUp(self):
        """Configura o cliente de teste Flask"""
        app.config['TESTING'] = True
        self.client = app.test_client()
    
    def test_conteudo_texto_existe(self):
        """Testa se há conteúdo textual"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
        html = response.data.decode('utf-8')
        
        # Verifica se há conteúdo textual
        self.assertIn('Saúde', html)
        self.assertIn('Bem-estar', html)
    
    def test_receitas_tem_conteudo(self):
        """Testa se as receitas têm conteúdo"""
        response = self.client.get('/receitas')
        self.assertEqual(response.status_code, 200)
        
        html = response.data.decode('utf-8')
        
        # Verifica se há conteúdo das receitas
        self.assertIn('Receitas', html)
    
    def test_exercicios_tem_conteudo(self):
        """Testa se os exercícios têm conteúdo"""
        response = self.client.get('/exercicios')
        self.assertEqual(response.status_code, 200)
        
        html = response.data.decode('utf-8')
        
        # Verifica se há conteúdo dos exercícios
        self.assertIn('Exercícios', html)

class TestAcessibilidadeResponsividade(unittest.TestCase):
    """Testes de acessibilidade para responsividade"""
    
    def setUp(self):
        """Configura o cliente de teste Flask"""
        app.config['TESTING'] = True
        self.client = app.test_client()
    
    def test_viewport_meta_existe(self):
        """Testa se há meta tag viewport"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
        html = response.data.decode('utf-8')
        
        # Verifica meta tag viewport
        self.assertIn('viewport', html)
        self.assertIn('width=device-width', html)
    
    def test_bootstrap_css_existe(self):
        """Testa se há CSS do Bootstrap para responsividade"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
        html = response.data.decode('utf-8')
        
        # Verifica se há Bootstrap CSS
        self.assertIn('bootstrap', html)

if __name__ == '__main__':
    unittest.main() 