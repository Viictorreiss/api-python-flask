
# API em Python (Flask) 🍀

É uma API simples com metodos GET, PUT, POST E DELETE

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


## Metodos 

```bash
@app.route('/carros',methods=['GET']) #GET
@app.route('/carros/<int:id>',methods=['GET']) #GET for ID
@app.route('/carros/<int:id>',methods=['PUT']) #PUT for ID
@app.route('/carros',methods=['POST'])  # POST
@app.route('/carros/<int:id>',methods=['DELETE']) # DELETE for ID
```

## Dependências

As informações abaixo são homologadas, caso utilize alguma divergente das informadas na sessão abaixa podem ocorrer quebras de consulta, métodos, bugs ou até mesmo inativação por completo do código.

|  Framework  |  Version  |
|-------------|-----------|
|    Python   |    3.12   |


|  Biblioteca |  Version  |
|-------------|-----------|
|    Flask    |   22.2.1  |
|    Flasgger   |   0.9.7 |
|    MySQL Connector  |   2.2.9  |


|   Database  |  Version  |
|-------------|-----------|
|  MySQL Server |   8.3   |

## Swagger
Acessivel através do caminho http://localhost:5000/apidocs, é possível realizar testes automatizados dos métodos da API tanto quanto entender quais parametros são necessários para realizar as requisições da aplicação.

<img src="assets\swagger.jpg" alt="swagger">

Toda a dependência do swagger fica encarregada da biblioteca Flasgger, com isso para funcionamento da documentação é necessário instalar ela via pip.

```bash
pip install flasgger
```


## Requisições

Para realizar os metodos PUT, POST e DELETE é necessário ter uma ferramenta de API para realizar as requisições, a utilizada no laboratório: 

```bash
Postman
```

<img src="assets\postman.jpeg" alt="postman">

## SGBD

Foi realizado a integração da API com um database MySQL para armazenar as requisições da nossa API.

Você pode criar o database com o seguinte script:

```
CREATE DATABASE IF NOT EXISTS sua_base_de_dados;
USE sua_base_de_dados;

CREATE TABLE IF NOT EXISTS carros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    modelo VARCHAR(255) NOT NULL,
    marca VARCHAR(255) NOT NULL
);
```

Para inserir dados de exemplos use:

```
INSERT INTO carros (modelo, marca) VALUES ('X1', 'BMW');
INSERT INTO carros (modelo, marca) VALUES ('Corolla', 'Toyota');
INSERT INTO carros (modelo, marca) VALUES ('Civic', 'Honda');

```
