
class animal:
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade

    def comer(self):
        print("Comendo...")

    def mostrar_idade(self):
        print(f"O animal {self.nome} tem: {self.idade} anos")

    def atualizar_peso(self, novo_peso):
        self.peso = novo_peso

    def mostrar_peso(self):
        print(f"O peso do animal {self.nome} é: {self.peso} kg")

class dog(animal):
    def __init__ (self, nome, idade, peso, qnt_amizade):
        super().__init__(nome, idade, peso)
        self.qnt_amizade = qnt_amizade
    
    def latir(self):
        print("Au Au")

class gato(animal):
    def __init__ (self, nome, idade, peso, qnt_vidas):
        super().__init__(nome, idade, peso)
        self.qnt_vidas = qnt_vidas

    def miar(self):
        print("Miau Miau")
    def comer(self):
        print("Comendo ração...")

objeto_cachorro = dog("Pitoco", 10, 20, 18)
objeto_gato = gato("Lili", 3, 6, 7)

objeto_cachorro.comer()
objeto_gato.comer()