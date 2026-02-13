class conta:
    def __init__(self, titular, saldo, senha):
        print("Entrou no construtor!")
        self.titular = titular
        self._saldo = saldo
        self._senha = senha

    def mostrar_saldo(self):
        
        tent_senha = input("Digite sua senha: ").strip()
        while tent_senha != self._senha:
            print("Senha incorreta!")
            tent_senha = input("Digite sua senha: ").strip()
        else:
            print(f"Seu saldo é: {self._saldo}")

    def atualizar_saldo(self, novo_saldo):
        self._saldo = novo_saldo

conta_bancaria_1 = conta("Caetano", 0000, "999")

conta_bancaria_2 = conta("Lucas", 60, "1234")



print(f"\nTítular: {conta_bancaria_1.titular}")
conta_bancaria_1.mostrar_saldo()


print(f"\nTítular: {conta_bancaria_2.titular}")
conta_bancaria_2.mostrar_saldo()
