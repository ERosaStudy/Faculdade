CREATE DATABASE IF NOT EXISTS steam_loja1;
USE steam_loja;

SET SQL_SAFE_UPDATES = 0;
-- questão 1 

CREATE TABLE IF NOT EXISTS Jogo (
    id_jogo INT AUTO_INCREMENT PRIMARY KEY,
    app_id CHAR(11) NOT NULL UNIQUE,
    titulo VARCHAR(50) NOT NULL,
    desenvolvedora VARCHAR(45) NOT NULL,
    genero VARCHAR(30) NOT NULL
);

CREATE TABLE IF NOT EXISTS Usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(30) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    data_cadastro DATE NOT NULL,
    faixa_etaria CHAR(3) NULL,
    CONSTRAINT chk_email_steam CHECK (email LIKE '%@steamplay.br')
);

CREATE TABLE IF NOT EXISTS Compra (
    id_compra INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    id_jogo INT,
    periodo VARCHAR(10) NOT NULL,
    status_compra ENUM('COMPRADO','ATIVADO','REEMBOLSADO','CANCELADO') NOT NULL DEFAULT 'COMPRADO',
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (id_jogo) REFERENCES Jogo(id_jogo)
);

-- questão 2

SHOW TABLES;
-- TRUNCATE TABLE Compra;
DROP DATABASE IF EXISTS steam_teste;

-- questão 3 

ALTER TABLE Jogo MODIFY titulo VARCHAR(50) NOT NULL;
ALTER TABLE Compra 
MODIFY status_compra ENUM('COMPRADO','ATIVADO','REEMBOLSADO','CANCELADO') 
NOT NULL DEFAULT 'COMPRADO';

-- update tabela Jogo

INSERT INTO Jogo (app_id, titulo, desenvolvedora, genero) VALUES
('10000000001','Stardew Valley','ConcernedApe','Simulação'),
('10000000002','Metaphor: ReFantazio','Atlus','JRPG'),
('10000000003','God of War III','Santa Monica Studios','Hack-n-Slash');

-- update tabela usuario

INSERT INTO Usuario (nome, email, data_cadastro, faixa_etaria) VALUES
('Amanda Loyola','amanda.l@steamplay.br','2021-02-01','ADU'),
('Danilo Almeida','danilo.a@steamplay.br','2021-02-01','JUV'),
('Jorge Augusto','jorge.a@steamplay.br','2022-02-01','INF'),
('Paula Carvalho','paula.c@steamplay.br','2023-02-01','IDO');

-- update tabela compra 

INSERT INTO Compra (id_usuario, id_jogo, periodo, status_compra) VALUES
(1,1,'2025-1','COMPRADO'),
(2,1,'2024-2','COMPRADO'),
(3,2,'2024-1','REEMBOLSADO'),
(4,3,'2024-1','ATIVADO'),
(1,2,'2024-2','CANCELADO');

-- questão 4
-- a
UPDATE Compra SET status_compra='COMPRADO' WHERE id_compra=4;
-- b
UPDATE Jogo SET genero='Indie' WHERE desenvolvedora='ConcernedApe';
-- c
UPDATE Usuario SET email='amanda.loyola@steamplay.br', faixa_etaria='JUV' WHERE id_usuario=1;

-- questao 5
DELETE FROM Compra WHERE id_compra =5;

-- A FK de Compra para Jogo deve usar ON DELETE SET NULL
-- para manter o histórico mesmo quando o jogo for removido.

-- questão 6

SELECT nome, email
FROM Usuario
WHERE faixa_etaria IN ('ADU','IDO')
ORDER BY email DESC;

SELECT id_jogo, COUNT(*) AS qtd_compras, MIN(periodo) AS periodo_antigo
FROM Compra
WHERE periodo LIKE '2024%'
GROUP BY id_jogo
ORDER BY qtd_compras ASC;

SELECT status_compra, COUNT(*) AS total
FROM Compra
GROUP BY status_compra
HAVING COUNT(*) > 1;
