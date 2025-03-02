# Loginiai operatoriai
# 1. Sukurkite programą, kuri leidžia vartotojui įvesti du skaičius ir tikrina:
# a. Ar abu skaičiai yra teigiami.
# b. Ar bent vienas iš jų yra neigiamas.


sk1 = int(input('Iveskite 1 sk:'))
sk2 = int(input('Iveskite 2 sk:'))

if sk1 > 0 and sk2 > 0:
    print('Teigiami')
if sk1 < 0 or sk2 < 0:
    print('Neigiami')
else:
    print('ivedete nuli')


# 2. Sukurkite programą, kuri leidžia vartotojui įvesti automobilio markę ir modelį.
# Patikrinkite:
# a. Ar markė yra iš sąrašo „vokiškų“ automobilių (pvz., „BMW“, „Audi“).
# b. Ar modelis yra sportinis pagal sąrašą (pvz., „M3“, „RS6“).

marke = input('Iveskite automobilio marke:')
modelis = input('Iveskite automobilio modeli:')

autos_germ = ["BMW", "Audi"]
autos_sports = ["M3", "RS6"]

if marke in autos_germ and modelis in autos_sports:
    print('auto yra is vokisku sportiniu automobiliu')
else:
    print('auto nera tarp vokisku sportiniu automobiliu')