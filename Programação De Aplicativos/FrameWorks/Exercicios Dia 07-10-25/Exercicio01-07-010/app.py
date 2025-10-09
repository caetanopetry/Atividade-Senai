from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Página inicial do site
    return render_template("index.html", titulo="Catálogo de Produtos Flask")

@app.route("/produtos")
def ver_produtos():

    lista_produtos = [
    {"nome": "Arroz Branco Tipo 1", "preco": 6.49, "estoque": 120},
    {"nome": "Feijão Carioca", "preco": 7.29, "estoque": 80},
    {"nome": "Macarrão Espaguete", "preco": 4.59, "estoque": 100},
    {"nome": "Açúcar Refinado", "preco": 3.99, "estoque": 60},
    {"nome": "Café Torrado e Moído", "preco": 15.90, "estoque": 45},
    {"nome": "Leite Integral 1L", "preco": 4.79, "estoque": 90},
    {"nome": "Biscoito Recheado Chocolate", "preco": 2.99, "estoque": 150},
    {"nome": "Refrigerante Cola 2L", "preco": 8.50, "estoque": 75},
    {"nome": "Óleo de Soja 900ml", "preco": 7.10, "estoque": 60},
    {"nome": "Margarina 500g", "preco": 5.60, "estoque": 40},
    {"nome": "Pão de Forma Tradicional", "preco": 6.20, "estoque": 55},
    {"nome": "Queijo Mussarela 500g", "preco": 22.90, "estoque": 25}
]

    return render_template("produtos.html", produtos =lista_produtos)


if __name__ == "__main__":
    app.run(debug=True)