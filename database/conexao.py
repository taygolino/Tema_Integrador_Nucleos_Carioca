import pymysql

def conectar():
    conexao = pymysql.connect(
        host="localhost",
        user="root",
        password="", #senha excluída por razões de segurança
        database="nucleos_cariocas",
        charset="utf8mb4"
    )
    return conexao