class Funcionario:
    def __init__(self, nome, horas, pag_por_h):
        self.nome = nome
        self.horas = horas
        self.pag_por_h = pag_por_h
        self.salario = self.calcular_pagamento()

    def calcular_pagamento(self):
        return self.horas * self.pag_por_h

class FuncionarioCLT(Funcionario):
    def __init__(self, nome, horas):
        pag_por_h = 25.5
        super().__init__(nome, horas, pag_por_h)

class Freelancer(Funcionario):
    def __init__(self, nome, horas):
        pag_por_h = 35.5
        super().__init__(nome, horas, pag_por_h)

clt1 = FuncionarioCLT("Ana", 40)
print(clt1.salario)

freelancer1 = Freelancer("João", 30)
print(freelancer1.salario)
