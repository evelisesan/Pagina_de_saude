import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, RECEITAS, EXERCICIOS

class TestIntegracaoCalculadoraCalorias(unittest.TestCase):
    """Testes de integração para a calculadora de calorias"""
    
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
    
    def test_integracao_calculo_calorias_web(self):
        dados = {
            'idade': 45,
            'peso': 70,
            'altura': 1.70,
            'genero': 'masculino',
            'nivel_atividade': 'moderado'
        }
        response = self.client.post('/api/calcular-calorias', json=dados)
        self.assertEqual(response.status_code, 200)
        resultado_api = response.get_json()
        self.assertIn('calorias_diarias', resultado_api)
        self.assertIn('tmb', resultado_api)

    def test_integracao_calculo_imc_web(self):
        dados = {
            'peso': 70,
            'altura': 1.70
        }
        response = self.client.post('/api/calcular-imc', json=dados)
        self.assertEqual(response.status_code, 200)
        resultado_api = response.get_json()
        self.assertIn('imc', resultado_api)
        self.assertIn('classificacao', resultado_api)

class TestIntegracaoFiltros(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
    
    def test_integracao_filtros_receitas(self):
        response = self.client.get('/api/receitas?vegetariano=true')
        self.assertEqual(response.status_code, 200)
        receitas_vegetarianas = response.get_json()
        for receita in receitas_vegetarianas:
            self.assertTrue(receita['vegetariano'])
        
        response = self.client.get('/api/receitas?baixa_caloria=true')
        self.assertEqual(response.status_code, 200)
        receitas_baixa_caloria = response.get_json()
        for receita in receitas_baixa_caloria:
            self.assertTrue(receita['baixa_caloria'])
        
        response = self.client.get('/api/receitas?orcamento=baixo')
        self.assertEqual(response.status_code, 200)
        receitas_economicas = response.get_json()
        for receita in receitas_economicas:
            self.assertEqual(receita['orcamento'], 'baixo')
        
        response = self.client.get('/api/receitas?vegetariano=true&baixa_caloria=true&orcamento=baixo')
        self.assertEqual(response.status_code, 200)
        receitas_filtradas = response.get_json()
        for receita in receitas_filtradas:
            self.assertTrue(receita['vegetariano'])
            self.assertTrue(receita['baixa_caloria'])
            self.assertEqual(receita['orcamento'], 'baixo')
    
    def test_integracao_filtros_exercicios(self):
        response = self.client.get('/api/exercicios?dificuldade=iniciante')
        self.assertEqual(response.status_code, 200)
        exercicios_iniciante = response.get_json()
        for exercicio in exercicios_iniciante:
            self.assertEqual(exercicio['dificuldade'], 'iniciante')

class TestIntegracaoNavegacao(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
    
    def test_fluxo_navegacao_completo(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/calorias')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/receitas')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/exercicios')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/imc')
        self.assertEqual(response.status_code, 200)
    
    def test_integracao_busca_receitas(self):
        response = self.client.get('/api/buscar-receitas?q=frango')
        self.assertEqual(response.status_code, 200)
        receitas_encontradas = response.get_json()
        for receita in receitas_encontradas:
            self.assertIn('titulo', receita)
            self.assertTrue('frango' in receita['titulo'].lower() or any('frango' in ing.lower() for ing in receita['ingredientes']))

class TestIntegracaoFormularios(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
    
    def test_integracao_formulario_calorias(self):
        dados_validos = {
            'idade': 45,
            'peso': 70,
            'altura': 1.70,
            'genero': 'masculino',
            'nivel_atividade': 'moderado'
        }
        response = self.client.post('/api/calcular-calorias', json=dados_validos)
        self.assertEqual(response.status_code, 200)
        resultado = response.get_json()
        self.assertIn('calorias_diarias', resultado)
        self.assertIn('tmb', resultado)
        
        dados_invalidos = {
            'idade': -5,
            'peso': 70,
            'altura': 1.70,
            'genero': 'masculino',
            'nivel_atividade': 'moderado'
        }
        response = self.client.post('/api/calcular-calorias', json=dados_invalidos)
        self.assertEqual(response.status_code, 400)
        resultado = response.get_json()
        self.assertIn('erro', resultado)
    
    def test_integracao_formulario_imc(self):
        dados_validos = {
            'peso': 70,
            'altura': 1.70
        }
        response = self.client.post('/api/calcular-imc', json=dados_validos)
        self.assertEqual(response.status_code, 200)
        resultado = response.get_json()
        self.assertIn('imc', resultado)
        self.assertIn('classificacao', resultado)
        
        dados_invalidos = {
            'peso': 70,
            'altura': 0
        }
        response = self.client.post('/api/calcular-imc', json=dados_invalidos)
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main() 