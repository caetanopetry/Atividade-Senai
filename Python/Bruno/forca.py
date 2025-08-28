palavra_sec = "Prusse".lower()
casas = ["_", "_", "_", "_", "_", "_"]

tent = 0
tent_max = 6

while tent < 6 and "_" in casas:
    print(f"Palavra: {casas}")
    letra = input("Qual letra? ").lower()

    for i in range(len(palavra_sec)):
        if palavra_sec[i] == letra:
            casas[i] = letra
            print("Você acertou uma letra!")
            break

    else:
        tent += 1
        print(f"Você errou! Tentativas restantes: {tent_max - tent}")

if "_" not in casas:
    print(f"Parabéns! Você ganhou! A palavra era: {palavra_sec}")
else:
    print(f"Você perdeu! A palavra era: {palavra_sec}")

