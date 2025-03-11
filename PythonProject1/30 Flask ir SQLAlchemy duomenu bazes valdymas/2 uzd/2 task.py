# 2. Pridėkite duomenų paiešką ir filtravimą
# Užduotis:
# 1. Sukurkite GET formą, kuri leidžia ieškoti mokinų pagal vardą.
# 2. Kai vartotojas įveda paieškos frazę ir paspaudžia „Ieškoti“, turi būti rodomi tik tie
# mokiniai, kurių vardas prasidės įvesta fraze.
# Papildoma užduotis:
# Leiskite naudoti dalinę paiešką (LIKE %fraze%), kad rezultatuose būtų rodomi mokiniai,
# turintys įvestą frazę bet kurioje vardo vietoje.

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

    def __init__(self, vardas, pavarde, klase):
        self.vardas = vardas
        self.pavarde = pavarde
        self.klase = klase

    def __repr__(self):
        return f'{self.id} {self.vardas} {self.pavarde} {self.klase} {self.sukurimo_data}'


with app.app_context():
    db.create_all()

mokiniai = [
    ("Jonas", "Jonaitis", 5),
    ("Petras", "Petraitis", 6),
    ("Asta", "Astaitė", 7),
    ("Giedrius", "Giedraitis", 9),
    ("Meta", "Metaite", 12),
    ("Tadas", "Tadaitis", 12)
]

with app.app_context():
    if not Mokinys.query.first():
        for vardas, pavarde, klase in mokiniai:
            db.session.add(Mokinys(vardas, pavarde, klase))
        db.session.commit()


@app.route('/', methods=['GET'])
def index():
    search_query = request.args.get('search', '')
    if search_query:
        mokiniai = Mokinys.query.filter(Mokinys.vardas.ilike(f'%{search_query}%')).all()
    else:
        mokiniai = Mokinys.query.all()
    return render_template('index.html', mokiniai=mokiniai, search_query=search_query)

app.run()