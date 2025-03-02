# round ir sorted funkcijos
# Užduotis: Sukurkite programą, kuri:
# • Duotų sąrašą skaičių, pvz., [1.234, 3.14159, 2.71828, 0.57721], ir apvalintų
# kiekvieną iki 3 skaitmenų po kablelio.
# • Rikiuotų sąrašą su lietuviškais žodžiais, pvz., ["Žalgiris", "Ąžuolas",
# "Lietuva", "Vilnius"], tinkama abėcėlės tvarka.
# • Išrikiuotų skaičių sąrašą [10, 3, 7, 1, 15] mažėjimo tvarka ir jį atspausdintų.

precision_digits = 3
list = [1.234, 3.14159, 2.71828, 0.57721]
for sk in list:
    sk = round(sk, precision_digits)
    print(sk)


listas = ["Žalgiris", "Ąžuolas", "Lietuva", "Vilnius"]
import locale
locale.setlocale(locale.LC_ALL, 'lt_LT')
list_lt = ["Žalgiris", "Ąžuolas", "Lietuva", "Vilnius"]
res = sorted(list_lt, key=locale.strxfrm)
print(res)

skaiciai = [10, 3, 7, 1, 15]
res = sorted(skaiciai, reverse = True) # Grąžins [15, 10, 7, 3, 1]
print(res)