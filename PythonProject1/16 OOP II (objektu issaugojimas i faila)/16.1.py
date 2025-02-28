# 2. Paveldėjimas (Inheritance)
# Užduotis:
# Sukurkite bazinę klasę Gyvunas, kuri turi atributus vardas ir amzius.
# Pridėkite metodą judeti(), kuris spausdina, kad gyvūnas juda.
# Sukurkite dvi paveldinčias klases: Kate ir Suo.
# Kate klasėje pridėkite metodą miaukseti(), kuris sako "Vardas sako MIAU!"
# Suo klasėje pridėkite metodą lot(), kuris sako "Vardas sako AU AU!"
# Papildoma užduotis:
# Sukurkite Kate ir Suo objektus, iškvieskite jų metodus ir patikrinkite, ar paveldėjimas
# veikia.

class Gyvunas:
    def __init__(self,vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius
    def judeti(self):
        print(f'{self.vardas} juda!!!')
class Kate(Gyvunas):
    def miaukseti(self):
        print(f'{self.vardas} sako Miau!!!')
class Suo(Gyvunas):
    def lot(self):
        print(f'{self.vardas} sako AU AU!!!')
kate = Kate('Murkis', 10)
kate.judeti()
kate.miaukseti()
suo = Suo('Rikis', 9)
suo.lot()
suo.judeti()

