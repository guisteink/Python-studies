"""

    Atributos normais -> self.numero
    Atributos privados -> self.__numero, não pode ser acessado em termos gerais (nivel de segunrança)

    Atributos de instância -> São atributos gerados na instancia do objeto, que tem seus próprios valores,
    são inicializados no construtor
    Atributos de classe -> São geralmente iniciados com valores, atributos estáticos, são inicializados na classe
    Atributo dinàmico -> É um atributo de instância que é criado em tempo de execução, e é exclusivo da instância que o criou

"""

from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:
    # atributos de classe (estáticos)
    ip = 1029310293
    contador = 0

    @classmethod
    def conta_usuarios(cls):  # é como se fosse um metodo estático no java, o cls passa o acesso como Usuario.contador
        print(f'Temos no momento {cls.contador} usuário(s) no sistema')  # ou seja um acesso estático

    # construtor
    def __init__(self, login, email, senha):
        # atributos de instancia
        self.__login = login
        self.__email = email
        self.__senha = senha

    # metodo pra verificação de senha
    def verify_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    # metodos básicos 'gets' para acesso aos atributos da classe
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


class Produto:
    # atributos de classe (estáticos)
    imposto = 1.02
    qtd = 10000

    # construtor no python
    def __init__(self, preco, nome, descricao):
        # atributos de instancia
        self.preco = preco
        self.nome = nome
        self.descricao = descricao

        # Métodos clássicos 'Gets' -> COMO PROPRIEDADES (MODO PYTHONICO)

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

    # Métodos clássicos 'Sets' -> Modo pythonico
    @nome.setter
    def nome(self, novo_nome):
        self.nome = novo_nome

    @preco.setter
    def preco(self, novo_preco):
        self.preco = novo_preco

