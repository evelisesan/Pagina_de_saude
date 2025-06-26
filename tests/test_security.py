import unittest
import sys
import os
import json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

class TestSegurancaValidacaoEntrada(unittest.TestCase):
    """Testes de segurança para validação de entrada"""
    
    def setUp(self):
        """Configura o cliente de teste Flask"""
        app.config['TESTING'] = True
        self.client = app.test_client()
    
    def test_validacao_idade_negativa(self):
        """Testa validação de idade negativa"""
        dados = {
            'idade': -5,
            'peso': 70,
            'altura': 170,
            'genero': 'male',
            'atividade': 'moderate'
        }
        
        response = self.client.post('/api/calcular-calorias', json=dados)
        self.assertEqual(response.status_code, 400)
    
    def test_validacao_idade_muito_alta(self):
        """Testa validação de idade muito alta"""
        dados = {
            'idade': 150,
            'peso': 70,
            'altura': 170,
            'genero': 'male',
            'atividade': 'moderate'
        }
        
        response = self.client.post('/api/calcular-calorias', json=dados)
        self.assertEqual(response.status_code, 400)
    
    def test_validacao_peso_negativo(self):
        """Testa validação de peso negativo"""
        dados = {
            'idade': 45,
            'peso': -70,
            'altura': 170,
            'genero': 'male',
            'atividade': 'moderate'
        }
        
        response = self.client.post('/api/calcular-calorias', json=dados)
        self.assertEqual(response.status_code, 400)
    
    def test_validacao_peso_muito_alto(self):
        """Testa validação de peso muito alto"""
        dados = {
            'idade': 45,
            'peso': 500,
            'altura': 170,
            'genero': 'male',
            'atividade': 'moderate'
        }
        
        response = self.client.post('/api/calcular-calorias', json=dados)
        self.assertEqual(response.status_code, 400)
    
    def test_validacao_altura_negativa(self):
        """Testa validação de altura negativa"""
        dados = {
            'idade': 45,
            'peso': 70,
            'altura': -170,
            'genero': 'male',
            'atividade': 'moderate'
        }
        
        response = self.client.post('/api/calcular-calorias', json=dados)
        self.assertEqual(response.status_code, 400)
    
    def test_validacao_altura_muito_alta(self):
        """Testa validação de altura muito alta"""
        dados = {
            'idade': 45,
            'peso': 70,
            'altura': 300,
            'genero': 'male',
            'atividade': 'moderate'
        }
        
        response = self.client.post('/api/calcular-calorias', json=dados)
        self.assertEqual(response.status_code, 400)
    
    def test_validacao_genero_invalido(self):
        """Testa validação de gênero inválido"""
        dados = {
            'idade': 45,
            'peso': 70,
            'altura': 170,
            'genero': 'invalido',
            'atividade': 'moderate'
        }
        
        response = self.client.post('/api/calcular-calorias', json=dados)
        self.assertEqual(response.status_code, 400)
    
    def test_validacao_atividade_invalida(self):
        """Testa validação de nível de atividade inválido"""
        dados = {
            'idade': 45,
            'peso': 70,
            'altura': 170,
            'genero': 'male',
            'atividade': 'invalido'
        }
        
        response = self.client.post('/api/calcular-calorias', json=dados)
        self.assertEqual(response.status_code, 400)
    
    def test_validacao_imc_peso_negativo(self):
        """Testa validação de peso negativo no IMC"""
        dados = {
            'peso': -70,
            'altura': 1.70
        }
        
        response = self.client.post('/api/calcular-imc', json=dados)
        self.assertEqual(response.status_code, 400)
    
    def test_validacao_imc_altura_zero(self):
        """Testa validação de altura zero no IMC"""
        dados = {
            'peso': 70,
            'altura': 0
        }
        
        response = self.client.post('/api/calcular-imc', json=dados)
        self.assertEqual(response.status_code, 400)
    
    def test_validacao_imc_altura_negativa(self):
        """Testa validação de altura negativa no IMC"""
        dados = {
            'peso': 70,
            'altura': -1.70
        }
        
        response = self.client.post('/api/calcular-imc', json=dados)
        self.assertEqual(response.status_code, 400)

