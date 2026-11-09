#importando geral
from repositories.turma_repository import buscar_turma, salvar_turma, atualizar_turma, deletar_turma, listar_turmas
from repositories.aluno_repository import listar_alunos, salvar_aluno, buscar_aluno, atualizar_aluno, deletar_aluno
from repositories.professor_repository import listar_professores, salvar_professor, buscar_professor, atualizar_professor, deletar_professor
from repositories.aula_repository import listar_aulas, salvar_aula, buscar_aula, atualizar_aula, deletar_aula
from repositories.aviso_repository import listar_avisos, salvar_aviso, buscar_aviso, atualizar_aviso, deletar_aviso
from repositories.presenca_repository import listar_presencas, salvar_presenca, buscar_presenca, atualizar_presenca, deletar_presenca
from database.conexao import conectar
from flask import Flask, render_template, redirect, request, url_for
from pymysql.err import IntegrityError

app = Flask(__name__)

#Página inicial -------------------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")
# Fim da página inicial -------------------------------------------------------

#Rotas para as Turmas -------------------------------------------------------
@app.route("/turma/lista", methods=["GET"])
def lista_de_turmas():
    turmas = listar_turmas()

    return render_template("listar_turma.html", turmas=turmas)

@app.route("/turma/<int:id_turma>")
def visualizar_turma(id_turma):
    turma = buscar_turma(id_turma)

    if turma is None:
        return "Turma não encontrada!", 404

    return render_template("turma.html", turma=turma)

@app.route("/turmas/cadastrar", methods=["GET", "POST"])
def cadastrar_turma():
    if request.method == "POST":
        nome = request.form.get("nome")
        descricao = request.form.get("descricao")

        id_turma = salvar_turma(nome, descricao)

        return redirect(url_for("visualizar_turma", id_turma=id_turma))

    return render_template("cadastrar_turma.html")

@app.route("/turmas/editar/<int:id_turma>", methods=["GET", "POST"])
def editar_turma(id_turma):
    turma = buscar_turma(id_turma)

    if turma is None:
        return "Turma não encontrada!", 404

    if request.method == "POST":
            nome = request.form.get("nome")
            descricao = request.form.get("descricao")
    
            atualizar_turma(turma.idTurma, nome, descricao)
    
            return redirect(url_for("visualizar_turma", id_turma=turma.idTurma))

    return render_template("atualizar_turma.html", turma=turma)

@app.route("/turmas/excluir/<int:id_turma>", methods=["POST"])
def excluir_turma(id_turma):
    turma = buscar_turma(id_turma)
    
    if turma is None:
        return "Turma não encontrada!", 404

    if request.method == "POST":
        linhas_afetadas = deletar_turma(id_turma)

        if (linhas_afetadas == 0):
            print("regristro não encontrado e/ou já excluído")
        else:
            print("Exclusão realizada com sucesso!")

    return redirect(url_for("cadastrar_turma"))

# Fim das rotas das turmas ---------------------------------------------------

# Rotas dos Alunos -------------------------------------------------------------
@app.route("/alunos/lista", methods=["GET"])
def lista_de_alunos():
    alunos = listar_alunos()

    return render_template("listar_alunos.html", alunos=alunos)

@app.route("/alunos/cadastrar", methods=["GET", "POST"])
def cadastrar_aluno():
    if request.method == "POST":
        cpf = request.form.get("cpf")
        nome = request.form.get("nome")
        telefone = request.form.get("telefone")
        endereco = request.form.get("endereco")
        nascimento = request.form.get("nascimento")
        peso = request.form.get("peso")
        altura = request.form.get("altura")
        sexo = request.form.get("sexo")
        idTurma = request.form.get("idTurma")
        senha = request.form.get("senha")

        salvar_aluno(cpf, nome, telefone, endereco, senha, nascimento, peso, altura, sexo, idTurma)


        return redirect(url_for("visualizar_aluno", cpf=cpf))

    return render_template("cadastrar_aluno.html")

