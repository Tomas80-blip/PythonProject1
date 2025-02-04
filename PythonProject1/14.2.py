# 4. Klasės instancijų atvaizdavimas
# Užduotis 4:
# 1. Išveskite bet kurią Book instanciją naudojant print().
# 2. Pastebėkite rezultatą (turėtų būti atminties adresas).


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

book = Book("1984", "George Orwell", 1949)

print(book)

# 5. Savų metodų kūrimas klasėje
# Užduotis 5:
# 1. Pridėkite metodą get_book_age(), kuris grąžins, kiek metų praėjo nuo knygos
# išleidimo.
# 2. Sukurkite kelias knygas ir iškvieskite šį metodą.

from datetime import datetime
class Book:
    publisher = "Penguin"  # Statinis laukas

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_book_age(self):
        current_year =  datetime.now().year
        return current_year - self.year

#
# book1 = Book('Roma', 'Petras Cvirka', 1960)
# book2 = Book('Drasiųjų Keliai', 'O. Hemingvejus', 1970)
#
# age1 = book1.get_book_age()
# print(age1)
# age2 = book2.get_book_age()
# print(age2)
# arba

books = [
    Book("1984", "George Orwell", 1949),
    Book("To Kill a Mockingbird", "Harper Lee", 1960)
]

for book in books:
    print(f"Book: {book.title}, Age: {book.get_book_age()} years")

# 6. Metodų iškvietimas ir rezultatų naudojimas
# Užduotis 6:
# 1. Sukurkite Book instanciją ir naudokite get_book_age() metodą.
# 2. Išveskite rezultatą kartu su pranešimu:
# "Knyga <pavadinimas> yra <amžius> metų senumo."

book1 = Book('Roma', 'Petras Cvirka', 1970)
age = book1.get_book_age()
print(f"Knyga '{book1.title}' yra {age} metu senumo.")