l = []
while True:
    numero = int(input("Digite um número: "))
    l.append(numero)

    if numero == 0:
        break
    else:
        l.append(numero)

print("Imprimindo os números")
for e in l:
    print(e)