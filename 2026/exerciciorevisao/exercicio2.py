#2- Agenda telefonica

#exemplos de uso de dicionário de forma dinamica


for i in range (3):
    nome = input("Informe o nome: ")
    telefone = input("Informe o telefone: ")

agenda_telefonica = {
'nome': nome,
'telefone': telefone
}

busca = input("Informe o nome para busca: ").lower()

if busca in agenda_telefonica['nome']:
    print(f"Telefone de {busca}: {agenda_telefonica['telefone']}")
else:
    print(f"{busca} não encontrado na agenda telefônica.")
