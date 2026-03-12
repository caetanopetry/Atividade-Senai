from flask import Flask, render_template, request
import re
app = Flask(__name__)

contatos = []

@app.route("/", methods=["GET", "POST"])
def main():
    erro = None
    if request.method == "POST":
        nome = request.form.get("nome")
        telefone = request.form.get("telefone").strip()
        email = request.form.get("email").strip()
        
        if not nome or not telefone or not email:
            erro = "Todos os campos são obrigatórios."

        elif not re.fullmatch(r"[0-9()+-]{1,16}", telefone):
            erro = "Telefone deve conter apenas números e no máximo 16 dígitos."

        else:
            contatos.append({
                "nome": nome,
                "telefone": telefone,
                "email": email
            })


    return render_template("index.html", erro=erro)



@app.route("/contato")
def contato():
    return render_template("contato.html", contatos=contatos)

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

if __name__ == "__main__":
    app.run(debug=True)
