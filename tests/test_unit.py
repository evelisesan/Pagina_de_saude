import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, RECEITAS, EXERCICIOS

class TestCalculadoraCalorias(unittest.TestCase):
    """Testes unitários para a calculadora de calorias"""
    
    def setUp(self):
        """Configura o cliente de teste Flask"""
        app.config['TESTING'] = True
        self.client = app.test_client()
    
    def test_calcular_calorias_homem_45_anos(self):
        """Testa cálculo de calorias para homem de 45 anos"""
        dados = {
            'idade': 45,
            'peso': 70,
            'altura': 1.70,
            'genero': 'masculino',
            'nivel_atividade': 'moderado'
        }
        
        response = self.client.post('/api/calcular-calorias', json=dados)
        self.assertEqual(response.status_code, 200)
        
        resultado = response.get_json()
        self.assertIn('calorias_diarias', resultado)
        self.assertIn('tmb', resultado)
        self.assertIn('nivel_atividade', resultado)
        self.assertGreater(resultado['calorias_diarias'], 0)
        self.assertGreater(resultado['tmb'], 0)
    
    def test_calcular_calorias_mulher_50_anos(self):
        """Testa cálculo de calorias para mulher de 50 anos"""
        dados = {
            'idade': 50,
            'peso': 65,
            'altura': 1.60,
            'genero': 'feminino',
            'nivel_atividade': 'sedentario'
        }
        
        response = self.client.post('/api/calcular-calorias', json=dados)
        self.assertEqual(response.status_code, 200)
        
        resultado = response.get_json()
        self.assertIn('calorias_diarias', resultado)
        self.assertIn('tmb', resultado)
        self.assertGreater(resultado['calorias_diarias'], 0)
    
    def test_calcular_calorias_idade_invalida(self):
        """Testa cálculo com idade inválida"""
        dados = {
            'idade': -5,
            'peso': 70,
            'altura': 1.70,
            'genero': 'masculino',
            'nivel_atividade': 'moderado'
        }
        
        response = self.client.post('/api/calcular-calorias', json=dados)
        # A API agora valida e rejeita valores negativos
        self.assertEqual(response.status_code, 400)
        resultado = response.get_json()
        self.assertIn('erro', resultado)
    
    def test_calcular_calorias_peso_invalido(self):
        """Testa cálculo com peso inválido"""
        dados = {
            'idade': 45,
            'peso': -70,
            'altura': 1.70,
            'genero': 'masculino',
            'nivel_atividade': 'moderado'
        }
        
        response = self.client.post('/api/calcular-calorias', json=dados)
        # A API agora valida e rejeita valores negativos
        self.assertEqual(response.status_code, 400)
        resultado = response.get_json()
        self.assertIn('erro', resultado)
    
    def test_calcular_calorias_altura_invalida(self):
        """Testa cálculo com altura inválida"""
        dados = {
            'idade': 45,
            'peso': 70,
            'altura': -1.70,
            'genero': 'masculino',
            'nivel_atividade': 'moderado'
        }
        
        response = self.client.post('/api/calcular-calorias', json=dados)
        # A API agora valida e rejeita valores negativos
        self.assertEqual(response.status_code, 400)
        resultado = response.get_json()
        self.assertIn('erro', resultado)

class TestCalculadoraIMC(unittest.TestCase):
    """Testes unitários para a calculadora de IMC"""
    
    def setUp(self):
        """Configura o cliente de teste Flask"""
        app.config['TESTING'] = True
        self.client = app.test_client()
    
    def test_calcular_imc_peso_normal(self):
        """Testa cálculo de IMC para peso normal"""
        dados = {
            'peso': 70,
            'altura': 1.70
        }
        
        response = self.client.post('/api/calcular-imc', json=dados)
        self.assertEqual(response.status_code, 200)
        
        resultado = response.get_json()
        self.assertIn('imc', resultado)
        self.assertIn('classificacao', resultado)
        self.assertAlmostEqual(resultado['imc'], 24.22, places=2)
        self.assertEqual(resultado['classificacao'], 'Peso Normal')
    
    def test_calcular_imc_sobrepeso(self):
        """Testa cálculo de IMC para sobrepeso"""
        dados = {
            'peso': 80,
            'altura': 1.70
        }
        
        response = self.client.post('/api/calcular-imc', json=dados)
        self.assertEqual(response.status_code, 200)
        
        resultado = response.get_json()
        self.assertAlmostEqual(resultado['imc'], 27.68, places=2)
        self.assertEqual(resultado['classificacao'], 'Sobrepeso')
    
    def test_calcular_imc_obesidade(self):
        """Testa cálculo de IMC para obesidade"""
        dados = {
            'peso': 100,
            'altura': 1.70
        }
        
        response = self.client.post('/api/calcular-imc', json=dados)
        self.assertEqual(response.status_code, 200)
        
        resultado = response.get_json()
        self.assertAlmostEqual(resultado['imc'], 34.60, places=2)
        self.assertEqual(resultado['classificacao'], 'Obesidade Grau I')
    
    def test_calcular_imc_altura_zero(self):
        """Testa cálculo com altura zero"""
        dados = {
            'peso': 70,
            'altura': 0
        }
        
        response = self.client.post('/api/calcular-imc', json=dados)
        self.assertEqual(response.status_code, 400)
        resultado = response.get_json()
        self.assertIn('erro', resultado)
    
    def test_calcular_imc_peso_negativo(self):
        """Testa cálculo com peso negativo"""
        dados = {
            'peso': -70,
            'altura': 1.70
        }
        
        response = self.client.post('/api/calcular-imc', json=dados)
        # A API agora valida e rejeita valores negativos
        self.assertEqual(response.status_code, 400)
        resultado = response.get_json()
        self.assertIn('erro', resultado)

