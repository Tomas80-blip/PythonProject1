# If
# 1. Parašykite programą, kuri tikrina vartotojo įvestą amžių:
# a. Jei amžius mažesnis nei 18, spausdina „Nepilnametis“.
# b. Jei amžius didesnis arba lygus 18, spausdina „Pilnametis“.


age = int(input('Amzius: '))
if age < 18:
    print('Nepilnametis')
else:
    print('Pilnametis')
if age >= 18:
    print('Pilnametis')

# 2. Sukurkite programą, kuri leidžia vartotojui įvesti temperatūrą ir patikrina:
# a. Jei temperatūra mažesnė už 0, spausdina „Šalta“.
# b. Jei temperatūra tarp 0 ir 20, spausdina „Vidutiniška“.
# c. Jei temperatūra viršija 20, spausdina „Šilta“.


temp = int(input('Iveskite temperatura:'))
if temp < 0:
    print('Salta')
if 0 <= temp <= 20:
    print('Vidutiniska')
if temp > 20:
    print('Silta')