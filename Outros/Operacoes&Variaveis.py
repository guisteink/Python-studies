#INTEIROS
num = 41
#passando somente a parte inteira da divisao
print(num//2)
#passando o resto da divisao
print(num%2)
#elevado
print(num**2)
#somador
num+=1
print(num)

#FLOAT
float = 1.455
print(float)

#numeros complexos
numcomplx = 5j
print(type(numcomplx))
print(numcomplx**2)

#STRINGS
nome = 'guilherme stein kuhn'
print(nome.upper())
#transforma em lista de strings
print(nome.split())
#transforma em titulo
print(nome.title())

#imprime somente a 1º posiçao da lista em forma de titulo
print('Ola '+nome.split()[0].title())

#inverter e transformar em titulo
print(nome[::-1].title())

#substituir letras especificas
print(nome.title().replace('e','a'))
