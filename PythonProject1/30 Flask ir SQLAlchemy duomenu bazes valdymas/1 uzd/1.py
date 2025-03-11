# 1. Sukurkite Flask aplikaciją su SQLAlchemy duomenų baze
# Užduotis:
# Sukurkite Flask aplikaciją, kuri:
# 1. Naudoja SQLite duomenų bazę mokiniai.db.
# 2. Turi lentelę Mokiniai su laukais:
# a. id (pirminis raktas),
# b. vardas(tekstinis laukas),
# c. pavarde(tekstinis laukas),
# d. klase(skaičius)
# e. sukurimo_data (data su numatyta dabartine reikšme).
# 3. Pagrindiniame puslapyje (/) atvaizduoja visus mokinius.

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mokiniai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


class Mokinys(db.Model):
    __tablename__ = 'mokinys'

    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column(db.String)
    pavarde = db.Column(db.String)
    klase = db.Column(db.Integer)
    sukurimo_data = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, vardas, pavarde, klase): #konstruktorius
        self.vardas = vardas
        self.pavarde = pavarde
        self.klase = klase


    def __repr__(self): #leidzia graziai atvaizduoti
        return f'{self.id} {self.vardas} {self.pavarde} {self.klase} {self.sukurimo_data}'


with app.app_context(): #
    db.create_all() #sukuria visas lenteles

mokiniai = [
    ("Jonas", "Jonaitis", 5),
    ("Petras", "Petraitis", 6),
    ("Asta", "Astaitė", 7),
    ("Giedrius", "Giedraitis", 9),
    ("Meta","Metaite", 12),
    ("Tadas", "Tadaitis", 12)
]


with app.app_context():
    if not Mokinys.query.first():  # Patikrina, ar lentelė tuščia
        for  vardas, pavarde, klase in mokiniai:
            db.session.add(Mokinys( vardas, pavarde, klase))
        db.session.commit()


@app.route('/')
def home():
    all_rows = Mokinys.query.all()
    return render_template('index.html', Mokinys_rows=all_rows)


app.run()