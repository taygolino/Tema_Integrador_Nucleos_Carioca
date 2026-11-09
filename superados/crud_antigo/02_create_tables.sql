CREATE TABLE pessoa (
	idPessoa INT AUTO_INCREMENT PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
telefone VARCHAR(15) UNIQUE NOT NULL,
endereco VARCHAR(100)
);

CREATE TABLE turma (
	idTurma INT AUTO_INCREMENT PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
descricao VARCHAR(100)
);

CREATE TABLE aluno (
idPessoa INT PRIMARY KEY,
idade INT,
peso DOUBLE,
altura DOUBLE,
sexo CHAR(1),
idTurma INT,
FOREIGN KEY (idPessoa) REFERENCES pessoa(idPessoa),
FOREIGN KEY (idTurma) REFERENCES turma(idTurma)
);

CREATE TABLE professor (
idPessoa INT PRIMARY KEY,
cref VARCHAR(11) UNIQUE NOT NULL,
FOREIGN KEY (idPessoa) REFERENCES pessoa(idPessoa)
);


CREATE TABLE aula (
idAula INT AUTO_INCREMENT PRIMARY KEY,
data DATE,
hora TIME,
descricao VARCHAR(100) NOT NULL,
idTurma INT,
FOREIGN KEY (idTurma) REFERENCES turma(idTurma)
);

CREATE TABLE aviso (
idAviso INT AUTO_INCREMENT PRIMARY KEY,
titulo VARCHAR(30) NOT NULL,
descricao VARCHAR(100) NOT NULL,
dataPublicacao DATE,
idTurma INT,
idProfessor INT,
FOREIGN KEY (idTurma) REFERENCES turma(idTurma),
FOREIGN KEY (idProfessor) REFERENCES professor(idPessoa)
);

CREATE TABLE presenca (
idPresenca INT AUTO_INCREMENT PRIMARY KEY,
status VARCHAR(20) DEFAULT 'pendente',
idAluno INT,
idAula INT,
idProfessor INT,
FOREIGN KEY (idAluno) REFERENCES aluno(idPessoa),
FOREIGN KEY (idAula) REFERENCES aula(idAula),
FOREIGN KEY (idProfessor) REFERENCES professor(idPessoa)
);
