qntd = int(input("Qual a quantidade de pessoas para o questionário? "))

def levels(qntd):
    nomes = []
    idades = []
    levels = []

    for i in range(qntd):
        nome = input("Qual o seu nome? ")
        idade = int(input("Qual sua idade? "))
        level = int(input("Qual o seu nível no Minecraft? "))

        nomes.append(nome)
        idades.append(idade)
        levels.append(level)

    maior = levels.index(max(levels))
    menor = levels.index(min(levels))

    print(f"A pessoa com o maior nível é {nomes[maior]} com {idades[maior]} anos! O nível dele é: {levels[maior]}")
    print(f"A pessoa com o menor nível é {nomes[menor]} com {idades[menor]} anos. O nível dele é: {levels[menor]}")

levels(qntd)
