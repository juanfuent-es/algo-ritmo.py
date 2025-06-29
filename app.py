from flask import Flask, render_template, request, jsonify, redirect, url_for
from models.task import Task
from models.database import Database
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'tu_clave_secreta_aqui')

# Configuración de la base de datos
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database', 'tasks.db')
database = Database(db_path)

@app.route('/')
def index():
    """Página principal que muestra la lista de tareas"""
    tasks = database.get_all_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """API endpoint para obtener todas las tareas"""
    tasks = database.get_all_tasks()
    return jsonify([task.to_dict() for task in tasks])

@app.route('/api/tasks', methods=['POST'])
def create_task():
    """API endpoint para crear una nueva tarea"""
    data = request.get_json()
    
    if not data or 'title' not in data:
        return jsonify({'error': 'El título es requerido'}), 400
    
    task = Task(
        title=data['title'],
        description=data.get('description', ''),
        priority=data.get('priority', 'medium'),
        due_date=data.get('due_date', None)
    )
    
    task_id = database.create_task(task)
    task.id = task_id
    
    return jsonify(task.to_dict()), 201

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """API endpoint para actualizar una tarea existente"""
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'Datos requeridos'}), 400
    
    task = database.get_task_by_id(task_id)
    if not task:
        return jsonify({'error': 'Tarea no encontrada'}), 404
    
    # Actualizar campos
    if 'title' in data:
        task.title = data['title']
    if 'description' in data:
        task.description = data['description']
    if 'priority' in data:
        task.priority = data['priority']
    if 'due_date' in data:
        task.due_date = data['due_date']
    if 'completed' in data:
        task.completed = data['completed']
    
    database.update_task(task)
    return jsonify(task.to_dict())

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """API endpoint para eliminar una tarea"""
    task = database.get_task_by_id(task_id)
    if not task:
        return jsonify({'error': 'Tarea no encontrada'}), 404
    
    database.delete_task(task_id)
    return jsonify({'message': 'Tarea eliminada exitosamente'})

@app.route('/api/tasks/<int:task_id>/toggle', methods=['PUT'])
def toggle_task(task_id):
    """API endpoint para cambiar el estado de completado de una tarea"""
    task = database.get_task_by_id(task_id)
    if not task:
        return jsonify({'error': 'Tarea no encontrada'}), 404
    
    task.completed = not task.completed
    database.update_task(task)
    return jsonify(task.to_dict())

# Crear la base de datos al iniciar la aplicación
@app.before_first_request
def init_database():
    """Inicializar la base de datos antes del primer request"""
    database.init_database()

if __name__ == '__main__':
    # Configuración para desarrollo local
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    # Crear la base de datos si no existe
    database.init_database()
    
    app.run(debug=debug, host='0.0.0.0', port=port) 