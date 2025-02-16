# Užduotis 3:
# 1. Paprašykite vartotojo įvesti du skaičius.
# 2. Naudokite try-except, kad suvaldytumėte:
# a. ValueError, jei vartotojas įveda ne skaičių.
# b. ZeroDivisionError, jei dalinama iš nulio.
# 3. Jei klaidos nėra, išveskite rezultatą.

while True:
    ivestis3 = input('Iveskite skaitikli: ')
    ivestis4 = input('Iveskite vardikli: ')

    try:
        skaitiklis = int(ivestis3)
        vardiklis = int(ivestis4)
        res = skaitiklis / vardiklis
        print(f'Rezultatas: {res}')
    except ZeroDivisionError:
        print("Klaida: Dalyba iš nulio negalima.")
    except ValueError:
        print("Klaida: Įvestas ne skaičius. Prašome įvesti skaičius.")