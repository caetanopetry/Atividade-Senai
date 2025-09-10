print("=== CADASTRO DE LIVRO ===")
autor = input("Digite o nome do autor: ")
titulo = (input("Qual o nome do livro?: "))
ano = int ("Ano do livro?: ")
disponivel = int (input("O livro está disponível? (1 para sim / 2 para não): "))
if disponivel == 1:
    disponivel = True
elif disponivel == 2:
    disponivel = False
else:
    print("Digite um número válido!")

p = livro(autor, titulo , disponivel)



def menu():

    while True:
        print("\n=== MENU DE OPÇÕES ===")
        print("1 - Visualizar dados do livro ")
        print("2 - Emprestar livro")
        print("3 - Devolver livro")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
           
        elif opcao == "2":
            
        elif opcao == "3":
            
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

menu()
