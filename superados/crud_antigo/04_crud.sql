-- Create
INSERT INTO aviso (titulo, descricao, dataPublicacao, idTurma, idProfessor) VALUES (
	'Suspensão de aula', 'No dia 15 de maio, não haverá aula', '2026-05-10', 1, 4
);

-- Read
SELECT 
  pessoa.nome,
  pessoa.telefone,
  aluno.idade,
  aluno.peso,
  aluno.altura,
  turma.nome AS turma
FROM aluno
INNER JOIN pessoa ON aluno.idPessoa = pessoa.idPessoa
INNER JOIN turma ON aluno.idTurma = turma.idTurma;

-- Update
UPDATE aluno SET peso = 70 WHERE idPessoa = 1;

-- Delete
DELETE FROM turma 
WHERE idTurma = 3 OR idTurma = 4;
