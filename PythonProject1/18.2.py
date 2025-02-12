# 2. Dekoratoriai
# Užduotis:
# Sukurkite dekoratorių sekimo_dekoratorius, kuris:
# 1. Išveda žinutę prieš ir po funkcijos vykdymo:
# a. Prieš: „Vykdoma funkcija: <funkcijos_pavadinimas>“
# b. Po: „Funkcija baigta!“
# 2. Pridėkite dekoratorių prie funkcijos dauginti(a, b), kuri grąžina dviejų skaičių
# sandaugą.
# Papildoma užduotis:
# Pridėkite funkciją dalinti(a, b) su tuo pačiu dekoratoriumi. Jei b == 0, grąžinkite
# klaidos pranešimą.

def sekimo_dekoratorius(funkcija):
    def vidine(*args, **kwargs):
        print(f"Vykdoma funkcija: {funkcija.__name__}")
        rezultatas = funkcija(*args, **kwargs)
        print("Funkcija baigta!")
        return rezultatas
    return vidine

@sekimo_dekoratorius
def dauginti(a, b):
    return a * b

@sekimo_dekoratorius
def dalinti(a, b):
    if b == 0:
        return "Klaida: dalyba iš nulio negalima!"
    return a / b

daug = dauginti(3, 4)
dal1 = dalinti(10, 2)
dal2 = dalinti(5, 0)
print(daug)
print(dal1)
print(dal2)