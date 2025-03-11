# Darbovietės valdymas
# Tikslas
# Sukurti internetinę aplikaciją, kuri leis administruoti darbovietes ir jų darbuotojus. Naudojant Flask
# ir SQLAlchemy, aplikacija turės CRUD funkcionalumą darbovietėms ir darbuotojams.
# Sąsaja turės paprastą dizainą su HTML + CSS, o duomenys bus saugomi SQLite duomenų bazėje.
#
# 1. Sistemos funkcionalumas
# 1.1. Darboviečių valdymas
# Sąrašo peržiūra: Vartotojas mato visų darboviečių sąrašą.
# Naujos darbovietės pridėjimas: Leidžia įvesti pavadinimą, miestą, darbuotojų skaičių.
# Darbovietės redagavimas: Galima keisti pavadinimą, miestą ir darbuotojų skaičių.
# Darbovietės šalinimas: Galima ištrinti darbovietę tik tada, jei ji neturi darbuotojų.
# 1.2. Darbuotojų valdymas
# Sąrašo peržiūra: Vartotojas gali matyti visus darbuotojus ir jų darbovietę.
# Naujo darbuotojo pridėjimas: Leidžia įvesti vardą, pavardę, darbo poziciją ir priskirti darbovietę.
# Darbuotojo redagavimas: Leidžia keisti darbuotojo duomenis.
# Darbuotojo pašalinimas: Leidžia ištrinti darbuotoją iš duomenų bazės.
# 1.3. Papildomas funkcionalumas
# Paieška: Galimybė ieškoti darboviečių pagal pavadinimą ir miestą.
# Statistika: Kiekvienos darbovietės puslapyje rodomas darbuotojų skaičius.

# 2. Sistemos architektūra
# Backend: Flask su SQLAlchemy (ORM)
# Frontend: HTML + CSS
# Duomenų bazė: SQLite
# Duomenų modeliai
# Darbovietė: id, pavadinimas, miestas, darbuotoju_skaicius
# Darbuotojas: id, vardas, pavarde, pareigos, darboviete_id (ForeignKey)

# 3. Techniniai reikalavimai
# 3.1. Backend (Flask + SQLAlchemy)
# Flask aplikacija su darboviečių ir darbuotojų CRUD operacijomis.
# SQLAlchemy modeliai darboviečių ir darbuotojų valdymui.
# Užklausų optimizavimas (naudoti JOIN santykiams tarp darbuotojų ir darboviečių).

# API endpoint’ai:
# / – darboviečių sąrašas.
# /darboviete/<int:id> – darbovietės peržiūra.
# /prideti-darboviete – naujos darbovietės kūrimas.
# /redaguoti-darboviete/<int:id> – darbovietės redagavimas.
# /trinti-darboviete/<int:id> – darbovietės trynimas.
# /darbuotojai – darbuotojų sąrašas.
# /prideti-darbuotoja – naujo darbuotojo pridėjimas.
# /redaguoti-darbuotoja/<int:id> – darbuotojo redagavimas.
# /trinti-darbuotoja/<int:id> – darbuotojo šalinimas.

# 3.2. Frontend (HTML + CSS)
# HTML šablonai darboviečių ir darbuotojų peržiūrai, pridėjimui, redagavimui.
# CSS stilius:
# Mygtukai: pridėti ( žalia ), redaguoti ( mėlyna ), ištrinti ( raudona ).
# Lentelės darbuotojų ir darboviečių atvaizdavimui.
# Formos duomenų įvedimui su tvarkingomis etiketėmis.


from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///darbovietes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # # Išjungia SQLAlchemy įspėjimus apie pakeitimus


db = SQLAlchemy(app)


class Darboviete(db.Model):
    __tablename__ = 'darboviete'

    id = db.Column(db.Integer, primary_key=True)
    pavadinimas = db.Column(db.String, nullable=False, unique=True)
    miestas = db.Column(db.String,nullable=False)
    darbuotojai = db.relationship('Darbuotojas', backref='darboviete')

    @property
    def darbuotoju_skaicius(self):
        return len(self.darbuotojai)


