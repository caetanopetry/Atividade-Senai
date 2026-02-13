produtos = []
class produto:
    def __init__(self, nome, preco, quantidade):
        
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
       total = self.preco * self.quantidade
       return f"O valor total do estoque do {self.nome} é: {total}"

def menu():
    while True:
        print("\n=== MENU HIPERMAIS ==="); print("1 - Adicionar produtos no estoque"); print("2 - Visualizar produtos no estoque "); print("3 - Sair");
        print("=== MENU HIPERMAIS ===\n")
    
        opcao = input("Escolha uma opção: ")
        print("\n")

        if opcao == "1":
            nome = input("Qual o nome do produto?: ")
            preco = input ("Qual o preço do produto?: ")
            quant = input("Qual a quantidade do produto?: ")
            produtos.append(produto(nome, preco, quant))

        elif opcao == "2":
            for i in produtos:
                    print("\n--------------------------------")
                    print(f"🪪 Nome: {i.nome}")
                    print(f"💰 Preço {i.preco}")
                    print(f"🛒 Quantidade: {i.quantidade}")
                    print("--------------------------------\n")
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")
menu()

