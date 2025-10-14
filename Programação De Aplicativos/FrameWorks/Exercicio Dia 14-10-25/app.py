from flask import Flask, render_template 
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():

    return render_template("index.html", titulo="Catálogo de Treinos Flask")

@app.route("/treinos.html")
def listar_treinos():
    conexao = mysql.connector.connect(host = 'localhost', port = '3306', user ='root', password = '', database = 'academia_flask')
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("select * from treinos")
    treinos = cursor.fetchall()

    return render_template("treinos.html", treinos = treinos)

@app.route("/alunos.html")
def ver_alunos():
    conexao = mysql.connector.connect(host='localhost', port='3306', user='root', password='', database='academia_flask')
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("select * from alunos")
    alunos = cursor.fetchall()
    total_alunos = len(alunos)

    return render_template("alunos.html", alunos=alunos, total_alunos=total_alunos)
    
if __name__ == "__main__":
    app.run(debug=True)