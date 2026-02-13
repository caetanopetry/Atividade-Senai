import time
import os
gabarito = ["A", "C", "D", "E", "E", "B", "A", "D", "C", "B"]
alunos = ["Caetano", "João", "Maria", "Pedro", "Ana", "Lucas", "Daniel", "Beatriz", "Eduardo", "Juscelia" ]
notas = []
questoes = 10

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')




for i, aluno in enumerate(alunos):
    print("Bem-vindo ao sistema de coreção da Professora Marisa \n");     print(f"Aluno: {aluno}")
    acertos = 0

    for j, resposta in enumerate(gabarito, start=1):
        print(f"Qual a resposta da questão {j}")
        tentativa = input("Resposta: ").upper()
        time.sleep(1)

        if tentativa == resposta:
            
            print("Resposta correta!\n")
            acertos += 1
        else:
            print("Resposta Incorreta\n")
    
    nota = (acertos / questoes) * 10
    notas.append(nota)
    print(f"Nota final do aluno {aluno}: {nota}\n")
    clear()

print("\n---------------------------\n")
print("Respostas dos alunos da Professora da Marisa")
print("Notas finais de todos os alunos:")
for i, aluno in enumerate(alunos):
    print(f"Nota do aluno: {aluno} --> {notas[i]}")

