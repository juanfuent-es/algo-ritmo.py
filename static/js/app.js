/**
 * TaskMaster - Sistema de Control de Tareas
 * JavaScript principal para el manejo de la interfaz de usuario
 */

// Variables globales
let currentTaskId = null;
let isEditing = false;

// Clase principal de la aplicación
class TaskManager {
    constructor() {
        this.tasks = [];
        this.currentFilter = 'all';
        this.init();
    }

    init() {
        this.setupEventListeners();
        this.loadTasks();
        this.updateStatistics();
    }

    // Configurar event listeners
    setupEventListeners() {
        // Botón de agregar tarea
        document.getElementById('addTaskBtn')?.addEventListener('click', () => this.openTaskModal());
        document.getElementById('addFirstTask')?.addEventListener('click', () => this.openTaskModal());

        // Formulario de tarea
        document.getElementById('taskForm')?.addEventListener('submit', (e) => this.handleTaskSubmit(e));

        // Botones de navegación
        document.getElementById('nav-all')?.addEventListener('click', (e) => this.filterTasks('all', e));
        document.getElementById('nav-pending')?.addEventListener('click', (e) => this.filterTasks('pending', e));
        document.getElementById('nav-completed')?.addEventListener('click', (e) => this.filterTasks('completed', e));

        // Botones de acción
        document.getElementById('refreshBtn')?.addEventListener('click', () => this.loadTasks());
        document.getElementById('filterBtn')?.addEventListener('click', () => this.toggleFilterSection());

        // Filtros
        document.getElementById('priorityFilter')?.addEventListener('change', () => this.applyFilters());
        document.getElementById('statusFilter')?.addEventListener('change', () => this.applyFilters());
        document.getElementById('dateFilter')?.addEventListener('change', () => this.applyFilters());
        document.getElementById('clearFilters')?.addEventListener('click', () => this.clearFilters());

        // Preview de prioridad
        document.getElementById('taskPriority')?.addEventListener('change', () => this.updatePriorityPreview());

        // Confirmación de eliminación
        document.getElementById('confirmDeleteBtn')?.addEventListener('click', () => this.confirmDeleteTask());

        // Event delegation para elementos dinámicos
        document.addEventListener('click', (e) => this.handleDynamicEvents(e));
    }

    // Manejar eventos de elementos dinámicos
    handleDynamicEvents(e) {
        // Checkbox de completado
        if (e.target.classList.contains('task-checkbox')) {
            this.toggleTaskComplete(e.target.dataset.taskId);
        }

        // Botones de editar
        if (e.target.closest('.edit-task')) {
            e.preventDefault();
            const taskId = e.target.closest('.task-item').dataset.taskId;
            this.editTask(taskId);
        }

        // Botones de eliminar
        if (e.target.closest('.delete-task')) {
            e.preventDefault();
            const taskId = e.target.closest('.task-item').dataset.taskId;
            this.deleteTask(taskId);
        }
    }

    // Cargar tareas desde el servidor
    async loadTasks() {
        try {
            this.showLoading(true);
            const response = await fetch('/api/tasks');
            
            if (!response.ok) {
                throw new Error('Error al cargar las tareas');
            }

            this.tasks = await response.json();
            this.renderTasks();
            this.updateStatistics();
        } catch (error) {
            this.showError('Error al cargar las tareas: ' + error.message);
        } finally {
            this.showLoading(false);
        }
    }

    // Renderizar tareas en la interfaz
    renderTasks() {
        const container = document.getElementById('tasksContainer');
        const emptyState = document.getElementById('emptyState');
        const taskCount = document.getElementById('taskCount');

        if (!container) return;

        // Filtrar tareas según el filtro actual
        let filteredTasks = this.getFilteredTasks();

        // Actualizar contador
        if (taskCount) {
            taskCount.textContent = `${filteredTasks.length} tarea${filteredTasks.length !== 1 ? 's' : ''}`;
        }

        // Mostrar estado vacío si no hay tareas
        if (filteredTasks.length === 0) {
            container.innerHTML = '';
            if (emptyState) {
                emptyState.style.display = 'block';
            }
            return;
        }

        // Ocultar estado vacío
        if (emptyState) {
            emptyState.style.display = 'none';
        }

        // Renderizar tareas
        container.innerHTML = '';
        filteredTasks.forEach(task => {
            const taskElement = this.createTaskElement(task);
            container.appendChild(taskElement);
        });
    }

