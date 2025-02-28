# Kelių argumentų tipų derinimas
# Užduotis 5:
# Sukurkite funkciją spausdinti_zinutes(kartai, *args, pabaiga="!"), kuri
# pakartotų kiekvieną perduotą žinutę kartai kartų, o pabaigoje pridėtų pabaiga reikšmę.

def spausdinti_zinutes(kartai, *args, pabaiga="!"):
    for zinute in args:
        print((zinute + " ") * kartai + pabaiga)# " " prideda tarpeli po zinutes

spausdinti_zinutes(3, "Labas", "Kaip sekasi", pabaiga="?") # jei be (pabaiga="?"), tai atvaizduos "!"

# Rezultatų grąžinimas naudojant *args
# Užduotis 6:
# Sukurkite funkciją dauginti_skaicius(n, *args), kuri priimtų skaičių n ir kitus
# skaičius *args, padaugintų kiekvieną iš n, o rezultatą grąžintų kaip sąrašą.

def dauginti_skaicius(n,*args):
    return [n * skaicius for skaicius in args] #Kiekvienas args elementas (skaicius)
    # padauginamas iš n ir įtraukiamas į lista.
res = dauginti_skaicius(2, 4,5,6)
print(res)