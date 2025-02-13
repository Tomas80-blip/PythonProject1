# Mokyklos duomenų valdymo sistema
# Tikslas
# Sukurti mokyklos duomenų valdymo sistemą naudojant Python objektinį programavimą, SQLite duomenų bazę,
# funkcijas, iteratorius, dekoratorius ir klaidų valdymą.
#
# 1. Sistemos Funkcionalumas
# Sukurti Python programą, kuri galėtų atlikti šiuos veiksmus:
#
# Pridėti naujus mokinius į duomenų bazę
# Pridėti naujus mokytojus
# Priskirti mokinius į klases
# Atvaizduoti visus mokinius ir jų informaciją
# Ieškoti mokinių pagal vardą/pavardę
# Atnaujinti mokinio informaciją (pvz., pakeisti klasę)
# Pašalinti mokinį iš sistemos
# Tvarkyti mokinių sąrašus naudojant iteratorius
# Naudoti dekoratorių funkcijoms registruoti
# Naudoti try-except bloką klaidų valdymui

# 2. Struktūra
# Klasės
# Asmuo (tėvinė klasė)
# Atributai:#
# vardas
# pavarde

# Mokinys (paveldi Asmuo)
# Papildomi atributai:#
# klase
# vidurkis

# Mokytojas (paveldi Asmuo)
# Papildomi atributai:
# dalykas
#

# 3. Realizacija
# 1. SQLite duomenų bazė
# Sukurti dvi lenteles: mokiniai ir mokytojai.
# Naudoti sqlite3, kad būtų galima atlikti INSERT, SELECT, UPDATE, DELETE užklausas.
# 2. Iteratorius mokinių sąrašui
# Sukurti iteratoriaus klasę, kuri leis eiti per mokinių sąrašą po vieną.
# 3. Dekoratorius funkcijoms registruoti
# Sukurti dekoratorių, kuris prieš iškviesdamas bet kurią duomenų bazės funkciją išspausdina "Vykdoma operacija...".
# 4. Try-except klaidų valdymas
# Užtikrinti, kad programa necrash'intų, jei vartotojas įveda blogus duomenis (pvz., ne skaičių, kai tikimasi skaičiaus).

# 4. Užduoties Etapai
# Turite atlikti šiuos žingsnius:#
# Sukurti SQLite duomenų bazę su dviem lentelėmis (mokiniai, mokytojai).
# Sukurti Asmuo, Mokinys, Mokytojas klases su atitinkamais atributais.
# Parašyti funkcijas mokinių/mokytojų įterpimui, atnaujinimui, trynimui ir paieškai naudojant SQLite.
# Sukurti iteratoriaus klasę, kuri leis peržiūrėti visus mokinius po vieną.
# Sukurti dekoratorių, kuris prideda log' ą prieš kiekvieną DB operaciją.
# Pridėti try-except bloką, kad būtų išvengta programos kritimų dėl blogos įvesties.
# Testuoti programą su keliais įvesties scenarijais.

import sqlite3

