# algoRitmo.py - Módulo de acceso a datos y gestión de la base de datos
# Proyecto: algoRitmo.py
# Autor: JuanFuent.es
# Descripción: Este archivo define la clase Database, que maneja la conexión y operaciones CRUD sobre SQLite.
# Documentación SQLite: https://docs.python.org/3/library/sqlite3.html
# Documentación sobre patrones DAO: https://en.wikipedia.org/wiki/Data_access_object
#
# Referencias:
# - https://flask.palletsprojects.com/en/2.3.x/patterns/sqlite3/
# - https://docs.python.org/3/library/datetime.html
#
import sqlite3
import os
from typing import List, Optional
from datetime import datetime
from .task import Task

class Database:
    """
    Clase que maneja todas las operaciones de base de datos SQLite.
    Implementa el patrón Model del MVC para la persistencia de datos.
    """
    
    def __init__(self, db_path: str):
        """
        Inicializa la conexión a la base de datos.
        
        Args:
            db_path (str): Ruta al archivo de base de datos SQLite
        """
        self.db_path = db_path
        self._ensure_database_directory()
    
    def _ensure_database_directory(self) -> None:
        """Asegura que el directorio de la base de datos existe"""
        db_dir = os.path.dirname(self.db_path)
        if db_dir and not os.path.exists(db_dir):
            os.makedirs(db_dir)
    
    def _get_connection(self) -> sqlite3.Connection:
        """
        Obtiene una conexión a la base de datos.
        
        Returns:
            sqlite3.Connection: Conexión a la base de datos
        """
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Permite acceder a las columnas por nombre
        return conn
    
    def init_database(self) -> None:
        """Inicializa la base de datos creando las tablas necesarias (si no existen).
        Crea la tabla 'tasks' para almacenar las tareas del usuario.
        """
        conn = self._get_connection()
        cursor = conn.cursor()
        # Crear tabla de tareas si no existe
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                priority TEXT DEFAULT 'medium',
                due_date TEXT,
                completed BOOLEAN DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()
    
    def create_task(self, task: Task) -> int:
        """
        Crea una nueva tarea en la base de datos.
        
        Args:
            task (Task): Tarea a crear
            
        Returns:
            int: ID de la tarea creada
        """
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO tasks (title, description, priority, due_date, completed, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            task.title,
            task.description,
            task.priority,
            task.due_date,
            task.completed,
            task.created_at,
            task.updated_at
        ))
        
        task_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return task_id
    
    def get_all_tasks(self) -> List[Task]:
        """
        Obtiene todas las tareas de la base de datos.
        
        Returns:
            List[Task]: Lista de todas las tareas
        """
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, title, description, priority, due_date, completed, created_at, updated_at
            FROM tasks
            ORDER BY created_at DESC
        ''')
        
        tasks = []
        for row in cursor.fetchall():
            task = Task(
                id=row['id'],
                title=row['title'],
                description=row['description'],
                priority=row['priority'],
                due_date=row['due_date'],
                completed=bool(row['completed'])
            )
            task.created_at = datetime.fromisoformat(row['created_at'])
            task.updated_at = datetime.fromisoformat(row['updated_at'])
            tasks.append(task)
        
        conn.close()
        return tasks
    
    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Obtiene una tarea por su ID.
        
        Args:
            task_id (int): ID de la tarea
            
        Returns:
            Optional[Task]: Tarea encontrada o None si no existe
        """
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, title, description, priority, due_date, completed, created_at, updated_at
            FROM tasks
            WHERE id = ?
        ''', (task_id,))
        
        row = cursor.fetchone()
        conn.close()
        
        if row:
            task = Task(
                id=row['id'],
                title=row['title'],
                description=row['description'],
                priority=row['priority'],
                due_date=row['due_date'],
                completed=bool(row['completed'])
            )
            task.created_at = datetime.fromisoformat(row['created_at'])
            task.updated_at = datetime.fromisoformat(row['updated_at'])
            return task
        
        return None
    
    def update_task(self, task: Task) -> bool:
        """
        Actualiza una tarea existente en la base de datos.
        
        Args:
            task (Task): Tarea a actualizar
            
        Returns:
            bool: True si la actualización fue exitosa, False en caso contrario
        """
        if not task.id:
            return False
        
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE tasks
            SET title = ?, description = ?, priority = ?, due_date = ?, 
                completed = ?, updated_at = ?
            WHERE id = ?
        ''', (
            task.title,
            task.description,
            task.priority,
            task.due_date,
            task.completed,
            datetime.now(),
            task.id
        ))
        
        rows_affected = cursor.rowcount
        conn.commit()
        conn.close()
        
        return rows_affected > 0
    
    def delete_task(self, task_id: int) -> bool:
        """
        Elimina una tarea de la base de datos.
        
        Args:
            task_id (int): ID de la tarea a eliminar
            
        Returns:
            bool: True si la eliminación fue exitosa, False en caso contrario
        """
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        
        rows_affected = cursor.rowcount
        conn.commit()
        conn.close()
        
        return rows_affected > 0
    
    def get_tasks_by_priority(self, priority: str) -> List[Task]:
        """
        Obtiene todas las tareas de una prioridad específica.
        
        Args:
            priority (str): Prioridad de las tareas a buscar
            
        Returns:
            List[Task]: Lista de tareas con la prioridad especificada
        """
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, title, description, priority, due_date, completed, created_at, updated_at
            FROM tasks
            WHERE priority = ?
            ORDER BY created_at DESC
        ''', (priority,))
        
        tasks = []
        for row in cursor.fetchall():
            task = Task(
                id=row['id'],
                title=row['title'],
                description=row['description'],
                priority=row['priority'],
                due_date=row['due_date'],
                completed=bool(row['completed'])
            )
            task.created_at = datetime.fromisoformat(row['created_at'])
            task.updated_at = datetime.fromisoformat(row['updated_at'])
            tasks.append(task)
        
        conn.close()
        return tasks
    
    def get_completed_tasks(self) -> List[Task]:
        """
        Obtiene todas las tareas completadas.
        
        Returns:
            List[Task]: Lista de tareas completadas
        """
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, title, description, priority, due_date, completed, created_at, updated_at
            FROM tasks
            WHERE completed = 1
            ORDER BY updated_at DESC
        ''')
        
        tasks = []
        for row in cursor.fetchall():
            task = Task(
                id=row['id'],
                title=row['title'],
                description=row['description'],
                priority=row['priority'],
                due_date=row['due_date'],
                completed=bool(row['completed'])
            )
            task.created_at = datetime.fromisoformat(row['created_at'])
            task.updated_at = datetime.fromisoformat(row['updated_at'])
            tasks.append(task)
        
        conn.close()
        return tasks
    
    def get_pending_tasks(self) -> List[Task]:
        """
        Obtiene todas las tareas pendientes.
        
        Returns:
            List[Task]: Lista de tareas pendientes
        """
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, title, description, priority, due_date, completed, created_at, updated_at
            FROM tasks
            WHERE completed = 0
            ORDER BY created_at DESC
        ''')
        
        tasks = []
        for row in cursor.fetchall():
            task = Task(
                id=row['id'],
                title=row['title'],
                description=row['description'],
                priority=row['priority'],
                due_date=row['due_date'],
                completed=bool(row['completed'])
            )
            task.created_at = datetime.fromisoformat(row['created_at'])
            task.updated_at = datetime.fromisoformat(row['updated_at'])
            tasks.append(task)
        
        conn.close()
        return tasks 