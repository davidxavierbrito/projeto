# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Funções matemáticas
def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Erro: Divisão por zero não permitida"
    return a / b

# Rotas Flask para as operações
@app.route('/soma', methods=['GET'])
def rota_soma():
    # Obtendo os parâmetros 'a' e 'b' da URL
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    resultado = soma(a, b)
    return jsonify({"resultado": resultado})

@app.route('/subtrai', methods=['GET'])
def rota_subtrai():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    resultado = subtrai(a, b)
    return jsonify({"resultado": resultado})

@app.route('/multiplica', methods=['GET'])
def rota_multiplica():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    resultado = multiplica(a, b)
    return jsonify({"resultado": resultado})

@app.route('/divide', methods=['GET'])
def rota_divide():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    resultado = divide(a, b)
    return jsonify({"resultado": resultado})

# Executando a aplicação Flask
if __name__ == "__main__":
    app.run(debug=True)