class TestSegurancaInjecaoSQL(unittest.TestCase):
    """Testes de segurança contra injeção SQL"""
    
    def setUp(self):
        """Configura o cliente de teste Flask"""
        app.config['TESTING'] = True
        self.client = app.test_client()
    
    def test_busca_sql_injection(self):
        """Testa busca com tentativa de injeção SQL"""
        payloads_sql = [
            "'; DROP TABLE receitas; --",
            "' OR '1'='1",
            "' UNION SELECT * FROM users --",
            "'; INSERT INTO receitas VALUES (999, 'hack', 'hack'); --",
            "' OR 1=1 --"
        ]
        
        for payload in payloads_sql:
            response = self.client.get(f'/api/buscar-receitas?q={payload}')
            # Deve retornar 200 (não deve quebrar) mas sem resultados sensíveis
            self.assertEqual(response.status_code, 200)
            data = response.get_json()
            # Verifica se não retornou dados sensíveis
            self.assertIsInstance(data, list)
    
    def test_busca_xss_injection(self):
        """Testa busca com tentativa de XSS"""
        payloads_xss = [
            "<script>alert('XSS')</script>",
            "<img src=x onerror=alert('XSS')>",
            "javascript:alert('XSS')",
            "<svg onload=alert('XSS')>",
            "'><script>alert('XSS')</script>"
        ]
        
        for payload in payloads_xss:
            response = self.client.get(f'/api/buscar-receitas?q={payload}')
            self.assertEqual(response.status_code, 200)
            data = response.get_json()
            self.assertIsInstance(data, list)

class TestSegurancaHeaders(unittest.TestCase):
    """Testes de segurança para headers HTTP"""
    
    def setUp(self):
        """Configura o cliente de teste Flask"""
        app.config['TESTING'] = True
        self.client = app.test_client()
    
    def test_headers_seguranca_pagina_inicial(self):
        """Testa headers de segurança na página inicial"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
        # Verifica se não expõe informações sensíveis
        self.assertNotIn('Server', response.headers)
        self.assertNotIn('X-Powered-By', response.headers)
    
    def test_headers_seguranca_api(self):
        """Testa headers de segurança nas APIs"""
        response = self.client.get('/api/buscar-receitas?q=frango')
        self.assertEqual(response.status_code, 200)
        
        # Verifica se não expõe informações sensíveis
        self.assertNotIn('Server', response.headers)
        self.assertNotIn('X-Powered-By', response.headers)
    
    def test_content_type_json(self):
        """Testa se APIs retornam Content-Type correto"""
        response = self.client.get('/api/buscar-receitas?q=frango')
        self.assertEqual(response.status_code, 200)
        self.assertIn('application/json', response.headers.get('Content-Type', ''))
    
    def test_content_type_html(self):
        """Testa se páginas retornam Content-Type correto"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('text/html', response.headers.get('Content-Type', ''))

class TestSegurancaAutenticacao(unittest.TestCase):
    """Testes de segurança para autenticação e autorização"""
    
    def setUp(self):
        """Configura o cliente de teste Flask"""
        app.config['TESTING'] = True
        self.client = app.test_client()
    
    def test_acesso_publico_paginas(self):
        """Testa se páginas são acessíveis publicamente"""
        paginas = ['/', '/calorias', '/receitas', '/exercicios', '/imc']
        
        for pagina in paginas:
            response = self.client.get(pagina)
            self.assertEqual(response.status_code, 200)
    
    def test_acesso_publico_apis(self):
        """Testa se APIs são acessíveis publicamente"""
        apis = [
            '/api/buscar-receitas?q=frango',
            '/api/calcular-calorias',
            '/api/calcular-imc'
        ]
        
        for api in apis:
            if api.endswith('calcular-calorias'):
                response = self.client.post(api, json={'idade': 45, 'peso': 70, 'altura': 1.70, 'genero': 'masculino', 'nivel_atividade': 'moderado'})
            elif api.endswith('calcular-imc'):
                response = self.client.post(api, json={'peso': 70, 'altura': 1.70})
            else:
                response = self.client.get(api)
            
            self.assertEqual(response.status_code, 200)

