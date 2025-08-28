import time
import os
biblioteca = []
def clear(): os.system('cls' if os.name == 'nt' else 'clear')

def cadastrar():
    nome = input("📕Digite o nome do livro que você quer adicionar: ")
    preco = float(input("💸Qual o preço do seu livro?: "))
    genero = input("🃏Qual o gênero do seu livro?: ")
    autor = input("✍️Qual o autor do seu livro?: ")

    livro ={
        "nome": nome, "preco": preco, "genero": genero, "autor": autor
    }
    biblioteca.append(livro)

    print("Livro adicionado com sucesso!")
    time.sleep(1.5)
    print("O que você deseja fazer?")
    print("-- 📖1 <-- Adicionar Mais um Livro --")
    print("-- 👋2 <-- Sair do Menu ---------")
    op = input("🤔Escolha uma opção: ")
    time.sleep(1.5)

    if op == "1":
        cadastrar()
    elif op == "2":
        breakpoint
    else:
        print("❌Opção digitada inválida.")
    clear()

def listar():
    for livro in biblioteca:
        print("\n")
        print("--------------------------------")
        print(f"📕Nome: {livro["nome"]}")
        print(f"💸Preço: {livro["preco"]}")
        print(f"🃏Gênero: {livro["genero"]}")
        print(f"✍️Autor: {livro["autor"]}")
        print("\n")

def excluir():
    for i, livro in enumerate(biblioteca):
        print(f"🔢Número: {i+1}")
        print(f"📕Nome: {livro["nome"]}")
        print(f"💸Preço: {livro["preco"]}")
        print(f"🃏Gênero: {livro["genero"]}")
        print(f"✍️Autor: {livro["autor"]}")
        print("\n")
        
    indice = int(input("📚❌Digite a posição do livro que você quer remover: "))
    livro_removido = biblioteca.pop(indice-1)
    print(f"👋Livro {livro_removido["nome"]} removido com sucesso!")
    time.sleep(4)
    clear()

def menu():
    while True:
        print("--------------------------------"); print("---------------MENU-------------"); print("________________________________"); print("----- Escolha uma opção --------"); print("----- 📖1 <-- Adicionar Livro ----"); print("----- 📚2 <-- Listar Livros ------"); print("----- ❌3 <-- Excluir Livros -----"); print("----- 👋4 <-- Sair do Menu -------"); print("________________________________"); print("---------------MENU-------------"); print("--------------------------------");
        op = input("🤔Escolha uma opção: ")
        time.sleep(1)
        clear()

        if op == "1":
            cadastrar()
        elif op == "2":
            listar()
        elif op == "3":
            excluir()
        elif op == "4":
            break
        else:
            print("Opção digitada inválida.")
menu()