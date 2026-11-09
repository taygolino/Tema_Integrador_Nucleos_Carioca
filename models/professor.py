
from models.pessoa import Pessoa
from models.aviso import Aviso
from models.aluno import Aluno
from datetime import date

#Criando a Classe professor
class Professor(Pessoa):

    def __init__(self, cpf, nome, telefone, endereco, senha, cref):
        super().__init__(cpf, nome, telefone, endereco, senha)
        self.cref = cref
        self.avisos = []

    def visualizarPerfil(self):
            super().visualizarPerfil()
            print(f"CREF: {self.cref}")

    def publicarAviso(self, idAviso, titulo, descricao, idTurma):
        aviso = Aviso(idAviso, titulo, descricao, date.today(), idTurma, self.cpf)
        self.avisos.append(aviso)
        print("Aviso publicado com sucesso!")

    #Aqui planejo fazer dois tipos, um relatório por turmas e um por alunos como parâmetro 
    def gerarRelatório(self):
        #preciso implementar
        print("Segue relatório")

    def validarPresenca(self, aluno):
        #preciso implementar
        print("Preseça validada com sucesso!")