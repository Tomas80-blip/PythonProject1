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

# 1. Sukurti duomenų bazę su dviem lentelėmis
class DatabaseManager:
    def __init__(self, db_name='mokykla.db'):
        self.db_name = db_name
        self.create_tables()

    def create_tables(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.executescript('''
                CREATE TABLE IF NOT EXISTS mokiniai (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    vardas TEXT NOT NULL,
                    pavarde TEXT NOT NULL,
                    klase TEXT NOT NULL,
                    vidurkis REAL CHECK (vidurkis BETWEEN 1 AND 10)
                );

                CREATE TABLE IF NOT EXISTS mokytojai (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    vardas TEXT NOT NULL,
                    pavarde TEXT NOT NULL,
                    dalykas TEXT NOT NULL
                );
            ''')
            conn.commit()

    def execute_query(self, query, params=(), fetchone=False, fetchall=False):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            if fetchone:
                return cursor.fetchone()
            if fetchall:
                return cursor.fetchall()
            conn.commit()

db = DatabaseManager()

# 2. Sukurti OOP klases
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
        return f"{self.vardas} {self.pavarde}, Klasė: {self.klase}, Vidurkis: {self.vidurkis:.2f}"

class Mokytojas(Asmuo):
    def __init__(self, vardas, pavarde, dalykas):
        super().__init__(vardas, pavarde)
        self.dalykas = dalykas

    def __str__(self):
        return f"{self.vardas} {self.pavarde}, Dėsto: {self.dalykas}"

# 3. Dekoratorius funkcijų registracijai
def log_dekoratorius(func):
    def wrapper(*args, **kwargs):
        print(f'Vykdoma operacija: {func.__name__} su parametrais {args}')
        try:
            return func(*args, **kwargs)
        except sqlite3.Error as e:
            print(f'Klaida vykdant {func.__name__}: {e}')
    return wrapper

# 4. Funkcijos duomenų valdymui
@log_dekoratorius
def prideti_mokini(mokinys):
    db.execute_query(
        'INSERT INTO mokiniai (vardas, pavarde, klase, vidurkis) VALUES (?, ?, ?, ?)',
        (mokinys.vardas, mokinys.pavarde, mokinys.klase, mokinys.vidurkis)
    )

@log_dekoratorius
def prideti_mokytoja(mokytojas):
    db.execute_query(
        'INSERT INTO mokytojai (vardas, pavarde, dalykas) VALUES (?, ?, ?)',
        (mokytojas.vardas, mokytojas.pavarde, mokytojas.dalykas)
    )

@log_dekoratorius
def perziureti_visus_mokinius():
    mokiniai = db.execute_query(
        'SELECT id, vardas, pavarde, klase, vidurkis FROM mokiniai', fetchall=True
    )
    if not mokiniai:
        print('Mokinių sąrašas tuščias.')
        return
    for mokinys in mokiniai:
        print(f'ID: {mokinys[0]}, Vardas: {mokinys[1]}, Pavardė: {mokinys[2]}, Klasė: {mokinys[3]}, Vidurkis: {mokinys[4]:.2f}')

@log_dekoratorius
def perziureti_visus_mokytojus():
    mokytojai = db.execute_query(
        'SELECT id, vardas, pavarde, dalykas FROM mokytojai', fetchall=True
    )
    if not mokytojai:
        print('Mokytojų sąrašas tuščias.')
        return
    for mokytojas in mokytojai:
        print(f'ID: {mokytojas[0]}, Vardas: {mokytojas[1]}, Pavardė: {mokytojas[2]}, Dėsto: {mokytojas[3]}')

@log_dekoratorius
def ieskoti_mokinio(vardas, pavarde):
    mokiniai = db.execute_query(
        'SELECT vardas, pavarde, klase, vidurkis FROM mokiniai WHERE vardas = ? AND pavarde = ?',
        (vardas, pavarde), fetchall=True
    )
    if not mokiniai:
        print('Mokinys nerastas.')
        return
    for mokinys in mokiniai:
        print(f'Vardas: {mokinys[0]}, Pavardė: {mokinys[1]}, Klasė: {mokinys[2]}, Vidurkis: {mokinys[3]:.2f}')


@log_dekoratorius
def ieskoti_mokytojo(vardas, pavarde):
    mokytojai = db.execute_query(
        'SELECT vardas, pavarde, dalykas FROM mokytojai WHERE vardas = ? AND pavarde = ?',
        (vardas, pavarde), fetchall=True
    )
    if not mokytojai:
        print('Mokytojas nerastas.')
        return
    for mokytojas in mokytojai:
        print(f'Vardas: {mokytojas[0]}, Pavardė: {mokytojas[1]}, dalykas: {mokytojas[2]}')

@log_dekoratorius
def atnaujinti_mokinio_klase(mokinys_id, nauja_klase):
    db.execute_query(
        'UPDATE mokiniai SET klase = ? WHERE id = ?',
        (nauja_klase, mokinys_id)
    )

@log_dekoratorius
def atnaujinti_mokytoja(mokytojas_id, naujas_dalykas):
    db.execute_query(
        'UPDATE mokytojai SET dalykas = ? WHERE id = ?',
        (naujas_dalykas, mokytojas_id)
    )

@log_dekoratorius
def istrinti_mokini(mokinys_id):
    db.execute_query(
        'DELETE FROM mokiniai WHERE id = ?',
        (mokinys_id,)
    )
@log_dekoratorius
def istrinti_mokytoja(mokytojas_id):
    db.execute_query(
        'DELETE FROM mokytojai WHERE id = ?',
        (mokytojas_id,)
    )

# 5. Iteratorius mokinių sąrašui
class MokiniuIteratorius:
    def __init__(self):
        self.mokiniai = db.execute_query(
            'SELECT vardas, pavarde, klase, vidurkis FROM mokiniai', fetchall=True
        )
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.mokiniai):
            duomenys = self.mokiniai[self.index]
            self.index += 1
            return Mokinys(*duomenys)
        raise StopIteration

