
from models.pessoa import Pessoa
from  models.presenca import Presenca

#Criando a Classe aluno
class Aluno(Pessoa):
    
    def __init__(self, cpf, nome, telefone, endereco, senha, nascimento, peso, altura, sexo, idTurma):
        super().__init__(cpf, nome, telefone, endereco, senha)
        self.nascimento = nascimento
        self.peso = peso
        self.altura = altura
        self.sexo = sexo
        self.idTurma = idTurma
        self.presencas = []

    # @override (sdds Java)
    def visualizarPerfil(self):
        super().visualizarPerfil()
        print(f"Idade: {self.nascimento}") #A ideia é calcular a idade antes
        print(f"Peso (kg): {self.peso}")
        print(f"Altura (cm): {self.altura}")
        print(f"Sexo: {self.sexo}")
        print(f"Turma: {self.idTurma}")

    def registrarPresenca(self, presenca):
        self.presencas.append(presenca)
        print("Presença Registrada!")
        print("Aguarde a confirmação de seu professor!")

    def consultarAgenda(self):
        #implementar o código
        print("-- Aulas disponíveis:")