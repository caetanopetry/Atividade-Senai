from flask import Flask, render_template 
import mysql.connector

app = Flask(__name__)

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
    

if __name__ == "__main__":
    app.run(debug=True)