@app.route("/alunos/<cpf>")
def visualizar_aluno(cpf):
    aluno = buscar_aluno(cpf)

    if aluno is None:
        return "Aluno não encontrado!", 404

    return render_template("aluno.html", aluno=aluno)

@app.route("/alunos/editar/<cpf>", methods=["GET", "POST"])
def editar_aluno(cpf):
    aluno = buscar_aluno(cpf)

    if aluno is None:
        return "Aluno(a) não encontrado(a)!", 404

    if request.method == "POST":
            nome = request.form.get("nome")
            telefone = request.form.get("telefone")
            endereco = request.form.get("endereco")
            nascimento = request.form.get("nascimento")
            peso = request.form.get("peso")
            altura = request.form.get("altura")
            sexo = request.form.get("sexo")
            idTurma = request.form.get("idTurma")
    
            atualizar_aluno(aluno.cpf, nome, telefone, endereco, nascimento, peso, altura, sexo, idTurma)
    
            return redirect(url_for("visualizar_aluno", cpf=aluno.cpf))

    return render_template("atualizar_aluno.html", aluno=aluno)

@app.route("/alunos/excluir/<cpf>", methods=["POST"])
def excluir_aluno(cpf):
    aluno = buscar_aluno(cpf)
    
    if aluno is None:
        return "Aluno(a) não encontrado(a)!", 404

    if request.method == "POST":
        linhas_afetadas = deletar_aluno(cpf)

        if (linhas_afetadas == 0):
            print("regristro não encontrado e/ou já excluído")
        else:
            print("Exclusão realizada com sucesso!")

    return redirect(url_for("cadastrar_aluno"))


# Fim das rotas dos Alunos -----------------------------------------------------

# Rotas do Professores -----------------------------------------------------------
@app.route("/professores/lista", methods=["GET"])
def lista_de_professores():
    professores = listar_professores()

    return render_template("listar_professor.html", professores=professores)

@app.route("/professores/cadastrar", methods=["GET", "POST"])
def cadastrar_professor():
    if request.method == "POST":
        cpf = request.form.get("cpf")
        nome = request.form.get("nome")
        telefone = request.form.get("telefone")
        endereco = request.form.get("endereco")
        cref = request.form.get("cref")
        senha = request.form.get("senha")

        salvar_professor(cpf, nome, telefone, endereco, senha, cref)


        return redirect(url_for("visualizar_professor", cpf=cpf))

    return render_template("cadastrar_professor.html")

@app.route("/professor/<cpf>")
def visualizar_professor(cpf):
    professor = buscar_professor(cpf)

    if professor is None:
        return "Professor(a) não encontrado(a)!", 404

    return render_template("professor.html", professor=professor)

@app.route("/professor/editar/<cpf>", methods=["GET", "POST"])
def editar_professor(cpf):
    professor = buscar_professor(cpf)

    if professor is None:
        return "Professor(a) não encontrado(a)!", 404

    if request.method == "POST":
            nome = request.form.get("nome")
            telefone = request.form.get("telefone")
            endereco = request.form.get("endereco")
            cref = request.form.get("cref")
    
            atualizar_professor(professor.cpf, nome, telefone, endereco, cref)
    
            return redirect(url_for("visualizar_professor", cpf=professor.cpf))

    return render_template("atualizar_professor.html", professor=professor)

@app.route("/professores/excluir/<cpf>", methods=["POST"])
def excluir_professor(cpf):
    professor = buscar_professor(cpf)
    
    if professor is None:
        return "Professor(a) não encontrado(a)!", 404

    if request.method == "POST":
        linhas_afetadas = deletar_professor(cpf)

        if (linhas_afetadas == 0):
            print("regristro não encontrado e/ou já excluído")
        else:
            print("Exclusão realizada com sucesso!")

    return redirect(url_for("cadastrar_professor"))

# Fim das rotas dos Professores -----------------------------------------------------

