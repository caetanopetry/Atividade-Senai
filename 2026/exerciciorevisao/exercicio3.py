class livro:
    
    def __init__(self, titulo, autor):
        self.autor = autor
        self.titulo = titulo

    def info(self):
        return f"Nome do livro: {self.titulo} \nAutor do livro: {self.autor}\n"

autor = input("Qual o autor do livro?: ")
titulo = input("Qual o titulo do livro?: ")
livro1 = livro(titulo, autor)


autor = input("Qual o autor do livro?: ")
titulo = input("Qual o titulo do livro?: ")
livro2 = livro(titulo, autor)


autor = input("Qual o autor do livro?: ")
titulo = input("Qual o titulo do livro?: ")
livro3 = livro(titulo, autor)

print("\n")
print(f"Livro 1: {livro1.info()}")
print(f"Livro 2: {livro2.info()}")
print(f"Livro 3: {livro3.info()}")
