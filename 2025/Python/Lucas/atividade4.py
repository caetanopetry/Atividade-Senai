lista = []

for i in range(0, 5):
    numero = int (input("Qual número você quer adicionar na lista?: "))
    lista.append(numero)
    
maior = max(lista)
menor = min(lista)


print(f"A lista é: {lista}")
print(f"O maior número da lista é: {maior}")
print(print(f"O maior número da lista é: {menor}"))