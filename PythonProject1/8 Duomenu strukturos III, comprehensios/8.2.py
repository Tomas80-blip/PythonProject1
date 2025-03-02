# 3. Vidinės struktūros sudarymas naudojant list comprehension
# Užduotis 3:
# Sukurkite sąrašą, kuriame yra šių skaičių [1, 2, 3, 4, 5] informacija:
# 1. Kiekvienas elementas turi būti sąrašas, kuriame yra: pats skaičius, jo kvadratas ir
# kubas.
# 2. Pvz.: [1, 1, 1], [2, 4, 8].
# 3. Papildykite struktūrą taip, kad kiekvienas vidinis sąrašas turėtų dar vieną elementą – informaciją,
# ar skaičius yra lyginis (True/False).
# 4. Duomenų filtravimas naudojant list comprehension

print('----------------------')
listas1 = [1, 2, 3, 4, 5]
print(listas1)

kaupiklis1 = [[elem, elem ** 2, elem ** 3, elem % 2 == 0] for elem in listas1]
print(kaupiklis1)


# Užduotis 4:
# Turite sąrašą skaičių [5, 8, 12, 18, 25, 30, 35, 40].
# 1. Sukurkite naują sąrašą, kuriame būtų tik skaičiai didesni nei 20.
# 2. Sukurkite sąrašą, kuriame būtų tik tie skaičiai, kurie dalijasi iš 5.
# 3. Sukurkite sąrašą su reikšmėmis „Lyginis“ arba „Nelyginis“, atitinkamai kiekvienam
# pradiniam sąrašo skaičiui.

print('----------------------')
listas2 = [5, 8, 12, 18, 25, 30, 35, 40]
print(listas2)
kaupiklis2 = [elem for elem in listas2 if elem > 20]
print(kaupiklis2)

kaupiklis3 = [elem for elem in listas2 if elem % 5 == 0]
print(kaupiklis3)

lyg_nelyg = [f'Lyginis {elem}' if elem % 2 == 0 else f'Nelyginis {elem}' for elem in listas2]
print(lyg_nelyg)