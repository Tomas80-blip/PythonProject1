# 1. Apsaugoti Atributai (Protected Attributes)
# Užduotis:
# Sukurkite klasę Studentas, kuri turi atributus vardas, pavarde ir apsaugotą atributą
# _pazymiai.
# • Pridėkite metodą prideti_pazymi(), kuris leidžia pridėti pažymį, jei jis yra tarp 1 ir
# 10.
# • Sukurkite metodą rodyti_vidurki(), kuris apskaičiuoja pažymių vidurkį.
# Papildoma užduotis:
# Paveldėkite klasę Studentas ir sukurkite klasę StudentasLyderis, kuri papildomai gali
# pridėti „bonus“ taškų prie vidurkio.

class Studentas:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde
        self._pazymiai = [] #tuscias sarasas

    def prideti_pazymi(self, pazymys):
        if 1 <= pazymys <= 10:
            self._pazymiai.append(pazymys)
        else:
            print('Klaida: Pažymys turi būti tarp 1 ir 10.')

    def rodyti_vidurki(self):
        if not self._pazymiai:
            return 0
        return sum(self._pazymiai) / len(self._pazymiai)


class StudentasLyderis(Studentas):
    def __init__(self, vardas, pavarde, bonus=0):
        super().__init__(vardas, pavarde)
        self.bonus = bonus


    def rodyti_vidurki(self):
        vidurkis = super().rodyti_vidurki() #rodo vidurkį.
        return vidurkis + self.bonus # vidurkis + bonusas

print('--------------')
studentas1 = Studentas('Jonas', 'Cvirka')
studentas1.prideti_pazymi(8)
studentas1.prideti_pazymi(9)
studentas1.prideti_pazymi(7)
print(f"{studentas1.vardas} vidurkis: {studentas1.rodyti_vidurki()}")


lyderis = StudentasLyderis('Petras', 'Petrauskas', bonus=0.5)
lyderis.prideti_pazymi(8)
lyderis.prideti_pazymi(9)
lyderis.prideti_pazymi(7)
print(f"{lyderis.vardas} (lyderis) vidurkis su bonusu: {lyderis.rodyti_vidurki()}")


# 2. Privatūs Atributai (Private Attributes)
# Užduotis:
# Sukurkite klasę BankoSaskaita, kuri turi atributus savininkas ir privatų atributą
# __balansas.
# • Sukurkite metodus gauti_balansa() ir prideti_pinigus(), kad būtų galima
# saugiai valdyti balansą.
# • Įsitikinkite, kad negalima tiesiogiai pasiekti __balansas atributo iš išorės.
# Papildoma užduotis:
# Pridėkite metodą nuskaičiuoti_pinigus(), kuris leis nuskaičiuoti pinigus tik tada, jei
# sąskaitoje pakanka lėšų.

print('--------------')

class BankoSaskaita:
    def __init__(self, savininkas):
        self.savininkas = savininkas
        self.__balansas = 0

    # __balansas yra privatus atributas, todel jį pasiektiam per sia f..
    def gauti_balansa(self):
        return self.__balansas

    def prideti_pinigus(self, suma):
        if suma > 0:
            self.__balansas += suma
            print(f'Į sąskaitą pridėti {suma}€. Naujas balansas: {self.__balansas}€')
        else:
            print("Suma turi būti didesnė už nulį.")

    def nuskaičiuoti_pinigus(self, suma):
        if suma > 0:
            if self.__balansas >= suma:
                self.__balansas -= suma
                print(f"Iš sąskaitos nuskaičiuota {suma}€. Naujas balansas: {self.__balansas}€")
            else:
                print("Nepakanka lėšų operacijai atlikti.")
        else:
            print("Suma turi būti didesnė už nulį.")

saskaita = BankoSaskaita("Jonas")
print(f"Sąskaitos savininkas: {saskaita.savininkas}")
print(f"Pradinis balansas: {saskaita.gauti_balansa()}€")

saskaita.prideti_pinigus(50)
saskaita.nuskaičiuoti_pinigus(30)
saskaita.nuskaičiuoti_pinigus(150)