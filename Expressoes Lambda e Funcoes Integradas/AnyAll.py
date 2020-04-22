#All eh uma funcao que retorna TRUE se todas as posicoes do array sao existentes, ex porta logica AND
lista = [0,1,2,3,4,5] #existe o 0, portanto existe uma posicao `None`
print('all Lista 1 ->',all(lista))

lista2 = [1,2,3,4,5,6,7] #nao existe o 0
print('all Lista 2 ->',all(lista2))

#exemplo usual
listanomes = ['Carlos','Carina','Caio','Cecilia','Davi']
print('all 1 ->',all(nome[0]=='C' for nome in listanomes))

listanomes2 = ['Carlos','Carina','Caio','Cecilia']
print('all 2 ->',all(nome[0]=='C' for nome in listanomes2))

#Any eh uma funcao que retorna TRUE se uma posicao do array ja for verdadeira, ex porta logica OR
print('Any lista 1->',any(lista))
print('Any lista 2->',any(lista2))

print('any 1 ->',any(nome[0]=='D' for nome in listanomes))
print('any 2 ->',any(nome[0]=='D' for nome in listanomes2))


