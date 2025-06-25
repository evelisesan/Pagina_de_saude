from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
import math

app = Flask(__name__)
CORS(app)

# Dados mockados para receitas
RECEITAS = [
    {
        "id": 1,
        "titulo": "Frango Grelhado com Legumes",
        "ingredientes": ["Peito de frango", "Brócolis", "Cenoura", "Azeite", "Sal", "Pimenta"],
        "modo_preparo": "1. Tempere o frango\n2. Grelhe por 8 minutos cada lado\n3. Cozinhe os legumes no vapor",
        "calorias": 280,
        "tempo_preparo": 25,
        "dificuldade": "Fácil",
        "categoria": "proteina",
        "vegetariano": False,
        "baixa_caloria": True,
        "orcamento": "baixo"
    },
    {
        "id": 2,
        "titulo": "Salada de Quinoa",
        "ingredientes": ["Quinoa", "Tomate", "Pepino", "Cebola", "Limão", "Azeite"],
        "modo_preparo": "1. Cozinhe a quinoa\n2. Corte os legumes\n3. Misture tudo com limão e azeite",
        "calorias": 180,
        "tempo_preparo": 20,
        "dificuldade": "Fácil",
        "categoria": "vegetariano",
        "vegetariano": True,
        "baixa_caloria": True,
        "orcamento": "baixo"
    },
    {
        "id": 3,
        "titulo": "Sopa de Lentilha",
        "ingredientes": ["Lentilha", "Cebola", "Cenoura", "Alho", "Louro", "Sal"],
        "modo_preparo": "1. Refogue a cebola e alho\n2. Adicione os legumes\n3. Cozinhe com lentilha até ficar macio",
        "calorias": 220,
        "tempo_preparo": 45,
        "dificuldade": "Fácil",
        "categoria": "vegetariano",
        "vegetariano": True,
        "baixa_caloria": True,
        "orcamento": "baixo"
    }
]

# Dados mockados para exercícios
EXERCICIOS = [
    {
        "id": 1,
        "titulo": "Caminhada",
        "descricao": "Caminhada moderada ao ar livre ou na esteira",
        "como_fazer": "1. Mantenha postura ereta\n2. Balance os braços naturalmente\n3. Respire profundamente",
        "beneficios": ["Melhora cardiovascular", "Fortalece músculos", "Reduz estresse"],
        "precaucoes": ["Use tênis adequado", "Hidrate-se bem", "Comece devagar"],
        "duracao": "30-45 minutos",
        "series_repeticoes": "1 série de 30-45 min",
        "dificuldade": "iniciante",
        "video_url": "/static/videos/caminhada.mp4"
    },
    {
        "id": 2,
        "titulo": "Flexões de Parede",
        "descricao": "Flexões adaptadas para iniciantes usando a parede",
        "como_fazer": "1. Fique de frente para a parede\n2. Apoie as mãos na altura dos ombros\n3. Flexione os cotovelos até tocar a parede",
        "beneficios": ["Fortalece peito", "Melhora postura", "Aumenta força"],
        "precaucoes": ["Mantenha o corpo alinhado", "Não force demais", "Respire normalmente"],
        "duracao": "10-15 minutos",
        "series_repeticoes": "3 séries de 10-15 repetições",
        "dificuldade": "iniciante",
        "video_url": "/static/videos/flexoes-parede.mp4"
    },
    {
        "id": 3,
        "titulo": "Agachamento com Cadeira",
        "descricao": "Agachamento usando uma cadeira como apoio",
        "como_fazer": "1. Fique de frente para a cadeira\n2. Agache até tocar a cadeira\n3. Levante-se lentamente",
        "beneficios": ["Fortalece pernas", "Melhora equilíbrio", "Aumenta mobilidade"],
        "precaucoes": ["Mantenha os joelhos alinhados", "Não deixe os joelhos passarem dos pés", "Respire profundamente"],
        "duracao": "15-20 minutos",
        "series_repeticoes": "3 séries de 12-15 repetições",
        "dificuldade": "iniciante",
        "video_url": "/static/videos/agachamento-cadeira.mp4"
    }
]

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/calorias')
def calorias():
    """Página da calculadora de calorias"""
    return render_template('calorias.html')

@app.route('/receitas')
def receitas():
    """Página de receitas"""
    return render_template('receitas.html', receitas=RECEITAS)

