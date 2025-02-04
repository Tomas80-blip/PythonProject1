# 7. Laiko skirtumo (timedelta) objekto gavimas atliekant datų atimtį
# Užduotis 7:
# 1. Sukurkite dvi datas:
# a. 2023-01-01
# b. 2024-01-01
# 2. Apskaičiuokite laiko skirtumą tarp jų naudojant - operatorių.
# 3. Išveskite rezultatą dienomis.

import datetime
data1 = datetime.datetime(2023, 1, 1)
data2 = datetime.datetime(2024, 1, 1)

# padarius atimtį datos-laiko iš datos-laiko, gaunamas kitas objektas
# laiko skirtumo(laiko tarpo) objektas datetime.timedelta
skirtumas = data2 - data1
print(skirtumas)
print(skirtumas.days)


# 8. Skaičiavimai su timedelta objektais
# Užduotis 8:
# 1. Sukurkite programą, kuri:
# a. Naudoja dabartinę datą.
# b. Prideda 90 dienų naudojant timedelta.
# 2. Išveskite rezultatą:
# "Data po 90 dienų bus: <data>"

skirtumas = datetime.timedelta(days=90)
dabar = datetime.datetime.today()
print(skirtumas)
res = dabar + skirtumas
print(f'data po 90 dienu bus: {res}')


# 9. timedelta objekto laukų prieiga
# Užduotis 9:
# 1. Apskaičiuokite skirtumą tarp 2000-01-01 ir šiandienos.
# 2. Išveskite:
# a. Dienų skaičių
# b. Valandų skaičių (naudojant .seconds)
# c. Bendrą sekundžių skaičių (.total_seconds())

import datetime
dabar = datetime.datetime.today()
mileniumas = datetime.datetime(2000, 1, 1)
skirtumas = dabar - mileniumas
print(skirtumas)
print(skirtumas.days)
print(skirtumas.seconds) # Valandų skaičiųs (naudojant .seconds)
print(skirtumas.total_seconds()) # Bendrą sekundžių skaičių (.total_seconds())