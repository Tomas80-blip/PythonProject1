# 1. Sukurkite funkciją tikrinti_amziu(amzius), kuri:
# a. Jei amzius < 0, iššaukia ValueError su pranešimu "Amžius negali
# būti neigiamas!".
# b. Jei amzius >= 18, grąžina "Vartotojas pilnametis.".
# c. Jei amzius < 18, grąžina "Vartotojas nepilnametis.".
# 2. Išbandykite funkciją su reikšmėmis (-5), (15), (21).

def tikrinti_amziu(amzius):
    if amzius < 0:
        raise ValueError('Amžius negali būti neigiamas!')
    elif amzius >= 18:
        print('Vartotojas pilnametis!')
    else:
        print('Vartotojas nepilnametis!')

tikrinti_amziu(21)
tikrinti_amziu(16)
tikrinti_amziu(-3)