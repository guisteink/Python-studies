"""
Dict != Set

Dict = {[chave: valor], ...}
Set = {chave, ...}

Sets são bons pra armazenação qndo nao se importa com a ordenação

"""
conjunto = {1, 2, 3, 4, 1, 43, 5}  # NAO ACEITAM NUMEROS REPETIDOS E NAO MANTEM  A ORDENACAO NA IMPRESSAO

print(conjunto)

############################# operações entre conjuntos #############################

conjunto_alunos = {'Pedro Roberto','Artur Costa','Joao Silva','Maria Elena','Tiago Rossi','BLABLA','BLABLA2','BLABLA3','BLABLA4'}
conjunto_professores = {'Pedro Roberto','Noel','Joao','Maria Elena','Tiago'}

conjunto_intersecao = conjunto_alunos.intersection(conjunto_professores)
print('Intersecao: ',conjunto_intersecao)

conjunto_uniao = conjunto_alunos.union((conjunto_professores))
print('Uniao: ',conjunto_uniao)

conjunto_dif = conjunto_alunos.difference(conjunto_professores)
print('Dif: ',conjunto_dif)