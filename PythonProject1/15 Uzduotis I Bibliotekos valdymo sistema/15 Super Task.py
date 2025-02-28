# Užduotis: Sukurkite paprastą bibliotekos valdymo sistemą

# 1. Reikalavimai:
# • Sukurti dvi klases: Book ir Library.
# • Naudoti datetime modulį knygų paskolos laikotarpiams valdyti.
# • Naudoti *args ir **kwargs knygų filtravimui.
# • Naudoti try-except klaidų valdymui.


# 2. Žingsniai:
# ŽINGSNIS 1: Sukurkite klasę Book
# • Laukai:
# o title (pavadinimas)
# o author (autorius)
# o year (išleidimo metai)
# o available (ar knyga prieinama) – pagal nutylėjimą True
# • Metodai:
# o __str__ – grąžina informaciją apie knygą gražiu formatu.
# o is_classic() – grąžina True, jei knyga išleista daugiau nei prieš 50 metų.

# ŽINGSNIS 2: Sukurkite klasę Library
# • Laukai:
# o books (sąrašas, kuriame saugomos knygos)
# • Metodai:
# o add_book(book) – prideda naują Book objektą į biblioteką.
# o display_books() – atvaizduoja visas knygas bibliotekoje.
# o borrow_book(title) – leidžia pasiskolinti knygą, jei ji prieinama.
# ▪ Naudoti try-except, kad suvaldytumėte klaidas (pvz., jei knygos
# nėra).
# o return_book(title) – leidžia grąžinti knygą.
# o filter_books(*args, **kwargs) – leidžia filtruoti knygas pagal autorių,
# metus ar pavadinimą.
# ▪ Pvz.: filter_books(author="Jonas") arba
# filter_books(year=2000)


# ŽINGSNIS 3: Naudokite datetime paskolos valdymui
# • Kai vartotojas pasiskolina knygą, įrašykite paskolos datą.
# • Pridėkite metodą due_date(), kuris grąžins datą, kada knyga turi būti grąžinta
# (pvz., po 14 dienų).

# ŽINGSNIS 4: Sukurkite sąveiką su vartotoju
# • Naudokite while ciklą, kad vartotojas galėtų:
# o Pridėti naują knygą į biblioteką.
# o Peržiūrėti visą bibliotekos knygų sąrašą.
# o Pasiskolinti knygą.
# o Grąžinti knygą.
# o Filtruoti knygas pagal autorių, metus ar pavadinimą.
# o Išeiti iš programos.
# 3. Papildomos Sąlygos:
# • Naudokite try-except klaidoms suvaldyti, pvz., neteisingai įvedus metus.
# • Naudokite *args ir **kwargs knygų filtravimui pagal skirtingus kriterijus.



from datetime import datetime

class Book:
    country = "LT"

    def __init__(self,title, author, year, available = True):
        self.title = title
        self.author = author
        self.year = year
        self.available = available

    def __str__(self):
        return f'Pavadinimas: "{self.title}",  autorius: {self.author}, isleista  - {self.year}m'

    def is_classic(self):
        now = datetime.today()
        current_year = now.year
        return current_year - self.year > 50

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'Knyga "{book.title}" sekmingai prideta i biblioteka')

    def display_books(self):
        if not self.books:
            print('Knygu nera bibliotekoje')
        else:
            for book in self.books:
                print(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                book.available = False
                print(f'Knyga "{book.title}" sėkmingai pasiskolinta.')
                return
        print('Knyga nerasta arba ji jau pasiskolinta.')

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.available:
                book.available = True
                print(f'Knyga "{book.title}" sėkmingai grąžinta.')
                return
        print('Knyga nerasta arba ji jau buvo bibliotekoje.')

library = Library()
while True:
    print('1. Pridėti naują knygą į biblioteką')
    print('2. Peržiūrėti visą bibliotekos knygų sąrašą')
    print('3. Pasiskolinti knygą')
    print('4. Grąžinti knygą')
    print('5. Filtruoti knygas pagal autorių, metus ar pavadinimą')
    print('6. Išeiti iš programos')

    choice = input("Pasirinkimas: ")

    if choice == '1':
        title = input("Iveskite knygos pavadinima: ")
        author = input('Iveskite knygos autoriu: ')
        try:
            year = int(input('Iveskite leidybos metus:'))
            library.add_book(Book(title, author, year))
        except ValueError:
            print('Neteisingas metu formatas')
    elif choice == '2':
        library.display_books()
    elif choice == '3':
        title = input("Įveskite knygos, kurią norite pasiskolinti, pavadinimą: ")
        library.borrow_book(title)
    elif choice == '4':
        title = input("Įveskite knygos, kurią norite grąžinti, pavadinimą: ")
        library.return_book(title)
    elif choice == '6':
        print('Išeiti iš programos')
        break
    else:
        print('Neteisingas pasirinkimas')