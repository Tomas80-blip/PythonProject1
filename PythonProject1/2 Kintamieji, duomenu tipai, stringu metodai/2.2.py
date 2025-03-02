# 1 uzduotis BMI skaičiavimas su pateiktais duomenimis

# 1. Jums pateikti žmogaus svorio ir ūgio duomenys.
# 2. Naudodami formulę BMI= svoris (kg) / (ūgis (cm) / 100)2, apskaičiuokite
# kiekvieno žmogaus BMI.
# 3. Pagal žemiau pateiktas BMI vertes, nustatykite zoną:
# a. Mažiau nei 18.5: Nepakankamas svoris
# b. 18.5–24.9: Normalus svoris
# c. 25.0–29.9: Antsvoris
# d. 30.0 ir daugiau: Nutukimas


# Žmogus          Svoris (kg)              Ūgis (m)
#
# Jonas               65                       1.75
#
# Ona                  50                      1.60
#
# Tomas                85                      1.80
#
# Rasa                 95                      1.68
#

# 1. Sukurkite Python kodą, kuris apskaičiuoja kiekvieno žmogaus BMI.
# 2. Parašykite rezultatą pagal pateiktas zonas.


# BMI
user_input0 = str(input("Žmogus: "))
user_input1 = int(input("Svoris:  "))
user_input2 = float(input("Ugis: "))
print ( user_input1 / (user_input2/ 100) ** 2)
print(f"Your BMI: {float(input('Svoris (kg): ')) / ((float(input('Ugis (cm): ')) / 100) ** 2)}")

# mase = float(input('Mase (kg): '))
# ugis = float(input('Ugis (cm): '))
# res = 'Jusu BMI: ' + str(mase / ((ugis / 100) ** 2))
# print(res)
#
# print(f'Your BMI: {(mase / ((ugis / 100) ** 2))}')
print('----------------')

# 2 uzduotis Kelionės kuro sąnaudų skaičiavimas

# 1. Jums pateikti automobilio kuro sąnaudų ir kelionės duomenys.
# 2. Naudodami formulę Kuro_sunaudojimas=(Atstumas (km) × Kuro sąnaudos
# (l/100 km)) ÷ 100, apskaičiuokite, kiek kuro reikės kiekvienai
# kelionei.
# 3. Taip pat apskaičiuokite kuro kainą, jei 1 litro kuro kaina yra
# 1.50 €.

# Automobilis          Atstumas (km)         Kuro sąnaudos (l/100 km)
# Toyota                   200                            6.5
# BMW                      350                            8.0
# Honda                    120                            5.0
# Audi                     500                            7.2
#

# 1. Sukurkite Python kodą, kuris apskaičiuoja, kiek kuro reikės
# kiekvienai kelionei.
# 2. Apskaičiuokite, kiek kainuos kuras kiekvienai kelionei.
# 3. Išveskite rezultatus ekrane.


user_input0 = str(input('Automobilis: '))
user_input1 = int(input('Atstumas (km):  '))
user_input2 = float(input('Kuro sanaudos (l/100km): '))
res = float(user_input1 * user_input2)/100
print (f'Automobiliui {user_input0} kuro reikes: {res}')
print(f'Automobiliui {user_input0} kuras kainuos: {res * 1.50}')