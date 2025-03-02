# Sąlygos programoje
# 1. Parašykite programą, kuri leidžia vartotojui įvesti du skaičius ir patikrina, kuris iš jų
# yra didesnis.
# 2. Sukurkite sąlygą, kuri patikrina, ar įvestas skaičius yra lyginis ar nelyginis,
# naudodami operatorių %.
# 3. Sukurkite sąrašą ir naudodami in operatorių patikrinkite, ar vartotojo įvestas žodis
# yra šiame sąraše.

# 2.1
sk1 = 100
sk2 = 300
print (sk1 > sk2)

# 2.2
skaicius = int(input('Iveskite skaiciu:'))
print(skaicius % 2 == 0)

# 2.3
text = 'tris'
sarasas = [ 'vienas', 'du', 'tris', 'keturi']
print(text in sarasas)
