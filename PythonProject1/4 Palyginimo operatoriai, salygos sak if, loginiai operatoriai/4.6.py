# task 2
# 6. Metodai, grąžinantys True arba False
# 1. Sukurkite programą, kuri leidžia vartotojui įvesti žodį ir tikrina:
# a. Ar žodis prasideda didžiąja raide.
# b. Ar visi žodžio simboliai yra mažosios raidės.

zodis = input('Įveskite žodį: ') # vilnius
ar_prasideda_didz = zodis.istitle()

ar_mazosios = zodis.islower() # True
# kitaip
# ar_mazosios = not zodis.isupper() # True

print(f'Žodis prasideda didžiąja raide: {ar_prasideda_didz}')
print(f'Visi žodžio simboliai yra mažosios raidės: {ar_mazosios}')


# 2. Parašykite programą, kuri leidžia vartotojui įvesti sakinio eilutę ir:
# a. Tikrina, ar eilutė prasideda tam tikru simboliu (pvz., „A“).
# b. Tikrina, ar eilutė yra parašyta tik didžiosiomis raidėmis.

eilute = input('Įveskite sakinį: ')
ar_prasideda_A = eilute.startswith('A')
ar_didziosios = eilute.isupper()
print(f'Eilutė prasideda simboliu „A“: {ar_prasideda_A}')
print(f'Eilutė parašyta tik didžiosiomis raidėmis: {ar_didziosios}')