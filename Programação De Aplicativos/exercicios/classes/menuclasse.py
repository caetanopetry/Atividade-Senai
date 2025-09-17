print("=== CADASTRO DE LIVRO ===")
autor = input("Digite o nome do autor: ")
titulo = (input("Qual o nome do livro?: "))
ano = int ("Ano do livro?: ")
disponivel = int (input("O livro está disponível? (1 para sim / 2 para não): "))




def menu():

    while True:
        print("\n=== MENU DE OPÇÕES ===")
        print("1 - Visualizar dados do livro ")
        print("2 - Emprestar livro")
        print("3 - Devolver livro")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
           print()
        elif opcao == "2":
            print()
        elif opcao == "3":
            print()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

menu()
