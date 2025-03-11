# 3. Flask šablonai ir duomenų perdavimas į HTML
# Užduotis:
# Sukurkite templates/index1.html šabloną, kuriame:
# Rodomas pasveikinimo pranešimas.
# Yra nuoroda į /vartotojai puslapį.
# Sukurkite maršrutą /vartotojai, kuris perduoda vardų sąrašą į šabloną
# vartotojai.html ir jame visi vardai išvedami per {% for ... %} ciklą.
# Papildoma užduotis:
# Pakeiskite HTML taip, kad kiekvienas vardas būtų pateiktas kaip nuoroda į
# /vartotojas/<vardas>.



from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/vartotojai')
def vartotojai():
    vardai = ["Jonas", "Petras", "Asta", "Laura", "Mantas"]
    return render_template('vartotojai.html', vardai=vardai)

@app.route('/vartotojas/<vardas>')
def vartotojas(vardas):
    return f"Vartotojo puslapis: {vardas}"

app.run()