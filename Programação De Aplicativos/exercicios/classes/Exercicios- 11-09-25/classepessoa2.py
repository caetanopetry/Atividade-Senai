class pessoa:
    
    def __init__(self, nome, idade, religiao, artista_favorito):
        
        self.nome = nome
        self.idade = idade
        self.religiao = religiao
        self.artista = artista_favorito


    def apresentar(self):
        return f"Oi, eu sou o {self.nome} e tenho {self.idade}"
    
    def 
    
caetano = pessoa ("Caetano", 16)
print(caetano.apresentar())

class dog:
    def __init__ (self, nome, idade, peso, raça):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.raça = raça
        
    def latir(self):
        print("Au Au")
        return f"O {self.nome} que tem {self.idade} anos, cujo raça é {self.raça} acabou de latir "

objeto_dog = dog("Pitoco", 15, 50, "Vira-lata")
print(objeto_dog.latir())
