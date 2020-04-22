"""

Usando GETS e SETS no modo pythonico, ou seja, usando @property

"""
class Produto:
    # atributos de classe (estáticos)
    qtd = 10000

    # construtor no python
    def __init__(self, preco, nome, descricao, imposto):
        #atributos de instancia
        self.__preco = preco
        self.__nome = nome
        self.__descricao = descricao
        self.__imposto = imposto

    #Métodos clássicos 'Gets' -> COMO PROPRIEDADES (MODO PYTHONICO)
    @property
    def preco(self):
        return self.preco

    @property
    def nome(self):
        return self.nome

    @property
    def descricao(self):
        return self.descricao

    @property
    def imposto(self):
        return self.__imposto

    #Métodos clássicos 'Sets' -> Modo pythonico
    @nome.setter
    def nome(self, novo_nome):
        self.nome = novo_nome

    @preco.setter
    def preco(self, novo_preco):
        self.preco = novo_preco