class TestFiltrosReceitas(unittest.TestCase):
    """Testes unitários para filtros de receitas"""
    
    def setUp(self):
        """Configura o cliente de teste Flask"""
        app.config['TESTING'] = True
        self.client = app.test_client()
    
    def test_filtrar_receitas_vegetarianas(self):
        """Testa filtro de receitas vegetarianas"""
        response = self.client.get('/api/receitas?vegetariano=true')
        self.assertEqual(response.status_code, 200)
        
        receitas_filtradas = response.get_json()
        self.assertIsInstance(receitas_filtradas, list)
        
        for receita in receitas_filtradas:
            self.assertTrue(receita['vegetariano'])
    
    def test_filtrar_receitas_baixa_caloria(self):
        """Testa filtro de receitas de baixa caloria"""
        response = self.client.get('/api/receitas?baixa_caloria=true')
        self.assertEqual(response.status_code, 200)
        
        receitas_filtradas = response.get_json()
        self.assertIsInstance(receitas_filtradas, list)
        
        for receita in receitas_filtradas:
            self.assertTrue(receita['baixa_caloria'])
    
    def test_filtrar_receitas_economicas(self):
        """Testa filtro de receitas econômicas"""
        response = self.client.get('/api/receitas?orcamento=baixo')
        self.assertEqual(response.status_code, 200)
        
        receitas_filtradas = response.get_json()
        self.assertIsInstance(receitas_filtradas, list)
        
        for receita in receitas_filtradas:
            self.assertEqual(receita['orcamento'], 'baixo')
    
    def test_filtrar_receitas_multiplos_filtros(self):
        """Testa múltiplos filtros aplicados simultaneamente"""
        response = self.client.get('/api/receitas?vegetariano=true&baixa_caloria=true&orcamento=baixo')
        self.assertEqual(response.status_code, 200)
        
        receitas_filtradas = response.get_json()
        self.assertIsInstance(receitas_filtradas, list)
        
        for receita in receitas_filtradas:
            self.assertTrue(receita['vegetariano'])
            self.assertTrue(receita['baixa_caloria'])
            self.assertEqual(receita['orcamento'], 'baixo')

class TestFiltrosExercicios(unittest.TestCase):
    """Testes unitários para filtros de exercícios"""
    
    def setUp(self):
        """Configura o cliente de teste Flask"""
        app.config['TESTING'] = True
        self.client = app.test_client()
    
    def test_filtrar_exercicios_iniciante(self):
        """Testa filtro de exercícios para iniciantes"""
        response = self.client.get('/api/exercicios?dificuldade=iniciante')
        self.assertEqual(response.status_code, 200)
        
        exercicios_filtrados = response.get_json()
        self.assertIsInstance(exercicios_filtrados, list)
        
        for exercicio in exercicios_filtrados:
            self.assertEqual(exercicio['dificuldade'], 'iniciante')
    
    def test_filtrar_exercicios_intermediario(self):
        """Testa filtro de exercícios intermediários"""
        response = self.client.get('/api/exercicios?dificuldade=intermediario')
        self.assertEqual(response.status_code, 200)
        
        exercicios_filtrados = response.get_json()
        self.assertIsInstance(exercicios_filtrados, list)
        # Como não há exercícios intermediários nos dados mockados, a lista pode estar vazia
        self.assertIsInstance(exercicios_filtrados, list)