@app.route('/receitas/<int:receita_id>')
def receita_detalhe(receita_id):
    """Página de detalhes da receita"""
    receita = next((r for r in RECEITAS if r['id'] == receita_id), None)
    if receita:
        return render_template('receita_detalhe.html', receita=receita)
    return "Receita não encontrada", 404

@app.route('/exercicios')
def exercicios():
    """Página de exercícios"""
    return render_template('exercicios.html', exercicios=EXERCICIOS)

@app.route('/exercicios/<int:exercicio_id>')
def exercicio_detalhe(exercicio_id):
    """Página de detalhes do exercício"""
    exercicio = next((e for e in EXERCICIOS if e['id'] == exercicio_id), None)
    if exercicio:
        return render_template('exercicio_detalhe.html', exercicio=exercicio)
    return "Exercício não encontrado", 404

@app.route('/imc')
def imc():
    """Página da calculadora de IMC"""
    return render_template('imc.html')

# APIs
@app.route('/api/calcular-calorias', methods=['POST'])
def calcular_calorias():
    """API para calcular calorias diárias"""
    data = request.get_json()
    
    idade = int(data.get('idade', 0))
    peso = float(data.get('peso', 0))
    altura = float(data.get('altura', 0))
    genero = data.get('genero', 'masculino')
    nivel_atividade = data.get('nivel_atividade', 'sedentario')
    
    # Fórmula de Harris-Benedict
    if genero == 'masculino':
        tmb = 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * idade)
    else:
        tmb = 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * idade)
    
    # Fatores de atividade
    fatores = {
        'sedentario': 1.2,
        'leve': 1.375,
        'moderado': 1.55,
        'ativo': 1.725,
        'muito_ativo': 1.9
    }
    
    calorias_diarias = tmb * fatores.get(nivel_atividade, 1.2)
    
    return jsonify({
        'calorias_diarias': round(calorias_diarias),
        'tmb': round(tmb),
        'nivel_atividade': nivel_atividade
    })

@app.route('/api/calcular-imc', methods=['POST'])
def calcular_imc():
    """API para calcular IMC"""
    data = request.get_json()
    
    peso = float(data.get('peso', 0))
    altura = float(data.get('altura', 0))
    
    imc = peso / (altura ** 2)
    
    # Classificação do IMC
    if imc < 18.5:
        classificacao = "Abaixo do Peso"
    elif imc < 25:
        classificacao = "Peso Normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    elif imc < 35:
        classificacao = "Obesidade Grau I"
    elif imc < 40:
        classificacao = "Obesidade Grau II"
    else:
        classificacao = "Obesidade Grau III"
    
    return jsonify({
        'imc': round(imc, 2),
        'classificacao': classificacao
    })

@app.route('/api/receitas')
def api_receitas():
    """API para listar receitas com filtros"""
    categoria = request.args.get('categoria')
    vegetariano = request.args.get('vegetariano')
    baixa_caloria = request.args.get('baixa_caloria')
    orcamento = request.args.get('orcamento')
    
    receitas_filtradas = RECEITAS.copy()
    
    if categoria:
        receitas_filtradas = [r for r in receitas_filtradas if r['categoria'] == categoria]
    if vegetariano == 'true':
        receitas_filtradas = [r for r in receitas_filtradas if r['vegetariano']]
    if baixa_caloria == 'true':
        receitas_filtradas = [r for r in receitas_filtradas if r['baixa_caloria']]
    if orcamento:
        receitas_filtradas = [r for r in receitas_filtradas if r['orcamento'] == orcamento]
    
    return jsonify(receitas_filtradas)

@app.route('/api/exercicios')
def api_exercicios():
    """API para listar exercícios com filtros"""
    dificuldade = request.args.get('dificuldade')
    
    exercicios_filtrados = EXERCICIOS.copy()
    
    if dificuldade:
        exercicios_filtrados = [e for e in exercicios_filtrados if e['dificuldade'] == dificuldade]
    
    return jsonify(exercicios_filtrados)

@app.route('/api/buscar-receitas')
def buscar_receitas():
    """API para buscar receitas por termo"""
    termo = request.args.get('q', '').lower()
    
    if not termo:
        return jsonify(RECEITAS)
    
    receitas_encontradas = []
    for receita in RECEITAS:
        if (termo in receita['titulo'].lower() or 
            any(termo in ingrediente.lower() for ingrediente in receita['ingredientes'])):
            receitas_encontradas.append(receita)
    
    return jsonify(receitas_encontradas)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)