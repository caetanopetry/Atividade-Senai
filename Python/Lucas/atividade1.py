palavra = input ("Digite uma palavra: ")
caractere = input("Digite um caractere: ").lower()

quantidade = palavra.count(caractere)

print(f"A quantidade de vezes que o caractere '{caractere}' aparece na palavra '{palavra}' é: {quantidade}")