"""
Geração de novos dados através do processamento iterável de dados existentes
"""
from Others import Funcoes

numeros = list(range(10))

res = [numero * Funcoes.fibonacci(numero) for numero in numeros] #atraves dos dados de 'numeros' (lista) gero 'res' uma nova lista
print(res)

pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)
impares = [numero for numero in numeros if numero % 2 != 0]
print(impares)

#listas aninhadas
lista = [[1,2,3],[3,4,5],[6,7,8]]
print(lista)

for n in lista:
    for n2 in n:
        print(n2)


#manipulação exemplar
res2 = ['X' for numero in lista]
print(res2)


#dict
numeros = {'a':1,'b':2,'c':3}

quadrado = {chave:valor**2 for chave, valor in numeros.items()}
print(quadrado)

chave = 'abcde'
num = [1,2,3,4,5]

mistura = {chave[i]:num[i] for i in range(0,len(chave))}
print(mistura)






