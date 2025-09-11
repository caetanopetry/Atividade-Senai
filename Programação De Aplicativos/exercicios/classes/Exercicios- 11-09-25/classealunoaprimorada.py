class aluno:
    def __init__(self, nome, curso):
        
        self.nome = nome
        self.curso = curso
        self.notas = []
        
    def adicionarnota(self):
        nota = float (input("Qual a nota do aluno?: "))
        self.notas.append(nota)

    def media(self):
        media = sum(self.notas) / len(self.notas)
        return (media)

        

    def mostrarinfo(self):
        print("\n--------------------------------")
        print(f" Nome: {self.nome}")
        print(f" Média: {self.media()}")
        print(f" Curso: {self.curso}")
        print("--------------------------------\n")



nome = input ("Qual o nome do aluno?: ")
curso = input ("Qual o nome do curso?: ")
aluno1 = aluno(nome, curso)

aluno1.adicionarnota()
aluno1.adicionarnota()
aluno1.adicionarnota()
aluno1.mostrarinfo()


nome = input ("Qual o nome do aluno?: ")
curso = input ("Qual o nome do curso?: ")
aluno2 = aluno(nome, curso)

aluno2.adicionarnota()
aluno2.adicionarnota()
aluno2.adicionarnota()
aluno2.adicionarnota()

aluno2.mostrarinfo()




    



#     def verificar_aprovacao(self):
#         if self.nota > 10 or self.nota < 1:
#             return f"Nota digitada inválida"
#         else:
#             if self.nota >=6:
#                 return f"Aluno {self.nome} com a nota {self.nota} Aprovado"
#             elif self.nota < 6:
#                 return f"Aluno {self.nome} com a nota {self.nota} Reprovado"
        
# caetano = aluno ("Caetano", 6)
# print(caetano.verificar_aprovacao())

# henrique = aluno ("Henrique", 3)
# print (henrique.verificar_aprovacao())

# guilherme = aluno ("Guilherme", 11)
# print(guilherme.verificar_aprovacao())