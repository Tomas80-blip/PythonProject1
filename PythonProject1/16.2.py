# 3. Komponavimas (Composition)
# Užduotis:
# Sukurkite klasę Variklis, kuri turi atributą galia ir metodą startuoti(), kuris
# spausdina "Variklis veikia su galia: X arklio galių".
# Tada sukurkite klasę Automobilis, kuri turi atributus marke ir modelis, bei naudoja
# Variklis kaip savo atributą.
# • Pridėkite metodą vaziuoti(), kuris iškviečia startuoti() metodą.
# Papildoma užduotis:
# Sukurkite kelis Automobilis objektus su skirtingais varikliais ir priverskite juos važiuoti.


class Variklis:
    def __init__(self, galia):
        self.galia = galia

    def startuoti(self):
        print(f'Variklis veikia su galia: {self.galia} arklio galių')


class Automobilis(Variklis):
    def __init__(self, marke, modelis, galia):
        self.marke = marke
        self.modelis = modelis
        self.variklis = Variklis(galia)

    def vaziuoti(self):
        print(f"{self.marke} {self.modelis} pradeda važiuoti.")
        self.variklis.startuoti()


masina1 = Automobilis('BMW', 'M3', 450)
masina1.vaziuoti()