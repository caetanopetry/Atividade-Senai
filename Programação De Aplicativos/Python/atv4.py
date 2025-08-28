total = 0
for i in range (1, 4):
    nota = int (input (f"Qual a nota do aluno {i}?: "))
    total = nota + total



media = total / 3

print(f"A média dos aluno é {media} ")

if media < 7:
    print("O aluno está de recuperação. ")

elif media >= 5 or media <7:
    print("O aluno foi aprovado.")

elif media <5:
    print("Reprovado")
