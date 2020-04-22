class Usuario:
    #atributos de classe (estáticos)
    ip = 1029310293

    #construtor
    def __init__(self,login,email,senha):
        # atributos de instancia
        self.__login = login
        self.__email = email
        self.__senha = senha

    #metodos básicos 'gets' para acesso aos atributos da classe
    @property
    def ip(self):
        return Usuario.ip

    @property
    def login(self):
        return self.login

    @property
    def email(self):
        return self.__email

    @property
    def senha(self):
        return self.__senha


