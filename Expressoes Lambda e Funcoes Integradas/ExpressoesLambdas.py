"""

Lambdas -> são funçoes anonimas (sem nome)

"""
import random

#normal
def funcao(x):
    return 3*x + 1

#lambda
funcaoLambda = lambda x: 3 * x+ 1

print(funcaoLambda(3))

#outro exemplo
nome_completo = lambda nome, sobrenome: nome.strip().title()+' '+sobrenome.strip().title()
print(nome_completo('guilherme', ' stein             '))

#usando lambda pra ordenaçao por sobrenome por ex.
autores = ['Isac Asinov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert','Orson Scott Card', 'Douglas Adams', 'H.G. Wells', 'Leigh Bracket', 'J.K. Rolling']
autores.sort(key = lambda sobrenome: sobrenome.split(' ')[-1].lower())
print('Lista ordenada por sobrenome:',autores)

#funcao quadratica
a = random.randrange(1,4)
b = random.randrange(4,7)
c = random.randrange(7,10)
x = random.randrange(0,4)

def func_quadratica(a,b,c):
    return lambda x: a*x**2+b*x**1+c*x**0

resultado = func_quadratica(a,b,c)

print('\nfuncao quadratica pra a,b,c gerados aleatoriamente \na:',a,' b:',b,' c:',c,'\nx: ',x,'\nresultado: ',resultado(x))

