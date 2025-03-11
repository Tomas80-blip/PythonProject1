# 3. Apskaičiuojamas property
# Užduotis:
# 1. Pridėkite metodą @property, kuris kiekvienam mokiniui apskaičiuoja sekančią
# kalsė (pvz klasė + 1).
# 2. Pagrindiniame puslapyje atvaizduokite ne tik klasę bet ir sekanti klasė.


# 4. Pridėkite naujų projektų įterpimo funkcionalumą (CREATE)
# Užduotis:
# 1. Sukurkite puslapį /prideti-mokini, kuris rodo POST formą su laukais:
# a. Vardas
# b. Pavarde
# c. Klasė
# 2. Kai vartotojas pateikia formą, duomenys turi būti išsaugoti duomenų bazėje.
# Papildoma užduotis:
# Padarykite, kad po mokinio pridėjimo vartotojas būtų nukreiptas atgal į pagrindinį puslapį.


from flask import Flask, render_template, request, redirect, url_for #pridedam redirect, url_for
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

    @property
    def sekanti_klase(self):
        # Calculate the next class
        return self.klase + 1


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


# Page to add a new student
@app.route('/prideti-mokini', methods=['GET', 'POST'])
def prideti_mokini():
    if request.method == 'POST':
        vardas = request.form['vardas']
        pavarde = request.form['pavarde']
        klase = request.form['klase']

        new_student = Mokinys(vardas=vardas, pavarde=pavarde, klase=int(klase))

        db.session.add(new_student)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('prideti_mokini.html')

app.run()