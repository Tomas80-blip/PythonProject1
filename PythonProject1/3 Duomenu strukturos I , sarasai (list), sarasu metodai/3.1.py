# uzduotis 1 Kas yra sąrašas?
# 1. Sukurkite tuščią sąrašą ir patikrinkite jo tipą.
# 2. Į tuščią sąrašą pridėkite šiuos elementus: "sausis", "vasaris", ir skaičių 2024.
# 3. Atspausdinkite sąrašo elementus po kiekvieno pridėjimo.

sarasas = []
print(type(sarasas))
print(sarasas)

sarasas.append('sausis')
print(sarasas)
sarasas.append('vasaris')
print(sarasas)
sarasas.append('2024')
print(sarasas)

# uzduotis 2 Sąrašų metodai
# 1. Sukurkite sąrašą su elementais: "šuo", "katė", "zuikis".
# a. Pridėkite elementą "dramblys" į pabaigą.
# b. Įdėkite elementą "žirafa" į antrąją poziciją.
# 2. Pašalinkite pirmą pasitaikiusį "katė" reikšmę iš sąrašo.
# 3. Naudokite pop() metodą, kad pašalintumėte ir išsaugotumėte paskutinį elementą.
# 4. Naudokite indeksus, kad pakeistumėte pirmąjį sąrašo elementą į "tigrai".

sarasas = []
gyv1 = "suo"
gyv2 = "kate"
gyv3 = "zuikis"
#

sarasas.append(gyv1)
print(sarasas)
sarasas.append(gyv2)
print(sarasas)
sarasas.append(gyv3)
print(sarasas)
sarasas.append('dramblys')
print(sarasas)
sarasas.insert(2, 'zirafa')
print(sarasas)

sarasas.remove('kate')
print(sarasas)
sarasas.pop()
print(sarasas)
sarasas[0] = 'tigrai'
print(sarasas)