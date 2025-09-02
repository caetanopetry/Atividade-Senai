import tkinter as tk


def calcular():
    try:
        resultado = eval(entrada.get())  
        label_resultado.config(text=f"Resultado: {resultado}")
    except:
        label_resultado.config(text="Erro na expressão")


janela = tk.Tk()
janela.title("Calculadora Simples")


entrada = tk.Entry(janela, width=20, font=("Arial", 14))
entrada.pack(pady=10)


botao = tk.Button(janela, text="Calcular", command=calcular, font=("Arial", 12))
botao.pack(pady=5)


label_resultado = tk.Label(janela, text="Resultado:", font=("Arial", 14))
label_resultado.pack(pady=10)


janela.mainloop()
