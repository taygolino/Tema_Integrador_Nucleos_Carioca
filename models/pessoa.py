
#Criando a Classe pessoa
class Pessoa: #Que agonia não ter chaves {}
    def __init__(self, cpf, nome, telefone, endereco, senha):
        self._cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self._senha = senha
        self.isLogado = False

    #Dica que peguei no google para getter no Python kkkkk
    @property
    def cpf(self):
        return self._cpf

    #E esse é o setter
    @cpf.setter
    def cpf(self, cpf):
        #Verificar se o CPF é válido
        self._cpf = cpf

    #Fazendo o mesmo para senha
    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha):
        self._senha = senha

    def visualizarPerfil(self):
        print("Visualizando o perfil")
        print(f"Cpf: {self.cpf}")
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}")
        #A senha não pode ser visualizada por motivos de segurança ;p

    def realizarLogin(self, cpf, senha):
        if(self.cpf == cpf and self.senha == senha):
            self.isLogado = True
            print("Você está logado")
        else:
            print("Erro!")
            print("Usuário e/ou senha incorreto(s)!")

    def realizarLogoff(self):
        self.isLogado = False
        print("Deslogado com sucesso!")