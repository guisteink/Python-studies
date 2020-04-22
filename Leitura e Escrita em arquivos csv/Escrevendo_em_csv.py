"""

Escrevendo em arquivos

writer() -> escrita
whiterow() -> escreve uma linha

"""
from csv import writer
from csv import DictWriter

# writter
with open('Filmes.csv', 'w') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Titulo ', 'Genero ', 'Duracao'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Genero: ')
            duracao = input('Duracao: ')
            escritor_csv.writerow([filme, genero, duracao])

# dictwritter
with open('Filmes2.csv', 'w') as arquivo2:
    cabecalho = ['Titulo', 'Genero', 'Duracao']
    escritor_csv = DictWriter(arquivo2, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme!='sair':
            genero = input('Informe o genero: ')
            duracao = input('Informe a duraçao (em minutos): ')
            escritor_csv.writerow({"Titulo": filme, "Genero": genero, "Duracao": duracao})
