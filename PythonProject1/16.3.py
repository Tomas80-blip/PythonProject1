# 4. Konstruktoriaus Perrašymas
# Užduotis:
# Sukurkite tėvinę klasę Asmuo, kuri turi atributus vardas ir amzius.
# • Sukurkite konstruktorių, kuris nustato šiuos atributus.
# Sukurkite paveldinčią klasę Darbuotojas, kuri paveldi Asmuo ir prideda papildomą
# atributą pareigos.
# • Perrašykite konstruktorių naudodami super(), kad pridėtumėte pareigos.
# Papildoma užduotis:
# Sukurkite Darbuotojas objektą ir atspausdinkite visą informaciją apie jį.

class Asmuo:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

class Darbuotojas(Asmuo):
    def __init__(self, vardas, amzius, pareigos):
        super().__init__(vardas, amzius)
        self.pareigos = pareigos

    def __str__(self):
        return f"Vardas: {self.vardas}, Amžius: {self.amzius}, Pareigos: {self.pareigos}"

darbuotojas = Darbuotojas('Jonas', 30, 'Mokytojas')
print(darbuotojas)



# 5. Kitų Metodų Perrašymas (Overriding)
# Užduotis:
# Sukurkite klasę TransportoPriemone su metodu judeti(), kuris spausdina „Transporto
# priemonė juda“.
# Sukurkite paveldinčią klasę Dviratis, kuri perrašo judeti() metodą, kad spausdintų
# „Dviratis važiuoja pedalais“.
# Papildoma užduotis:
# Sukurkite TransportoPriemone ir Dviratis objektus bei patikrinkite jų judeti()
# metodų veikimą.

class TransportoPriemone:
    def judeti(self):
        print("Transporto priemonė juda")

class Dviratis(TransportoPriemone):
    def judeti(self):
        super().judeti()
        print("Dviratis važiuoja pedalais")


transporto_priemone = TransportoPriemone()
dviratis = Dviratis()

transporto_priemone.judeti()
dviratis.judeti()