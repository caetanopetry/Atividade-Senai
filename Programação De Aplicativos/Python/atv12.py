import random

numero_aleatorio = random.randint(1, 20)

numero_esc = int (input("Digite um número entre 1 e 20: "))


while numero_esc != numero_aleatorio:

    if numero_esc > numero_aleatorio:
        print("O número aleatorio é menor que o número escolhido.")
        numero_esc = int (input("Digite um número entre 1 e 20: "))

    elif numero_esc < numero_aleatorio:
        print("O número aleatorio é maior que o número escolhido.")
        numero_esc = int (input("Digite um número entre 1 e 20: "))


else:
    print(f"Parabéns, você acertou o número aleatório, que era {numero_aleatorio}.")