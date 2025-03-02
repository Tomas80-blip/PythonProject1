# 5. Sudėtingas list comprehension su keliais for ir sąlyginiais sakiniais
# Užduotis 5:
# Turite sąrašus:
# • Raidės: ['A', 'B', 'C']
# • Skaičiai: [1, 2, 3]
# 1. Sukurkite sąrašą, kuriame kiekviena raidė derinama su kiekvienu skaičiumi.
# Pvz.: ['A1', 'A2', 'A3', 'B1', ...].
# 2. Sukurkite sąrašą, kuriame derinamos tik tos raidės ir skaičiai, kurių suma (raidės
# indeksas + skaičius) yra didesnė nei 3.
# 3. Sukurkite sąrašą, kuriame derinami tik lyginiai skaičiai su mažosiomis raidėmis.
# 6. Comprehension naudojimas su kitomis duomenų struktūromis

print('--------------------')
raides = ['A', 'B', 'C']
skaiciai = [1, 2, 3]


result1 = [raid + str(sk) for raid in raides for sk in skaiciai]
print(result1)

# indeksai     1    2     3
# # raides = ['A', 'B', 'C']
# skaiciai = [1, 2, 3]
# ['A3', 'B2', 'B3', 'C1', 'C2', 'C3']

#                                               Pridedame 1, kad indeksas prasidėtų nuo 1, o ne nuo 0
result2 = [raid + str(sk) for raid in raides for sk in skaiciai if raides.index(raid) + 1 + sk > 3]
print(result2)                       #rąžina raidės indeksą sąraše (0 pagrindu)^^         Pridedame skaičių sk.
#                                                      Jei suma yra didesnė nei 3, tuomet išraiška pridedama į result2.

mazosios_raides = [raid.lower() for raid in raides]
result3 = [raid + str(sk) for raid in mazosios_raides for sk in skaiciai if sk % 2 == 0]
print(result3)

# Užduotis 6:
# Turite sąrašą: [1, 2, 3, 2, 1, 4, 5, 5].
# 1. Naudodami set comprehension, sukurkite aibę, kurioje yra tik unikalios reikšmės.
# 2. Naudodami tuple comprehension, sukurkite tuple, kuriame yra visos reikšmės
# padidintos vienetu.
# 3. Naudodami dict comprehension, sukurkite žodyną, kurio raktai yra skaičiai, o
# reikšmės – jų kvadratai.


# Task 6
# Given list
skaiciai = [1, 2, 3, 2, 1, 4, 5, 5]

# 1. Create a set containing only unique values
unikalus = {x for x in skaiciai}
print("Unikalios reikšmės (aibė):", unikalus)

# 2. Create a tuple with all values incremented by 1
tuple_pakeistas = tuple(x + 1 for x in skaiciai)
print("Padidintos reikšmės (tuple):", tuple_pakeistas)

# 3. Create a dictionary where keys are numbers, and values are their squares
kvadratai = {x: x ** 2 for x in skaiciai}
print("Žodynas su kvadratais:", kvadratai)