"""
Dicionarios:
    - São representados por {}
    - Funcionam da forma CHAVE/VALOR

    OBS:
        - Chave : Valor
        - Tanto chave quanto valor podem ser de qualquer tipo de dado
        - Pode-se misturar o tipo de dados

"""
print(type({}))

#mais usual
paises={'br':'Brasil','eua':'Estados Unidos','arg':'Argentina'}
print(paises.values())

#menos usual
paises02 = dict(br='Brasil',eua='Estados Unidos')

paisExist=paises.get('ru')
if paisExist:
    print('Encontrado o pais')
else:
    print('Pais nao encontrado')

#ask bool
print('br' in paises)

#Exemplo de utilização de um dict
localizacao = {
    (30.409 , 47.908) : 'Casa da minha mae',
    (40.908 , 54.018) : 'Casa do meu pai',
    (98.098 , 68.092) : 'Minha casa'
}
print(localizacao.keys())  #utilizadas tuplas nas coordenadas pois nao necessita-se de mudança
print(localizacao.values())

#outro exemplo, add uma chave com valor
receita = dict(jan='100',fev='140',marc='202')
receita['abr'] = 400
print(receita)
#outra forma
novo = {'dez':500}
receita.update(novo) #serve pra adicionar ou atualizar
print(receita)

#pop
retirar = receita.pop('dez')
print(retirar)

#metodo fromkeys
teste = {}.fromkeys(['a','b','c','d'],'null')
print(teste)

teste02 = {}.fromkeys(range(1,10),'novo')
print(teste02)

print(max(teste02))

