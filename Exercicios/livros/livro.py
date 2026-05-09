class Livro:

    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True

    def __str__(self):
        return f""



    @property
    def emprestar(self):
        self._disponivel = False



livro1 = Livro("Cem Anos de Solidão", "Gabriel García Márquez", 1967)
livro2 = Livro("Dom Casmurro", "Machado de Assis", 1899)
livro3 = Livro("Orgulho e Preconceito", "Jane Austen", 1813)

print(Livro.exibindo_livros)
