# 1. Klasės kūrimas ir statiniai laukai
# Užduotis 1:
# 1. Sukurkite klasę Car, kurioje būtų statinis laukas manufacturer su reikšme
# "Toyota".
# 2. Išveskite manufacturer reikšmę.
# 3. Sukurkite kitą klasę Bike, kurioje būtų statinis laukas manufacturer su reikšme
# "Yamaha" ir taip pat išveskite šią reikšmę.

class Car:#klase
    manufacture = "Toyota" #statinis laukas

print(Car.manufacture)  # Toyota

class Bike:
    manufacture = "Yamaha"

print(Bike.manufacture)  # Yamaha

# 2. Konstruktorius __init__ ir instancijos laukų inicializavimas
# Užduotis 2:
# 1. Sukurkite klasę Book, kuri turės laukus: title, author, year.
# 2. Naudodami __init__ konstruktorių, inicializuokite šiuos laukus.
# 3. Sukurkite kelias Book instancijas su skirtingais duomenimis.

class Book:
    def __init__(self, title,author,year):
        self.title = title
        self.author = author
        self.year = year
book1 = Book('Roma', 'Petras Cvirka', 1960)
book2 = Book('Drasiuju Keliai', 'O. Hemingvejus', 1970)
print(f'Book 1: {book1.title},Author: {book1.author}, Year: {book1.year}')
print(f'Book 2: {book2.title},Author: {book2.author}, Year: {book2.year}')

# 3. Statinio lauko ir instancijų naudojimas
# Užduotis 3:
# 1. Naudodami klasę Book iš ankstesnės užduoties, išveskite:
# a. Statinį lauką publisher (pridėkite jį kaip "Penguin").
# b. Kiekvienos knygos pavadinimą ir autorių.

class Book:
    publisher = "Penguin"  # Statinis laukas

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year



book1 = Book('Roma', 'Petras Cvirka', 1960)
book2 = Book('Drasiųjų Keliai', 'O. Hemingvejus', 1970)

# statinis laukas
print(f"Leidykla: {Book.publisher}")

print(f"Knyga: '{book1.title}', Autorius: {book1.author}")
print(f"Knyga: '{book2.title}', Autorius: {book2.author}")

# arba
books = [book1, book2]

for book in books:
    print(f"Knyga: '{book.title}', Autorius: {book.author}")