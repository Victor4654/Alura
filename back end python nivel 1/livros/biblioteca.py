
class Biblioteca:
    def __init__(self,livros):
        self.livros = [livros]
        
    def exibir(self):
        for livro in self.livros:
            print(livro)
            print("")


lista = ["Cem Anos de Solidão", "Gabriel García Márquez", 1967,"Dom Casmurro", "Machado de Assis", 1899,"Orgulho e Preconceito", "Jane Austen", 1813]

livro = Biblioteca(lista)
livro.exibir



