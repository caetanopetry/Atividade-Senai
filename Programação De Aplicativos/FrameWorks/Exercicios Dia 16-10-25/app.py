from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

conexao = mysql.connector.connect(host = 'localhost', port = '3306', user ='root', password = '', database = 'cinema_db')

@app.route("/")
def index():
    cursor = conexao.cursor(dictionary = True)
    cursor.execute("SELECT * FROM filmes")
    filmes = cursor.fetchall()
    
    return render_template("index.html", filmes = filmes)
 
@app.route("/novo")
def novo_filme():
    
    return render_template("novo.html")

@app.route("/salvar-filme", methods=["POST"])
def salvar_filme():
    titulo = request.form["titulo"]
    genero = request.form["genero"]
    ano = request.form["ano"]
    avaliacao = request.form["avaliacao"]
    
    sql = f"INSERT INTO filmes (titulo, genero, ano, avaliacao) VALUES (%s, %s, %s, %s)"
    cursor = conexao.cursor()       
    valores = (titulo, genero, ano, avaliacao)
    cursor.execute(sql, valores)
    conexao.commit()

    return redirect("/")


if __name__ == "__main__":

    
    app.run(debug=True)

    