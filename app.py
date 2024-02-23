from flask import Flask, jsonify, request

app = Flask(__name__)

carros = [
    {
        'id':1,
        'modelo': 'X1',
        'marca': 'BMW'
    },
    {
        'id':2,
        'modelo': 'Corolla',
        'marca': 'Toyota'
    },
    {
        'id':3,
        'modelo': 'Civic',
        'marca': 'Honda'
    },
]

# Consultar todos os carros (GET)
@app.route('/carros',methods=['GET']) #rota que o usuario vai chamar 
def obter_carros():                     # é a minha função, que é obter_carros
    return jsonify(carros)              # para retornar do db (sgbd) carros


# GET POR ID
@app.route('/carros/<int:id>',methods=['GET'])
def obter_carro_por_id(id):
    for carro in carros:
        if carro.get('id') == id:
            return jsonify(carro)

# PUT = EDITAR
@app.route('/carros/<int:id>',methods=['PUT'])
def editar_carro_por_id(id):
    carro_alterado = request.get_json()
    for indice,carro in enumerate(carros):
        if carro.get('id') == id:
            carros[indice].update(carro_alterado)
            return jsonify(carros[indice])

# POST = CRIAR
@app.route('/carros',methods=['POST'])      
def incluir_novo_carro():
    novo_carro = request.get_json()
    carros.append(novo_carro)
    return jsonify(carros)


# Deletar um carro (DEL)
@app.route('/carros/<int:id>',methods=['DELETE'])
def excluir_carro(id):
    for indice, carro in enumerate(carros):
        if carro.get('id') == id:
            del carros[indice]
        return jsonify(carros)


app.run(port=5000,host='localhost',debug=True)
