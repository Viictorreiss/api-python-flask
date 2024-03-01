from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def conectar():
    try:
        conn = mysql.connector.connect(
            host='seu_host',
            database='seu_banco_de_dados',
            user='seu_usuario',
            password='sua_senha'
        )
        if conn.is_connected():
            return conn
    except Error as e:
        print(e)

# Consultar todos os carros (GET)
@app.route('/carros', methods=['GET'])
def obter_carros():
    try:
        conn = conectar()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM carros")
        rows = cursor.fetchall()
        return jsonify(rows)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Consultar todos os carros por ID (GET)
@app.route('/carros/<int:id>', methods=['GET'])
def obter_carro_por_id(id):
    try:
        conn = conectar()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM carros WHERE id = %s", (id,))
        row = cursor.fetchone()
        return jsonify(row)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Editar os carros por ID (PUT)
@app.route('/carros/<int:id>', methods=['PUT'])
def editar_carro_por_id(id):
    carro_alterado = request.get_json()
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("UPDATE carros SET modelo = %s, marca = %s WHERE id = %s",
                       (carro_alterado['modelo'], carro_alterado['marca'], id))
        conn.commit()
        return jsonify(carro_alterado)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Criar carro (POST)
@app.route('/carros', methods=['POST'])
def incluir_novo_carro():
    novo_carro = request.get_json()
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO carros (modelo, marca) VALUES (%s, %s)",
                       (novo_carro['modelo'], novo_carro['marca']))
        conn.commit()
        novo_carro['id'] = cursor.lastrowid
        return jsonify(novo_carro)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Deletar um carro (DELETE)
@app.route('/carros/<int:id>', methods=['DELETE'])
def excluir_carro(id):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM carros WHERE id = %s", (id,))
        conn.commit()
        return jsonify({'message': 'Carro deletado com sucesso'})
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
