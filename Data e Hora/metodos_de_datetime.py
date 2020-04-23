"""
    Metodos no datetime

        YY/MM/DD FORMATO AMERICANO


"""
import datetime

agora = datetime.datetime.now()  # agora, pode se especificar uma timezone
# today = datetime.datetime.today() #hoje

print(f'Horario de agora:{agora}')
# print(today)

aniversario = '15/02/1997'
aniversario = aniversario.split('/')

aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))
if aniversario.weekday() == 0:
    print('Voce nasceu numa segunda')
elif aniversario.weekday() == 1:
    print('voce nasceu numa terça')
elif aniversario.weekday() == 2:
    print('voce nasceu numa quarta')
elif aniversario.weekday() == 3:
    print('voce nasceu numa quinta')
elif aniversario.weekday() == 4:
    print('voce nasceu numa sexta')
elif aniversario.weekday() == 5:
    print('voce nasceu num sabado')
elif aniversario.weekday() == 6:
    print('voce nasceu num domingo')

# FORMATANDO DATA PRO PADRAO BRASILEIRO
HOJE = datetime.datetime.today()
HOJE = HOJE.strftime('Data br:%d/%m/%y')
print(HOJE)

# calculando o tempo de execução de um código com o timeit
import timeit

# essa funcao timeit recebe a funcao que deve ser executada e o numero de vezes executada
# O 1º parametro é uma funcao pra criar uma lista de 0 a 1000, concatecando com '-', ex: 1-2-3-4-5-6-7...-1000.
# Loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f'Tempo gasto para um loop: {tempo}')

# List comprehension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(f'Tempo gasto para uma Lista {tempo}')

# Map
tempo = timeit.timeit('"-".join(map(str,range(100)))', number=10000)
print(f'Tempo gasto para um map {tempo}')

import functools, random


# funcao
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


x = random.randrange(50, 100)
a = random.randrange(1, 10)
b = random.randrange(11, 20)
tempo = timeit.timeit(functools.partial(fibonacci, random.randrange(a, b)), number=x)
print(f'\nTempo gasto pra executar a funcao fibonacci {x} vezes, um numero aleatorio de {a} até {b}: {tempo}')
