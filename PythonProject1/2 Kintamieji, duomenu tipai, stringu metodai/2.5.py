# Stringų Metodai
# Metodai tai yra funkcijos priklausančios tik tam tikriems duomenų tipams. Stringų metodai leidžia atlikti
# įvairias operacijas su tekstais. Kviečiant str metodus naudojamas . - taško operatorius.

#  Konvertavimas i didziasias raides:
# upper() metodas konvertuoja visas str raides i didziasias raides.
text = 'hello world'
print('text - ' + text)


text2 = text.upper()
print('text2 - ' + text2)
print('-----')

# Konvertavimas i mazasias raides
# lower() metodas konvertuoja str i mazasias raides
text2 = 'Hello World'
print(text2.lower())
user = 'Darius'
imported_user = 'DArius'
print(user.lower())
print(imported_user.lower())
print('-------')

# Simbolių Pasikartojimų Skaičiavimas:
# count() metodas (pasikartojimu skaiciavimas)
print(text.count('l'))
print(text.count('ll'))
print('------')

# Indekso Paieška su index():
# index() metodas (metodas grąžina pirmojo nurodyto simbolio ar simbolių sekos atsiradimo indeksą stringe
print(text.index('r'))
print(text.index('l'))
print(text.index('world'))
# print(text.index('abracadabra')) # programa nulus jei taip naudosime
# todel geriau naudoti find metoda
print('---------')

# Indekso Paieška su .find():
# find() metodas panašus į index(), tačiau, jei simbolis ar simbolių seka nerandama,
# grąžina -1 vietoj klaidos.
print(text.find('r'))
print(text.find('l'))
print(text.find('world'))
print(text.find('abracadabra')) # su find- neluzta programa
print('-------')

# Simbolių Keitimas:
# replace() metodas leidžia pakeisti nurodytus simbolius ar simbolių sekas kitais.
text2 = text.replace('l', 'w')
text3 = text.replace('hello', 'how are you')
print(text2)
print(text3)
print('-------')


# Tarpų Pašalinimas:
# strip() metodas pašalina tarpus ar kitus nurodytus simbolius iš stringo pradžios
# ir pabaigos, neliečiant vidurio.
user = '   Darius Daskevicius        '
user2 = 'Darius Daskevicius'

print(user.strip())
user = user.strip()
print(user)
print(user == user2)
print('-------')