# else blokas cikluose
# Užduotis 9:
# Sukurkite programą, kuri:
# 1. Naudodama for ciklą ieško pirmo lyginio skaičiaus sąraše [1, 3, 5, 7, 8, 10,
# 11].
# 2. Kai suranda lyginį skaičių, išspausdina jį ir nutraukia ciklą.
# 3. Jei ciklas baigiasi neradęs lyginio skaičiaus, išspausdina „Lyginių skaičių nėra“.

list = [1, 3, 5, 7, 8, 10, 11]

for skaicius in list:
    if skaicius % 2 == 0:
        print("Skaičius", skaicius, "yra lyginis")
        break
else:
    print("Lyginiu skaiciu nera")