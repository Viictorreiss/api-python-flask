
# API em Python (Flask)

É uma API simples com metodos GET, PUT, POST E DELETE

## Metodos

```bash
@app.route('/carros',methods=['GET']) #GET
@app.route('/carros/<int:id>',methods=['GET']) #GET for ID
@app.route('/carros/<int:id>',methods=['PUT']) #PUT for ID
@app.route('/carros',methods=['POST'])  # POST
@app.route('/carros/<int:id>',methods=['DELETE']) # DELETE for ID
```

## Instalação

Instale my-project com npm

```bash
  python3 install
  pip install
  pip install flask
  pip install mysql.connector
```
    

## Dependências

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
