class retangulo():
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def area(self):
        area = self.altura * self.largura
        return f"A área do retângulo que tem {self.altura} de altura e {self.largura} de largura é {area}"
    
    def peri(self):
        perimetro = 2 * (self.altura + self.largura)
        return f"O perímetro do retângulo que tem {self.altura} de altura e {self.largura} de largura é {perimetro}"
    
retangulo1 = retangulo(15, 30)
retangulo2 = retangulo(30, 15)

print(retangulo1.area())
print(retangulo2.area())
print(retangulo1.peri())
print(retangulo2.peri())
