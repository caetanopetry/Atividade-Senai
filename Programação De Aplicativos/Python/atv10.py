import time
import os
lista = []
def clear(): os.system('cls' if os.name == 'nt' else 'clear')

def cadastrar():
    nome = input("Digite seu nome: ")
    telefone = input("✍️Qual o seu telefone?: ")
    
    while len(telefone) < 13:
        print("TELEFONE DIGITADO INVÁLIDO")
        telefone = input("✍️Qual o seu telefone?: ")
    
    for pessoa in lista:
        if pessoa["nome"].lower() == nome.lower():
            print("⚠️ Já existe uma pessoa cadastrada com esse nome!")
            time.sleep(2)
            clear()
        if pessoa["telefone"] == telefone:
            print("⚠️ Já existe uma pessoa cadastrada com esse telefone!")
            time.sleep(2)
            clear()
    
    pessoa = {
        "nome": nome,  
        "telefone": telefone
    }
    lista.append(pessoa)
    print("✅ Cadastro realizado com sucesso!")
    time.sleep(2)
    clear()

def listar():
    if not lista:
        print("📭 Nenhuma pessoa cadastrada ainda.")
        return
    for pessoa in lista:
        print("\n--------------------------------")
        print(f"📕 Nome: {pessoa['nome']}")
        print(f"📞 Telefone: {pessoa['telefone']}")
    print("--------------------------------\n")

def menu():
    while True:
        print("--------------------------------"); print("---------------MENU-------------"); print("________________________________"); print("----- Escolha uma opção --------"); print("----- 📖1 <-- Cadastrar Pessoa ----"); print("----- 📚2 <-- Listar Pessoas ------"); print("----- ❌3 <-- Sair do Menu ----")
        op = input("🤔Escolha uma opção: ")
        time.sleep(1)
        clear()

        if op == "1":
            cadastrar()
        elif op == "2":
            listar()
        elif op == "3":
            print("👋Bye bye")
            break
        else:
            print("Opção digitada inválida.")
menu()
