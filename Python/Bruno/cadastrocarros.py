carros = []

def cadastrar():
    modelo = input("Qual o modelo do seu carro? : ")
    marca = input("Qual a marca do seu carro? : ")
    preco = float(input("Qual o preço do seu carro? : "))
    ano = int(input("Qual o ano do seu carro? : "))

    carro = [modelo, marca, preco, ano]
    carros.append(carro)

    print("\nCarro cadastrado com sucesso!\n")

def remover():
    print("\n------ CARROS CADASTRADOS ------")
    for i in range(len(carros)):
        print(f"{i+1}. {carros[i][1]} {carros[i][0]} - R${carros[i][2]} - Ano {carros[i][3]}")

    pos = int(input("Digite o número do carro que deseja remover:(0 para cancelar): "))

    if pos == 0:
        print("Remoção de carro cancelada!")
        menu()
    
    if pos > 0 and pos <= len(carros):
        removido = carros.pop(pos - 1)
        print(f"\nCarro {removido[1]} {removido[0]} removido com sucesso!\n")
    else:
        print("\nNúmero inválido!\n")

def ver_carros():
    print("\n------ LISTA DE CARROS ------")
    for i in range(len(carros)):
        print(f"{i+1}. {carros[i][1]} {carros[i][0]} - R${carros[i][2]} - Ano {carros[i][3]}")
    print()

def menu():
    while True:
        print('\n========================================')
        print('    CONCESSIONÁRIA PYTHON')
        print('========================================')
        print('1 - Cadastrar carros')
        print('2 - Remover carros')
        print('3 - Ver carros cadastrados')
        print('4 - Sair do programa')
        print('----------------------------------------')
        
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("\nPor favor, digite um número válido!\n")
            continue

        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            remover()
        elif opcao == 3:
            ver_carros()
        elif opcao == 4:
            print("Fechando o programa...")
            break
        else:
            print("Opção inválida!\n")

menu()
