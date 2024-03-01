CREATE DATABASE IF NOT EXISTS sua_base_de_dados;
USE sua_base_de_dados;

CREATE TABLE IF NOT EXISTS carros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    modelo VARCHAR(255) NOT NULL,
    marca VARCHAR(255) NOT NULL
);

-- Inserindo alguns dados de exemplo
INSERT INTO carros (modelo, marca) VALUES ('X1', 'BMW');
INSERT INTO carros (modelo, marca) VALUES ('Corolla', 'Toyota');
INSERT INTO carros (modelo, marca) VALUES ('Civic', 'Honda');
