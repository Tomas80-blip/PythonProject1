# Python - programavimo kalba, dažnai naudojama kurti svetainėms(backendui), bendro pobūdžio programinei įrangai,
# užduotims automatizuoti ir duomenų analizei atlikti. Python yra bendrosios paskirties kalba, t. y. su ja galima
# kurti įvairias programas ir ji nėra specializuota kokiems nors konkretiems uždaviniams spręsti.

# ⬇️ Atsisiųsti Python
# https://www.python.org/downloads/release/python-31011/
#
# ❗ Šiame kurse bus naudojama 3.10 "Phyton" versija.
# During installation, check "Add Python to PATH" before clicking Install.
#
# ⬇️ Atsisiųsti PyCharm Community edition
# https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windowsARM64&code=PCC
#
# Šiame kurse naudosime PyCharm - integruotą programų kūrimo aplinką (IDE - Integrated development environment).
#
# Ką reikia padaryti:
#
# Įsidiekite Python ir PyCharm Community edition IDE.


# 💻 Pirmoji programa
# Tradiciškai pirmoji programa, kurią rašo kiekvienas programuotojas, yra Hello, World programa,
# kur išspausdina terminale šią frazę. Padarykime tą patį:

print("Hello, World")

# Sveikiname, dabar jūs _kalbate _Python kalba! Pradėkime:

print('----------------')
# 1 užduotis: Paprasti skaičiavimai
#   Naudodami Python operatorius, atlikite šiuos skaičiavimus:
# 1. Sudėkite skaičius 15 ir 27.
print(15 + 27)
# 2. Iš 50 atimkite 23.
print(50 - 23)
# 3. Padauginkite 12 iš 8.
print(12 * 8)
# 4. Padalinkite 144 iš 12.
print(144 / 12)
# 5. Apskaičiuokite skaičiaus 100 dalybos iš 9 liekaną.
print(100 % 9)