class TestRotasFlask(unittest.TestCase):
    """Testes unitários para as rotas Flask"""
    
    def setUp(self):
        """Configura o cliente de teste Flask"""
        app.config['TESTING'] = True
        self.client = app.test_client()
    
    def test_rota_home(self):
        """Testa a rota da página inicial"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sa\xc3\xbade e Bem-estar', response.data)
    
    def test_rota_calorias(self):
        """Testa a rota da calculadora de calorias"""
        response = self.client.get('/calorias')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Calculadora de Calorias', response.data)
    
    def test_rota_receitas(self):
        """Testa a rota de receitas"""
        response = self.client.get('/receitas')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Receitas Saud\xc3\xa1veis', response.data)
    
    def test_rota_exercicios(self):
        """Testa a rota de exercícios"""
        response = self.client.get('/exercicios')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Exerc\xc3\xadcios para Pessoas', response.data)
    
    def test_rota_imc(self):
        """Testa a rota da calculadora de IMC"""
        response = self.client.get('/imc')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Calculadora de IMC', response.data)
    
    def test_rota_404(self):
        """Testa rota inexistente"""
        response = self.client.get('/rota-inexistente')
        self.assertEqual(response.status_code, 404)

class TestAPIs(unittest.TestCase):
    """Testes unitários para as APIs REST"""
    
    def setUp(self):
        """Configura o cliente de teste Flask"""
        app.config['TESTING'] = True
        self.client = app.test_client()
    
    def test_api_buscar_receitas(self):
        """Testa API de busca de receitas"""
        response = self.client.get('/api/buscar-receitas?q=frango')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)
    
    def test_api_buscar_receitas_sem_query(self):
        """Testa API de busca sem parâmetro de busca"""
        response = self.client.get('/api/buscar-receitas')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)
    
    def test_api_calcular_calorias(self):
        """Testa API de cálculo de calorias"""
        dados = {
            'idade': 45,
            'peso': 70,
            'altura': 1.70,
            'genero': 'masculino',
            'nivel_atividade': 'moderado'
        }
        response = self.client.post('/api/calcular-calorias', json=dados)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('calorias_diarias', data)
        self.assertIn('tmb', data)
    
    def test_api_calcular_imc(self):
        """Testa API de cálculo de IMC"""
        dados = {
            'peso': 70,
            'altura': 1.70
        }
        response = self.client.post('/api/calcular-imc', json=dados)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('imc', data)
        self.assertIn('classificacao', data)

class TestDadosMockados(unittest.TestCase):
    """Testes unitários para os dados mockados"""
    
    def test_estrutura_receitas(self):
        """Testa estrutura dos dados de receitas"""
        for receita in RECEITAS:
            # Verifica campos obrigatórios
            self.assertIn('id', receita)
            self.assertIn('titulo', receita)
            self.assertIn('ingredientes', receita)
            self.assertIn('modo_preparo', receita)
            self.assertIn('calorias', receita)
            self.assertIn('tempo_preparo', receita)
            self.assertIn('dificuldade', receita)
            self.assertIn('categoria', receita)
            self.assertIn('vegetariano', receita)
            self.assertIn('baixa_caloria', receita)
            self.assertIn('orcamento', receita)
            
            # Verifica tipos de dados
            self.assertIsInstance(receita['id'], int)
            self.assertIsInstance(receita['titulo'], str)
            self.assertIsInstance(receita['ingredientes'], list)
            self.assertIsInstance(receita['modo_preparo'], str)
            self.assertIsInstance(receita['calorias'], int)
            self.assertIsInstance(receita['tempo_preparo'], int)
            self.assertIsInstance(receita['dificuldade'], str)
            self.assertIsInstance(receita['categoria'], str)
            self.assertIsInstance(receita['vegetariano'], bool)
            self.assertIsInstance(receita['baixa_caloria'], bool)
            self.assertIsInstance(receita['orcamento'], str)
    
    def test_estrutura_exercicios(self):
        """Testa estrutura dos dados de exercícios"""
        for exercicio in EXERCICIOS:
            # Verifica campos obrigatórios
            self.assertIn('id', exercicio)
            self.assertIn('titulo', exercicio)
            self.assertIn('descricao', exercicio)
            self.assertIn('como_fazer', exercicio)
            self.assertIn('beneficios', exercicio)
            self.assertIn('precaucoes', exercicio)
            self.assertIn('duracao', exercicio)
            self.assertIn('series_repeticoes', exercicio)
            self.assertIn('dificuldade', exercicio)
            self.assertIn('video_url', exercicio)
            
            # Verifica tipos de dados
            self.assertIsInstance(exercicio['id'], int)
            self.assertIsInstance(exercicio['titulo'], str)
            self.assertIsInstance(exercicio['descricao'], str)
            self.assertIsInstance(exercicio['como_fazer'], str)
            self.assertIsInstance(exercicio['beneficios'], list)
            self.assertIsInstance(exercicio['precaucoes'], list)
            self.assertIsInstance(exercicio['duracao'], str)
            self.assertIsInstance(exercicio['series_repeticoes'], str)
            self.assertIsInstance(exercicio['dificuldade'], str)
            self.assertIsInstance(exercicio['video_url'], str)

if __name__ == '__main__':
    unittest.main() 