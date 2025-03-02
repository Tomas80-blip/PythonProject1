# break ir continue naudojimas while cikle
#
# uzduotis 2
#
# Sukurkite programa, kuri:
#
# 1. Vykdytu while cikla, kuriame prasoma ivesti skaiciu nuo 1 iki 10.
# 2. Jei ivesta reiksme ne siame intervale, programa naudotu continue ir paprasytu pakartoti ivesti
# 3. Jei ivesta '5', ciklas butu nutrauktas su break
# 4. Isspausdintu visu ivestu skaiciu suma, neskaiciuojant '5'.

res = 0
while True:
    pasirinkimas = int(input('iveskite sk nuo 1 iki 10:'))
    if pasirinkimas < 1 or pasirinkimas > 10:
        print(f'Pakartokite ivesti, skaicius turi buti intervale nuo 1 iki 10')
        continue
    elif pasirinkimas == 5:
        break
    res += pasirinkimas
    print(f'suma:{res}')

