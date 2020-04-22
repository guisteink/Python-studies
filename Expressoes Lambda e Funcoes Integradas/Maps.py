import math

#Map é uma funcao que recebe 2 parametros em que, 1 é uma funcao e o segundo é um iterável(array)
#e aplica a funçao em todo o iterável

def calcArea(r):
    return math.pi * (r ** 2)


raios = [2, 4, 5, 6, 7]
areas =[]

#forma 1
for numero in raios:
    areas.append(calcArea(numero))

print(areas)

#forma 2 - com map
areas = map(calcArea,raios)
print(list(areas))

#forma 3 - map com lambda (wtf)
print(list(map(lambda x: math.pi*(x**2),raios)))



