palavra = input("Digite a palavra desejada: ").lower()

vogais = ["a", "e", "i", "o", "u"]
consoantes = [ "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
cont_vogais = []
cont_consoantes = []

for letra in palavra:
    if letra in vogais:
        
        cont_vogais.append(letra)
    elif letra in consoantes:
        cont_consoantes.append(letra)
        
quant_vog = len(cont_vogais) 
quant_consoantes = len(cont_consoantes) 

print(f"Vogais: {cont_vogais}")
print(f"Consoantes: {cont_consoantes}")
print(f"A quantidade de vogais na palavra: {palavra} é {quant_vog} e a quantidade de consoantes é {quant_consoantes}")
