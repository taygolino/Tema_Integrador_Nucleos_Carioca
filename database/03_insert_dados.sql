INSERT INTO pessoa (nome, telefone, endereco) VALUES (
'Lucia Olimpio', '(021)98755-4115', 'Rua A, nº50 - Oswaldo Cruz'
);

INSERT INTO pessoa (nome, telefone, endereco) VALUES (
'Madalena Olimpio', '(021)98445-5515', 'Rua A, nº51 - Oswaldo Cruz'
);

INSERT INTO pessoa (nome, telefone, endereco) VALUES (
'Maria Lucia', '(021)98777-1115', 'Rua A, nº70 - Oswaldo Cruz'
);

INSERT INTO pessoa (nome, telefone, endereco) VALUES (
'Sergio', '(021)95555-4444', 'Rua B, nº30 - Penha'
);

INSERT INTO turma (nome, descricao) VALUES (
	'manhã', 'Turma de exercícios funcionais para idosos'
);

INSERT INTO turma (nome, descricao) VALUES (
	'tarde', 'Turma de alongamento do período da tarde'
);

INSERT INTO turma (nome, descricao) VALUES (
	'manhã', 'Turma de exercícios funcionais para idosos'
);

INSERT INTO turma (nome, descricao) VALUES (
	'tarde', 'Turma de alongamento do período da tarde'
);

INSERT INTO aluno (idPessoa, idade, peso, altura, sexo, idTurma) VALUES (
	1, 67, 72.5, 1.60, 'F', 1
);

INSERT INTO aluno (idPessoa, idade, peso, altura, sexo, idTurma) VALUES (
	2, 70, 68.0, 1.58, 'F', 1
);

INSERT INTO aluno (idPessoa, idade, peso, altura, sexo, idTurma) VALUES (
	3, 65, 75.3, 1.63, 'F', 1
);

INSERT INTO professor (idPessoa, cref) VALUES (
	4, '123456-G/RJ'
);
