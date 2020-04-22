""""
->len(): Retorna o tamanho de um array seja de qualquer tipo
->abs(): Retorna o valor absoluto de um numero inteiro ou real. De forma básica, seu valor sem o sinal
->sum(): Recebe um iterável como parâmetro e retorna a soma
->round(): Retorna um numero arredondado para n digito de precisao após a casa decimal
->zip(): Cria um iterável (Zip object) que agrega elemento de cada um dos iteráveis passados como entrada em pares. OBS: em iteraveis de tamanho diferente, para de iterar no menor
"""
import random

print('\nLEN:')
print(len([1, 2, 3, 4, 6, 7, 3, 0]))

print('\nABS:')
print(abs(-4))

print('\nSUM:')
print(sum([1.2, 42, 51, 1, 3, 5, 1]))

print('\nROUND:')
print(round(10.3334))
print(round(10.3334, 5))  ##precisao passada como parametro

print('\nZIP:')
zip1 = zip([1,2,3],[4,5,6])
print(list(zip1))
zip1 = zip([1,2,3],[4,5,6])
print(tuple(zip1))
zip1 = zip([1,2,3],[4,5,6])
print(set(zip1))
zip1 = zip([1,2,3],[4,5,6])
print(dict(zip1))
