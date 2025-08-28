n = int(input("Digite um número: "))

pares = []  
for i in range(1, n + 1):
    if i % 2 == 0:  
        pares.append(i)

print("Números pares de 1 até", n, ":", pares)
