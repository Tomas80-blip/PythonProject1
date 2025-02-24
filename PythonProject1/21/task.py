# Šiame pavyzdyje sukuriama projektai lentelė su trimis laukais:
#
# id – unikalus projekto identifikatorius.
# pavadinimas – projekto pavadinimas.
# kaina – projekto kaina.

# 1. Duomenų bazės ir modelio sukūrimas
# Užduotis:
# • Sukurkite SQLite duomenų bazę mokykla.db.
# • Sukurkite SQLAlchemy modelį Mokinys, kuris turės šiuos laukus:
# o id (pirminis raktas, Integer)
# o vardas (String)
# o pavarde (String)
# o klase (Integer)

# Papildomas iššūkis: Sukurkite antrą modelį Mokytojas, kuris turės laukus:
# • id (pirminis raktas, Integer)
# • vardas (String)
# • pavarde (String)
# • dalykas (String)

# Sukurta ir patalpinta i papkute models,  failiuka .projektai


# 2. Duomenų įterpimas
# Užduotis:
# • Įterpkite bent 3 mokinius ir 2 mokytojus į duomenų bazę naudojant SQLAlchemy
# ORM.
# • Užtikrinkite, kad duomenys būtų išsaugoti naudojant session.commit().
# Papildomas iššūkis: Įterpkite naują mokinį tik tuo atveju, jei jo dar nėra duomenų
# bazėje.

# 3. Duomenų skaitymas
# Užduotis:
# • Parašykite funkciją, kuri išveda visų mokinių sąrašą.
# • Parašykite funkciją, kuri išveda visus mokytojus.

from models import Mokinys, Mokytojas, engine
from sqlalchemy.orm import sessionmaker

# Sukuriame sesiją
Session = sessionmaker(bind=engine)
session = Session()

# Funkcija, kuri patikrina, ar mokinys jau yra duomenų bazėje
def ar_mokinys_yra(vardas, pavarde):
    return session.query(Mokinys).filter_by(vardas=vardas, pavarde=pavarde).first() is not None
# objekta grazina jei jis is not None

#arba kitu budu patikrinti
# def ar_mokinys_yra(vardas, pavarde):
#     mokiniai = session.query(Mokinys).all()
#     for row in mokiniai:
#         if row.vardas == vardas and row.pavarde == pavarde:
#             return True



# Sukuriam mokinius, jei jų dar nėra
mokiniai = [
    ("Jonas", "Jonaitis", 5),
    ("Petras", "Petraitis", 6),
    ("Asta", "Astaitė", 7),
    ("Giedrius", "Giedraitis", 9),
    ("Meta","Metaite", 12),
    ("Tadas", "Tadaitis", 12)
]
# pridedam mokinius
for vardas, pavarde, klase in mokiniai:
    if not ar_mokinys_yra(vardas, pavarde):
        session.add(Mokinys(vardas=vardas, pavarde=pavarde, klase=klase))

# Sukuriam mokytojus
mokytojai = [
    Mokytojas(vardas="Rasa", pavarde="Rasaitė", dalykas="Matematika"),
    Mokytojas(vardas="Tomas", pavarde="Tomaitis", dalykas="Fizika")
]


# #pridedam visus mokytojus
# session.add_all(mokytojai)

# arba
for mok in mokytojai:
    session.add(mok)

# Išsaugome pakeitimus
session.commit()

# Funkcija mokinių sąrašo išvedimui
def spausdinti_mokinius():
    mokiniai = session.query(Mokinys).all()
    for mokinys in mokiniai:
        print(f"Mokinys: {mokinys.id} {mokinys.vardas} {mokinys.pavarde}, klasė: {mokinys.klase}")

# Funkcija mokytojų sąrašo išvedimui
def spausdinti_mokytojus():
    mokytojai = session.query(Mokytojas).all()
    for mokytojas in mokytojai:
        print(f"Mokytojas: {mokytojas.id} {mokytojas.vardas} {mokytojas.pavarde}, dėsto: {mokytojas.dalykas}")



# mokytokai kaskart prisideda nes nera funkcijos kuri tikrintu ar jau yra toks mokytojas duomenu bazeje

