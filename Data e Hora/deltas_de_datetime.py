"""

data inicial = dd/mm/yyyy 00h00m00s
data final = dd/mm/yyyy 00h00m00s

delta = data inicial - data final

"""

import datetime

data_agora = datetime.datetime.now()
aniversario = datetime.datetime(2023, 3, 3, 0)
tempo_delta = aniversario - data_agora

print(type(tempo_delta))
print(tempo_delta)