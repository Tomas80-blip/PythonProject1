# 7. Importai iš mūsų sukurto modulio
# Užduotis 7:
# 1. Sukurkite naują Python failą matematika.py.
# 2. Šiame faile parašykite funkcijas:
# a. sudetis(a, b), kuri grąžina dviejų skaičių sumą.
# b. daugyba(a, b), kuri grąžina dviejų skaičių sandaugą.
# 3. Sukurkite kitą Python failą main.py, kuris importuoja šias funkcijas ir jas iškviečia.

from matematika import daugink, sumuok
res = daugink(1, 9)
res1 = sumuok(5, 6)
print(res)
print(res1)

# 8. Visas modulio importavimas
# Užduotis 8:
# 1. Sukurkite Python programą, kuri importuoja matematika modulį (sukurtą
# ankstesnėje užduotyje).
# 2. Naudoja matematika.sudetis(10, 20) ir matematika.daugyba(5, 4).
# 3. Išspausdina rezultatus.


import matematika

res = matematika.daugink(2, 3)
print(res)
res1 = matematika.sumuok(5, 4)
print(res1)



# 9. Specifinių funkcijų importavimas
# Užduotis 9:
# 1. Naudodami from matematika import sudetis, daugyba, importuokite tik tas
# funkcijas, kurios reikalingos.
# 2. Paskaičiuokite sumą ir sandaugą skaičių 8 ir 3.
# 3. Išspausdinkite rezultatus.

from matematika import sumuok, daugink

res = sumuok(10, 7)
print(res)

res = daugink(10, 7)
print(res)


# 10. Modulio trumpinimas naudojant alias
# Užduotis 10:
# 1. Importuokite matematika modulį kaip m.
# 2. Naudokite m.sudetis(12, 18) ir m.daugyba(7, 6).
# 3. Išspausdinkite rezultatus.

import matematika as m

res = m.daugink(10, 7)
print(res)

res = m.sumuok(10, 7)
print(res)