palavra = input("Digite a palavra desejada: ")

cont = 0
letradesejada = ["a"]

for letra in palavra:
    if letra in letradesejada:
        cont = cont +1
    

print(f"A quantidade de vezes que a letra 'A' aparece na palavra: {palavra} é {cont}")