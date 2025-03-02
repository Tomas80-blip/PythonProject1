
# 1. List Comprehensions naudojimas
# Užduotis 1:
# Turite sąrašą skaičių [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# 1. Naudodami list comprehension, sukurkite naują sąrašą, kuriame būtų visi
# elementai padvigubinti.
# 2. Sukurkite sąrašą, kuriame būtų visi pradinio sąrašo elementai pakelti kvadratu.

print('-------------------')
listaS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(listaS)

kaupikliS = [elem * 2 for elem in listaS]
print(kaupikliS)
kaupiklis6 = [elem ** 2 for elem in listaS]
print(kaupiklis6)


# 2. Operacijų atlikimas naudojant list comprehension
# Užduotis 2:
# Turite sąrašą kainų eurais: [10, 15, 20, 25, 30].
# 1. Naudodami list comprehension, konvertuokite visas kainas į dolerius, pritaikant
# kursą 1 EUR = 1.1 USD.
# 2. Sukurkite sąrašą su pranešimais, pvz., „Kaina: 10 EUR“, „Kaina: 15 EUR“ ir t.t.

listas1 = [10, 15, 20, 25, 30]

kaupiklis1 = [round(elem * 1.1, 1) for elem in listas1]

print(kaupiklis1)

kaupiklis2 = [f'Kaina: {elem} EUR' for elem in listas1]
print(kaupiklis2)