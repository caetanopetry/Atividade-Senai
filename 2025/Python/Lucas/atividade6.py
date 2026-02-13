palavra= input("Qual palavra você quer?: ")
letra = input("Você quer trocar qual letra?: ")
nvletra = input (f"Por qual letra você quer trocar o {letra}?: ")

nova_palavra = palavra.replace(letra, nvletra)
print(nova_palavra)