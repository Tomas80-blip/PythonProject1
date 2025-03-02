# f-string
# F-stringai: F-stringai Pythone yra specialia sintakse sudaromi str tipo tekstiniai duomenys, ši priemonė
# leidžia formatuoti tekstą lengvai ir patogiai. Duomenys prijungiami naudojant {} kaip žymę kintamiesiems.

month = "sausis"
day = 31
ftext = f"Mėnesis yra {month}, diena {day}d."
print(ftext)  # Mėnesis yra sausis, diena 31d.
ftext = f"Mėnesis yra {month}, diena {day - 1}d."
print(ftext)  # Mėnesis yra sausis, diena 30d.

# Šis konspektas padės suprasti pagrindines Python operacijas su skaičiais ir tekstu bei jų naudojimo būdus.



month = 'sausis'
day = 14
#  jei darome dideli stringa per daug eiluciu, turime ideti tris kabutes
ftext = f'''Mėnesis yra {
month
}, diena {round(day / 3)}d.
'''
print(ftext)

name = 'John'
surname = 'Doe'
print(f'Hello {name} {surname}!')
#jei atidarom f stringa su dvigubom kabutem, tai viduje naudoja viengubas kabutes arba
# jei atidarom f stringa su viengubom kabutem, tai viduje naudojam dviguba kabutes
# negalima naudoti vienodu kabuciu f stringe
# print(f"Hello, {input('Name: ')} {input('Surname: ')}!")


mass = float(input('Mass (kg): '))
height = float(input('Height (cm): '))
res = mass / ((height / 100) ** 2)
# print(f'BMI is: {res}')
# arba
print(f"Your BMI: {float(input('Mass (kg): ')) / ((float(input('Height (cm): ')) / 100) ** 2)}")
