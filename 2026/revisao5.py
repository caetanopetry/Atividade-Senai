print("RESPONDA TUDO COM SIM OU NÃO")

saldo = input("Você tem saldo?: ").lower()
if saldo == "sim":
    tem_saldo = True
elif saldo == "nao":
    tem_saldo = False
else:
    tem_saldo = False

cartao = input("Você tem cartão?: ").lower()
if cartao == "sim":
    cartao_credito = True
elif cartao == "não" or cartao == "nao":
    cartao_credito = False
else:
    cartao_credito = False

if cartao_credito and tem_saldo:
    print("Você pode comprar como preferir")

elif cartao_credito:
    print("Você pode comprar com crédito")

elif tem_saldo:
    print("Você pode comprar à vista")

else:
    print("Você não pode comprar")
