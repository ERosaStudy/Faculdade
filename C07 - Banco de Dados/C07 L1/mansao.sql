USE laboratorio;

DROP TABLE IF EXISTS investigacao;
	
CREATE TABLE IF NOT EXISTS investigacao (
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(100),
idade INT,
profissao VARCHAR(100),
cidade VARCHAR(100),
estava_na_sala_do_cofre BOOLEAN,
horario_visto TIME,
possui_alibi BOOLEAN,
quantidade_evidencias INT,
nivel_suspeita INT
);

-- inserção de dados 
INSERT INTO investigacao(nome, idade, profissao,
 cidade, estava_na_sala_do_cofre, horario_visto,
 possui_alibi, quantidade_evidencias, nivel_suspeita) VALUES ('Arthur Carvalho',
 45,'Empresário', 'São Paulo',TRUE,'23:00:00',FALSE,3,4);

INSERT INTO investigacao(nome, idade, profissao,
 cidade, estava_na_sala_do_cofre, horario_visto,
 possui_alibi, quantidade_evidencias, nivel_suspeita) VALUES ('Beatriz Moura',
 34,'Curadora de Arte', 'Campinas',FALSE,'23:45:00',TRUE,1,2);


INSERT INTO investigacao (nome, idade, profissao,
 cidade, estava_na_sala_do_cofre, horario_visto,
 possui_alibi, quantidade_evidencias, nivel_suspeita) VALUES ('Carlos Nogueira',
 52,'Colecionador', 'São Paulo',TRUE,'23:00:00',FALSE,4,5);
 
 
INSERT INTO investigacao (nome, idade, profissao,
 cidade, estava_na_sala_do_cofre, horario_visto,
 possui_alibi, quantidade_evidencias, nivel_suspeita) VALUES ('Daniela Rocha',
 29,'Jornalista', 'Santos',FALSE,'23:10:00',FALSE,2,3);

INSERT INTO investigacao (nome, idade, profissao,
 cidade, estava_na_sala_do_cofre, horario_visto,
 possui_alibi, quantidade_evidencias, nivel_suspeita) VALUES ('Eduardo Lima',
 41,'Advogado', 'Campinas',TRUE,'22:55:00',FALSE,2,4);


INSERT INTO investigacao (nome, idade, profissao,
 cidade, estava_na_sala_do_cofre, horario_visto,
 possui_alibi, quantidade_evidencias, nivel_suspeita) VALUES ('Fernanda Alves',
 38,'Arquiteta', 'Santos',FALSE,'22:40:00',TRUE,0,1);


INSERT INTO investigacao (nome, idade, profissao,
 cidade, estava_na_sala_do_cofre, horario_visto,
 possui_alibi, quantidade_evidencias, nivel_suspeita) VALUES ('Gustavo Prado',
 47,'Artista', 'São Paulo',TRUE,'23:00:00',FALSE,3,4);


INSERT INTO investigacao (nome, idade, profissao,
 cidade, estava_na_sala_do_cofre, horario_visto,
 possui_alibi, quantidade_evidencias, nivel_suspeita) VALUES ('Helena Duarte',
 31,'Restauradora de Arte', 'Campinas',FALSE,'22:50:00',FALSE,1,2);

-- update 
UPDATE investigacao SET nivel_suspeita = 3 WHERE id = 2;

SELECT * FROM investigacao;


 