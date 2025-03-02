# range funkcija
# Užduotis: Sukurkite programą, kuri:
# • Atspausdintų visus lyginius skaičius nuo 1 iki 20 naudojant range.
# • Atliktų šių skaičių kvadratų sumą ir ją išspausdintų.
# • Panaudotų range, kad sukurtų skaičių seką nuo 10 iki 1 (atvirkštine tvarka) ir juos
# atspausdintų.

#1
lyginiai_skaiciai = list(range(2, 21, 2)) #range(2, 21, 2): Sugeneruoja skaičius nuo 2 iki 20, kas 2 žingsnį.
print(lyginiai_skaiciai)
#2
skaiciu_suma = 0
for skaicius in lyginiai_skaiciai:
    skaiciu_suma += skaicius ** 2
print(f'Lyginiu skaiciu kvadratu suma: {skaiciu_suma}')

# arba
suma = sum(skaiciai ** 2 for skaiciai in range(2,21,2))
print(f'Suma:{suma}')

print(f'skaiciu seka nuo 10 iki 1 (atvirkstine tvarka):')
atvirkstine_seka = list(range(10, 0, -1))
print(atvirkstine_seka)