# 4. @staticmethod Dekoratorius
# Užduotis:
# Sukurkite klasę Matematika, kuri turi statinius metodus:
# • sudeti(a, b) – grąžina dviejų skaičių sumą.
# • atimti(a, b) – grąžina dviejų skaičių skirtumą.
# • dauginti(a, b) – grąžina sandaugą.
# • dalinti(a, b) – grąžina dalmenį, bet įsitikinkite, kad nedalinama iš nulio.
# Papildoma užduotis:
# Pridėkite statinį metodą ar_lyginis(skaicius), kuris patikrina, ar skaičius yra lyginis.

class Matematika:
    @staticmethod
    def sudeti(a, b):
        return a + b
    @staticmethod
    def atimti(a, b):
        return a - b
    @staticmethod
    def dauginti(a, b):
        return a * b
    @staticmethod
    def dalinti(a, b):
        if b == 0:
            return f'Klaida: dalinti is nulio negalima'
        return a / b

    @staticmethod
    def ar_lyginis(skaicius):
        return skaicius % 2 == 0

print(Matematika.sudeti(5, 3))
print(Matematika.atimti(10, 4))
print(Matematika.dauginti(2, 7))
print(Matematika.dalinti(8, 2))
print(Matematika.dalinti(5, 0))
print(Matematika.ar_lyginis(6))
print(Matematika.ar_lyginis(7))

# 5. @classmethod Dekoratorius
# Užduotis:
# Sukurkite klasę Automobilis, kuri turi atributus marke, modelis, metai.
# • Pridėkite klasės metodą sukurti_is_string(), kuris sukuria objektą iš teksto
# eilutės, pvz.: "Toyota Corolla 2020".
# Papildoma užduotis:
# Pridėkite klasės metodą naujausias_modelis(), kuris grąžina naujausią automobilį iš
# pateikto automobilių sąrašo.

class Automobilis:
    def __init__(self, marke, modelis, metai):
        self.marke = marke
        self.modelis = modelis
        self.metai = int(metai)


    @classmethod
    def sukurk_is_string(cls, eilute):
        marke, modelis, metai = eilute.split()
        return cls(marke, modelis, metai)


    @classmethod
    def naujausias_modelis(cls, automobiliu_sarasas):
        return max(automobiliu_sarasas, key=lambda auto: auto.metai)

    def __str__(self):
        return f'{self.marke} {self.modelis} {self.metai}'
auto1 = Automobilis('Toyota', 'Corola', 2020)
auto2 = Automobilis.sukurk_is_string('Honda Civic 2018')
auto3 = Automobilis.sukurk_is_string('Ford Focus 2022')
auto4 = Automobilis.sukurk_is_string('BMW X5 2023')


print(auto1)
print(auto2)
print(auto3)
print(auto4)

naujausias = Automobilis.naujausias_modelis([auto1, auto2, auto3, auto4])
print(f'Naujausias automobilis: {naujausias}')