    // Crear elemento HTML para una tarea
    createTaskElement(task) {
        const template = document.getElementById('taskTemplate');
        if (!template) return document.createElement('div');

        const clone = template.content.cloneNode(true);
        const taskItem = clone.querySelector('.task-item');

        // Configurar datos
        taskItem.dataset.taskId = task.id;
        taskItem.classList.add(`priority-${task.priority}`);

        if (task.completed) {
            taskItem.classList.add('task-completed');
        }

        // Verificar si está vencida
        if (this.isTaskOverdue(task)) {
            taskItem.classList.add('overdue');
        }

        // Configurar checkbox
        const checkbox = taskItem.querySelector('.task-checkbox');
        checkbox.checked = task.completed;
        checkbox.dataset.taskId = task.id;

        // Configurar título
        const title = taskItem.querySelector('.task-title');
        title.textContent = task.title;

        // Configurar descripción
        const description = taskItem.querySelector('.task-description');
        description.textContent = task.description || 'Sin descripción';

        // Configurar badge de prioridad
        const priorityBadge = taskItem.querySelector('.task-priority-badge');
        priorityBadge.textContent = this.getPriorityText(task.priority);
        priorityBadge.className = `task-priority-badge badge ${this.getPriorityBadgeClass(task.priority)}`;

        // Configurar fecha de vencimiento
        const dueDate = taskItem.querySelector('.task-due-date');
        if (task.due_date) {
            dueDate.textContent = `Vence: ${this.formatDate(task.due_date)}`;
        } else {
            dueDate.style.display = 'none';
        }

        // Configurar badge de vencida
        const overdueBadge = taskItem.querySelector('.task-overdue-badge');
        if (this.isTaskOverdue(task)) {
            overdueBadge.style.display = 'inline';
        }

        return taskItem;
    }

    // Obtener tareas filtradas
    getFilteredTasks() {
        let filtered = [...this.tasks];

        // Aplicar filtro de estado
        switch (this.currentFilter) {
            case 'pending':
                filtered = filtered.filter(task => !task.completed);
                break;
            case 'completed':
                filtered = filtered.filter(task => task.completed);
                break;
        }

        // Aplicar filtros adicionales
        const priorityFilter = document.getElementById('priorityFilter')?.value;
        const statusFilter = document.getElementById('statusFilter')?.value;
        const dateFilter = document.getElementById('dateFilter')?.value;

        if (priorityFilter) {
            filtered = filtered.filter(task => task.priority === priorityFilter);
        }

        if (statusFilter) {
            if (statusFilter === 'pending') {
                filtered = filtered.filter(task => !task.completed);
            } else if (statusFilter === 'completed') {
                filtered = filtered.filter(task => task.completed);
            }
        }

        if (dateFilter) {
            filtered = filtered.filter(task => task.due_date === dateFilter);
        }

        return filtered;
    }

    // Filtrar tareas
    filterTasks(filter, event) {
        event?.preventDefault();
        this.currentFilter = filter;
        
        // Actualizar navegación activa
        document.querySelectorAll('.nav-link').forEach(link => link.classList.remove('active'));
        event?.target.classList.add('active');
        
        this.renderTasks();
    }

    // Aplicar filtros adicionales
    applyFilters() {
        this.renderTasks();
    }

    // Limpiar filtros
    clearFilters() {
        document.getElementById('priorityFilter').value = '';
        document.getElementById('statusFilter').value = '';
        document.getElementById('dateFilter').value = '';
        this.renderTasks();
    }

    // Mostrar/ocultar sección de filtros
    toggleFilterSection() {
        const filterSection = document.getElementById('filterSection');
        if (filterSection) {
            filterSection.style.display = filterSection.style.display === 'none' ? 'block' : 'none';
        }
    }

    // Abrir modal de tarea
    openTaskModal(task = null) {
        isEditing = !!task;
        currentTaskId = task?.id || null;

        const modal = new bootstrap.Modal(document.getElementById('taskModal'));
        const modalTitle = document.getElementById('taskModalLabel');
        const form = document.getElementById('taskForm');

        // Configurar título del modal
        if (modalTitle) {
            modalTitle.innerHTML = isEditing ? 
                '<i class="bi bi-pencil me-2"></i>Editar Tarea' : 
                '<i class="bi bi-plus-circle me-2"></i>Nueva Tarea';
        }

        // Limpiar formulario
        form.reset();

        // Llenar datos si es edición
        if (task) {
            document.getElementById('taskTitle').value = task.title;
            document.getElementById('taskDescription').value = task.description || '';
            document.getElementById('taskPriority').value = task.priority;
            document.getElementById('taskDueDate').value = task.due_date || '';
        }

        this.updatePriorityPreview();
        modal.show();
    }

    // Manejar envío del formulario
    async handleTaskSubmit(event) {
        event.preventDefault();

        const formData = new FormData(event.target);
        const taskData = {
            title: formData.get('title'),
            description: formData.get('description'),
            priority: formData.get('priority'),
            due_date: formData.get('due_date') || null
        };

        try {
            this.showLoading(true);
            
            const url = isEditing ? `/api/tasks/${currentTaskId}` : '/api/tasks';
            const method = isEditing ? 'PUT' : 'POST';

            const response = await fetch(url, {
                method: method,
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(taskData)
            });

            if (!response.ok) {
                throw new Error('Error al guardar la tarea');
            }

            const result = await response.json();
            
            // Cerrar modal
            const modal = bootstrap.Modal.getInstance(document.getElementById('taskModal'));
            modal.hide();

            // Recargar tareas
            await this.loadTasks();

            // Mostrar mensaje de éxito
            this.showSuccess(isEditing ? 'Tarea actualizada exitosamente' : 'Tarea creada exitosamente');

        } catch (error) {
            this.showError('Error al guardar la tarea: ' + error.message);
        } finally {
            this.showLoading(false);
        }
    }

