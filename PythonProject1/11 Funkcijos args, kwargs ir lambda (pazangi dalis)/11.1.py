# *args naudojimas funkcijose
# Užduotis 2:
# Parašykite funkciją sudeti_skaicius(), kuri priimtų neribotą kiekį skaičių kaip
# argumentus ir grąžintų jų sumą.
# 1. Iškvieskite funkciją su (5, 10, 15).
# 2. Iškvieskite funkciją su (100, 200, 300, 400).

def sudeti_skaicius(*skaiciai):
    return sum(skaiciai)

res1 = sudeti_skaicius (5, 10, 15)
print(res1)
res2 = sudeti_skaicius(100, 200, 300, 400)
print(res2)

# Funkcija su daugybe vardų
# Užduotis 3:
# Parašykite funkciją sveikinti_vardus(*args), kuri priimtų kelis vardus ir grąžintų žinutę
# su pasisveikinimu kiekvienam vardui.
# Pvz.: sveikinti_vardus("Jonas", "Asta", "Mantas")

def sveikinti_vardus(*args):
    res = ''
    for i in args:
        res += f'Labas, {i}!\n'
    return res
print(sveikinti_vardus("Jonas", "Asta", "Mantas"))

# Argumentų derinimas su *args
# Užduotis 4:
# Parašykite funkciją pakelti_laipsniu(n, *args), kuri priimtų
# pagrindinį skaičių n- laipsni ir keletą kitų skaičių, kuriuos reikia pakelti n
# laipsniu.


def pakelti_laipsniu(n, *args):
    """
    Pakelia kiekvieną iš pateiktų skaičių n laipsniu.

    :param n: Laipsnis, kuriuo reikia pakelti skaičius.
    :param args: Skaičiai, kuriuos reikia pakelti laipsniu.
    :return: Sąrašas su pakeltais skaičiais.
    """
    return [x ** n for x in args]

rezultatai = pakelti_laipsniu(2, 3, 4, 5)
print(rezultatai)