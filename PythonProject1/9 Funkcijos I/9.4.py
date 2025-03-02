# Loginiai jungikliai funkcijose
# Užduotis 5:
# Sukurkite funkciją skaiciuoti_sumos_tipą(x, y, tik_teigiama=False), kuri
# priimtų du skaičius ir grąžintų jų sumą.
# • Jei tik_teigiama=True, funkcija grąžintų tik teigiamą sumą (jei suma neigiama,
# grąžintų 0).

def skaiciuoti_sumos_tipa(x: int, y: int, tik_teigiama=False) -> int:
    suma = x + y
    if tik_teigiama:
        return max(suma, 0)
    return suma

print(skaiciuoti_sumos_tipa(5, 3))   # 5 + 3 = 8
print(skaiciuoti_sumos_tipa(5, -30, True))  # 5 + (-30) = -25, bet kadangi tik_teigiama=True, grąžinama 0



# Docstringai funkcijose
# Užduotis 6:
# Sukurkite funkciją apskaiciuok_vidurki(skaiciai), kuri apskaičiuotų ir grąžintų
# sąrašo skaičių vidurkį. Pridėkite docstring su informacija apie:
# • Funkcijos paskirtį.
# • Argumentus (sąrašas skaičių).
# • Grąžinamą reikšmę (vidurkis).

def apskaiciuok_vidurki(skaiciai):
    """
    Apskaičiuoja ir grąžina sąrašo skaičių vidurkį.

    Argumentai:
    skaiciai (list): Sąrašas skaičių.

    Grąžinama reikšmė:
    float: Skaičių vidurkis.
    """
    if not skaiciai:
        return 0  # Jei sąrašas tuščias, grąžiname 0
    return sum(skaiciai) / len(skaiciai)

print(apskaiciuok_vidurki([1, 2, 3, 4, 5]))


# Type hints ir anotacijos
# Užduotis 7:
# Sukurkite funkciją prideti_zodi(tekstas: str, zodis: str) -> str, kuri priimtų
# sakinį ir pridedamą žodį, o tada grąžintų sakinį su tuo žodžiu gale.

def prideti_zodi(tekstas: str, zodis: str) -> str:
    """
    Prideda žodį prie sakinio galo.

    Argumentai:
    tekstas (str): Pradinis sakinys.
    zodis (str): Žodis, kurį reikia pridėti.

    Grąžinama reikšmė:
    str: Atnaujintas sakinys su pridėtu žodžiu gale.
    """
    return tekstas + " " + zodis

print(prideti_zodi("Labas, pasauli!", "kaip sekasi?"))