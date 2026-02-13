def maior_menor(maior, menor):
    numeros = [maior, menor] 

    maior_numero = max(numeros)  
    menor_numero = min(numeros)   

    print(f"O maior número é: {maior_numero}")
    print(f"O menor número é: {menor_numero}")

numero = int(input("Qual o primeiro número inteiro desejado? "))
numero2 = int(input("Qual o segundo número inteiro desejado? "))

maior_menor(numero, numero2)