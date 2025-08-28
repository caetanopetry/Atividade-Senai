frase = input("Digite a frase desejada: ")

cont = 0

for palavra in frase:
    if palavra == " ":
        cont += 1
    

print(f"A quantidade de palavras na frase: {frase} é {cont}")