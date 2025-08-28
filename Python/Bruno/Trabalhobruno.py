import time
import os
from datetime import datetime

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

agora = datetime.now()
data_pt = agora.strftime("%A, %d de %B de %Y")

hora = datetime.strptime("14:00", "%H:%M")

usuarios = []
reservas = []
pontos = {}

def cadastrar():
    clear()
    print("\n----------------------------------------")
    print("--- Cadastro ---")
    print("----------------------------------------\n")
    nome = input("Usuário: ")
    senha = input("Senha: ")

    for u in usuarios:
        if u[0] == nome:
            print("Usuário já existe!\n")
            return

    usuarios.append([nome, senha])
    pontos[nome] = 3
    print("\nVerificando Cadastro...")
    time.sleep(2)
    print("Cadastro feito com sucesso!\n")

def login():
    clear()
    print("\n----------------------------------------")
    print("--- Login ---")
    print("----------------------------------------\n")
    nomelog = input("Usuário: ")
    senhalog = input("Senha: ")

    if len(usuarios) == 0:
        print("\nPor favor! Faça cadastro primeiro!\n")
        return

    for usuario in usuarios:
        nome_salvo, senha_salva = usuario
        if nome_salvo == nomelog and senha_salva == senhalog:
            print("\nEntrando...")
            time.sleep(2)
            print("Login bem-sucedido!\n")
            menu_reserva(usuario)
            return

    print("\nEntrando...")
    time.sleep(2)
    print("Usuário ou senha incorretos!\n")

def mostrar_reservas():
    clear()
    if len(reservas) == 0:
        print("\nNenhuma reserva feita.\n")
        return

    print("\n--- Reservas Feitas ---")
    for r in reservas:
        print(r[0][0], "-", r[1], "-", r[2], "-", r[3], "das", r[4], "às", r[5])
    print()

def tem_conflito(data, inicio, fim, laboratorio, sala):
    for reserva in reservas:
        if reserva[3] == data and reserva[1] == laboratorio and reserva[2] == sala:
            inicio_reserva = reserva[4]
            fim_reserva = reserva[5]
            if fim > inicio_reserva and inicio < fim_reserva:
                return True  
    return False 

def emitir_nota(usuario, lab, sala, data, ini, fim):
    clear()
    print("\n--- NOTA FISCAL DE RESERVA ---")
    print(f"Professor: {usuario[0]}")
    print(f"Laboratório: {lab}")
    if lab != "Auditório":
        print(f"Sala: {sala}")
    print(f"Data da Reserva: {data}")
    print(f"Horário: das {ini} às {fim}")
    print(f"Data de Emissão: {data_pt}")
    print(f"Pontos Restantes: {pontos[usuario[0]]}")
    print("------------------------------\n")

def fazer_reserva(usuario, lab):
    clear()
    data_atual = datetime.now()

    if pontos[usuario[0]] <= 0:
        print("Você atingiu o limite de reservas deste mês.\n")
        return

    print(f"\n--- Reserva no laboratório de {lab} ---")
    if lab != "Auditório":
        sala = int(input("Sala (1 a 3): "))
        while sala < 1 or sala > 3:
            sala = int(input("Sala (1 a 3): "))

    else:
        sala = "1"

    data = input("Data (ex: 20/08/2025): ")
    while not "/" in data:
        print("Por favor, adicione '/' na sua resposta")
        data = input("Data (ex: 20/08/2025):  ")
        print("\n")

    diaescolhido = datetime.strptime(data, "%d/%m/%Y")

    while diaescolhido < data_atual:
        print("Por favor insira uma data válida! \n")
        data = input("Data (ex: 20/08/2025): ")
        diaescolhido = datetime.strptime(data, "%d/%m/%Y")

    ini = input("Início (ex: 14:00): ")
    while not ":" in ini:
        print("Por favor, adicione ':' na sua resposta")
        ini = input("Início (ex: 14:00): ")
        print("\n")

    fim = input("Fim (ex: 15:00): ")
    while not ":" in fim:
        print("Por favor, adicione ':' na sua resposta")
        fim = input("Fim (ex: 15:00): ")
        print("\n")

    formato = "%H:%M"
    hora_ini = datetime.strptime(ini, formato)
    hora_fim = datetime.strptime(fim, formato)

    if hora_fim <= hora_ini:
        print("\nHorário inválido: o horário de fim deve ser maior que o de início.\n")
        return

    if tem_conflito(data, ini, fim, lab, sala):
        print("\nJá existe uma reserva nesse horário para essa sala.\n")
        return

    reservas.append([usuario, lab, sala, data, ini, fim])
    pontos[usuario[0]] -= 1
    print("\nAnalisando Dados...")
    time.sleep(2)
    print("✅ Reserva feita!\n")

    emitirNota = False

    r = int(input("Você deseja imprimir sua nota fiscal? (--- 1 para sim / 2 para não ---)"))

    if r == 1:
        emitirNota = True
    else:
        emitirNota = False

    if emitirNota is True:
        emitir_nota(usuario, lab, sala, data, ini, fim)
    else:
        print("Ok, não iremos imprimir sua nota fiscal.")

def reservar(usuario):
    valido = False
    while not valido:
        clear()
        print("\n----------------------------------------")
        print("--- Sistema de Reservas ---")
        print("----------------------------------------\n")
        print("Informe o laboratório desejado:")
        print("[1] - Informática")
        print("[2] - Mecânica")
        print("[3] - Robótica")
        print("[4] - Auditório")
        print("[5] - Voltar ao menu anterior\n")
        res = input("Escolha: ")

        if res == "1":
            fazer_reserva(usuario, "Informática")
            valido = True
        elif res == "2":
            fazer_reserva(usuario, "Mecânica")
            valido = True
        elif res == "3":
            fazer_reserva(usuario, "Robótica")
            valido = True
        elif res == "4":
            fazer_reserva(usuario, "Auditório")
            valido = True    
        elif res == "5":
            time.sleep(1)
            print("Voltando ao menu de reservas...")
            return
        else:
            print("Opção inválida. Escolha entre as opções abaixo:\n")

def menu_reserva(usuario):
    clear()
    while True:
        print("\n----------------------------------------")
        print("--- Menu de Reservas ---")
        print("----------------------------------------\n")
        print("1 - Fazer reserva")
        print("2 - Ver reservas")
        print("3 - Sair")
        op = input("Escolha: ")

        if op == "1":
            reservar(usuario)
        elif op == "2":
            mostrar_reservas()
        elif op == "3":
            print("\nSaindo do menu de reservas...\n")
            break
        else:
            print("Opção inválida.\n")

def menu_principal():
    while True:
        clear()
        print("\n----------------------------------------")
        print("--- Sistema de Reservas ---")
        print("----------------------------------------\n")
        print("[1] - Cadastrar")
        print("[2] - Login")
        print("[3] - Sair\n")

        
        op = input("Escolha: ")

        if op == "1":
            cadastrar()
        elif op == "2":
            login()
        elif op == "3":
            print("\nEncerrando o sistema.")
            break
        else:
            print("Opção inválida.\n")

menu_principal()
