from models.professor import Professor
from database.conexao import conectar

def listar_professores():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT pessoa.cpf, pessoa.nome, pessoa.telefone, professor.cref FROM professor INNER JOIN pessoa ON professor.cpf = pessoa.cpf"
    cursor.execute(sql)

    professores = cursor.fetchall()

    cursor.close()
    conexao.close()

    return professores

def salvar_professor(cpf, nome, telefone, endereco, senha, cref):
    conexao = conectar()
    cursor = conexao.cursor()

    #Primeiro inserimos os dados em pessoa
    sql = "INSERT INTO pessoa (cpf, nome, telefone, endereco, senha_hash) VALUES (%s, %s, %s, %s, %s)"
    valores = (cpf, nome, telefone, endereco, senha)
    cursor.execute(sql, valores)

    #Agora inserimos em Professor
    sql = "INSERT INTO professor (cpf, cref) VALUES (%s, %s)"
    valores = (cpf, cref)
    cursor.execute(sql, valores)

    conexao.commit()

    print("Professor cadastrado com sucesso!")
    
    cursor.close()
    conexao.close()

def buscar_professor(cpf):
    conexao = conectar()
    cursor = conexao.cursor()
    professorEncontrado = None

    sql = "SELECT * FROM pessoa WHERE cpf = %s"
    cursor.execute(sql, (cpf,))
    pessoa = cursor.fetchone()

    sql = "SELECT * FROM professor WHERE cpf = %s"
    cursor.execute(sql, (cpf,))
    professor = cursor.fetchone()

    if pessoa is not None and professor is not None:
        professorEncontrado = Professor(pessoa[0],pessoa[1],pessoa[2],pessoa[3],pessoa[4],professor[1])
    else:
        print("Erro! Professor(a) não encontrado(a)!")

    cursor.close()
    conexao.close()
    return professorEncontrado

def atualizar_professor(cpf, nome, telefone, endereco, cref):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "UPDATE pessoa SET nome = %s, telefone = %s, endereco = %s WHERE cpf = %s"
    valores = (nome, telefone, endereco, cpf)
    cursor.execute(sql, valores)

    sql = "UPDATE professor SET cref = %s WHERE cpf = %s"
    valores = (cref, cpf)
    cursor.execute(sql, valores)

    conexao.commit()

    print("Professor(a) atualizado(a) com sucesso!")
    
    cursor.close()
    conexao.close()

def deletar_professor(cpf):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        sql = "DELETE from professor WHERE cpf = %s"
        valor = (cpf,)
        cursor.execute(sql, valor)
        linhas_afetadas = cursor.rowcount

        if linhas_afetadas > 0:
            sql = "DELETE from pessoa WHERE cpf = %s"
            valor = (cpf,)
            cursor.execute(sql, valor)

        conexao.commit()
        print("Professor(a) excluído(a) com sucesso!")
        return linhas_afetadas


    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()
