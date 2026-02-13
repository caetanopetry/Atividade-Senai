produtos = []
precos = []

for i in range (0, 5):
    print("INSIRA O NOME DE 5 PRODUTOS E SEUS PREÇOS: ")
    produto = input("Nome: ")
    produtos.append(produto)
    preco = int(input("Preço: "))
    precos.append(preco)

print(produtos)
print(precos)

