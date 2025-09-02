class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos=1):
        for _ in range(anos):
            self.idade += 1
            if self.idade <= 21:
                self.altura += 0.5  

    def engordar(self, kg=1):
        self.peso += kg

    def emagrecer(self, kg=1):
        self.peso -= kg

    def crescer(self, cm=1):
        self.altura += cm

print("=== CADASTRO DE PESSOA ===")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (cm): "))

p = Pessoa(nome, idade, peso, altura)

def menu():

    while True:
        print("\n=== MENU DE OPÇÕES ===")
        print("1 - Visualizar dados da pessoa")
        print("2 - Alterar nome")
        print("2 - Alterar idade")
        print("3 - Alterar peso")
        print("4 - Alterar altura")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print(f"\n{p.nome}, {p.idade} anos, {p.peso}kg, {p.altura}cm")
        elif opcao == "2":
            p.idade = int(input("Digite a nova idade: "))
        elif opcao == "3":
            p.peso = float(input("Digite o novo peso (kg): "))
        elif opcao == "4":
            p.altura = float(input("Digite a nova altura (cm): "))
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


menu()