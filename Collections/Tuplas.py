#Listas imutáveis, representadas por () (parenteses)
#Nao existem métodos de adiçao ou remoçao em tuplas, devido a sua imutabilidade
#TUPLAS SÃO MAIS RAPIDAS DO QUE LISTAS E DEIXAM O CÓDIGO MAIS SEGURO
tupla01 = 1,2,3,4,5
tupla02 = {1,2}
tupla03 = tuple(range(11))
print(tupla03)

#desempacotando de tupla
escola, curso = tupla02 #escola recebe 1, e curso recebe 2

#alguns metodos, para caso tenha apenas inteiros ou reais
print(sum(tupla03))
print(max(tupla03))
print(min(tupla03))
print(len(tupla03))

#ask bool
print(3 in tupla03)

#contando elementos de uma tupla
tupla04 = ('a','a','a','a','a','a')
print(tupla04.count('a'))

#EXEMPLO DE UTILIDADE DE UMA TUPLA, UMA LISTA DE ELEMENTOS QUE NAO PRECISAM SER ALTERADOS
dias = ('segunda','terca','quarta','quinta','sexta','sabado','domingo')

i=0
while i < len(dias):
    print(dias[i])
    i=i+1