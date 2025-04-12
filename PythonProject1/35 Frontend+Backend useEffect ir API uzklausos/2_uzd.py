# 3. Duomenų gavimas iš Flask API
# Užduotis:
# 1. Sukurkite Flask API, kuris grąžina produktų sąrašą (produkto_pavadinimas,
# kaina).
# 2. Sukurkite React komponentą Produktai.js, kuris kreipiasi į šį API
# (http://localhost:5000/api/produktai).
# 3. Atvaizduokite produktus lentelėje.
# Rezultatas:
# Flask API, kuris grąžina produktų duomenis, ir React komponentas, kuris juos atvaizduoja.


from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Leidžia React aplikacijai pasiekti API

# Produktų sąrašas
produktai = [
    {"id":1, "produkto_pavadinimas": "Obuolys", "kaina": 1.20},
    {"id":2, "produkto_pavadinimas": "Bananai", "kaina": 0.80},
    {"id":3, "produkto_pavadinimas": "Pienas", "kaina": 1.50},
    {"id":4, "produkto_pavadinimas": "Duona", "kaina": 1.10},
]

@app.route('/api/produktai', methods=['GET'])
def get_produktai():
    return jsonify(produktai)

app.run(port=5000)