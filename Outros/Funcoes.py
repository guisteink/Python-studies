import random

#fibonacci so pra relembrar
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


enesimo = random.randrange(1,101)  #random gera entre 1 e 100
inteiro=fibonacci(enesimo)

print('n random: ',enesimo,'enesimo termo fibonacci: ',inteiro)

