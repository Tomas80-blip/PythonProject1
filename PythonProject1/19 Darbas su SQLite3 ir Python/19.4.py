# 4. Duomenų Atnaujinimas (UPDATE)
# Užduotis:
# 1. Parašykite Python funkciją atnaujinti_mokiniu_skaiciu, kuri:
# a. Priima mokyklos pavadinimą ir naują mokinių skaičių kaip parametrus.
# b. Atnaujina nurodytos mokyklos mokinių skaičių duomenų bazėje.
# 2. Patikrinkite, ar atnaujinimas įvyko sėkmingai, išvesdami visų mokyklų sąrašą po
# pakeitimo.

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
print('-----------------------------------------')
# pagal sia tema
def atnaujinti_mokiniu_skaiciu(pavadinimas, naujas_mokiniu_skaicius):
    with sqlite3.connect('mokykla.db') as conn:
        c = conn.cursor()
        c.execute("UPDATE mokykla SET mokiniu_skaicius = ? WHERE pavadinimas = ?", ( naujas_mokiniu_skaicius, pavadinimas))
#                 pakeitimas konkrečiai mokyklai pagal  jos pavadinimą ^^
    conn.commit()
atnaujinti_mokiniu_skaiciu('Kauno gimnazija', 1200)
rodyti_mokyklas()