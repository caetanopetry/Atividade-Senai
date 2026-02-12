#exemplo de função
#função sem passagem de parametro

def mensagem():
    print("Aprendendendo python!")

def calculartotal(qt, valor):
    total = qt * valor
    return total

mensagem()
quantidade = int(input("Quantidade: "))
valor = float(input("Valor: "))
resultado = calculartotal(quantidade, valor)
print(f"O resultado é{[resultado]}")