print('----------------')
# 2 užduotis: Padalijimas iš apačios
#   Naudodami operatorių //, apskaičiuokite:
# 1. Kiek kartų skaičius 25 telpa į 8.
print(8 // 25)
# 2. Kiek kartų skaičius 97 telpa į 10.
print(10 // 97)
# Papildomas klausimas: Kuo rezultatai skiriasi nuo įprasto dalijimo su /?

print('----------')
# 3 užduotis: Eksponentija
# Naudodami operatorių **, atlikite šiuos veiksmus:
# 1. Pakelkite skaičių 3 kvadratu.
print(3 ** 2)
# 2. Apskaičiuokite 2 penktą laipsnį.
print(2 ** 5)
# 3. Pakelkite skaičių 10 nuliu. Ar rezultatas toks, kokio tikėjotės?
print(10 ** 0)

print('-----------')
# 4 užduotis: Problemos sprendimas
# Įsivaizduokite, kad perkate kelis daiktus ir turite apskaičiuoti išlaidas. Naudodami
# operatorius:
# 1. Turite 3 daiktus, kurių kiekvienas kainuoja 15 eurų. Kokia bendra suma?
print(3 * 15)
# 2. Jei turite tik 40 eurų, kiek tokių daiktų galite nusipirkti? (Naudokite // operatorių.)
print(40 // 15)
# 3. Jei lieka pinigų po pirkimo, kiek jų liktų? (Naudokite % operatorių.)
print(40 % 15)

print('---------')
# 5 užduotis: Reikšmių palyginimas
# Pateikite atsakymus į šiuos klausimus naudodami Python operatorius:
# 1. Kas yra didesnis: 45 % 7 ar 6?
print(45 % 7 > 6)
# 2. Ar skaičius 10 + 5 yra didesnis už 15 // 2?
# (Naudokite operatorių >.)
print(10 + 5 > 15 // 2)
# 3. Apskaičiuokite, ar skaičius 20 padalinus iš 5 yra lygus 4.
# (Naudokite operatorių ==.)
print(20 / 5 == 4)

print('-----------')
# 6 užduotis: Išspręskite formulę
# Turite formulę, kurią reikia apskaičiuoti:
# Rezultatas=(20+15)×2−(30//3)+(50%6)
print((20 + 15) * 2 - (30 // 3) + (50 % 6))
# Naudokite Python operatorius, kad apskaičiuotumėte rezultatą.

print('-------')
# 7 užduotis: Sukurkite savo užduotį
# Sukurkite savo skaičiavimo užduotį naudodami Python operatorius. Ji turi būti
# sudėtingesnė nei paprasti aritmetiniai veiksmai (pvz., gali būti keli operatoriai vienoje
# formulėje). Pasidalykite ja su šalia esančiu studentu ir paprašykite, kad jis išspręstų.
print((50 + 3 ** 3) * 4 - (70 % 3) + (60 // 6))

print('----------')
# 8 užduotis: Skaičių santykis
# Naudodami Python operatorius, atlikite šiuos veiksmus:
# 6. Apskaičiuokite santykį tarp skaičių 45 ir 9 (padalinkite).
print(45 / 9)
# 7. Patikrinkite, ar skaičius 15 yra dalijamas iš 3 be liekanos (naudokite % operatorių).
print(15 % 3)
# 8. Koks yra rezultatas, jei dalijant 100 iš 7 paimame tik visą dalybos dalį (naudokite //
# operatorių)?
print(100 // 7)

print('-----------')
# 9 užduotis: Matematinė lygtis
# Turite lygtį:
# x=10+20−(15%4)×2
# Naudodami Python operatorius, apskaičiuokite x reikšmę.
print(10 + 20 - (15 % 4) *2)

print('---------')
# 10 užduotis: Pirkinių krepšelis
# Įsivaizduokite, kad perkate vaisius:
# 3. Obuolys kainuoja 2 eurus, o jūs norite nusipirkti 8 obuolius. Kokia bendra kaina?
print(2 * 8)
# 4. Jei jūsų biudžetas yra 15 eurų, kiek obuolių galite nusipirkti? (Naudokite //
# operatorių.)
print(15 // 2)
# 5. Kiek pinigų liks po pirkimo? (Naudokite % operatorių.)
print(15 % 2)

print('-------------')
# 11 užduotis: Aritmetiniai palyginimai
# Naudodami Python operatorius, atsakykite:
# 4. Ar 50 yra didesnis už 5 ** 2?
print(50 > 5 ** 2)
# 5. Ar rezultatas 15 // 4 yra lygus 20 % 4?
print(15 // 4 == 20 % 4)
# 6. Apskaičiuokite, ar 10 + 5 - 3 yra mažiau už 15 ** 0.
print(10 + 5 - 3 < 15 ** 0)
print(15 ** 0)

print('-------')
# 12 užduotis: Eksponentijos galimybės
# Išbandykite eksponentijos operatorių:
# 4. Pakelkite skaičių 2 į 10 laipsnį.
print(2 ** 10)
# 5. Apskaičiuokite, kokiu laipsniu pakeltas skaičius 3 sudaro 27.
print(3 ** 3)
# 6. Kiekvienam skaičiui nuo 1 iki 5 apskaičiuokite kvadratą.

print('---------')
# 13 užduotis: Duomenų apdorojimas
# Turite skaičius 56, 23, ir 8. Naudodami Python operatorius:
# 4. Sudėkite juos visus.
print(56 + 23 + 8)
# 5. Apskaičiuokite, koks yra liekana, padalijus gautą sumą iš 9.
print(87 % 9)
# 6. Apskaičiuokite, kiek kartų skaičius 8 telpa į pirmąjį skaičių.
print(87 // 8)

print('--------')
# 14 užduotis: Lygybės tikrinimas
# Pateikite atsakymus:
# 1. Patikrinkite, ar 100 % 9 yra lygu 10 ** 1.
print(100 % 9 == 10 ** 1)
# 2. Ar 15 + 10 - 5 yra lygu 20?
print(15 + 10 - 5 == 20)
# 3. Apskaičiuokite, ar (5 + 5) ** 2 yra didesnis už 50.
print((5 + 5) ** 2 > 50)

print('-----------')
# 15 užduotis: Sudėtingesnės operacijos
# Spręskite formulę:
# Rezultatas=((25 //3 + 10 % 4) * (32 - 10) +50
# Naudodami Python, apskaičiuokite galutinį rezultatą.
print((25 //3 + 10 % 4) * (32 - 10) +50)

print('-----------')
# 16 užduotis: Dienų skaičiavimas
# Įsivaizduokite, kad turite 1000 dienų:
# 1. Kiek metų sudaro šias dienas, jei vieni metai turi 365 dienas? (Naudokite //
# operatorių.)
print(1000 // 365)
# 2. Kiek dienų lieka po pilnų metų? (Naudokite % operatorių.)
print(1000 % 365)
# 3. Jei metai turi 12 mėnesių, kiek mėnesių atitinka visas šias dienas?
print(1000 // (365 // 12))

print('------------')
# 17 užduotis: Skaičių serija
# Naudodami Python operatorius, atlikite šiuos veiksmus:
# 1. Sudėkite visus skaičius nuo 1 iki 10 (panaudokite operatorių kelis kartus).
print(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10)

# 2. Apskaičiuokite, koks yra gauto rezultato modulis dalijant iš 5.
print(55 % 5)
# 3. Pakelkite gautą skaičių į kvadratą.
print(0 ** 2)

print('------------')
# 18 užduotis: Studentų grupė
# Turite 53 studentus, kuriuos reikia padalyti į grupes po 5:
# 1. Kiek grupių galite sudaryti?
print(53 // 5)
# 2. Kiek studentų liks be grupės?
print(53 % 5)
# 3. Jei būtų suformuota papildoma grupė tik iš likusių studentų, kiek studentų dar
# trūktų pilnai grupei?
print(5-(53 % 5))

print('-----------')
# 19 užduotis: Įdomi formulė
# Pateikta formulė:
# Rezultatas=(100−25)%7+(50//3)**2
# Naudodami Python operatorius, apskaičiuokite galutinį rezultatą ir paaiškinkite, kaip jis
# buvo gautas.
print((100 - 25) % 7+(50 // 3) ** 2)