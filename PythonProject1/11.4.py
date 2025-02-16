# 11. Įvadas į lambda funkcijas
# Užduotis 11:
# Sukurkite lambda funkciją pakelti_kvadratu, kuri priima vieną skaičių ir grąžina jo
# kvadratą.

pakelti_kvadratu = lambda a: a ** 2
print(pakelti_kvadratu(3))

# 12. Lambda funkcijos ir rūšiavimas
# Užduotis 12:
# Turite sąrašą darbuotojų su vardais ir atlyginimais:
# darbuotojai = [("Jonas", 2500), ("Asta", 3200), ("Mantas", 2100)]
# Naudodami sorted() ir lambda funkciją, surūšiuokite sąrašą pagal atlyginimą nuo
# mažiausio iki didžiausio.

darbuotojai = [("Jonas", 2500), ("Asta", 3200), ("Mantas", 2100)]
res = sorted(darbuotojai, key=lambda listas: listas[1])
print(res)

# sorted() funkcija naudojama surikiuoti sąrašą.
# Rikiavimo kriterijus (key=lambda listas: listas[1]):
# listas[1] reiškia antra tuple elementą (atlyginimą) ir kad sąrašas bus surikiuotas  nuo
# #mažiausio iki didžiausio.


# 13. Lambda funkcija su filter()
# Užduotis 14:
# Turite sąrašą [5, 10, 15, 20, 25, 30]. Naudodami filter() ir lambda funkciją,
# palikite tik skaičius, kurie dalijasi iš 10.

skaiciai = [5, 10, 15, 20, 25, 30]
lyginiai_skaiciai = list(filter(lambda x: x % 10 == 0, skaiciai))
print(lyginiai_skaiciai)

filter(lambda x: x % 10 == 0, skaiciai)

# lambda x: x % 10 == 0 – tai anoniminė (lambda) funkcija, kuri tikrina, ar skaičius
# x dalijasi iš 10 be liekanos (% 10 == 0).
# filter(...) – ši funkcija taiko pateiktą lambda funkciją kiekvienam sąrašo skaiciai
# elementui ir atrenka tik tuos, kurie atitinka sąlygą.