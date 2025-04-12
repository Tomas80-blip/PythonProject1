from flask import Flask, request, jsonify
from flask_cors import CORS
from database import db
from models import Task

# ------------------ CONFIGURATION ------------------ #

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'
db.init_app(app)

with app.app_context():
    db.create_all()

# ------------------ API ROUTES ------------------ #

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """
    Gauti visas uzduotis
    """
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])

@app.route('/tasks', methods=['POST'])
def add_task():
    """
    Prideti taska
    """
    data = request.json
    new_task = Task(title=data['title'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.to_dict()), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """
    Atnaujinti taska
    """
    task = Task.query.get(task_id)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404

    data = request.json
    task.title = data.get('title', task.title)
    task.completed = data.get('completed', task.completed)

    db.session.commit()

    return jsonify(task.to_dict())

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404

    db.session.delete(task)
    db.session.commit()

    return '', 204

app.run()





