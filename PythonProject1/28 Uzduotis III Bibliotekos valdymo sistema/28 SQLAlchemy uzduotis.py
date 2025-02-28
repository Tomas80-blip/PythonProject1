# Užduoties aprašymas
# Jūs turite sukurti paprastą bibliotekos sistemą, kurioje būtų galima valdyti knygas ir skaitytojus.
# Turite įgyvendinti duomenų bazės modelius, ryšius tarp lentelių, bei suteikti galimybę pridėti, keisti ir
# šalinti duomenis naudojant konsolę.

# 1. Duomenų bazės modeliai su SQLAlchemy
# Sukurkite duomenų bazės struktūrą su šiomis lentelėmis:
#
# Knygos (books)#
# id (pirminis raktas, autogeneruojamas)
# title (knygos pavadinimas, unikalus)
# author (autorius)
# year_published (leidimo metai)
# available (Boolean – ar galima skolintis)

# Skaitytojai (readers)#
# id (pirminis raktas, autogeneruojamas)
# name (skaitytojo vardas)
# email (el. paštas, unikalus)

# Skaitytojų paskolintos knygos (borrowed_books)#
# id (pirminis raktas, autogeneruojamas)
# book_id (užsienio raktas į books.id)
# reader_id (užsienio raktas į readers.id)
# borrowed_at (data, kada paimta knyga)
# return_due_date (grąžinimo terminas)

# Santykiai:
# One-to-Many ryšys tarp Skaitytojų ir Skaitytojų paskolintų knygų.
# One-to-Many ryšys tarp Knygų ir Skaitytojų paskolintų knygų

# 2. Programos funkcionalumas

# Sukurkite Python programą, kuri leistų per konsolę atlikti šias operacijas:
#
# Pridėti naują knygą
# Pridėti naują skaitytoją
# Paskolinti knygą skaitytojui (jei ji prieinama)
# Atnaujinti knygos informaciją (pvz., pakeisti pavadinimą ar autorių)
# Pašalinti skaitytoją arba knygą (su visais susijusiais duomenimis)
# Parodyti visų knygų sąrašą su jų būkle
# Parodyti visų paskolintų knygų sąrašą

# Papildomi apribojimai:#
# Negalima leisti paskolinti jau paskolintos knygos.
# El. paštas turi būti unikalus (naudoti constraints).

# 3. SQL Injection Apsauga
# Užtikrinkite, kad vartotojo įvestis nėra pažeidžiama SQL Injection atakoms (naudokite bind parameters
# vietoj tiesioginių SQL užklausų).
#
# 4. Užduoties atlikimas
# Sukurkite duomenų bazę naudodami SQLAlchemy
# Parašykite Python skriptą, kuris leidžia atlikti duomenų modifikavimą per konsolę
# Išbandykite pridėti, atnaujinti ir pašalinti duomenis per terminalą


# Papildoma užduotis (jei liks laiko)
# Pridėti funkcionalumą, kuris rodo, kiek laiko knyga jau yra paskolinta.
# Implementuoti funkciją, kuri leidžia matyti skaitytojo paskolintų knygų istoriją.

# Patarimai:#
# Naudokite session.query() metodus vietoje tiesioginių SQL užklausų.
# Testuokite programą mažais žingsniais – pirmiausia sukurkite lenteles, tada pridėkite duomenų įrašus,
# o galiausiai testuokite jų modifikavimą per konsolę.
# Sėkmės! 🚀



from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from datetime import datetime, timedelta


engine = create_engine("sqlite:///library.db")
Base = declarative_base()

# STEP 1 Lenteliu kurimas

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    author = Column(String, nullable=False)
    year_published = Column(Integer, nullable=False)
    available = Column(Boolean, default=True)


class Reader(Base):
    __tablename__ = 'readers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    borrowed_books = relationship("BorrowedBook", back_populates="reader")


class BorrowedBook(Base):
    __tablename__ = 'borrowed_books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    reader_id = Column(Integer, ForeignKey('readers.id'), nullable=False)
    borrowed_at = Column(DateTime)
    return_due_date = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(days=14))

    book = relationship("Book")
    reader = relationship("Reader", back_populates="borrowed_books")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# 2. Programos funkcionalumas

def add_book(session, title, author, year_published):
    if session.query(Book).filter_by(title=title).first():
        print("Knyga su tokiu pavadinimu jau egzistuoja.")
        return
    book = Book(title=title, author=author, year_published=year_published)
    session.add(book)
    session.commit()
    print("Knyga pridėta sėkmingai.")

