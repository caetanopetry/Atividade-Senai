palavra = input("Digite a palavra desejada: ")

cont = 0
vogais = ["a", "e", "i", "o", "u"]

for letra in palavra:
    if letra in vogais:
        cont = cont +1
    

print(f"A quantidade de vogais na palavra: {palavra} é {cont}")