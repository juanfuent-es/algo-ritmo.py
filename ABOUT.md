# 📖 Acerca de TaskMaster

## 🎓 Guía para Estudiantes Principiantes

Este proyecto está diseñado para enseñarte los conceptos básicos de desarrollo web de manera práctica y divertida. A continuación te explico cada parte del proyecto de forma sencilla.

## 🏗️ ¿Cómo está organizado el proyecto?

### 1. **app.py** - El cerebro de la aplicación
Este es el archivo principal que:
- Inicia el servidor web
- Define las rutas (URLs) que puedes visitar
- Maneja las peticiones del navegador
- Conecta el frontend con la base de datos

**Conceptos que aprenderás:**
- **Servidor web**: Programa que responde a peticiones del navegador
- **Rutas**: Direcciones web como `/api/tasks`
- **API**: Forma de comunicación entre programas

### 2. **models/** - Los datos y la base de datos
Esta carpeta contiene las clases que manejan la información:

#### **task.py** - La clase Tarea
```python
class Task:
    def __init__(self, title, description, priority, due_date):
        self.title = title          # Título de la tarea
        self.description = description  # Descripción
        self.priority = priority    # Prioridad (baja, media, alta)
        self.due_date = due_date    # Fecha de vencimiento
        self.completed = False      # Si está completada
```

**Conceptos que aprenderás:**
- **Clase**: Plantilla para crear objetos
- **Atributos**: Características de un objeto
- **Métodos**: Acciones que puede hacer un objeto

#### **database.py** - Manejo de la base de datos
Esta clase se encarga de:
- Guardar tareas en la base de datos
- Recuperar tareas de la base de datos
- Actualizar tareas existentes
- Eliminar tareas

**Conceptos que aprenderás:**
- **Base de datos**: Lugar donde se guarda información permanentemente
- **SQLite**: Tipo de base de datos simple (un archivo)
- **CRUD**: Crear, Leer, Actualizar, Eliminar datos

### 3. **templates/** - Las páginas web
Esta carpeta contiene los archivos HTML que se muestran en el navegador:

#### **base.html** - El diseño base
- Define el diseño general de todas las páginas
- Incluye Bootstrap para hacer la página bonita
- Contiene la barra de navegación
- Define los estilos CSS

#### **index.html** - La página principal
- Muestra la lista de tareas
- Contiene las tarjetas de estadísticas
- Incluye los filtros y botones

#### **modals.html** - Ventanas emergentes
- Formulario para crear/editar tareas
- Ventana de confirmación para eliminar
- Mensajes de éxito y error

**Conceptos que aprenderás:**
- **HTML**: Lenguaje para estructurar páginas web
- **CSS**: Lenguaje para dar estilo a las páginas
- **Bootstrap**: Biblioteca que facilita el diseño
- **Template**: Plantilla reutilizable

### 4. **static/js/app.js** - La interactividad
Este archivo hace que la página sea interactiva:
- Maneja los clics en botones
- Envía datos al servidor
- Actualiza la página sin recargar
- Muestra mensajes al usuario

**Conceptos que aprenderás:**
- **JavaScript**: Lenguaje para hacer páginas interactivas
- **Eventos**: Acciones del usuario (clic, envío de formulario)
- **AJAX**: Envío de datos sin recargar la página
- **DOM**: Estructura de la página web

## 🔄 ¿Cómo funciona todo junto?

### Flujo de una acción típica (crear tarea):

1. **Usuario hace clic en "Agregar Tarea"**
   - JavaScript detecta el clic
   - Abre una ventana emergente (modal)

2. **Usuario llena el formulario y hace clic en "Guardar"**
   - JavaScript recoge los datos del formulario
   - Envía los datos al servidor (Flask)

3. **Servidor recibe los datos**
   - Flask recibe la petición en `/api/tasks`
   - Crea un objeto Task con los datos
   - Lo guarda en la base de datos

4. **Servidor responde**
   - Envía confirmación al navegador
   - JavaScript recibe la respuesta

5. **Página se actualiza**
   - JavaScript actualiza la lista de tareas
   - Muestra mensaje de éxito
   - Cierra la ventana emergente

## 🎯 Patrón MVC (Modelo-Vista-Controlador)

Este proyecto sigue el patrón MVC, que es una forma organizada de escribir código:

### **Modelo (Model)**
- **task.py**: Define qué es una tarea
- **database.py**: Maneja cómo se guardan las tareas

### **Vista (View)**
- **templates/**: Los archivos HTML que se ven en el navegador
- **static/js/app.js**: La interactividad de la interfaz

### **Controlador (Controller)**
- **app.py**: Maneja las peticiones y conecta modelo con vista

## 🛠️ Tecnologías explicadas de forma simple

### **Flask**
- Framework de Python para crear aplicaciones web
- Como un "constructor" que te da herramientas para hacer sitios web
- Muy simple para principiantes

### **Bootstrap**
- Biblioteca de CSS que hace las páginas bonitas
- Te da botones, formularios y diseños ya hechos
- Responsive (se ve bien en móviles y computadoras)

### **JavaScript**
- Lenguaje que hace las páginas interactivas
- Se ejecuta en el navegador del usuario
- Permite actualizar la página sin recargar

### **SQLite**
- Base de datos muy simple
- Se guarda en un archivo (no necesitas instalar nada más)
- Perfecta para proyectos pequeños

## 📚 Conceptos importantes que aprenderás

### **Frontend vs Backend**
- **Frontend**: Lo que ves en el navegador (HTML, CSS, JavaScript)
- **Backend**: Lo que procesa datos en el servidor (Python, Flask)

### **Cliente-Servidor**
- **Cliente**: Tu navegador web
- **Servidor**: El programa Python que responde a las peticiones

### **API REST**
- Forma estándar de comunicar frontend con backend
- Usa URLs y métodos HTTP (GET, POST, PUT, DELETE)

### **Base de datos**
- Lugar donde se guarda información permanentemente
- Permite buscar, filtrar y organizar datos

## 🎨 Características del diseño

### **Interfaz de usuario**
- Diseño limpio y moderno
- Colores que indican prioridad (rojo=alta, amarillo=media, verde=baja)
- Iconos intuitivos
- Responsive (funciona en móviles)

### **Experiencia de usuario**
- Mensajes de confirmación
- Indicadores de carga
- Validación de formularios
- Filtros fáciles de usar

## 🔧 Personalización y mejoras

### **Cosas que puedes agregar fácilmente:**
- Categorías para las tareas
- Notificaciones por email
- Exportar tareas a PDF
- Temas de colores
- Búsqueda de tareas

### **Para practicar más:**
- Agregar usuarios y contraseñas
- Compartir tareas entre usuarios
- Calendario de tareas
- Recordatorios automáticos

## 🎓 Consejos para aprender

1. **Empieza simple**: No te abrumes con todo de una vez
2. **Experimenta**: Cambia colores, textos, funcionalidades
3. **Lee el código**: Entiende qué hace cada línea
4. **Haz preguntas**: No hay preguntas tontas
5. **Practica**: Crea tus propios proyectos pequeños

## 🚀 Próximos pasos

Después de entender este proyecto, puedes aprender:
- Más Python (clases, decoradores, manejo de errores)
- Más JavaScript (funciones, promesas, frameworks)
- Más bases de datos (MySQL, PostgreSQL)
- Más frameworks web (Django, FastAPI)
- Despliegue en la web (Heroku, AWS, Vercel)

---

**¡Recuerda: La programación es como aprender un idioma nuevo. Toma tiempo, pero es muy gratificante! 🌟** 