def add_reader(session, name, email):
    if session.query(Reader).filter_by(email=email).first():
        print("Skaitytojas su tokiu el. paštu jau egzistuoja.")
        return
    reader = Reader(name=name, email=email)
    session.add(reader)
    session.commit()
    print("Skaitytojas pridėtas sėkmingai.")

def borrow_book(session, book_title, reader_email):
    book = session.query(Book).filter_by(title=book_title, available=True).first()
    if not book:
        print("Knyga nėra prieinama paskolinti.")
        return
    reader = session.query(Reader).filter_by(email=reader_email).first()
    if not reader:
        print("Nėra tokio skaitytojo.")
        return
    borrowed_book = BorrowedBook(book_id=book.id, reader_id=reader.id, borrowed_at=datetime.utcnow())
    book.available = False
    session.add(borrowed_book)
    session.commit()
    print("Knyga sėkmingai paskolinta.")

def update_book(session, old_title, new_title=None, new_author=None):
    book = session.query(Book).filter_by(title=old_title).first()
    if not book:
        print("Tokios knygos nėra.")
        return
    if new_title:
        book.title = new_title
    if new_author:
        book.author = new_author
    session.commit()
    print("Knyga sėkmingai atnaujinta.")

def delete_book(session, title):
    book = session.query(Book).filter_by(title=title).first()
    if not book:
        print("Tokios knygos nėra.")
        return
    session.query(BorrowedBook).filter_by(book_id=book.id).delete()
    session.delete(book)
    session.commit()
    print("Knyga sėkmingai ištrinta.")

def delete_reader(session, email):
    reader = session.query(Reader).filter_by(email=email).first()
    if not reader:
        print("Tokio skaitytojo nėra.")
        return
    session.query(BorrowedBook).filter_by(reader_id=reader.id).delete()
    session.delete(reader)
    session.commit()
    print("Skaitytojas sėkmingai ištrintas.")


def list_books(session):
    books = session.query(Book).all()
    for book in books:
        status = "Prieinama" if book.available else "Paskolinta"
        print(f"{book.title} ({book.author}, {book.year_published}) - {status}")

def list_borrowed_books(session):
    borrowed_books = session.query(BorrowedBook).all()
    for bb in borrowed_books:
        book = session.query(Book).filter_by(id=bb.book_id).first()
        reader = session.query(Reader).filter_by(id=bb.reader_id).first()
        print(f"{book.title} paskolino {reader.name} iki {bb.return_due_date.strftime('%Y-%m-%d')}")


# Vartotojo sąsaja

def pasirinkti_veiksma(session):
    veiksmai = {
        '1': lambda: add_book(session,
                              input("Įveskite knygos pavadinimą: "),
                              input("Įveskite autorių: "),
                              int(input("Įveskite leidimo metus: "))),
        '2': lambda: add_reader(session,
                                input("Įveskite skaitytojo vardą: "),
                                input("Įveskite el. paštą: ")),
        '3': lambda: borrow_book(session,
                                 input("Įveskite knygos pavadinimą: "),
                                 input("Įveskite skaitytojo el. paštą: ")),
        '4': lambda: update_book(session,
                                 input("Įveskite seną pavadinimą: "),
                                 input("Naujas pavadinimas (palikite tuščią, jei nekeisite): "),
                                 input("Naujas autorius (palikite tuščią, jei nekeisite): ")),
        '5': lambda: delete_book(session,
                                 input("Įveskite knygos pavadinimą: ")),
        '6': lambda: delete_reader(session,
                                   input("Įveskite skaitytojo el. paštą: ")),
        '7': lambda: list_books(session),
        '8': lambda: list_borrowed_books(session),
        '9': exit
    }

    while True:
        print("\nPasirinkite veiksmą:")
        print("1. Pridėti knygą")
        print("2. Pridėti skaitytoją")
        print("3. Paskolinti knygą")
        print("4. Atnaujinti knygą")
        print("5. Ištrinti knygą")
        print("6. Ištrinti skaitytoją")
        print("7. Rodyti visas knygas")
        print("8. Rodyti paskolintas knygas")
        print("9. Išeiti")

        pasirinkimas = input('Pasirinkite veiksmą: ')
        veiksmai.get(pasirinkimas, lambda: print('Neteisingas pasirinkimas!'))()

# Vykdymas
pasirinkti_veiksma(session)