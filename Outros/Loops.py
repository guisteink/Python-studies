############################################################################# FOR
numeros = range(1,10)
nome = 'guilherme stein'
lista = list(range(10))

for numero in range(1,10):
    print(numero)

for letra in nome*3:
    print(letra, end = '')

for x in range(3):
    for num in range(1,11):
        print('\U0001F65D' *num) #codigo de um emoji

for num in range(1,11,2): #ultimo argumento modela o passo do loop
    print (num)

print(lista)
################################################################################# WHILE
num =0
while num < 10:
    print('gay',end=' ')
    num = num+1

while 1:
    comando = input('\ndigite 1 pra finalizar o loop ')
    if comando == '1':
        break;
