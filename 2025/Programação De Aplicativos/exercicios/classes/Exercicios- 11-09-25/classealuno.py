class aluno:
    def __init__(self, nome, nota):
        
        self.nome = nome
        self.nota = nota

    def verificar_aprovacao(self):
        if self.nota > 10 or self.nota < 1:
            return f"Nota digitada inválida"
        else:
            if self.nota >=6:
                return f"Aluno {self.nome} com a nota {self.nota} Aprovado"
            elif self.nota < 6:
                return f"Aluno {self.nome} com a nota {self.nota} Reprovado"
        
caetano = aluno ("Caetano", 6)
print(caetano.verificar_aprovacao())

henrique = aluno ("Henrique", 3)
print (henrique.verificar_aprovacao())

guilherme = aluno ("Guilherme", 11)
print(guilherme.verificar_aprovacao())