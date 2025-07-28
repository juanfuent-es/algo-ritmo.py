# algoRitmo.py - Aplicación principal Flask para gestión de tareas
# Proyecto: algoRitmo.py
# Autor: JuanFuent.es
# Descripción: Este archivo inicia la aplicación web Flask, configura rutas y conecta con la base de datos.
# Documentación Flask: https://flask.palletsprojects.com/
# Documentación oficial Python: https://docs.python.org/3/
#
# Este archivo es el punto de entrada de la app. Aquí se inicializa la base de datos y se definen los endpoints principales.
#
# Referencias:
# - https://flask.palletsprojects.com/en/2.3.x/tutorial/
# - https://docs.python.org/3/library/sqlite3.html
#

from flask import Flask, render_template, request, jsonify, redirect, url_for, Response
from models.task import Task
from models.database import Database
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

# Configuración de la base de datos
# Se crea una instancia de la clase Database, que gestiona la conexión y operaciones con SQLite.
database = Database(app.config['DATABASE_PATH'])

# Inicializar la base de datos al crear la aplicación
# Esto asegura que la tabla 'tasks' exista antes de cualquier operación.
with app.app_context():
    database.init_database()

# Variables de entorno seguras para autenticación
USER = os.environ.get("APP_USER")
PASSWORD = os.environ.get("APP_PASSWORD")

def check_auth(username, password):
    return username == USER and password == PASSWORD

def authenticate():
    return Response(
        "Acceso restringido", 401,
        {"WWW-Authenticate": 'Basic realm="Login Required'"}
    )

def require_auth(f):
    def wrapper(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper

# Endpoint principal: muestra la lista de tareas en la página de inicio
@app.route('/')
@require_auth
def index():
    """Página principal que muestra la lista de tareas"""
    tasks = database.get_all_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/api/tasks', methods=['GET'])
@require_auth
def get_tasks():
    """API endpoint para obtener todas las tareas"""
    tasks = database.get_all_tasks()
    return jsonify([task.to_dict() for task in tasks])

@app.route('/api/tasks', methods=['POST'])
@require_auth
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
@require_auth
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
@require_auth
def delete_task(task_id):
    """API endpoint para eliminar una tarea"""
    task = database.get_task_by_id(task_id)
    if not task:
        return jsonify({'error': 'Tarea no encontrada'}), 404
    
    database.delete_task(task_id)
    return jsonify({'message': 'Tarea eliminada exitosamente'})

@app.route('/api/tasks/<int:task_id>/toggle', methods=['PUT'])
@require_auth
def toggle_task(task_id):
    """API endpoint para cambiar el estado de completado de una tarea"""
    task = database.get_task_by_id(task_id)
    if not task:
        return jsonify({'error': 'Tarea no encontrada'}), 404
    
    task.completed = not task.completed
    database.update_task(task)
    return jsonify(task.to_dict())

# Endpoint de salud para monitoreo y pruebas automáticas
@app.route('/health')
def health_check():
    """Endpoint para verificar el estado de la aplicación"""
    return jsonify({'status': 'healthy', 'message': 'TaskMaster API is running'})

if __name__ == '__main__':
    app.run(
        debug=app.config['DEBUG'],
        host=app.config['HOST'],
        port=app.config['PORT']
    ) 
