"""
LISTAS EM PYTHON:
    - São dinamicas, não possuem tamanho fixo, pode-se ir adicionando enquanto o comp. tiver memória
    - Qualquer tipo de dado
"""

lista01 = list(range(11, 22))
# verificar numa lista
if 4 in lista01:
    print('encontrei 4 na lista')
else:
    print('nao')

lista02 = list(range(50, 75))
# adicionando mais elementos, de forma ordenada
lista01.extend(lista02)
lista01.append('Guilherme')
#impressão revertida
print(lista01[::-1])

#pop remove o ultimo elemente e retorna ele, tambem pode se remover pelo indice
lista01.pop()

mensagem = 'Programaçao em python'
print(mensagem)

#split transforma numa lista
mensagem = mensagem.split(' ')
print(mensagem)

#transformando uma lista em uma string, colocando espaços entre cada elemento, ou ---
mensagem02 = '---'.join(mensagem)
print(mensagem02)

#for dentro de uma lista
soma = 0
for numero in lista01:
    print(numero,end='-')
    soma = numero +soma

print('soma=',soma)

#slicing
#lista[inicio:fim:passo]
lista03 = list(range(0,10))
print(lista03[::])

#copia

lista04 = lista03.copy()
lista04.append('outra lista')
print(lista04)