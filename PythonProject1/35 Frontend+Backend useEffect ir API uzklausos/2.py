from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

vartotojai = [
    {'id': 1, 'vardas': 'Jonas', 'amzius': 25},
    {'id': 2, 'vardas': 'Laura', 'amzius': 30},
]

@app.route('/api/vartotojai', methods=['GET', 'POST'])
def handle_vartotojai():
    if not request.method == 'POST':
        return jsonify(vartotojai)
    naujas_vartotojas = request.json
    naujas_vartotojas['id'] = len(vartotojai) + 1
    vartotojai.append(naujas_vartotojas)
    return jsonify(naujas_vartotojas), 201

app.run(port=5000)

#
# from flask import Flask, jsonify, request
# from flask_cors import CORS
#
# app = Flask(__name__)
# CORS(app)
#
# @app.route('/api/zmones')
# def get_zmones():
#     # if user != admin
#     #     return 'neturite pakankamai teisiu sitai info!'
#     zmones = [
#         {'id': 1, 'vardas': 'Jonas', 'amzius': 25},
#         {'id': 1, 'vardas': 'Laura', 'amzius': 30},
#         {'id': 1, 'vardas': 'Petras', 'amzius': 40},
#     ]
#     return jsonify(zmones)
# app.run(port=5000)
