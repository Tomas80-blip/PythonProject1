# 3. @property Dekoratorius
# Užduotis:
# Sukurkite klasę Darbuotojas, kuri turi atributus vardas, pavarde ir privatų atributą
# __atlyginimas.
# • Naudokite @property dekoratorių, kad galėtumėte gauti ir nustatyti atlyginimą.
# • Užtikrinkite, kad atlyginimas negali būti mažesnis nei minimalus (pvz., 500).
# Papildoma užduotis:
# Pridėkite papildomą @property metodą mokesciai, kuris apskaičiuoja mokesčius (pvz.,
# 20% nuo atlyginimo).

class Darbuotojas:
    def __init__(self, vardas, pavarde, atlyginimas=500):
        self.vardas = vardas
        self.pavarde = pavarde
        self.__atlyginimas = max(atlyginimas, 500)  # Užtikriname minimalų atlyginimą

    @property
    def atlyginimas(self):
        return self.__atlyginimas

    @atlyginimas.setter
    def atlyginimas(self, naujas_atlyginimas):
        if naujas_atlyginimas >= 500:
            self.__atlyginimas = naujas_atlyginimas
        else:
            raise ValueError("Atlyginimas negali būti mažesnis nei 500!")

    @property
    def mokesciai(self):
        return self.__atlyginimas * 0.2  # Tarkime, kad mokestis yra 20%



darbuotojas = Darbuotojas("Jonas", "Jonaitis", 200)
print(f"Atlyginimas: {darbuotojas.atlyginimas} EUR")
print(f"Mokesčiai: {darbuotojas.mokesciai} EUR")

try:
    darbuotojas.atlyginimas = 400
except ValueError as e:
    print(e)