# 6. Vartotojo sąsaja
def pasirinkti_veiksma():
    veiksmai = {
        '1': lambda: prideti_mokini(
            Mokinys(
                vardas=input('Mokinio vardas: '),
                pavarde=input('Mokinio pavardė: '),
                klase=input('Mokinio klasė: '),
                vidurkis=float(input('Mokinio vidurkis: '))
            )
        ),
        '2': lambda: prideti_mokytoja(
            Mokytojas(
                vardas=input('Mokytojo vardas: '),
                pavarde=input('Mokytojo pavardė: '),
                dalykas=input('Mokytojo dėstomas dalykas: ')
            )
        ),
        '3': perziureti_visus_mokinius,
        '4': perziureti_visus_mokytojus,
        '5': lambda: ieskoti_mokinio(
            vardas=input('Mokinio vardas: '),
            pavarde=input('Mokinio pavardė: ')
        ),
        '6': lambda: ieskoti_mokytojo(
            vardas=input('Mokytojo vardas: '),
            pavarde=input('Mokytojo pavardė: ')
        ),
        '7': lambda: atnaujinti_mokinio_klase(
            int(input('Mokinio ID: ')),
            input('Nauja klasė: ')
        ),
        '8': lambda: atnaujinti_mokytoja(
            int(input('Mokytojo ID: ')),
            input('Naujas dalykas: ')
        ),
        '9': lambda: istrinti_mokini(int(input('Mokinio ID: '))),
        '10': lambda: istrinti_mokytoja(int(input('Mokytojo ID: '))),
        '11': exit
        # '9': lambda:
    }

    while True:
        print('\nMokyklos duomenų valdymo sistema')
        print('1. Pridėti mokinį')
        print('2. Pridėti mokytoją')
        print('3. Peržiūrėti visus mokinius')
        print('4. Peržiūrėti visus mokytojus')
        print('5. Ieškoti mokinio pagal vardą ir pavarde')
        print('6. Ieškoti mokytojo pagal vardą ir pavarde')
        print('7. Atnaujinti mokinio klasę')
        print('8. Atnaujinti mokytojo mokoma dalyką')
        print('9. Ištrinti mokinį')
        print('10. Ištrinti mokytoją')
        print('11. Išeiti')

        pasirinkimas = input('Pasirinkite veiksmą: ')
        veiksmai.get(pasirinkimas, lambda: print('Neteisingas pasirinkimas!'))()

# 7. Vykdymas
pasirinkti_veiksma()
