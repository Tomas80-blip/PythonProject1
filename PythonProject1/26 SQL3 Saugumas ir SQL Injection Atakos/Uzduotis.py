# SQL Injection Atakos Demonstracija
# Užduotis:
# 1. Sukurkite lentelę admin_users su šiais laukais:
# a. id (pirminis raktas, INTEGER)
# b. username (TEXT, unikalus)
# c. password (TEXT, negali būti NULL)
# d. role (TEXT, numatytoji reikšmė "user")
# 2. Įterpkite tris vartotojus: vieną administratorių (role="admin") ir du paprastus
# vartotojus.
# 3. Parašykite SQL užklausą, kuri leidžia prisijungti vartotojui pagal username ir
# password, tačiau nenaudokite parametrizuotų užklausų.
# 4. Naudodami SQL Injection techniką prisijunkite prie administratoriaus paskyros,
# nors nežinote slaptažodžio.

# SQL Injection Atakų Prevencija
# Užduotis:
# 1. Pataisykite ankstesnę užklausą, kad ji būtų apsaugota nuo SQL Injection,
# naudodami parametrizuotas užklausas.
# 2. Pabandykite prisijungti naudodami ' OR 1=1;-- kaip username. Ar sistema vis dar
# pažeidžiama?


import sqlite3
conn = sqlite3.connect("sql_injection1.db")
c = conn.cursor()

# query = """CREATE TABLE admin_users (
#     id INTEGER PRIMARY KEY,
#     username TEXT UNIQUE,
#     password TEXT NOT NULL,
#     role TEXT DEFAULT 'user'
# );
# """
#
# with conn:
#     c.execute(query)

# -- 2. Įterpiame tris vartotojus
# with conn:
#     c.execute("INSERT INTO admin_users VALUES(1, 'admin', 'admin123', 'admin')")
#     c.execute("INSERT INTO admin_users VALUES(2, 'user1', 'password1', 'user')")
#     c.execute("INSERT INTO admin_users VALUES(3, 'user2', 'password2', 'user')")

# STEP 1 : Check if users created
# with conn:
#     c.execute('SELECT * FROM admin_users;')
# print(c.fetchall())



# 3. Parašykite SQL užklausą, kuri leidžia prisijungti vartotojui pagal username ir
# password, tačiau nenaudokite parametrizuotų užklausų.
# inp_username = input("Įveskite username: ")
# inp_password = input("Įveskite slaptažodį: ")
#
# query = f"SELECT * FROM admin_users WHERE admin_users.username='{inp_username}' AND admin_users.password='{inp_password}';"
#
# with conn:
#     print('>>>>>>>>', query)
#     c.execute(query)
#     res = c.fetchall()
#     if res:
#         print("Jūsų profilio duomenys yra:")
#         print(res)
#     else:
#         print(f"Vartotojas {inp_username} neegzistuoja arba neteisingas slaptažodis")

# 4. Naudodami SQL Injection techniką prisijunkite prie administratoriaus paskyros,
# nors nežinote slaptažodžio.

# print('---------------Atakos Demonstracija---------------')
# inp_username = "' OR True;--"
# inp_password = ""
#
# query = f"SELECT * FROM admin_users WHERE admin_users.username='{inp_username}' AND admin_users.password='{inp_password}';"
#
# with conn:
#     print("=>>>>> ", query)
#     c.execute(query)
#     res = c.fetchall()
#     print("Jūsų profilio duomenys yra:", res)

print('---------------Atakos Prevencijs---------------')

# 4 SQL Injection apsauga naudojant parametrizuotas užklausas
inp_username = "' OR True;--"
inp_password = ""

with conn:
    c.execute("SELECT * FROM admin_users WHERE admin_users.username=? AND admin_users.password=?;", (inp_username, inp_password))
    res = c.fetchall()
    if res:
        print("Jūsų profilio duomenys yra:")
        print(res)
    else:
        print(f"Vartotojas {inp_username} neegzistuoja arba neteisingas slaptažodis")


# dest

