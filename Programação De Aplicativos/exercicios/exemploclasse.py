# class pessoa:
    
#     def __init__(self, nome, idade):
        
#         self.nome = nome
#         self.idade = idade

#     def apresentar(self):
#         return f"Oi, eu sou o {self.nome} e tenho {self.idade}"
    
# caetano = pessoa ("Caetano", 16)
# print(caetano.apresentar())

# class dog:
#     def __init__ (self, nome, idade, peso, raça):
#         self.nome = nome
#         self.idade = idade
#         self.peso = peso
#         self.raça = raça
        
#     def latir(self):
#         print("Au Au")
#         return f"O {self.nome} que tem {self.idade} anos, cujo raça é {self.raça} acabou de latir "

# objeto_dog = dog("Pitoco", 15, 50, "Vira-lata")
# print(objeto_dog.latir())

# class livro:
    
#     def __init__(self, titulo, autor, ano, disponivel):
        
#         self.autor = autor
#         self.titulo = titulo
#         self.ano = ano
#         self.disponivel = True



#     def emprestar(self):
#         if self.disponivel:
#             self.disponivel = False
#             return f"Livro {self.titulo} foi emprestado"
#         else:
#             return f"Livro não disponível"


#     def devolver(self):
#         self.disponivel = True
#         return f"O livro {self.titulo} foi devolvido"

#     def info(self):
#         if self.disponivel:
#             status = "Disponível"
#         else: 
#             "Emprestado"
#         return f"Nome do livro:{self.titulo} \n Autor do livro {self.autor} \n Ano do livro {self.ano} \n Disponível: {self.disponivel}"
        
    

# class ContaBancaria:
#     def __init__(self, titular, saldo, numero):
#         self.titular = titular
#         self._saldo = saldo
#         self.numero = numero

#     def depositar(self):
#         print(f"SALDO ATUAL: {self._saldo}")
#         deposito = float(input("Qual a quantidade de dinheiro que você quer depositar?: "))
#         self._saldo += deposito
#         print("Depósito concluído com sucesso!")
        

#     def sacar(self):
#         print(f"SALDO ATUAL: {self._saldo}")
#         saque = float(input("Qual a quantidade de dinheiro que você quer sacar?: "))
#         if saque > self._saldo:
#             print("Saldo insuficiente!")
#         else:
#             self._saldo -= saque
#             print("Saque concluído com sucesso!")
       

#     @property
#     def consultar(self):
#         return f"Seu saldo atual: {self._saldo}\n"

# conta1 = ContaBancaria("João", 150, 111)
# conta2 = ContaBancaria("Roberto", 00, 333)




# conta1.sacar()
# print(conta1.consultar)


# conta2.sacar()
# print(conta1.consultar)


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
