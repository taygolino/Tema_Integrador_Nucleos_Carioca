
class Presenca:
    def __init__(self, idPresenca, cpfAluno, idAula, cpfProfessorValidador, status="PENDENTE"):
        self.idPresenca = idPresenca
        self.status = status
        self.cpfAluno = cpfAluno
        self.idAula = idAula
        self.cpfProfessorValidador = cpfProfessorValidador

