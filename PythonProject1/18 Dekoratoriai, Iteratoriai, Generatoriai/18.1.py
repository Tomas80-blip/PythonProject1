# 1. Funkcijos kaip Pirmos Klasės Objektai
# Užduotis:
# Sukurkite šias funkcijas:
# 1. prideti_zenkliuka(tekstas) – prideda žvaigždutę * prie teksto pabaigos.
# 2. apversti_teksta(tekstas) – apverčia pateiktą tekstą.
# 3. Sukurkite funkciją apdoroti_teksta(tekstas, funkcija=None), kuri:
# a. Jei nurodyta funkcija, pritaiko ją tekstui.
# b. Jei funkcija nenurodyta, tiesiog grąžina tekstą mažosiomis raidėmis.
# Papildoma užduotis:
# Sukurkite funkciją keli_apdorojimai(tekstas, *funkcijos), kuri pritaiko kelias
# funkcijas iš eilės tam pačiam tekstui.


def prideti_zenkliuka(tekstas):
 return tekstas + "*"


def apversti_teksta(tekstas):
 return tekstas[::-1]

def apdoroti_teksta(tekstas, funkcija=None):
 # Jei nurodyta funkcija, pritaiko ją tekstui.
 # Jei funkcija nenurodyta, grąžina tekstą mažosiomis raidėmis.
 return funkcija(tekstas) if funkcija else tekstas.lower()


def keli_apdorojimai(tekstas, *args): # * kaip args
#Pritaiko kelias funkcijas iš eilės tam pačiam tekstui
 for funkcija in args:
  tekstas = funkcija(tekstas)
 return tekstas

print(prideti_zenkliuka("Labas"))
print(apversti_teksta("Labas"))
print(apdoroti_teksta("Labas"))
print(apdoroti_teksta("Labas", prideti_zenkliuka))
print(keli_apdorojimai("Labas", prideti_zenkliuka, apversti_teksta))