from flask import Flask, render_template, request

app = Flask (__name__)

@app.route("/")

#rota principal
def home():
    ficha_personagem = { 'nome' : 'Arion, o Bravo' , 'classe' : 'Guerreiro' , 'nivel' : 12 , 'habilidades' : [ 'Ataque Giratório' , 'Fúria de Batalha' , 'Escudo Protetor' ], 'tem_pet' : True }
    return render_template( 'personagem.html' , personagem=ficha_personagem)


if __name__ == "__main__":
    app.run(debug = True)
