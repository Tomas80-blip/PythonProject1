# Užduotis: Knygų valdymo aplikacija su Flask ir React
#
# Tikslas Sukurti web aplikaciją, leidžiančią vartotojams valdyti knygų sąrašą.
# Aplikacija turės galimybę pridėti, peržiūrėti, redaguoti ir ištrinti knygas,
# naudojant Flask kaip backend ir React kaip frontend.
#
# Užduoties aprašymas Jūsų užduotis - sukurti dvi aplikacijos dalis:
#
# 1. Backend (Flask + SQLite)
# Sukurti Flask serverį.
# Naudoti SQLite duomenų bazę.
# Sukurti "Book" modelį su laukais:
# id (unikalus identifikatorius)
# title (knygos pavadinimas)
# author (autorius)
# year (išleidimo metai)
# Įdiegti šiuos API maršrutus:
# Gauti visas knygas (GET /books)
# Pridėti knygą (POST /books)
# Redaguoti knygą (PUT /books/)
# Ištrinti knygą (DELETE /books/)
# API grąžins duomenis JSON formatu.
# Naudoti CORS, kad frontend galėtų pasiekti backend.


# 2. Frontend (React + Fetch API)
# Sukurti React aplikaciją su pagrindiniu komponentu App.js.
# Naudoti fetch API jungimui su backend.
# Implementuoti šias funkcijas:
# Atvaizduoti knygų sąrašą.
# Pridėti knygą.
# Redaguoti knygą.
# Ištrinti knygą.
# Sukurti UI su laukais knygos pavadinimui, autoriui ir metams.
# Pridėti mygtukus pridėti, redaguoti ir ištrinti knygas.
# Papildomos užduotys
#
# Pridėti klaidų pranešimus (pvz., jei neįvesti visi reikalingi duomenys).
# Patobulinti UI naudojant CSS.
# Sukurti paieškos funkciją knygų sąraše.


from flask import Flask, request, jsonify
from flask_cors import CORS
from database import db
from models import Book


# ------------------ CONFIGURATION ------------------ #

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db.init_app(app)

with app.app_context():
    db.create_all()

# ------------------ API ROUTES ------------------ #

@app.route('/books', methods=['GET'])
def get_books():
    """
    Gauti visas knygas
    """
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

@app.route('/books', methods=['POST'])
def add_book():
    """
    Prideti knyga
    """
    data = request.json
    if not all(k in data for k in ('title', 'author', 'year')):
        return jsonify({'error': 'Trūksta duomenų'}), 400

    new_book = Book(title=data['title'], author=data['author'], year=int(data['year']))
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    """
    Atnaujinti knyga
    """
    book = Book.query.get(book_id)
    if book is None:
        return jsonify({'error': 'Book not found'}), 404

    data = request.json
    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.year = data.get('year', book.year)

    db.session.commit()

    return jsonify(book.to_dict())

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    """
    Istrinti knyga
    """
    book = Book.query.get(book_id)
    if book is None:
        return jsonify({'error': 'Book not found'}), 404

    db.session.delete(book)
    db.session.commit()

    return '', 204

app.run()