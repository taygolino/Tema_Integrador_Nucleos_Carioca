from models.aula import Aula
from database.conexao import conectar

def listar_aulas():
    conexao = conectar()
    cursor = conexao.cursor()

    #TIME_FORMAT porque o pymysql devolve o campo TIME como timedelta (fica feio na tela)
    sql = "SELECT aula.idAula, aula.data, TIME_FORMAT(aula.hora, '%H:%i'), aula.descricao, turma.nome FROM aula INNER JOIN turma ON aula.idTurma = turma.idTurma ORDER BY aula.data, aula.hora"
    cursor.execute(sql)

    aulas = cursor.fetchall()

    cursor.close()
    conexao.close()

    return aulas

def buscar_aula(idAula):
    conexao = conectar()
    cursor = conexao.cursor()
    aula = None

    #Com parâmetro (%s) o pymysql exige %% para escrever um % literal
    sql = "SELECT idAula, data, TIME_FORMAT(hora, '%%H:%%i'), descricao, idTurma FROM aula WHERE idAula = %s"
    cursor.execute(sql, (idAula,))
    aulaNova = cursor.fetchone()

    if aulaNova is not None:
        aula = Aula(aulaNova[0], aulaNova[1], aulaNova[2], aulaNova[3], aulaNova[4])
    else:
        print("Erro! Aula não encontrada!")

    cursor.close()
    conexao.close()
    return aula

def salvar_aula(data, hora, descricao, idTurma):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        sql = "INSERT INTO aula (data, hora, descricao, idTurma) VALUES (%s, %s, %s, %s)"
        valores = (data, hora, descricao, idTurma)
        cursor.execute(sql, valores)
        conexao.commit()

        id_nova_aula = cursor.lastrowid

        print("Aula cadastrada com sucesso!")
        return id_nova_aula

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()

def atualizar_aula(id_aula, data, hora, descricao, idTurma):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        sql = "UPDATE aula SET data = %s, hora = %s, descricao = %s, idTurma = %s WHERE idAula = %s"
        valores = (data, hora, descricao, idTurma, id_aula)
        cursor.execute(sql, valores)
        conexao.commit()

        print("Aula atualizada com sucesso!")

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()

def deletar_aula(id_aula):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        sql = "DELETE from aula WHERE idAula = %s"
        valor = (id_aula,)
        cursor.execute(sql, valor)
        linhas_afetadas = cursor.rowcount

        conexao.commit()
        print("Aula excluída com sucesso!")
        return linhas_afetadas

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()
