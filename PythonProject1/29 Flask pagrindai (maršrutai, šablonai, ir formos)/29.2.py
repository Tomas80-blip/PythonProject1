# 1. Pagrindiniai maršrutai ir dinaminių parametrų naudojimas
# Užduotis:
# Sukurkite Flask aplikaciją, kurioje būtų šie maršrutai:
# 1. Pagrindinis puslapis /, kuris grąžina "Sveiki atvykę į Flask aplikaciją!".
# 2. Puslapis /apie, kuris grąžina "Tai yra apie mus puslapis.".
# 3. Puslapis /vartotojas/<vardas>, kuris priima vartotojo vardą ir grąžina "Sveiki,
# [vardas]!".
# 4. Puslapis /skaicius/<int:nr>, kuris priima skaičių ir grąžina "Jūs įvedėte
# skaičių: [nr]".
# Papildoma užduotis:
# Sukurkite maršrutą /kelione/<start>/<end>, kuris grąžina "Kelionės maršrutas:
# iš [start] į [end]".

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Sveiki atvykę į Flask aplikaciją!"

@app.route("/apie")
def apie():
    return "Tai yra apie mus puslapis."

@app.route("/vartotojas/<vardas>")
def vartotojas(vardas):
    return f"Sveiki, {vardas}!"

@app.route("/skaicius/<int:nr>")
def news_item(nr):
    return f"Jūs įvedėte skaičių: {nr}"

@app.route("/kelione/<start>/<end>")
def kelione(start,end):
    return f"Kelionės maršrutas: iš {start} į {end}"

app.run()