from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

conexao = mysql.connector.connect(host = 'localhost', port = '3306', user ='root', password = '', database = 'cinema_flask')
cursor = conexao.cursor(dictionary=True)

@app.route("/")
def home():

    return render_template("index.html", titulo="Catálogo de Filmes Flask")

@app.route("/filmes.html")
def listar_filmes():
    conexao = mysql.connector.connect(host = 'localhost', port = '3306', user ='root', password = '', database = 'cinema_flask')
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("select * from filmes")
    filmes = cursor.fetchall()

    return render_template("filmes.html", filmes = filmes)

@app.route("/salas.html")
def ver_salas():
    conexao = mysql.connector.connect(host = 'localhost', port = '3306', user ='root', password = '', database = 'cinema_flask')
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("select * from salas")
    salas = cursor.fetchall()

    return render_template("salas.html", salas = salas)

@app.route("/nova_sala.html")
def novo_sala():
    
    return render_template("nova_sala.html")

@app.route("/salvar_sala", methods=["POST"])
def salvar_sala():
    nome = request.form["nome"]
    capacidade = request.form["capacidade"]
    localizacao = request.form["localizacao"]
    
    sql = f"INSERT INTO salas (nome, capacidade, localizacao) VALUES (%s, %s, %s)"
    cursor = conexao.cursor()       
    valores = (nome, capacidade, localizacao)
    cursor.execute(sql, valores)
    conexao.commit()

    return redirect("/")

@app.route("/novo_filme.html")
def novo_filme():
    
    return render_template("novo_filme.html")


@app.route("/salvar_filme", methods=["POST"])
def salvar_filme():
    titulo = request.form["titulo"]
    genero = request.form["genero"]
    avaliacao = request.form["avaliacao"]
    ano = request.form["ano"]
    
    sql = f"INSERT INTO filmes (titulo, genero, avaliacao, ano) VALUES (%s, %s, %s, %s)"
    cursor = conexao.cursor()       
    valores = (titulo, genero, avaliacao, ano)
    cursor.execute(sql, valores)
    conexao.commit()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)