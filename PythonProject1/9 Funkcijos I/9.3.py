# 3. Funkcijos su keliais argumentais
# Užduotis 3:
# Sukurkite funkciją trys_sveikinimai(vardas1, vardas2, vardas3), kuri priimtų tris
# vardus ir kiekvienam iš jų atspausdintų pasisveikinimą.
# Pvz.: „Labas, Jonas!“, „Labas, Asta!“, „Labas, Mantas!“.


def trys_sveikinimai(vardas1, vardas2, vardas3):
    if not vardas1 or not vardas2 or not vardas3:
        return
    hello_str = f'Labas, {vardas1}!, Labas, {vardas2}!, Labas, {vardas3}!'
    return hello_str
res = trys_sveikinimai('Jonas','Asta', 'Mantas')
print(res)