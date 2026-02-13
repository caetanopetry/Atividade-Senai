nome = input("Informe o nome: ")
nota1 = float(input ("Primeira nota: "))
nota2 = float(input ("Segunda nota: "))
freq = float (input ("Informe a frequencia: "))
media = (nota1 + nota2) / 2
if media >=7 and freq >=75:
    print("Aprovado")

elif media <7 and freq <75:
    print("Reprovado")

