-- novo banco solicitado
CREATE DATABASE IF NOT EXISTS exercicio_loja;

-- Troca o ponteiro para o novo banco
USE exercicio_loja;

-- Cria as tabelas dele normalmente
CREATE TABLE clientes (
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(100));


SELECT * FROM clientes