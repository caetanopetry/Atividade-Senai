from abc import ABC

class forma(ABC):
    def area(self):
        pass

class quadrado(forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        print( self.lado * self.lado)

class circulo(forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        print(3.14 * self.raio * self.raio)