# 5. Duomenų trynimas
# Užduotis:
# • Parašykite funkciją, kuri pašalina mokinį iš duomenų bazės pagal id.
# • Parašykite funkciją, kuri pašalina mokytoją pagal id.
# Papildomas iššūkis:
# • Ištrinkite visus mokinius, kurie jau baigė mokyklą (12 klasė).


def delete_student_by_id(student_id):
    student = session.get(Mokinys, student_id)
    if student:
        session.delete(student)
        session.commit()
        print(f'Mokinys su ID {student_id} pašalintas.')
    else:
        print(f'Mokinys su ID {student_id} nerastas.')

def delete_teacher_by_id(teacher_id):
    teacher = session.get(Mokytojas, teacher_id)
    if teacher:
        session.delete(teacher)
        session.commit()
        print(f'Mokytojas su ID {teacher_id} pašalintas.')
    else:
        print(f'Mokytojas su ID {teacher_id} nerastas.')

def delete_graduated_students():
    graduated_students = session.query(Mokinys).filter_by(klase=12).all()
    for student in graduated_students:
        session.delete(student)
    session.commit()
    print(f'Visi 12 klasės mokiniai pašalinti.')

# 6. Paieška ir filtravimas
# Užduotis:
# • Parašykite funkciją, kuri randa mokinį pagal vardą.
# • Parašykite funkciją, kuri randa visus mokinius, kurių pavardė prasideda raide "P".
# Papildomas iššūkis:
# • Raskite visus mokytojus, kurių vardas baigiasi raide „s“.


from sqlalchemy.exc import MultipleResultsFound, NoResultFound
def find_student_by_name(name):
    try:
        mokinys = session.query(Mokinys).filter_by(vardas=name).one()
        print(f"Mokinys: {mokinys.id} {mokinys.vardas} {mokinys.pavarde}, klasė: {mokinys.klase}")
    except NoResultFound:
        print(f'Mokinys su vardu {name} nerastas.')
    except MultipleResultsFound:
        print(f'Rasta daugiau nei viena įrašų su vardu {name}.')

def find_students_by_lastname_initial(letter):
    mokiniai = session.query(Mokinys).filter(Mokinys.pavarde.ilike(f'{letter}%')).all()
    for mokinys in mokiniai:
        print(f"Mokinys: {mokinys.id} {mokinys.vardas} {mokinys.pavarde}, klasė: {mokinys.klase}")

def find_teachers_by_name_endswith(letter):
    mokytojai = session.query(Mokytojas).filter(Mokytojas.vardas.ilike(f'%{letter}')).all()
    for mokytojas in mokytojai:
        print(f"Mokytojas: {mokytojas.id} {mokytojas.vardas} {mokytojas.pavarde}, dėsto: {mokytojas.dalykas}")

# 7. Rikiavimas ir skaičiavimai
# Užduotis:
# • Parašykite funkciją, kuri išveda visus mokinius pagal klasę (didėjančia tvarka).
# • Parašykite funkciją, kuri suskaičiuoja, kiek yra mokinukų kiekvienoje klasėje.
# Papildomas iššūkis:
# • Suskaičiuokite vidutinį mokinių skaičių klasėje.

from sqlalchemy import func

def list_students_by_class():
    mokiniai = session.query(Mokinys).order_by(Mokinys.klase).all()
    for mokinys in mokiniai:
        print(f"Mokinys: {mokinys.id} {mokinys.vardas} {mokinys.pavarde}, klasė: {mokinys.klase}")

def count_students_per_class():
    class_counts = session.query(Mokinys.klase, func.count(Mokinys.id)).group_by(Mokinys.klase).all()
    for klase, count in class_counts:
        print(f'Klasė {klase}: {count} mokiniai')

def average_students_per_class():
    total_students = session.query(func.count(Mokinys.id)).scalar()
    total_classes = session.query(func.count(func.distinct(Mokinys.klase))).scalar()
    avg_students = total_students / total_classes if total_classes else 0
    print(f'Vidutinis mokinių skaičius klasėje: {avg_students:.2f}')






# Testuojame funkcijas
print("Mokiniai:")
spausdinti_mokinius()

print("\nMokytojai:")
spausdinti_mokytojus()

delete_student_by_id(3)
delete_teacher_by_id(2)
# delete_graduated_students()
find_student_by_name("Jonas")
find_students_by_lastname_initial("P")
find_teachers_by_name_endswith("s")
list_students_by_class()
count_students_per_class()
average_students_per_class()
