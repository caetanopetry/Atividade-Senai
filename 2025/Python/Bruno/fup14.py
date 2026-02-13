import random

numero_aleatorio = random.randint(1, 100)

numero_esc = int (input("Digite um número entre 1 e 100: "))

tentativas = 0

while numero_esc != numero_aleatorio:

    if numero_esc > numero_aleatorio:
        print("O número aleatorio é menor que o número escolhido.")
        numero_esc = int (input("Digite um número entre 1 e 100: "))
        tentativas += 1

    elif numero_esc < numero_aleatorio:
        print("O número aleatorio é maior que o número escolhido.")
        numero_esc = int (input("Digite um número entre 1 e 100: "))
        tentativas +=1

    if tentativas >= 3:
        break

else:
    print(f"Parabéns, você acertou o número aleatório em{tentativas}")