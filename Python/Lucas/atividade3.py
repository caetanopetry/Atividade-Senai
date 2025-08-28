lista = []

for i in range(0, 5):
    numero = int (input("Qual número você quer adicionar na lista?: "))
    lista.append(numero)

multi = 1
for numero in lista:
    
    multi = multi * numero

print(multi)
