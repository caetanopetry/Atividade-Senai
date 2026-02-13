from flask import Flask, render_template 
import mysql.connector

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1> Cherry Store</h1><a href = '/produtos'>Ver Produtos</a>"

@app.route("/produtos")
def listar_produtos():
    conexao = mysql.connector.connect(host = 'localhost', port = '3306', user ='root', password = '', database = 'cherry_store')
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("select * from produtos")
    produtos = cursor.fetchall()

    return render_template("produtos.html", produtos=produtos)

@app.route("/comprar")
def comprar():
    
    return render_template("produtos.html")

if __name__ == "__main__":
    app.run(debug=True)