class Darbuotojas(db.Model):
    __tablename__ = 'darbuotojas'

    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column(db.String, nullable=False)
    pavarde = db.Column(db.String, nullable=False)
    pareigos = db.Column(db.String, nullable=False)
    darboviete_id = db.Column(db.Integer, db.ForeignKey("darboviete.id"), nullable=False)

with app.app_context():
    db.create_all()

#Endpointai:
# darboviečių sąrašas suranda ieskoma darboviete
@app.route('/')
def index():
    search_query = request.args.get('search', '')
    if search_query:
        darbovietes = Darboviete.query.filter(Darboviete.pavadinimas.ilike(f'%{search_query}%')).all()
    else:
        darbovietes = Darboviete.query.all()
    return render_template('darbovietes.html', darbovietes=darbovietes)
#darbovietes=darbovietes perduoda į HTML šabloną darboviečių sąrašą(i for'a), kad jis galėtų būti
# atvaizduotas puslapyje.
#

#perziureti viena darboviete
@app.route('/darboviete/<int:id>')
def perziureti_darboviete(id):
    darboviete = Darboviete.query.get(id)
    if darboviete:
        return render_template('darboviete.html', darboviete=darboviete)
    return 'Bloga nuoruoda i projekta!'

@app.route('/prideti-darboviete', methods=['GET', 'POST'])
def prideti_darboviete():
    if request.method == 'POST':
        pavadinimas = request.form['pavadinimas']
        miestas = request.form['miestas']
        nauja_darboviete = Darboviete(pavadinimas=pavadinimas, miestas=miestas)
        db.session.add(nauja_darboviete)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('prideti_darboviete.html')

@app.route('/redaguoti-darboviete/<int:id>', methods=['GET', 'POST'])
def redaguoti_darboviete(id):
    darboviete = Darboviete.query.get(id)
    if request.method == 'POST':
        darboviete.pavadinimas = request.form['pavadinimas']
        darboviete.miestas = request.form['miestas']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('redaguoti_darboviete.html', darboviete=darboviete)

# darbovietes salinimas
@app.route('/trinti-darboviete/<int:id>', methods=['POST'])
def trinti_darboviete(id):
    darboviete = Darboviete.query.get(id)
    if darboviete.darbuotojai:
        return 'Negalima istrinti darbovietes, kurioje yra darbuotoju!'
    db.session.delete(darboviete)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/darbuotojai')
def darbuotojai():
    darbuotojai = Darbuotojas.query.all()
    return render_template('darbuotojai.html', darbuotojai=darbuotojai)


@app.route('/prideti-darbuotoja', methods=['GET', 'POST'])
def prideti_darbuotoja():
    darbovietes = Darboviete.query.all()
    if request.method == 'POST':
        vardas = request.form['vardas']
        pavarde = request.form['pavarde']
        pareigos = request.form['pareigos']
        darboviete_id = request.form['darboviete_id']
        naujas_darbuotojas = Darbuotojas(vardas=vardas, pavarde=pavarde, pareigos=pareigos,darboviete_id=darboviete_id)
        db.session.add(naujas_darbuotojas)
        db.session.commit()
        return redirect(url_for('darbuotojai'))
    return render_template('prideti_darbuotoja.html', darbovietes=darbovietes)

@app.route ('/redaguoti-darbuotoja/<int:id>', methods=['GET', 'POST'])
def redaguoti_darbuotoja(id):
    darbuotojas = Darbuotojas.query.get(id)
    darbovietes = Darboviete.query.all()
    if request.method == 'POST':
        darbuotojas.vardas = request.form['vardas']
        darbuotojas.pavarde = request.form['pavarde']
        darbuotojas.pareigos = request.form['pareigos']
        darbuotojas.darboviete_id = request.form['darboviete_id']
        db.session.commit()
        return redirect(url_for('darbuotojai'))
    return render_template('redaguoti_darbuotoja.html', darbuotojas=darbuotojas, darbovietes=darbovietes)

@app.route('/trinti-darbuotoja/<int:id>', methods= ['POST'])
def trinti_darbuotoja(id):
    darbuotojas= Darbuotojas.query.get(id)
    db.session.delete(darbuotojas)
    db.session.commit()
    return redirect(url_for('darbuotojai'))

app.run()