from datetime import date
from models.aviso import Aviso
from database.conexao import conectar

def listar_avisos():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT aviso.idAviso, aviso.titulo, aviso.dataPublicacao, turma.nome, pessoa.nome FROM aviso INNER JOIN turma ON aviso.idTurma = turma.idTurma INNER JOIN pessoa ON aviso.cpfProfessor = pessoa.cpf ORDER BY aviso.dataPublicacao DESC, aviso.idAviso DESC"
    cursor.execute(sql)

    avisos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return avisos

def buscar_aviso(idAviso):
    conexao = conectar()
    cursor = conexao.cursor()
    aviso = None

    sql = "SELECT idAviso, titulo, descricao, dataPublicacao, idTurma, cpfProfessor FROM aviso WHERE idAviso = %s"
    cursor.execute(sql, (idAviso,))
    avisoNovo = cursor.fetchone()

    if avisoNovo is not None:
        aviso = Aviso(avisoNovo[0], avisoNovo[1], avisoNovo[2], avisoNovo[3], avisoNovo[4], avisoNovo[5])
    else:
        print("Erro! Aviso não encontrado!")

    cursor.close()
    conexao.close()
    return aviso

def salvar_aviso(titulo, descricao, idTurma, cpfProfessor):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        #A data de publicação é a de hoje (mesma ideia do Professor.publicarAviso)
        sql = "INSERT INTO aviso (titulo, descricao, dataPublicacao, idTurma, cpfProfessor) VALUES (%s, %s, %s, %s, %s)"
        valores = (titulo, descricao, date.today(), idTurma, cpfProfessor)
        cursor.execute(sql, valores)
        conexao.commit()

        id_novo_aviso = cursor.lastrowid

        print("Aviso publicado com sucesso!")
        return id_novo_aviso

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()

#Quem publicou e a data de publicação não mudam na edição
def atualizar_aviso(id_aviso, titulo, descricao, idTurma):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        sql = "UPDATE aviso SET titulo = %s, descricao = %s, idTurma = %s WHERE idAviso = %s"
        valores = (titulo, descricao, idTurma, id_aviso)
        cursor.execute(sql, valores)
        conexao.commit()

        print("Aviso atualizado com sucesso!")

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()

def deletar_aviso(id_aviso):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        sql = "DELETE from aviso WHERE idAviso = %s"
        valor = (id_aviso,)
        cursor.execute(sql, valor)
        linhas_afetadas = cursor.rowcount

        conexao.commit()
        print("Aviso excluído com sucesso!")
        return linhas_afetadas

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()
