import datetime

print(datetime.MAXYEAR)
print(datetime.MINYEAR)

agora = datetime.datetime.now()

print(agora)

agora = agora.replace(year=2011, day=13, month=2, hour=0, minute=0, second=0)

print(agora)
