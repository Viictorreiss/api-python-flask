# API in Python (Flask) 

It is a simple API with GET, PUT, POST and DELETE methods

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


## Methods 

```bash
@app.route('/carros',methods=['GET']) #GET
@app.route('/carros/<int:id>',methods=['GET']) #GET for ID
@app.route('/carros/<int:id>',methods=['PUT']) #PUT for ID
@app.route('/carros',methods=['POST']) # POST
@app.route('/carros/<int:id>',methods=['DELETE']) # DELETE for ID
```

## Dependencies

The information below is approved, if you use any information that differs from that informed in the section below, query breaks, methods, bugs or even complete inactivation of the code may occur.

|  Framework |  Version |
|-------------|-----------|
|    Python |    3.12 |


|  Library |  Version |
|-------------|-----------|
|    Flask |   22.2.1 |
|    Flagger |   0.9.7 |
|    MySQL Connector |   2.2.9 |


|   Database |  Version |
|-------------|-----------|
|  MySQL Server |   8.3 |

## Swagger
Accessible via the path http://localhost:5000/apidocs, it is possible to carry out automated tests of the API methods as well as understand which parameters are necessary to carry out the application's requests.

<img src="assets\swagger.jpg" alt="swagger">

All swagger dependencies are handled by the Flasgger library, so for the documentation to work it is necessary to install it via pip.

```bash
pip install flagger
```

## Requests

To perform the PUT, POST and DELETE methods it is necessary to have an API tool to make the requests, the one used in the laboratory: 

```bash
Postman
```

<img src="assets\postman.jpeg" alt="postman">

## DBMS

The API was integrated with a MySQL database to store our API requests.

You can create the database with the following script:

```
CREATE DATABASE IF NOT EXISTS your_data_base;
USE your_data_base;

CREATE TABLE IF NOT EXISTS cars (
    id INT AUTO_INCREMENT PRIMARY KEY,
    model VARCHAR(255) NOT NULL,
    mark VARCHAR(255) NOT NULL
);
```

To enter example data use:

```
INSERT INTO cars (model, make) VALUES ('X1', 'BMW');
INSERT INTO cars (model, make) VALUES ('Corolla', 'Toyota');
INSERT INTO cars (model, make) VALUES ('Civic', 'Honda');
```

## Observations

This template is a technical guide to follow and even study (if necessary) how Python + Streamlit works. 

### The template is open source for everyone to enjoy and implement their idea on top of it as needed.