def init_database():
    conn = sqlite3.connect('mokykla.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS mokiniai (
        vardas TEXT,
        pavarde TEXT,
        klase TEXT,
        vidurkis REAL
    )''')
    c.execute('''
    CREATE TABLE IF NOT EXISTS mokytojai (
        vardas TEXT,
        pavarde TEXT,
        dalykas TEXT
    )''')
    conn.commit()
    conn.close()

class Asmuo:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde

class Mokinys(Asmuo):
    def __init__(self, vardas, pavarde, klase, vidurkis):
        super().__init__(vardas, pavarde)
        self.klase = klase
        self.vidurkis = vidurkis

    def __str__(self):
        return f"{self.vardas} {self.pavarde}, {self.klase} klasė, vidurkis: {self.vidurkis}"

class Mokytojas(Asmuo):
    def __init__(self, vardas, pavarde, dalykas):
        super().__init__(vardas, pavarde)
        self.dalykas = dalykas

def prideti_mokini(vardas, pavarde, klase, vidurkis):
    try:
        with sqlite3.connect('mokykla.db') as conn:
            c = conn.cursor()
            c.execute("INSERT INTO mokiniai (vardas, pavarde, klase, vidurkis) VALUES (?, ?, ?, ?)",
                      (vardas, pavarde, klase, vidurkis))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Klaida pridedant mokinį: {e}")

def atnaujinti_mokini(vardas, pavarde, nauja_klase, naujas_vidurkis):
    try:
        with sqlite3.connect('mokykla.db') as conn:
            c = conn.cursor()
            c.execute("UPDATE mokiniai SET klase=?, vidurkis=? WHERE vardas=? AND pavarde=?",
                      (nauja_klase, naujas_vidurkis, vardas, pavarde))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Klaida atnaujinant mokinį: {e}")

def trinti_mokini(vardas, pavarde):
    try:
        with sqlite3.connect('mokykla.db') as conn:
            c = conn.cursor()
            c.execute("DELETE FROM mokiniai WHERE vardas=? AND pavarde=?", (vardas, pavarde))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Klaida trinant mokinį: {e}")

def gauti_mokini(vardas, pavarde):
    try:
        with sqlite3.connect('mokykla.db') as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM mokiniai WHERE vardas=? AND pavarde=?", (vardas, pavarde))
            mokinys = c.fetchone()
            return Mokinys(*mokinys) if mokinys else None
    except sqlite3.Error as e:
        print(f"Klaida ieškant mokinio: {e}")
        return None

def print_all_mokiniai_rows():
    with sqlite3.connect('mokykla.db') as conn:
        c = conn.cursor()
        for row in c.execute("SELECT * FROM mokiniai"):
            print(row)

def prideti_mokytoja(vardas, pavarde, dalykas):
    try:
        with sqlite3.connect('mokykla.db') as conn:
            c = conn.cursor()
            c.execute("INSERT INTO mokytojai (vardas, pavarde, dalykas) VALUES (?, ?, ?)",
                      (vardas, pavarde, dalykas))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Klaida pridedant mokinį: {e}")

def print_all_mokytojai_rows():
    with sqlite3.connect('mokykla.db') as conn:
        c = conn.cursor()
        for row in c.execute("SELECT * FROM mokytojai"):
            print(row)

def atnaujinti_mokytoja(vardas, pavarde, naujas_dalykas):
    try:
        with sqlite3.connect('mokykla.db') as conn:
            c = conn.cursor()
            c.execute("UPDATE mokytojai SET dalykas=? WHERE vardas=? AND pavarde=?",
                      (naujas_dalykas, vardas, pavarde))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Klaida atnaujinant mokinį: {e}")

def trinti_mokytoja(vardas, pavarde):
    try:
        with sqlite3.connect('mokykla.db') as conn:
            c = conn.cursor()
            c.execute("DELETE FROM mokytojai WHERE vardas=? AND pavarde=?", (vardas, pavarde))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Klaida trinant mokinį: {e}")



init_database() # Inicializuojame duomenų bazę Svarbu! kad teisingai sukurtu db failiuka (su klaustuku)
print_all_mokiniai_rows()
prideti_mokini("Jonas", "Jonaitis", "10", 8.5)
prideti_mokini("Petras","Petrauskas","11",9.0)
atnaujinti_mokini("Jonas","Jonaitis", "12", 10)

# Gauname mokinį ir atspausdiname
mokinys1 = gauti_mokini("Jonas", "Jonaitis")
print(mokinys1)
# trinti_mokinys1 = trinti_mokini("Jonas", "Jonaitis")
# trinti_mokinys2 = trinti_mokini("Petras", "Petrauskas")


print_all_mokytojai_rows()
prideti_mokytoja("Janina", "Jonaitiene", "matematika")
atnaujinti_mokytoja("Janina", "Jonaitiene", "Istorija")
# trinti_mokytoja("Janina", "Jonaitiene")