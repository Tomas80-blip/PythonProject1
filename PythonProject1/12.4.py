# 1. Sukurkite funkciją tikrinti_amziu(amzius), kuri:
# a. Jei amzius < 0, iššaukia ValueError su pranešimu "Amžius negali
# būti neigiamas!".
# b. Jei amzius >= 18, grąžina "Vartotojas pilnametis.".
# c. Jei amzius < 18, grąžina "Vartotojas nepilnametis.".
# 2. Išbandykite funkciją su reikšmėmis (-5), (15), (21).

def tikrinti_amziu(amzius: int) -> int:
    if amzius < 0:
        raise ValueError('Amžius negali būti neigiamas!')
    elif amzius >= 18:
        return 'Vartotojas pilnametis'
    else:
        return 'Vartotojas nepilnametis'

print(tikrinti_amziu(21))
print(tikrinti_amziu(16))
print(tikrinti_amziu(-5))