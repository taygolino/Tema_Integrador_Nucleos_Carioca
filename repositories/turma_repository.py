from models.turma import Turma
from database.conexao import conectar

def listar_turmas():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM turma"
    cursor.execute(sql)

    turmas = cursor.fetchall()

    cursor.close()
    conexao.close()

    return turmas

def buscar_turma(idTurma):
    conexao = conectar()
    cursor = conexao.cursor()
    turma = None

    sql = "SELECT * FROM turma WHERE idTurma = %s"
    cursor.execute(sql, (idTurma,))
    turmaNova = cursor.fetchone()

    if turmaNova is not None:
        turma = Turma(turmaNova[0], turmaNova[1], turmaNova[2])
    else:
        print("Erro! Turma não encontrada!")

    cursor.close()
    conexao.close()
    return turma

def salvar_turma(nome, descricao):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "INSERT INTO turma (nome, descricao) VALUES (%s, %s)"
    valores = (nome, descricao)
    cursor.execute(sql, valores)
    conexao.commit()

    id_nova_turma = cursor.lastrowid

    print("Turma cadastrada com sucesso!")
    
    cursor.close()
    conexao.close()

    return id_nova_turma

def atualizar_turma(id_turma, nome, descricao):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "UPDATE turma SET nome = %s, descricao = %s WHERE idTurma = %s"
    valores = (nome, descricao, id_turma)
    cursor.execute(sql, valores)
    conexao.commit()

    print("Turma atualizada com sucesso!")
    
    cursor.close()
    conexao.close()


def deletar_turma(id_turma):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "DELETE from turma WHERE idTurma = %s"
    valor = (id_turma,)
    cursor.execute(sql, valor)
    conexao.commit()

    print("Turma excluída com sucesso!")

    linhas_afetadas = cursor.rowcount
    
    cursor.close()
    conexao.close()

    return linhas_afetadas