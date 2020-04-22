"""
Funcoes Min e Max:
->Max(): retorna o maior valor de um array iterável
->Min(): retorna o menor valor de um array iterável
->Reversed(): Reverte qualquer tipo de iterável, nao confundir com reverse() que so funciona com listas e modifica ela. Retorna um iterável chamado list_reversediterator
"""

#Max, tbm serve pro Min
listanomes = ['Carlos', 'Carina', 'Caio', 'Cecilia', 'Davi']
lista2 = [1, 2, 3, 4, 5, 6, 7]
a, b = 5, 10
tupla = (1,2,3,5,2,1)

print(max(listanomes))
print(max(lista2))
print(max(a, b))
print(max(40,33,100,1000,39))

#Reversed
res = reversed(tupla)
res2 = reversed(lista2)
print(list(res))
print(list(lista2))