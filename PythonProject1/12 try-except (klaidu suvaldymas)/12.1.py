# Užduotis 2:
# 1. Sukurkite funkciją dalinti(a, b), kuri dalina a iš b.
# 2. Jei b == 0, funkcija turėtų sugauti ZeroDivisionError ir grąžinti "Dalyba iš
# nulio negalima.".
# 3. Išbandykite funkciją su reikšmėmis (10, 2), (5, 0), (8, 4).

def dalinti(a: (int, float), b: (int, float)) -> float:
    try:
        return  a / b
    except Exception as e:# Exception- parodo visu rusiu erorus
        print(e.__class__)  # išspausdina klaidos klasę
        return "Dalyba iš nulio negalima."


# su lambda, nepagavus klaidos (be exepto)
# dalinti = lambda a, b: a / b

print(dalinti(10, 2))
print(dalinti(5, 0))
print(dalinti(8, 4))