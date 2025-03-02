# 3. print funkcija su parametrais
# Užduotis: Sukurkite programą, kuri:
# • Išspausdintų sąrašą žodžių (['Obuolys', 'Kriaušė', 'Bananas',
# 'Vyšnia']), atskirdama juos simboliu „|“.
# • Naudojant print, suformuotų tokį rezultatą vienoje eilutėje: „1) Obuolys, 2)
# Kriaušė, 3) Bananas, 4) Vyšnia“.
# • Panaudotų end parametrą, kad išspausdintų kelias eilutes vienoje konsolės
# eilutėje.

print('Obuolys', 'Kriause', 'Bananas', 'Vysnia', sep="|")

zodziai = ['Obuolys', 'Kriause', 'Bananas', 'Vysnia']
indeksas = 1
for zodis in zodziai:
    if zodis != zodziai [-1]: # Tikriname, ar tai ne paskutinis žodis
        print(f'{indeksas}) {zodis}', end=', ')
        indeksas +=1 # Didiname indeksą
    else:
        print(f'{indeksas}) {zodis}')# Paskutinį žodį spausdiname be kablelio

print ('Pirma eilute', end="|" )
print ('Antra eilute', end="|" )
print ('Trecia eilute')

# 4. type funkcija ir tipų patikra
# Užduotis: Sukurkite programą, kuri:
# • Priimtų sąrašą įvairių tipų duomenų, pvz., [123, 'Labas', True, 45.6, None].
# • Naudodama type, patikrintų kiekvieno elemento tipą ir atliktų šiuos veiksmus:
# o Jei tai sveikasis skaičius (int), padaugintų jį iš 10.
# o Jei tai eilutė (str), išspausdintų didžiosiomis raidėmis.
# o Jei tai bool, atspausdintų „True arba False aptikta“.
# o Jei tai float, apvalintų iki dviejų skaičių po kablelio.
# • Išspausdintų visus apdorotus rezultatus.

list = [123, 'Labas', True, 45.61231, None]
for elem in list:
    if type(elem) is int:
        print(elem * 10)  # ABC
    elif type(elem) is str:
        print(elem.upper())
    elif type(elem) == bool and elem == True:
        print('„True arba False aptikta')
    elif type(elem) is float:
        res = round(elem, 2)
        print(res)

