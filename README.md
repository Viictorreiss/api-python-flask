
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
```
    

## Dependências

Para realizar os metodos PUT, POST e DELETE é necessário ter uma ferramenta de API para realizar as requisições, a utilizada no laboratório: 

```bash
Postman
```

<img src="assets\postman.jpeg" alt="postman">

## SGBD

Para realizar o laboratório de uma forma simples foi configurado uma lista no python invés de um SGBD

```
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
```