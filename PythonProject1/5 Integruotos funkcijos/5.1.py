# 1. Python integruotos funkcijos: Pagrindai
# Užduotis: Sukurkite programą, kuri:
# • Paprašytų vartotojo įvesti savo vardą ir amžių naudojant input.
# • Išspausdintų sveikinimo žinutę, pvz., „Sveikas, Jonas! Tau 25 metai.“
# • Paskaičiuotų, kiek simbolių sudaro vartotojo vardas, ir išspausdintų šią informaciją.
# • Patikrinkite, ar amžius didesnis nei 18, ir atitinkamai spausdinkite „Pilnametis“ arba
# „Nepilnametis“.

vardas = str(input('Iveskite varda:'))
amzius = float(input('Iveskite amziu:'))
print(f'Sveikas {vardas}! Tau {amzius} metai')
print(f'vartotojo varda sudaro {len(vardas)} simboliai')
if amzius > 18:
    print ('Pilnametis')
else:
    print('Nepilnametis')