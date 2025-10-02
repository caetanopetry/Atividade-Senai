class pessoa:
    
    def __init__(self, nome, idade):
        
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Oi, eu sou o {self.nome} e tenho {self.idade}"
    
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
