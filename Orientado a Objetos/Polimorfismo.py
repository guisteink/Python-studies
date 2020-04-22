class Animal:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comunicar(self):
        raise NotImplementedError('A classe filha deve implementar este método para ser utilizado')

    def comer(self):
        print(f'{self.nome} está comendo')


class Dog(Animal):
    def __init__(self, nome, raça):
        super().__init__(nome)
        self.__raça = raça

    @property
    def raça(self):
        return self.__raça

    def comunicar(self):
        print(f'{self.nome} says: AUAU')

class Cat(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome)
        self.__cor = cor

    @property
    def cor(self):
        return self.__cor

    def comunicar(self):
        print(f'{self.nome} says: MIAU')


#######################################################################################################################
newcat = Cat('Celso','Preto')
newdog = Dog('Otavio','Xauxau')

newcat.comunicar()
newdog.comunicar()