"""
    Decorators são funções que envolvem outras funções e aprimoram seus comportamentos;
    Sao exemplos de HOF, possuem sintaxe própria (sugar sintático, pra ficar mais identificavel)

"""

def elogio(funcao):
    def elogiando():
        print('Ola')
        funcao()
        print('Tenha um ótimo dia!')
    return elogiando

@elogio # <--- isso é um decorator
def cumprimento():
    nome = input('Qual seu nome? ')

cumprimento()


"""
#outro exemplo de segurança por exemplo

def verifica():
    if not request.usuario():
        redirect('htpp:www.seusite.com.br/login')

def home(request):
    return 'Acesso permitido'

@verifica
def serviços(request):
    return 'Acesso permitido'

@verifica
def produtos(request):
    return 'Acesso permitido'

"""