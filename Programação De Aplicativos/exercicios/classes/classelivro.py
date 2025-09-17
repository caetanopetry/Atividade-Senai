class livro:
    
    def __init__(self, titulo, autor, ano, disponivel):
        
        self.autor = autor
        self.titulo = titulo
        self.ano = ano
        self.disponivel = True



    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return f"Livro {self.titulo} foi emprestado"
        else:
            return f"Livro não disponível"


    def devolver(self):
        self.disponivel = True
        return f"O livro {self.titulo} foi devolvido"

    def info(self):
        if self.disponivel:
            status = "Disponível"
        else: 
            "Emprestado"
        return f"Nome do livro:{self.titulo} \n Autor do livro {self.autor} \n Ano do livro {self.ano} \n Disponível: {self.disponivel}"