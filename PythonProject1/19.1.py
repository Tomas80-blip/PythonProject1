# 1. Prisijungimas prie Duomenų Bazės
# Užduotis:
# 1. Sukurkite Python programą, kuri:
# a. Prisijungia prie SQLite duomenų bazės pavadinimu mokykla.db.
# b. Sukuria lentelę mokykla su stulpeliais: pavadinimas (TEXT), adresas
# (TEXT), mokiniu_skaicius (INTEGER).

import sqlite3

# Prisijungimas prie duomenų bazės
conn = sqlite3.connect("mokykla.db")
c = conn.cursor() # sukuriamas kursorius(tai atidarymas tam tikro veiksmo)

# Lentelės sukūrimas
c.execute(
'''
CREATE TABLE IF NOT EXISTS mokykla (
    pavadinimas TEXT,
    adresas TEXT,
    mokiniu_skaicius INTEGER)
''')

conn.commit() #commitinimas
conn.close() #uzdarymas
# atsiranda kaireje failiukas   pavyzdys.db (kaip exelio failiukas)