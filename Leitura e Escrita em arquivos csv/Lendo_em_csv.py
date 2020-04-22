"""

CSV - Comma Separeted Values (Valores separados por virgula)

#SEPARADOR POR VIRGULA
1, 2, 3, 4, 5, 6, 7
"oi", "tchau", "python", "programacao"

#SEPARADOR POR PONTO E VIRGULA
1; 2; 3; 4; 5; 6; 7
"oi"; "tchau"; "python"; "programacao"

#SEPARADOR POR ESPAÇO
1 2 3 4 5 6 7
"oi" "tchau" "python" "programacao"

ex: htpp://dados.gov.br/dataset

"""

#organiza todos os dados numa lista - muito trabalhoso
with open('Lutadores.csv') as arq:
    dados = arq.read()
    dados = dados.split()
    print(dados)

"""

O python possui duas formas diferentes pra ler dados e arquivos em csv:
    - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
    - DictReader -> Permite que iteremos sobre as linhas de arquivo CSV como OrderedDicts.

"""
print('\n')

from csv import reader
from csv import DictReader

# reader
with open('Lutadores.csv') as arquivo:
    leitor_csv = reader(arquivo)
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu no(a) {linha[1]} e mede {linha[2]} centímetros')

print('\n')
# dictreader
with open('Lutadores.csv') as arquivo2:
    leitor_csv2 = DictReader(arquivo2, delimiter = ',')
    for linha2 in leitor_csv2:
        # Cada linha é uma OrderedDict
        print(f"{linha2['Nome']}")



















