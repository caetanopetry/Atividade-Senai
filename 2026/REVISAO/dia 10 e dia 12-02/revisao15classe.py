class Receita:
    def __init__(self, nome, ingredientes, tempo_preparo):
        self.nome = nome
        self.ingredientes = ingredientes
        self.tempo_preparo = tempo_preparo

    def exibir_Receita(self):
        print(f"Receita: {self.nome}")
        print("Ingredientes")

        for ingrediente in self.ingredientes:
            print(f"- {ingrediente}")
        print(f"Tempo de preparo: {self.tempo_preparo} minutos")

bolodechocolate = Receita(
    "Bolo de chocolate",
    ["2 xícaras de farinha",
    "1 xícara de açucar",
    "1 xícara de chocolate em pó",
    "3 ovos",
    "1 xícara de leite"],30
)

bolodemorango = Receita(
    "Bolo de Morango",
    ["2 xícaras de farinha",
    "1 xícara de açúcara",
    "1 xícara de morangos picados",
    "3 ovos",
    "1 xícara de leite"],30
)

tortadebolacha = Receita(
    "Torta de bolacha",
    ["200gr de bolacha",
    "1 lata de condensado",
    "1 lata de creme de leite",
    "1 xícara de café forte"],30
)
print("-" * 30)
print("EXIBIR RECEITA!\n")
bolodechocolate.exibir_Receita()
print("-" * 30)
print("EXIBIR RECEITA!\n")
bolodemorango.exibir_Receita()
print("-" * 30)
print("EXIBIR RECEITA!\n")
tortadebolacha.exibir_Receita()
print("-" * 30)
