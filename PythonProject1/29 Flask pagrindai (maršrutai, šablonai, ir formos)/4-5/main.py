# 4. GET ir POST formos su Flask
# Užduotis:
# 1. Sukurkite maršrutą /paieska, kuris rodo GET formą (forma_get.html).
# 2. Kai vartotojas įveda paieškos frazę ir paspaudžia „Ieškoti“, ji turi būti rodoma
# puslapyje.
# Papildoma užduotis:
# Sukurkite maršrutą /prisijungti, kuris naudoja POST metodą:
# 1. Rodo POST formą (forma_post.html).
# 2. Po prisijungimo parodo pranešimą: "Prisijungėte kaip: [vartotojo
# vardas]".

# 5. Paprasta registracijos forma su validacija
# Užduotis:
# 1. Sukurkite maršrutą /registracija, kuris rodo POST formą su laukais:
# a. Vartotojo vardas
# b. Slaptažodis
# c. Pakartotas slaptažodis
# 2. Kai vartotojas užpildo formą, patikrinkite:
# a. Ar visi laukai užpildyti.
# b. Ar slaptažodis sutampa su pakartotu slaptažodžiu.
# 3. Jei viskas gerai, parodykite "Sėkmingai užsiregistravote!", kitu atveju –
# klaidos pranešimą.
# Papildoma užduotis:
# Pridėkite validaciją, kad slaptažodis būtų bent 6 simbolių ilgio.

from flask import Flask, render_template, request

app = Flask(__name__)

# 4. GET forma
@app.route('/paieska', methods=['GET'])
def paieska():
    uzklausa = request.args.get('query', '')
    return render_template('forma_get.html', uzklausa=uzklausa)

# 4. POST prisijungimo forma
@app.route('/prisijungti', methods=['GET', 'POST'])
def prisijungti():
    if request.method == 'POST':
        vardas = request.form.get('vardas', '')
        return f"Prisijungėte kaip: {vardas}"
    return render_template('forma_post.html')

# 5. Registracijos forma su validacija
@app.route('/registracija', methods=['GET', 'POST'])
def registracija():
    klaida = None
    if request.method == 'POST':
        vardas = request.form.get('vardas', '')
        slaptazodis = request.form.get('slaptazodis', '')
        slaptazodis2 = request.form.get('slaptazodis2', '')

        if not vardas or not slaptazodis or not slaptazodis2:
            klaida = "Visi laukai turi būti užpildyti!"
        elif slaptazodis != slaptazodis2:
            klaida = "Slaptažodžiai nesutampa!"
        elif len(slaptazodis) < 6:
            klaida = "Slaptažodis turi būti bent 6 simbolių ilgio!"
        else:
            return "Sėkmingai užsiregistravote!"

    return render_template('forma_registracija.html', klaida=klaida)


app.run()
