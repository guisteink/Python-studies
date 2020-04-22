"""

Metodos mágicos sao os metodos que usam o dunder -> __ , exemplo "dunder init" -> __init__()

dunder __init__ -> construtor em python, construçao da instância de classe
dunder __repr__ -> repr = representaçao da classe
dunder __str__ -> toString em python, retorna a string
dunder __len__ -> retorna o tamanho de um objeto, caso necessário

"""

class Livro:
    def __init__(self, titulo,autor,paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    @property
    def paginas(self):
        return self.__paginas

    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'

    #print(object), indica para o __str__
    def __str__(self):
        return self.titulo

    def __len__(self):
        return self.paginas

livro01 = Livro('Python books', 'Guilherme Stein', 588)
print(livro01.__repr__())
print(livro01)
print(livro01.paginas)