# Rotas das Aulas -------------------------------------------------------------
#IntegrityError acontece quando o idTurma digitado não existe (ou a aula já tem presenças e não pode ser excluída)
@app.route("/aulas/lista", methods=["GET"])
def lista_de_aulas():
    aulas = listar_aulas()

    return render_template("listar_aula.html", aulas=aulas)

@app.route("/aulas/cadastrar", methods=["GET", "POST"])
def cadastrar_aula():
    if request.method == "POST":
        data = request.form.get("data")
        hora = request.form.get("hora")
        descricao = request.form.get("descricao")
        idTurma = request.form.get("idTurma")

        try:
            id_aula = salvar_aula(data, hora, descricao, idTurma)
        except IntegrityError:
            return "Não foi possível cadastrar a aula: confira se a turma informada existe!", 400

        return redirect(url_for("visualizar_aula", id_aula=id_aula))

    return render_template("cadastrar_aula.html")

@app.route("/aulas/<int:id_aula>")
def visualizar_aula(id_aula):
    aula = buscar_aula(id_aula)

    if aula is None:
        return "Aula não encontrada!", 404

    return render_template("aula.html", aula=aula)

@app.route("/aulas/editar/<int:id_aula>", methods=["GET", "POST"])
def editar_aula(id_aula):
    aula = buscar_aula(id_aula)

    if aula is None:
        return "Aula não encontrada!", 404

    if request.method == "POST":
            data = request.form.get("data")
            hora = request.form.get("hora")
            descricao = request.form.get("descricao")
            idTurma = request.form.get("idTurma")

            try:
                atualizar_aula(aula.idAula, data, hora, descricao, idTurma)
            except IntegrityError:
                return "Não foi possível atualizar a aula: confira se a turma informada existe!", 400

            return redirect(url_for("visualizar_aula", id_aula=aula.idAula))

    return render_template("atualizar_aula.html", aula=aula)

@app.route("/aulas/excluir/<int:id_aula>", methods=["POST"])
def excluir_aula(id_aula):
    aula = buscar_aula(id_aula)

    if aula is None:
        return "Aula não encontrada!", 404

    try:
        linhas_afetadas = deletar_aula(id_aula)
    except IntegrityError:
        return "Não é possível excluir: esta aula já possui presenças registradas!", 400

    if (linhas_afetadas == 0):
        print("regristro não encontrado e/ou já excluído")
    else:
        print("Exclusão realizada com sucesso!")

    return redirect(url_for("cadastrar_aula"))

# Fim das rotas das Aulas -----------------------------------------------------

# Rotas dos Avisos ------------------------------------------------------------
@app.route("/avisos/lista", methods=["GET"])
def lista_de_avisos():
    avisos = listar_avisos()

    return render_template("listar_aviso.html", avisos=avisos)

@app.route("/avisos/cadastrar", methods=["GET", "POST"])
def cadastrar_aviso():
    if request.method == "POST":
        titulo = request.form.get("titulo")
        descricao = request.form.get("descricao")
        idTurma = request.form.get("idTurma")
        cpfProfessor = request.form.get("cpfProfessor")

        try:
            id_aviso = salvar_aviso(titulo, descricao, idTurma, cpfProfessor)
        except IntegrityError:
            return "Não foi possível publicar o aviso: confira se a turma e o CPF do professor existem!", 400

        return redirect(url_for("visualizar_aviso", id_aviso=id_aviso))

    return render_template("cadastrar_aviso.html")

@app.route("/avisos/<int:id_aviso>")
def visualizar_aviso(id_aviso):
    aviso = buscar_aviso(id_aviso)

    if aviso is None:
        return "Aviso não encontrado!", 404

    return render_template("aviso.html", aviso=aviso)

