"""

Utilizamos o 'assert' em uma expressão que queremos checar se é valida ou nao. Se a expressao for verdadeira, retorna
None e caso seja falsa  retorna um AssertionError
obs: Da pra personalizar a mensagem de erro

"""


# essa funcao deve somar apenas numeros positivos
def soma(a, b):
    # caso seja a e b sejam maiores que zero, retorma a soma normal
    assert a > 0 and b > 0, 'A soma deve ser de numeros maiores que zero'  # mensagem de erro
    return a + b


def comendo(comida):
    assert comida in [
        'macarrao', 'arroz', 'feijao', 'ovo', 'frango'
    ], 'A comida deve ser de pobre'
    return f'Estou comendo {comida}'

