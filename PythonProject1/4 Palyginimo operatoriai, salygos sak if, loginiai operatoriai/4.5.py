# 5. Sutrumpintas if sakinys
# 1. Parašykite programą, kuri leidžia vartotojui įvesti skaičių ir nustato, ar skaičius yra
# teigiamas ar neigiamas, naudodama vieną eilutę.
# 2. Sukurkite programą, kuri tikrina vartotojo įvestą simbolių eilutę. Jei eilutė prasideda
# didžiąja raide, spausdina „Didžioji raidė“, kitu atveju – „Mažoji raidė“.

# 1.
# 3 lines
# number = float(input('Ivesti skaiciu:'))
# result = 'teigiamas' if number > 0 else 'neigiamas'
# print(result)

# 1 line
# #            2                           1                            3
# print('Teigiamas' if float(input('Ivesti skaiciu:')) > 0 else 'neigiamas')

print('Teigiamas' if (number := float(input('Įveskite skaičių: '))) > 0 else 'Neigiamas' if number != 0 else 'Nulis')


# 2.
simboliai = 'dbcd'
result = ''
if simboliai.istitle():
    result = 'Didzioji raide'
else:
    print('Mazoji raide')
print(result)