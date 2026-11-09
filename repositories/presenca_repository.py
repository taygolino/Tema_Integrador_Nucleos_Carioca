from models.presenca import Presenca
from database.conexao import conectar

def listar_presencas():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT presenca.idPresenca, pessoa.nome, aula.data, aula.descricao, presenca.status FROM presenca INNER JOIN pessoa ON presenca.cpfAluno = pessoa.cpf INNER JOIN aula ON presenca.idAula = aula.idAula ORDER BY aula.data DESC, presenca.idPresenca DESC"
    cursor.execute(sql)

    presencas = cursor.fetchall()

    cursor.close()
    conexao.close()

    return presencas

def buscar_presenca(idPresenca):
    conexao = conectar()
    cursor = conexao.cursor()
    presenca = None

    sql = "SELECT idPresenca, cpfAluno, idAula, cpfProfessorValidador, status FROM presenca WHERE idPresenca = %s"
    cursor.execute(sql, (idPresenca,))
    presencaNova = cursor.fetchone()

    if presencaNova is not None:
        presenca = Presenca(presencaNova[0], presencaNova[1], presencaNova[2], presencaNova[3], presencaNova[4])
    else:
        print("Erro! Presença não encontrada!")

    cursor.close()
    conexao.close()
    return presenca

#É o aluno quem registra: nasce PENDENTE e sem professor validador
def salvar_presenca(cpfAluno, idAula):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        sql = "INSERT INTO presenca (status, cpfAluno, idAula, cpfProfessorValidador) VALUES (%s, %s, %s, %s)"
        valores = ("PENDENTE", cpfAluno, idAula, None)
        cursor.execute(sql, valores)
        conexao.commit()

        id_nova_presenca = cursor.lastrowid

        print("Presença registrada com sucesso! Aguarde a confirmação do professor!")
        return id_nova_presenca

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()

#É o professor quem valida: só o status e o validador mudam (aluno e aula não)
def atualizar_presenca(id_presenca, status, cpfProfessorValidador):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        sql = "UPDATE presenca SET status = %s, cpfProfessorValidador = %s WHERE idPresenca = %s"
        valores = (status, cpfProfessorValidador, id_presenca)
        cursor.execute(sql, valores)
        conexao.commit()

        print("Presença atualizada com sucesso!")

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()

def deletar_presenca(id_presenca):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        sql = "DELETE from presenca WHERE idPresenca = %s"
        valor = (id_presenca,)
        cursor.execute(sql, valor)
        linhas_afetadas = cursor.rowcount

        conexao.commit()
        print("Presença excluída com sucesso!")
        return linhas_afetadas

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()
