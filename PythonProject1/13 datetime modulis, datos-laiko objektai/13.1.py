# 1. Atskiri datos-laiko laukai iš datetime objekto
# Užduotis 1:
# 1. Sukurkite programą, kuri:
# a. Naudoja datetime.datetime.today() dabartinės datos ir laiko gavimui.
# b. Išveda šiuos laukus: metai, mėnuo, diena, valanda, minutė, sekundė.
# 2. Išveskite pranešimą:
# "Dabar yra <valanda>:<minutė>, <diena>-<mėnuo>-<metai>"
print('-------------------------------------------------')
# 1.A
import datetime
dt_res = datetime.datetime.today()
# 1.B
metai = dt_res.year
menuo = dt_res.month
diena = dt_res.day
valanda = dt_res.hour
minute = dt_res.minute
sekunde = dt_res.second

print(dt_res)
print(dt_res.year)  # 2025
print(dt_res.month)
print(dt_res.day)
print(dt_res.hour)
print(dt_res.minute)
print(dt_res.second)

# 2
print(f'Dabar yra {valanda}:{minute}, {diena}--{menuo}--{metai}')