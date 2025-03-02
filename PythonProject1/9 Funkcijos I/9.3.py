# 3. Funkcijos su keliais argumentais
# Užduotis 3:
# Sukurkite funkciją trys_sveikinimai(vardas1, vardas2, vardas3), kuri priimtų tris
# vardus ir kiekvienam iš jų atspausdintų pasisveikinimą.
# Pvz.: „Labas, Jonas!“, „Labas, Asta!“, „Labas, Mantas!“.


# def trys_sveikinimai(vardas1, vardas2, vardas3):
#     if not vardas1 or not vardas2 or not vardas3:
#         return
#     hello_str = f'Labas, {vardas1}!, Labas, {vardas2}!, Labas, {vardas3}!'
#     return hello_str
# res = trys_sveikinimai('Jonas','Asta', 'Mantas')
# print(res)

# 1 case
def trys_sveikinimai(vardas1, vardas2, vardas3):

    print(f'Labas, {vardas1}')
    print(f'Labas, {vardas2}')
    print(f'Labas, {vardas3}')

# 1 case
trys_sveikinimai('Vardas1', 'Vardas2', 'Vardas3')
print('-----------------------------')

# 2 case
def trys_sveikinimai(vardas1, vardas2, vardas3):

    return f'Labas, {vardas1}! Labas, {vardas2}! Labas, {vardas3}!'

print(trys_sveikinimai('Vardas1', 'Vardas2', 'Vardas3'))


print('-----------------------------')
# 3 case
def trys_sveikinimai(vardas1, vardas2, vardas3):
    return f'Labas, {vardas1}!', f'Labas, {vardas2}!', f'Labas, {vardas3}!'

for sveikinimas in trys_sveikinimai('Vardas1', 'Vardas2', 'Vardas3'):
    print(sveikinimas)

print('-----------------------------')

# 4. Numatytosios reikšmės ir keyword argumentai
# Užduotis 4:
# Sukurkite funkciją sveikink_su_pavadinimu(vardas, pavadinimas="drauge"), kuri
# atspausdintų žinutę: „Sveikas, [vardas]! Ką veiki, [pavadinimas]?“.
# 1. Iškvieskite funkciją nenurodydami pavadinimo.
# 2. Iškvieskite funkciją, nurodydami pavadinimą „kolega“.


def sveikink_su_pavadinimu(vardas, pavadinimas = 'drauge'):
    print( f'Sveikas, {vardas}! Ka veiki, {pavadinimas}?')

sveikink_su_pavadinimu('Edita')
sveikink_su_pavadinimu('Edita','kolega')
