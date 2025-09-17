class ContaBancaria:
    def __init__(self, titular, saldo, numero):
        self.titular = titular
        self._saldo = saldo
        self.numero = numero

    def depositar(self):
        print(f"SALDO ATUAL: {self._saldo}")
        deposito = float(input("Qual a quantidade de dinheiro que você quer depositar?: "))
        self._saldo += deposito
        print("Depósito concluído com sucesso!")
        

    def sacar(self):
        print(f"SALDO ATUAL: {self._saldo}")
        saque = float(input("Qual a quantidade de dinheiro que você quer sacar?: "))
        if saque > self._saldo:
            print("Saldo insuficiente!")
        else:
            self._saldo -= saque
            print("Saque concluído com sucesso!")
       

    @property
    def consultar(self):
        return f"Seu saldo atual: {self._saldo}\n"

conta1 = ContaBancaria("João", 150, 111)
conta2 = ContaBancaria("Roberto", 00, 333)

conta1.sacar()
print(conta1.consultar)


conta2.sacar()
print(conta1.consultar)

