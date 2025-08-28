import tkinter as tk

# Função que calcula a expressão digitada
def calcular():
    try:
        resultado = eval(entrada.get())  # eval avalia a expressão matemática
        label_resultado.config(text=f"Resultado: {resultado}")
    except:
        label_resultado.config(text="Erro na expressão")

# Criando a janela principal
janela = tk.Tk()
janela.title("Calculadora Simples")

# Caixa de entrada
entrada = tk.Entry(janela, width=20, font=("Arial", 14))
entrada.pack(pady=10)

# Botão de calcular
botao = tk.Button(janela, text="Calcular", command=calcular, font=("Arial", 12))
botao.pack(pady=5)

# Label do resultado
label_resultado = tk.Label(janela, text="Resultado:", font=("Arial", 14))
label_resultado.pack(pady=10)


janela.mainloop()