    // Editar tarea
    editTask(taskId) {
        const task = this.tasks.find(t => t.id == taskId);
        if (task) {
            this.openTaskModal(task);
        }
    }

    // Cambiar estado de completado
    async toggleTaskComplete(taskId) {
        try {
            const response = await fetch(`/api/tasks/${taskId}/toggle`, {
                method: 'PUT'
            });

            if (!response.ok) {
                throw new Error('Error al cambiar el estado de la tarea');
            }

            const updatedTask = await response.json();
            
            // Actualizar tarea en la lista local
            const index = this.tasks.findIndex(t => t.id == taskId);
            if (index !== -1) {
                this.tasks[index] = updatedTask;
            }

            this.renderTasks();
            this.updateStatistics();

        } catch (error) {
            this.showError('Error al cambiar el estado: ' + error.message);
        }
    }

    // Eliminar tarea
    deleteTask(taskId) {
        const task = this.tasks.find(t => t.id == taskId);
        if (task) {
            document.getElementById('deleteTaskTitle').textContent = task.title;
            currentTaskId = taskId;
            
            const modal = new bootstrap.Modal(document.getElementById('deleteModal'));
            modal.show();
        }
    }

    // Confirmar eliminación
    async confirmDeleteTask() {
        try {
            const response = await fetch(`/api/tasks/${currentTaskId}`, {
                method: 'DELETE'
            });

            if (!response.ok) {
                throw new Error('Error al eliminar la tarea');
            }

            // Cerrar modal
            const modal = bootstrap.Modal.getInstance(document.getElementById('deleteModal'));
            modal.hide();

            // Recargar tareas
            await this.loadTasks();

            // Mostrar mensaje de éxito
            this.showSuccess('Tarea eliminada exitosamente');

        } catch (error) {
            this.showError('Error al eliminar la tarea: ' + error.message);
        }
    }

    // Actualizar estadísticas
    updateStatistics() {
        const total = this.tasks.length;
        const completed = this.tasks.filter(t => t.completed).length;
        const pending = total - completed;
        const overdue = this.tasks.filter(t => this.isTaskOverdue(t)).length;

        document.getElementById('totalTasks').textContent = total;
        document.getElementById('pendingTasks').textContent = pending;
        document.getElementById('completedTasks').textContent = completed;
        document.getElementById('overdueTasks').textContent = overdue;
    }

    // Actualizar preview de prioridad
    updatePriorityPreview() {
        const priority = document.getElementById('taskPriority')?.value;
        const preview = document.getElementById('priorityPreview');
        const priorityText = document.getElementById('priorityText');
        const priorityDescription = document.getElementById('priorityDescription');

        if (!priority || !preview) return;

        const priorityInfo = {
            low: { text: 'Baja', description: 'Tareas que pueden esperar' },
            medium: { text: 'Media', description: 'Tareas importantes pero no urgentes' },
            high: { text: 'Alta', description: 'Tareas urgentes y críticas' }
        };

        priorityText.textContent = priorityInfo[priority].text;
        priorityDescription.textContent = priorityInfo[priority].description;
        preview.style.display = 'block';
    }

    // Utilidades
    isTaskOverdue(task) {
        if (!task.due_date || task.completed) return false;
        const today = new Date().toISOString().split('T')[0];
        return task.due_date < today;
    }

    getPriorityText(priority) {
        const texts = { low: 'Baja', medium: 'Media', high: 'Alta' };
        return texts[priority] || priority;
    }

    getPriorityBadgeClass(priority) {
        const classes = {
            low: 'bg-success',
            medium: 'bg-warning',
            high: 'bg-danger'
        };
        return classes[priority] || 'bg-secondary';
    }

    formatDate(dateString) {
        const date = new Date(dateString);
        return date.toLocaleDateString('es-ES', {
            year: 'numeric',
            month: 'short',
            day: 'numeric'
        });
    }

    // Mostrar/ocultar loading
    showLoading(show) {
        const spinner = document.getElementById('loadingSpinner');
        const container = document.getElementById('tasksContainer');
        
        if (spinner) {
            spinner.style.display = show ? 'block' : 'none';
        }
        
        if (container) {
            container.classList.toggle('loading', show);
        }
    }

    // Mostrar mensaje de éxito
    showSuccess(message) {
        document.getElementById('successMessage').textContent = message;
        const toast = new bootstrap.Toast(document.getElementById('successToast'));
        toast.show();
    }

    // Mostrar mensaje de error
    showError(message) {
        document.getElementById('errorMessage').textContent = message;
        const toast = new bootstrap.Toast(document.getElementById('errorToast'));
        toast.show();
    }
}

// Inicializar la aplicación cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', function() {
    window.taskManager = new TaskManager();
});

// Funciones globales para compatibilidad con el código existente
function loadTasks() {
    window.taskManager?.loadTasks();
}

function setupEventListeners() {
    // Los event listeners se configuran automáticamente en la clase TaskManager
}

function updateStatistics() {
    window.taskManager?.updateStatistics();
} 