class Pessoa:

    # CONSTRUTOR
    def __init__(self, nome, idade, cpf):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf  # acesso restrito (private)

    # métodos clássicos gets para retornos, e sets para alterações possíveis - SOBREPOSIÇAO
    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def cpf(self):
        return self.__cpf

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    #EQUALS - funcao padrao booleana adaptada para a classe - SOBREPOSIÇAO
    def __eq__(self, other):
        if self.getNome() == other.getNome() and self.getIdade() == other.getIdade() and self.getCpf() == other.getCpf():
            return True
        return False

    #CompareTo adaptada pra saber qual pessoa é mais velha, adaptada pra situaçaõ de uma possivel comparaçãos - SOBREPOSIÇAO
    def __cmp__(self, other):
        if self.getIdade() > other.getIdade():
            return 1
        if self.getIdade() == other.getIdade():
            return 0
        else:
            return -1

    #toString padrao pra fornecer os dados encapsulados - SOBREPOSIÇAO
    def __repr__(self):
        return f'Nome:{self.getNome()}\nIdade:{self.getCpf()}\nCpf:{self.getCpf()}'



