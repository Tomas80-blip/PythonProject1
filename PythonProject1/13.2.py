# 2. Norimos datos ir laiko objekto sukūrimas
# Užduotis 2:
# 1. Sukurkite datetime objektą, kuris atitinka datą: 1995 m. liepos 14 d., 15:30:00.
# 2. Išveskite šią datą ir laiką.
# 3. Sukurkite antrą datetime objektą tik su data: 2023-01-01 (be laiko).

import datetime
my_datetime = datetime.datetime(1995, 7, 14, 15, 30, 00)
print(my_datetime)

my_datetime = datetime.datetime(2023, 1, 1)
print(my_datetime)



# 3. Laiko skirtumo tarp datų skaičiavimas
# Užduotis 3:
# 1. Apskaičiuokite, kiek dienų praėjo nuo 2000-01-01 iki šiandienos.
# 2. Išveskite rezultatą tokia forma:
# "Praėjo <dienų skaičius> dienų nuo 2000-01-01."

my_datetime = datetime.datetime(2000, 1, 1)
time_from_2000 = datetime.datetime.today() - my_datetime
print(f'Praejo {time_from_2000} dienu nuo 2000-01-01')