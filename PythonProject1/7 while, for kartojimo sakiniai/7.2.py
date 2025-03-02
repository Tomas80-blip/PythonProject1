# 6 Operacijos for cikle
# uzd 6
#
# sukurti programa kuri:
# 1. Iteruos per sarasa [5, 7, 6, 8, 15, 3, 20, 12]
# 2. Isspausdins tik tuos skaicius, kurie yra lyginiai arba dalijasi is 5.
# 3. Jei suras skaiciu, didesni nei 10, programa nutrauks iteracija.


sarasas = [5, 7, 6, 8, 15, 3, 20, 12]


for skaicius in sarasas:
    if skaicius % 2 == 0 or skaicius % 5 == 0:
        print(skaicius)
    if skaicius > 10:
        break

# 7. Kaupikliai cikluose
# uzd 7
# Sukurkite programa, kuri:
#
# 1. Naudodama for cikla iteruos per sarasa [-10, -5, 0, 5, 10, 15, 20]
# 2. Apskaiciuos teigiamu ir neigiamu skaiciu sumas atskirai
# 3. Isspausdins didziausia ir maziausia reiksme sarase.


skaiciai = [-10, -5, 0, 5, 10, 15, 20]

teigiamu_suma = 0
neigiamu_suma = 0
didziausias = skaiciai[0]
maziausias = skaiciai[0]

for skaicius in skaiciai:
    if skaicius > 0:
        teigiamu_suma += skaicius
    if skaicius < 0:
        neigiamu_suma += skaicius
    if skaicius > didziausias:
        didziausias = skaicius
    if skaicius < maziausias:
        maziausias = skaicius

print(f'"Teigiamu skaiciu suma:", {teigiamu_suma}')
print(f'"Neigiamu skaiciu suma:", {neigiamu_suma}')
print(f'"Didziausia reiksme sarase:", {didziausias}')
print(f'"Maziausia reiksme sarase:", {maziausias}')