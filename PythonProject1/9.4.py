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