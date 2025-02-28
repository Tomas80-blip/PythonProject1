# 11. Importai iš folderio
# Užduotis 11:
# 1. Sukurkite folderį moduliai.
# 2. Sukurkite šiame folderyje failą aritmetika.py su funkcijomis atimtis(a, b) ir
# dalyba(a, b).
# 3. Sukurkite main.py, kuris importuoja aritmetika ir iškviečia šias funkcijas.

import moduliai
moduliai.aritmetika.atimk(6,3)
from moduliai.aritmetika import dalink, atimk

res = round(dalink(10, 7), 2)
print(res)

res = atimk(10, 7)
print(res)

# 12. Visas modulio importavimas iš folderio
# Užduotis 12:
# 1. Sukurkite Python programą, kuri importuoja moduliai.aritmetika.
# 2. Naudokite moduliai.aritmetika.atimtis(20, 5) ir
# moduliai.aritmetika.dalyba(10, 2).
# 3. Išspausdinkite rezultatus.

import moduliai.aritmetika

res = moduliai.aritmetika.atimk(10, 7)
print(res)

res = round(moduliai.aritmetika.dalink(10, 7), 2)
print(res)




# 13. Specifinių funkcijų importavimas iš folderio
# Užduotis 13:
# 1. Importuokite iš moduliai.aritmetika tik atimtis ir dalyba.
# 2. Paskaičiuokite 50 - 25 ir 100 / 4.
# 3. Išspausdinkite rezultatus.

import moduliai.aritmetika

res = moduliai.aritmetika.atimk(50, 25)
print(res)

res = moduliai.aritmetika.dalink(100, 4)
print(res)





# 14. Modulio trumpinimas naudojant alias iš folderio
# Užduotis 14:
# 1. Importuokite moduliai.aritmetika kaip ar.
# 2. Naudokite ar.atimtis(30, 10) ir ar.dalyba(50, 5).
# 3. Išspausdinkite rezultatus.

import moduliai.aritmetika as ar

res = ar.atimk(50, 25)
print(res)

res = ar.dalink(100, 4)
print(res)



# 15. Importavimas viso folderio
# Užduotis 15:
# 1. Sukurkite __init__.py failą folderyje moduliai, kad jis būtų laikomas Python
# paketu.
# 2. Importuokite visą folderį import moduliai ir naudokite
# moduliai.aritmetika.atimtis(15, 5).
# 3. Išspausdinkite rezultatą.

import moduliai

res = moduliai.aritmetika.atimk(15, 5)
print(res)