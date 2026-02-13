from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", titulo="Catálogo de Filmes Flask")

@app.route("/filmes")
def filmes():

    lista_filmes = [
        {"titulo": "Interstellar", "ano": 2014, "genero": "Ficção Científica"},
        {"titulo": "O Rei do Show", "ano": 2017, "genero": "Musical"},
        {"titulo": "A Origem", "ano": 2010, "genero": "Ação"},
        {"titulo": "Soul", "ano": 2020, "genero": "Animação"},
        {"titulo": "Quarteto Fantástico:  Primeiros Passos", "ano": 2025, "genero": "Ação/Ficção científica"},

    ]
    return render_template("filmes.html", filmes=lista_filmes)

@app.route("/sobre")
def sobre():

    return render_template("sobre.html")

if __name__ == "__main__":
    app.run(debug=True)