"""

São decorators usando *args, **kwargs. Que são ponteiros que identificam qualquer qtd. de parametros de entrada

"""

def titúla_nome(funcao):
    def aumentar(*args,**kwargs):
        return funcao(*args,**kwargs).title()
    return aumentar

@titúla_nome
def digita_nome(nome):
    return f'Ola {nome}'
@titúla_nome
def digita_nomes(nome1,nome2):
    return f'Ola senhores, respectivamente, {nome1} e {nome2}'

print(digita_nome(nome = input('Digite o nome: ')))
print(digita_nomes(nome1 = input('Nome: '), nome2 = input('Nome: ')))
