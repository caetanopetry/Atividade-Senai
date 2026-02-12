id_cliente = 5
nome = "Josué"
email = "jose@gmail.com"
tele=  478923123



#produto:
id_produto = 10
descricao = "Notebook Dell"
preco = 6000
quant = 15

dados_cliente ={
    'id_cliente': 5,
    'nome': 'José',
    'email': "jose@gmail.com",
    'telefone': 4987231233

}

dados_produto = {
    'id_produto' : 10,
    'descricao' : "Notebook Dell",
    'preco' : 6000,
    'quant' : 15

}

#exemplos de uso de dicionário de forma dinamica
id_cliente = int(input("Informe o id"))
nome = input("Informe o nome")
email = input("Informe o email")
telefone = int(input("Informe o telefone"))

dados_cliente = {
    'id_cliente': id_cliente,
    'nome': nome,
    'email': email,
    'telefone': telefone
}

print("Obtendo os dados do produto")
id_produto = int(input("Informe o id do produto"))
descricao = input("Informe a descrição")
preco = int(input("Qual o preço?"))
quant = int(input("Informe a quantidade"))

dados_produto = {
    'id_produto' : id_produto,
    'descricao' : descricao,
    'preco' : preco,
    'quant' : quant

}

print("Exivindo o nome do cliente e do produto:")
print(f"Cliente: {dados_cliente['nome']}")
print(f"Produto: {dados_produto[descricao]}")
print   