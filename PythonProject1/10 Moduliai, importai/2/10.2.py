# 3. Specifinių funkcijų importavimas
# Užduotis 3:
# Sukurkite Python programą, kuri naudoja:
# 1. from random import randint, choice
# 2. Sugeneruoja atsitiktinį skaičių nuo 1 iki 10 naudojant randint().
# 3. Pasirenka atsitiktinį elementą iš sąrašo ['obuolys', 'bananas', 'kriaušė',
# 'vyšnia'] naudodama choice().
# 4. Išspausdina abu rezultatus.

from random import randint, choice

atsitiktinis_skaicius = randint(1, 10)
atsitiktinis_elementas = choice(['obuolys', 'bananas', 'kriaušė', 'vyšnia'])

print(atsitiktinis_skaicius)
print(atsitiktinis_elementas)

from random import randint as rnt
from random import choice as ch

atsitiktinis_skaicius = rnt(1, 10)
atsitiktinis_elementas = ch(['obuolys', 'bananas', 'kriaušė', 'vyšnia'])

print(atsitiktinis_skaicius)
print(atsitiktinis_elementas)


# 4. Modulio trumpinimas naudojant alias
# Užduotis 4:
# Sukurkite Python programą, kuri:
# 1. Importuoja datetime modulį su alias dt.
# 2. Naudoja dt.datetime.now() funkciją, kad gautų dabartinę datą ir laiką.
# 3. Išspausdina rezultatą su formatu: Dabartinė data ir laikas: YYYY-MM-DD
# HH:MM:SS.

import datetime as dt
print(dt.datetime.now())
# arba
print(dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))