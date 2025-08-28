altura = float(input("Qual sua altura?: "))
peso = float(input("Qual seu peso?: "))

imc = peso / (altura ** 2)
if imc < 18.5:
    print("Abaixo do peso normal")

elif 18.5 <= imc <= 24.9:
    print("Peso normal")

elif 25 <= imc <= 29.9:
    print("Sobrepeso de peso")

elif 30 <= imc <= 34.9:
    print("Obesidade Classe I")
