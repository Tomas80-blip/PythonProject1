# Įvadas į **kwargs
# Užduotis 7:
# Parašykite funkciją rodyti_duomenis(**kwargs), kuri išspausdintų visus perduotus
# vardinius argumentus raktu ir reikšme.


def rodyti_duomenis(**kwargs):
    for raktas, reiksme in kwargs.items():
        print(f"{raktas}: {reiksme}")

rodyti_duomenis(vardas="Jonas", amzius=25, miestas="Vilnius")


# **kwargs su numatytaisiais argumentais
# Užduotis 8:
# Sukurkite funkciją registruoti_naudotoja(vardas, el_pastas, **kwargs), kuri
# priimtų vardą, el. paštą ir papildomus pasirinktinus duomenis.

def registruoti_naudotoja(vardas, el_pastas, **kwargs):
    naudotojas = {
        "vardas": vardas,
        "el_pastas": el_pastas,
        **kwargs}
    print(kwargs)
    print('New user created:')
    for key, value in naudotojas.items():
        print(f' - {key}: {value}')
    return naudotojas

# Pavyzdys:
naudotojas_info = registruoti_naudotoja("Jonas", "jonas@example.com", amzius=25, miestas="Vilnius")
print(naudotojas_info)



# **kwargs naudojimas kitoje funkcijoje
# Užduotis 9:
# Sukurkite funkciją atspausdinti_lista(listas, **kwargs), kuri perduoda **kwargs
# į print(), leisdama valdyti formatavimą.

def atspausdinti_lista(listas, **kwargs):
    print(*listas, **kwargs)# *listas - ispakuoja lista (t.y nuima skliaustelius)
    # ir tam kad galiotu seperatoriai (nenaudoti su for ciklu)

# Pavyzdys:
atspausdinti_lista([1, 2, 3, 4], sep=", ", end=".\n")
atspausdinti_lista(["Obuolys", "Bananai", "Vyšnios"], sep=" | ", end=".\n")

# nes darant su for ciklu, neisigalioja seperatorius
def atspausdinti_lista(listas, **kwargs):
    for i in listas:
        print(i, **kwargs)
    # print(*listas, **kwargs)

# Pavyzdys:
atspausdinti_lista(["Obuolys", "Bananai", "Vyšnios"], sep=" | ", end=".\n")