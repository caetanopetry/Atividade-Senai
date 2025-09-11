class carro:
    
    def __init__(self, ano, marca, modelo):
        self.ano = ano
        self.marca = marca
        self.modelo = modelo

    def ligar(self):
        return f"{self.modelo} Carro LIGANDO "

    def desligar(self):
        return f"{self.modelo} DESLIGANDOOOOO"
    
    def apresentar(self):
        return f"Olá, eu sou o {self.modelo} da marca {self.marca} do ano {self.ano}"
    
carro1 = carro(2006, "Chevrolet", "TrailBLAZER")
carro2 = carro(1997, "Chevrolet", "Vectra Elegance")
carro3 = carro(2014, "Renault", "Duster")

print(carro1.apresentar())
print(carro1.ligar())
print(carro1.desligar())
print("\n")

print(carro2.apresentar())
print(carro2.ligar())
print(carro2.desligar())
print("\n")

print(carro3.apresentar())
print(carro3.ligar())
print(carro3.desligar())
print("\n")