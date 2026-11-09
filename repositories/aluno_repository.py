from models.aluno import Aluno
from database.conexao import conectar

def listar_alunos():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT pessoa.cpf, pessoa.nome, pessoa.telefone, aluno.idTurma FROM aluno INNER JOIN pessoa ON aluno.cpf = pessoa.cpf INNER JOIN turma ON aluno.idTurma = turma.idTurma"
    cursor.execute(sql)

    alunos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return alunos

def salvar_aluno(cpf, nome, telefone, endereco, senha, nascimento, peso, altura, sexo, idTurma):
    conexao = conectar()
    cursor = conexao.cursor()

    #Primeiro inserimos os dados em pessoa
    sql = "INSERT INTO pessoa (cpf, nome, telefone, endereco, senha_hash) VALUES (%s, %s, %s, %s, %s)"
    valores = (cpf, nome, telefone, endereco, senha)
    cursor.execute(sql, valores)

    #Agora inserimos em aluno
    sql = "INSERT INTO aluno (cpf, nascimento, peso, altura, sexo, idTurma) VALUES (%s, %s, %s, %s, %s, %s)"
    valores = (cpf, nascimento, peso, altura, sexo, idTurma)
    cursor.execute(sql, valores)

    conexao.commit()

    print("Aluno cadastrado com sucesso!")
    
    cursor.close()
    conexao.close()

def buscar_aluno(cpf):
    conexao = conectar()
    cursor = conexao.cursor()
    alunoEncontrado = None

    sql = "SELECT * FROM pessoa WHERE cpf = %s"
    cursor.execute(sql, (cpf,))
    pessoa = cursor.fetchone()

    sql = "SELECT * FROM aluno WHERE cpf = %s"
    cursor.execute(sql, (cpf,))
    aluno = cursor.fetchone()

    if pessoa is not None and aluno is not None:
        alunoEncontrado = Aluno(pessoa[0],pessoa[1],pessoa[2],pessoa[3],pessoa[4],aluno[1], aluno[2], aluno[3], aluno[4], aluno[5])
    else:
        print("Erro! Aluno não encontrado(a)!")

    cursor.close()
    conexao.close()
    return alunoEncontrado

def atualizar_aluno(cpf, nome, telefone, endereco, nascimento, peso, altura, sexo, idTurma):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "UPDATE pessoa SET nome = %s, telefone = %s, endereco = %s WHERE cpf = %s"
    valores = (nome, telefone, endereco, cpf)
    cursor.execute(sql, valores)

    sql = "UPDATE aluno SET nascimento = %s, peso = %s, altura = %s, sexo = %s, idTurma = %s WHERE cpf = %s"
    valores = (nascimento, peso, altura, sexo, idTurma, cpf)
    cursor.execute(sql, valores)

    conexao.commit()

    print("Aluno atualizado(a) com sucesso!")
    
    cursor.close()
    conexao.close()

def deletar_aluno(cpf):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        sql = "DELETE from aluno WHERE cpf = %s"
        valor = (cpf,)
        cursor.execute(sql, valor)
        linhas_afetadas = cursor.rowcount

        if linhas_afetadas > 0:
            sql = "DELETE from pessoa WHERE cpf = %s"
            valor = (cpf,)
            cursor.execute(sql, valor)

        conexao.commit()
        print("Aluno(a) excluído(a) com sucesso!")
        return linhas_afetadas


    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()
