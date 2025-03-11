
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projektai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


class Projektas(db.Model):
    __tablename__ = 'projektas'

    id = db.Column(db.Integer, primary_key=True)
    pavadinimas = db.Column(db.String)
    kaina = db.Column(db.Float)
    sukurimo_data = db.Column(db.DateTime, default=datetime.datetime.now)

    @property
    def kaina_su_pvm(self):
        return round(self.kaina * 1.21)

    def __init__(self, pavadinimas, kaina):
        self.pavadinimas = pavadinimas
        self.kaina = kaina

    def __repr__(self):
        return f'{self.id} {self.pavadinimas} {self.kaina} {self.sukurimo_data}'

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    search_text = request.args.get('searchlaukelis')
    if search_text:
        filtered_rows = Projektas.query.filter(Projektas.pavadinimas.ilike(search_text + '%'))
        return render_template('index.html', projektas_rows=filtered_rows)
    all_rows = Projektas.query.all()
    return render_template('index.html', projektas_rows=all_rows)

@app.route('/prideti-projekta', methods=['GET', 'POST'])
def new_project():
    if request.method == 'GET':
        return render_template('ivedimo_forma.html')
    elif request.method == 'POST':
        pavadinimas = request.form.get('laukelispavadinimas')
        try:
            kaina = float(request.form.get('laukeliskaina'))
        except ValueError:
            raise ValueError('Kaina shoud be float!')
        if pavadinimas and kaina:
            new_project_row = Projektas(pavadinimas, kaina)
            db.session.add(new_project_row)
            db.session.commit()
        return redirect(url_for('home')) # home - funkcijos pavinimas(endpoint "/")

@app.route('/trinti-projekta/<int:project_id>', methods=['POST'])
def delete_project(project_id):
    one_project_row = Projektas.query.get(project_id)
    if one_project_row:
        db.session.delete(one_project_row)
        db.session.commit()
    return redirect(url_for('home'))

@app.route('/redaguoti-projekta/<int:project_id>', methods=['GET', 'POST'])
def edit_project(project_id):
    one_project_row = Projektas.query.get(project_id)
    if not one_project_row:
        return 'projektas neegzistuoja'
    if request.method == 'GET':
        return render_template('redagavimo_forma.html', one_project_row=one_project_row)
    if request.method == 'POST':
        pavadinimas = request.form.get('laukelispavadinimas')
        try:
            kaina = float(request.form.get('laukeliskaina'))
        except ValueError:
            raise ValueError('kaina should be float!')

        one_project_row.pavadinimas = pavadinimas
        one_project_row.kaina = kaina
        db.session.commit()

        return redirect(url_for('home'))

@app.route('/projektai/<int:project_id>')
def one_project(project_id):
    one_project_row = Projektas.query.get(project_id)
    if one_project_row:
        return render_template('vienas_projektas.html', one_project_row=one_project_row)
    return 'Bloga nuoruoda i projekta!'



app.run()




























