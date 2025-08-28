senha = "1234"

tent = input("Digite a senha: ")
tentativas = 1

while tent != senha:
    print("SENHA ERRADA SEU BOBÃO!")
    tent = input("Digite a senha: ")
    tentativas += 1

    if tent == senha:
        print("Você acertou a senha")
        break

    if tentativas >= 3:
        print("VOCÊ ERROU TANTO QUE O SISTEMA QUEBROU")
        print("VAI TER QUE FECHAR O TERMINAL BOBAO!!!")
        while True:
            print("FECHA O TERMINAL AI BOBAO!" * 1000)
