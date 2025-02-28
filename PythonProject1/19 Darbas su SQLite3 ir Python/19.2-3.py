# 2. Duomenų Įterpimas (INSERT)
# Užduotis:
# 1. Įterpkite šiuos duomenis į lentelę mokykla:
# a. "Vilniaus progimnazija", "Vilniaus g. 10", 500
# b. "Kauno gimnazija", "Kauno g. 5", 800
# 2. Parašykite Python funkciją prideti_mokykla, kuri priima tris parametrus
# (pavadinimas, adresas, mokinių skaičius) ir įterpia juos į duomenų bazę.


import sqlite3

def init_database():
    conn = sqlite3.connect('mokykla.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS mokykla (
        pavadinimas TEXT,
        adresas TEXT,
        mokiniu_skaicius INTEGER
    )
    ''')
    conn.commit()
    conn.close()


def prideti_mokykla(pavadinimas, adresas, mokiniu_skaicius):
    with sqlite3.connect('mokykla.db') as conn:
        c = conn.cursor()
        c.execute("INSERT INTO mokykla (pavadinimas, adresas, mokiniu_skaicius) VALUES (?, ?, ?)", (pavadinimas, adresas, mokiniu_skaicius))
        conn.commit()

prideti_mokykla("Vilniaus progimnazija", "Vilniaus g. 10", 500)
prideti_mokykla("Kauno gimnazija", "Kauno g. 5", 800)


# 3. Duomenų Skaitymas (SELECT)
# Užduotis:
# 1. Sukurkite Python programą, kuri:
# a. Nuskaito visus duomenis iš lentelės mokykla.
# b. Išveda juos tvarkingai formatuotu tekstu (pvz., „Mokykla: Vilniaus
# progimnazija, Adresas: Vilniaus g. 10, Mokinių skaičius: 500“).
# 2. Pridėkite galimybę filtruoti duomenis pagal minimalų mokinių skaičių (pvz., rodyti
# tik tas mokyklas, kuriose yra daugiau nei 600 mokinių).


# Funkcija duomenų nuskaitymui su filtru
def rodyti_mokyklas(min_mokiniu_skaicius=0):
    with sqlite3.connect('mokykla.db') as conn:
        c = conn.cursor()
        c.execute(''' SELECT * FROM mokykla WHERE mokiniu_skaicius > ?
    ''', (min_mokiniu_skaicius,))

    mokyklos = c.fetchall()

    for mokykla in mokyklos:
        print(f"Mokykla: {mokykla[0]}, Adresas: {mokykla[1]}, Mokinių skaičius: {mokykla[2]}")


# Rodome visas mokyklas
print("Visos mokyklos:")
rodyti_mokyklas()

# Rodome mokyklas su daugiau nei 600 mokinių
print("\nMokyklos su daugiau nei 600 mokinių:")
rodyti_mokyklas(600)

# Uždaryti duomenų bazės ryšį
# conn.close()