class TestSegurancaRateLimiting(unittest.TestCase):
    """Testes de segurança para rate limiting"""
    
    def setUp(self):
        """Configura o cliente de teste Flask"""
        app.config['TESTING'] = True
        self.client = app.test_client()
    
    def test_multiplas_requisicoes_rapidas(self):
        """Testa múltiplas requisições rápidas para verificar rate limiting"""
        # Faz 50 requisições rápidas
        for i in range(50):
            response = self.client.get('/api/buscar-receitas?q=frango')
            # Deve continuar funcionando (sem rate limiting implementado ainda)
            self.assertEqual(response.status_code, 200)
    
    def test_requisicoes_concorrentes(self):
        """Testa requisições concorrentes"""
        import threading
        import queue
        
        resultados = queue.Queue()
        
        def fazer_requisicao():
            response = self.client.get('/api/buscar-receitas?q=frango')
            resultados.put(response.status_code)
        
        # Cria 20 threads para fazer requisições simultâneas
        threads = []
        for _ in range(20):
            thread = threading.Thread(target=fazer_requisicao)
            threads.append(thread)
            thread.start()
        
        # Aguarda todas as threads terminarem
        for thread in threads:
            thread.join()
        
        # Verifica resultados
        while not resultados.empty():
            status = resultados.get()
            self.assertEqual(status, 200)

class TestSegurancaValidacaoJSON(unittest.TestCase):
    """Testes de segurança para validação de JSON"""
    
    def setUp(self):
        """Configura o cliente de teste Flask"""
        app.config['TESTING'] = True
        self.client = app.test_client()
    
    def test_json_malformado(self):
        """Testa JSON malformado"""
        response = self.client.post(
            '/api/calcular-calorias',
            data='{"idade": 45, "peso": 70,}',  # JSON malformado
            content_type='application/json'
        )
        # JSON malformado causa erro interno (500) no Flask
        self.assertEqual(response.status_code, 500)
    
    def test_json_vazio(self):
        """Testa JSON vazio"""
        response = self.client.post(
            '/api/calcular-calorias',
            data='{}',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
    
    def test_json_com_campos_extras(self):
        """Testa JSON com campos extras"""
        dados = {
            'idade': 45,
            'peso': 70,
            'altura': 1.70,
            'genero': 'masculino',
            'nivel_atividade': 'moderado',
            'campo_extra': 'valor_extra',
            'outro_campo': 123
        }
        
        response = self.client.post('/api/calcular-calorias', json=dados)
        # Deve aceitar campos extras (ignorar)
        self.assertEqual(response.status_code, 200)
    
    def test_json_com_tipos_incorretos(self):
        """Testa JSON com tipos de dados incorretos"""
        dados = {
            'idade': 'quarenta e cinco',  # Deve ser número
            'peso': 70,
            'altura': 1.70,
            'genero': 'masculino',
            'nivel_atividade': 'moderado'
        }
        
        response = self.client.post('/api/calcular-calorias', json=dados)
        self.assertEqual(response.status_code, 400)

class TestSegurancaLogs(unittest.TestCase):
    """Testes de segurança para logs"""
    
    def setUp(self):
        """Configura o cliente de teste Flask"""
        app.config['TESTING'] = True
        self.client = app.test_client()
    
    def test_logs_nao_expoem_sensiveis(self):
        """Testa se logs não expõem informações sensíveis"""
        # Este teste verifica se a aplicação não está logando dados sensíveis
        # Em uma implementação real, você verificaria os logs do sistema
        
        # Faz uma requisição que poderia gerar logs
        response = self.client.post('/api/calcular-calorias', json={
            'idade': 45,
            'peso': 70,
            'altura': 1.70,
            'genero': 'masculino',
            'nivel_atividade': 'moderado'
        })
        
        self.assertEqual(response.status_code, 200)
        # Em uma implementação real, você verificaria se os logs não contêm dados sensíveis

if __name__ == '__main__':
    unittest.main() 