from flask import Flask, render_template, request

app = Flask (__name__)

@app.route("/")

#rota principal
def home():
    return render_template("index.html")


@app.route("/alunos")
def mostrar_alunos():
    alunos = [
        {"Nome": "Lucas", "Idade": 18, "Nota": 0},
        {"Nome": "Caetano", "Idade": 16, "Nota": 9},
        {"Nome": "Guilherme", "Idade": 16, "Nota": 10},
        {"Nome": "Henrique", "Idade": 16, "Nota": 10}
    ]
    return render_template("alunos.html", lista_alunos = alunos)


if __name__ == "__main__":
    app.run(debug = True)