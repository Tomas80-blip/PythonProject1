# 1. Žodyno sukūrimas ir duomenų pasiekimas
# Užduotis 1:
# Sukurkite programą, kuri:
# 1. Sukurtų žodyną apie mokyklą, kuriame yra:
# a. pavadinimas: mokyklos pavadinimas.
# b. mokytojai: sąrašas žodynų apie mokytojus. Kiekvienas mokytojas turi:
# i. vardas, pavardė, mokomas_dalykas.
# c. mokinių_skaičius: mokinių skaičius.
# 2. Atliktų šiuos veiksmus:
# a. Išspausdintų pirmo mokytojo vardą ir mokomą dalyką.
# b. Patikrintų, ar mokykloje yra daugiau nei 500 mokinių, ir atspausdintų
# atitinkamą žinutę.

mokykla = {
    "Pavadinimas": "Saules",
    "Mokytojai": {
        'Lietuviu': {
            'Vardas': 'Ona',
            'Pavarde': 'Lape',
            'Mokomas_dalykas': 'Lietuviu'
        },
        'Istorijos': {
            'Vardas': 'Rasa',
            'Pavarde': 'Snaige',
            'Mokomas_dalykas': 'Istorija'
        },
        'Matematikos': {
            'Vardas': 'Lina',
            'Pavarde': 'Kate',
            'Mokomas_dalykas': 'Matematika'

        }
    },
    'Mokiniu_skaicius': 700

}
print(type(mokykla))
print(mokykla['Mokytojai']['Lietuviu']['Vardas'])
print(mokykla['Mokytojai']['Lietuviu']['Mokomas_dalykas'])


if mokykla['Mokiniu_skaicius'] > 500:
    print('Mokiniu daugiau nei 500')
else:
    print('Mokiniu maziau nei 500')

# 2. Reikšmių pasiekimas pagal raktus
# Užduotis 2:
# Turite šį žodyną apie įmonės darbuotojus:
# company = {
#   "name": "TechCorp",
#   "employees": [ {"name": "Jonas", "role": "Developer",
# "salary": 3000}, {"name": "Asta", "role": "Designer", "salary": 2500}, {"name": "Tomas",
# "role": "Manager", "salary": 4000} ], "location": "Vilnius", "industry": "IT" }
# Atlikite šiuos veiksmus:
# 1. Gaukite ir išspausdinkite visų darbuotojų vardus bei jų pareigas.
# 2. Apskaičiuokite ir išspausdinkite visų darbuotojų atlyginimų vidurkį.
# 3. Patikrinkite, ar žodyne yra raktas location. Jei yra, atspausdinkite jo reikšmę.

company = {
    "name": "TechCorp",
    "employees": [ {"name": "Jonas", "role": "Developer","salary": 3000},
                   {"name": "Asta", "role": "Designer", "salary": 2500},
                   {"name": "Tomas","role": "Manager", "salary": 4000} ],
    "location": "Vilnius",
    "industry": "IT",
    }

for darbuotojas in company["employees"]:
    print(f'Vardas: {darbuotojas["name"]}, Pareigos: {darbuotojas["role"]}')

suma = 0
for darbuotojas in company["employees"]:
    suma+=darbuotojas['salary']
vidurkis = suma/ len(company["employees"])
print(f'Algu vidurkis:{vidurkis}')

print(company.get('location'))
#arba
print(company['location'])

# 3. Iteracija per žodyną
# Užduotis 3:
# Turite žodyną apie knygų biblioteką:
# library = { "books": [ {"title": "1984", "author": "George Orwell", "copies": 3}, {"title": "To Kill a
# Mockingbird", "author": "Harper Lee", "copies": 5}, {"title": "The Great Gatsby", "author": "F.
# Scott Fitzgerald", "copies": 2} ], "location": "Kaunas", "open_hours": {"start": "8:00", "end":
# "20:00"} }
# Atlikite šiuos veiksmus:
# 1. Iteruokite per knygų sąrašą ir išspausdinkite knygos pavadinimą bei autorių.
# 2. Suraskite knygą su mažiausiai kopijų ir išspausdinkite jos pavadinimą.

library = {
    "books": [ {"title": "1984", "author": "George Orwell", "copies": 3},
               {"title": "To Kill aMockingbird", "author": "Harper Lee", "copies": 5},
               {"title": "The Great Gatsby", "author": "F.Scott Fitzgerald", "copies": 2} ],
    "location": "Kaunas", "open_hours": {"start": "8:00", "end":"20:00"} }

print('Knygų sąrašas:')
for book in library['books']:
    print(f'Pavadinimas: {book["title"]}, autorius: {book["author"]}')

min_copies_book = library['books'][0]
for book in library['books']:
    if book['copies'] < min_copies_book['copies']:
        min_copies_book = book
print(f'Knyga su mažiausiai kopijų: {min_copies_book["title"]}')



# Pradžioje sukuriamas tuščias žodynas auto, kuris vėliau pildomas duomenimis apie automobilį.
# Naujų raktų-reikšmių porų pridėjimas ir esamų reikšmių keitimas.

# pradedam nuo tuščio
auto = {}
print(auto)

# pildom duomenimis
auto["make"] = "Audi"
print(auto)  # {'make': 'Audi'}

auto["make"] = "BMW"
print(auto)  # {'make': 'BMW'}

auto["model"] = "x5"
print(auto)  # {'make': 'BMW', 'model': 'x5'}

auto["colors"] = ["red", "white", "black"]
print(auto)  # {'make': 'BMW', 'model': 'x5', 'colors': ['red', 'white', 'black']}


# Toliau žodynas papildomas kitų žodynų informacija, naudojant .update() metodą.

# keletos žodynų sujungimas
bonus_info = {"engine": 2, "interior": "leather"}
auto.update(bonus_info)
print(auto)  # {'make': 'BMW', 'model': 'x5', 'colors': ['red', 'white', 'black'], 'engine': 2, 'interior': 'leather'}

auto.update({"year": 2000, "eco2000": True})
print(auto)  # {'make': 'BMW', 'model': 'x5', 'colors': ['red', 'white', 'black'], 'engine': 2, 'interior': 'leather', 'year': 2000, 'eco2000': True}