@app.route("/avisos/editar/<int:id_aviso>", methods=["GET", "POST"])
def editar_aviso(id_aviso):
    aviso = buscar_aviso(id_aviso)

    if aviso is None:
        return "Aviso não encontrado!", 404

    if request.method == "POST":
            titulo = request.form.get("titulo")
            descricao = request.form.get("descricao")
            idTurma = request.form.get("idTurma")

            try:
                atualizar_aviso(aviso.idAviso, titulo, descricao, idTurma)
            except IntegrityError:
                return "Não foi possível atualizar o aviso: confira se a turma informada existe!", 400

            return redirect(url_for("visualizar_aviso", id_aviso=aviso.idAviso))

    return render_template("atualizar_aviso.html", aviso=aviso)

@app.route("/avisos/excluir/<int:id_aviso>", methods=["POST"])
def excluir_aviso(id_aviso):
    aviso = buscar_aviso(id_aviso)

    if aviso is None:
        return "Aviso não encontrado!", 404

    linhas_afetadas = deletar_aviso(id_aviso)

    if (linhas_afetadas == 0):
        print("regristro não encontrado e/ou já excluído")
    else:
        print("Exclusão realizada com sucesso!")

    return redirect(url_for("cadastrar_aviso"))

# Fim das rotas dos Avisos ----------------------------------------------------

# Rotas das Presenças ---------------------------------------------------------
@app.route("/presencas/lista", methods=["GET"])
def lista_de_presencas():
    presencas = listar_presencas()

    return render_template("listar_presenca.html", presencas=presencas)

#O aluno registra a presença (fica PENDENTE até o professor validar)
@app.route("/presencas/cadastrar", methods=["GET", "POST"])
def cadastrar_presenca():
    if request.method == "POST":
        cpfAluno = request.form.get("cpfAluno")
        idAula = request.form.get("idAula")

        try:
            id_presenca = salvar_presenca(cpfAluno, idAula)
        except IntegrityError:
            return "Não foi possível registrar a presença: confira o CPF do aluno e o código da aula (a presença também não pode ser registrada duas vezes)!", 400

        return redirect(url_for("visualizar_presenca", id_presenca=id_presenca))

    return render_template("cadastrar_presenca.html")

@app.route("/presencas/<int:id_presenca>")
def visualizar_presenca(id_presenca):
    presenca = buscar_presenca(id_presenca)

    if presenca is None:
        return "Presença não encontrada!", 404

    return render_template("presenca.html", presenca=presenca)

@app.route("/presencas/editar/<int:id_presenca>", methods=["GET", "POST"])
def editar_presenca(id_presenca):
    presenca = buscar_presenca(id_presenca)

    if presenca is None:
        return "Presença não encontrada!", 404

    if request.method == "POST":
            status = request.form.get("status")
            #Campo vazio vira None (NULL no banco), senão o MariaDB tentaria achar um professor de CPF ""
            cpfProfessorValidador = request.form.get("cpfProfessorValidador") or None

            if status == "PENDENTE":
                cpfProfessorValidador = None
            elif cpfProfessorValidador is None:
                return "Informe o CPF do professor que está validando/recusando a presença!", 400

            try:
                atualizar_presenca(presenca.idPresenca, status, cpfProfessorValidador)
            except IntegrityError:
                return "Não foi possível atualizar a presença: confira se o CPF do professor existe!", 400

            return redirect(url_for("visualizar_presenca", id_presenca=presenca.idPresenca))

    return render_template("atualizar_presenca.html", presenca=presenca)

@app.route("/presencas/excluir/<int:id_presenca>", methods=["POST"])
def excluir_presenca(id_presenca):
    presenca = buscar_presenca(id_presenca)

    if presenca is None:
        return "Presença não encontrada!", 404

    linhas_afetadas = deletar_presenca(id_presenca)

    if (linhas_afetadas == 0):
        print("regristro não encontrado e/ou já excluído")
    else:
        print("Exclusão realizada com sucesso!")

    return redirect(url_for("cadastrar_presenca"))

# Fim das rotas das Presenças -------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)



