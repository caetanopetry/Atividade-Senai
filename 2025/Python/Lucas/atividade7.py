print("Bem vindo á tabuada.")
numero = int (input("Qual número você quer ver a tabuada?: "))
for i in range (1, 11):
    resultado = (i *numero)
    print(f"{i} x {numero} = {resultado}")