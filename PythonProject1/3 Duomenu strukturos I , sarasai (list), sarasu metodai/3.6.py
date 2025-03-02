# Sąrašai sąrašuose
# Sudėtinių sąrašų panaudojimas:
#
#   Sąrašai sąrašuose: Python leidžia kurti sąrašus, kuriuose gali būti kiti sąrašai kaip elementai.
# Tai naudinga, kai norite saugoti sudėtinius duomenis, pavyzdžiui, darbuotojų duomenis (vardas, pareigos, atlyginimas).
#   Vidinių sąrašų iteracija: Naudodami for ciklą galite iteruoti per išorinius sąrašus,
# o tada – per vidinius sąrašus.
#   Sudėtingų duomenų apdorojimas: Demonstracija, kaip suskaičiuoti vidinių sąrašų duomenis (pvz., bendrą atlyginimų
#   sumą arba kiek yra tam tikrų pareigų darbuotojų).


darbuotojai = [
    ['Valdas', 'programuotojas', 2000],
    ['Adomas', 'direktorius', 3000],
    ['Aldona', 'vadybininkas', 1800],
    ['Jogaila', 'programuotojas', 2500]
]

print(type(darbuotojai))
print(darbuotojai[0])  # ['Valdas', 'programuotojas', 2000]
print(darbuotojai[0][1])  # programuotojas
print(darbuotojai[0][1].upper())  # PROGRAMUOTOJAS
print('--------')

# printinam po 1 vidinį pilną listą
for darbuotojas in darbuotojai:
    print(darbuotojas)  # ['Valdas', 'programuotojas', 2000], ['Adomas', 'direktorius', 3000],...
print('--------')
# printinam atskirus elementus iš kiekvieno vidinio listo
# imdami per indeksą
for darbuotojas in darbuotojai:
    print(darbuotojas[0], darbuotojas[2])  # Valdas programuotojas Adomas 3000 Aldona 1800 ..
print('--------')
# python priimta yra išardyti listus for eilutėje
for vardas, pareigos, atlyginimas in darbuotojai:# cia svarbu teisingai sudeti pavadinimus
    # o printinant nesvarbu jau eiliskumas
    print(atlyginimas, vardas, pareigos)  # Valdas 2000 programuotojas, ..
print('--------')
# susumuojam atlyginimus
# variantas 1
suma = 0
for vardas, pareigos, atlyginimas in darbuotojai:
    suma += atlyginimas

print(suma)  # 9300

# variantas 2
atlyginimai = []  # tuščias listas, sukaupti visiems atlyginimams
for vardas, pareigos, atlyginimas in darbuotojai:
    atlyginimai.append(atlyginimas)

print(atlyginimai)  # [2000, 3000, 1800, 2500]
print(sum(atlyginimai))  # 9300
print('--------')
# suskaičiuojam programuotojus
pozicijos = []
for vardas, pareigos, atlyginimas in darbuotojai:
    pozicijos.append(pareigos)

print(pozicijos)  # ['programuotojas', 'direktorius', 'vadybininkas', 'programuotojas']
print("Programuotojų skaičius yra", pozicijos.count("programuotojas"))  # Programuotojų skaičius yra 2