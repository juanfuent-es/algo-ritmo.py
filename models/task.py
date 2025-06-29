from datetime import datetime
from typing import Optional, Dict, Any

class Task:
    """
    Clase que representa una tarea en el sistema de todo list.
    Implementa el patrón Model del MVC.
    """
    
    def __init__(self, title: str, description: str = "", priority: str = "medium", 
                 due_date: Optional[str] = None, completed: bool = False, id: Optional[int] = None):
        """
        Inicializa una nueva tarea.
        
        Args:
            title (str): Título de la tarea
            description (str): Descripción de la tarea
            priority (str): Prioridad de la tarea (low, medium, high)
            due_date (Optional[str]): Fecha de vencimiento en formato YYYY-MM-DD
            completed (bool): Estado de completado de la tarea
            id (Optional[int]): ID único de la tarea
        """
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = completed
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convierte la tarea a un diccionario para serialización JSON.
        
        Returns:
            Dict[str, Any]: Diccionario con los datos de la tarea
        """
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'due_date': self.due_date,
            'completed': self.completed,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
    
    def mark_completed(self) -> None:
        """Marca la tarea como completada"""
        self.completed = True
        self.updated_at = datetime.now()
    
    def mark_incomplete(self) -> None:
        """Marca la tarea como incompleta"""
        self.completed = False
        self.updated_at = datetime.now()
    
    def toggle_completed(self) -> None:
        """Cambia el estado de completado de la tarea"""
        self.completed = not self.completed
        self.updated_at = datetime.now()
    
    def is_overdue(self) -> bool:
        """
        Verifica si la tarea está vencida.
        
        Returns:
            bool: True si la tarea está vencida, False en caso contrario
        """
        if not self.due_date or self.completed:
            return False
        
        try:
            due_date = datetime.strptime(self.due_date, '%Y-%m-%d')
            return due_date.date() < datetime.now().date()
        except ValueError:
            return False
    
    def get_priority_color(self) -> str:
        """
        Obtiene el color CSS para la prioridad de la tarea.
        
        Returns:
            str: Clase CSS para el color de prioridad
        """
        priority_colors = {
            'low': 'text-success',
            'medium': 'text-warning',
            'high': 'text-danger'
        }
        return priority_colors.get(self.priority, 'text-secondary')
    
    def get_priority_badge(self) -> str:
        """
        Obtiene el badge de Bootstrap para la prioridad.
        
        Returns:
            str: Clase CSS del badge de Bootstrap
        """
        priority_badges = {
            'low': 'badge bg-success',
            'medium': 'badge bg-warning',
            'high': 'badge bg-danger'
        }
        return priority_badges.get(self.priority, 'badge bg-secondary')
    
    def __str__(self) -> str:
        """Representación en string de la tarea"""
        status = "✓" if self.completed else "○"
        return f"[{status}] {self.title} ({self.priority})"
    
    def __repr__(self) -> str:
        """Representación detallada de la tarea para debugging"""
        return f"Task(id={self.id}, title='{self.title}', completed={self.completed}, priority='{self.priority}')" 