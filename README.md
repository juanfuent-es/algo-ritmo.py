# 📝 TaskMaster - Sistema de Control de Tareas

Un sistema simple y efectivo para organizar tus tareas diarias, creado con tecnologías web básicas.

## 🎯 ¿Qué hace este proyecto?

Este es un **sistema de todo list** (lista de tareas) que te permite:
- ✅ Crear nuevas tareas
- 📝 Editar tareas existentes
- 🗑️ Eliminar tareas
- ☑️ Marcar tareas como completadas
- 🏷️ Asignar prioridades (Baja, Media, Alta)
- 📅 Establecer fechas de vencimiento
- 🔍 Filtrar tareas por estado y prioridad
- 📊 Ver estadísticas de tus tareas

## 🛠️ Tecnologías utilizadas

- **Flask**: Framework de Python para crear aplicaciones web
- **Bootstrap**: Biblioteca de CSS para hacer la interfaz bonita
- **JavaScript**: Para hacer la página interactiva
- **SQLite**: Base de datos simple (se guarda en un archivo)

## 📋 Requisitos previos

Antes de empezar, necesitas tener instalado:

1. **Python 3.8 o superior**
   - Descárgalo desde [python.org](https://www.python.org/downloads/)
   - Asegúrate de marcar "Add Python to PATH" durante la instalación

2. **Un editor de código**
   - Recomendamos [Visual Studio Code](https://code.visualstudio.com/)
   - O cualquier editor que prefieras

## 🚀 Instalación y configuración

### Paso 1: Descargar el proyecto
1. Descarga todos los archivos del proyecto
2. Colócalos en una carpeta de tu computadora
3. Abre esa carpeta en tu editor de código

### Paso 2: Crear un entorno virtual (recomendado)
Abre la terminal en la carpeta del proyecto y ejecuta:

**En Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**En macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Paso 3: Instalar dependencias
Con el entorno virtual activado, ejecuta:
```bash
pip install -r requirements.txt
```

### Paso 4: Ejecutar el proyecto
```bash
python app.py
```

### Paso 5: Abrir en el navegador
Ve a tu navegador web y abre:
```
http://localhost:5000
```

¡Listo! Ya deberías ver tu sistema de tareas funcionando.

## 🌐 Deploy en la web (Render.com)

¿Quieres que tu aplicación esté disponible en internet? Puedes desplegarla gratis en Render.com:

### Opción 1: Instalación automática
1. Sube tu código a GitHub
2. Ve a [render.com](https://render.com)
3. Conecta tu repositorio
4. ¡Listo! Tu app estará disponible en la web

### Opción 2: Configuración manual
Consulta el archivo `DEPLOY.md` para instrucciones detalladas.

## 📁 Estructura del proyecto

```
algo-ritmo.py/
├── app.py                 # Archivo principal de la aplicación
├── requirements.txt       # Lista de dependencias
├── render.yaml           # Configuración para Render.com
├── runtime.txt           # Versión de Python
├── Procfile              # Comando de inicio para producción
├── README.md             # Este archivo
├── ABOUT.md              # Información detallada del proyecto
├── DEPLOY.md             # Guía de deploy
├── INSTRUCCIONES_RAPIDAS.md # Instrucciones rápidas
├── models/               # Carpeta con las clases de datos
│   ├── __init__.py
│   ├── task.py           # Clase que representa una tarea
│   └── database.py       # Clase para manejar la base de datos
├── static/               # Archivos estáticos (CSS, JS, imágenes)
│   └── js/
│       └── app.js        # Código JavaScript del frontend
├── templates/            # Plantillas HTML
│   ├── base.html         # Plantilla base con el diseño general
│   ├── index.html        # Página principal
│   └── modals.html       # Ventanas emergentes
└── database/             # Carpeta donde se guarda la base de datos
    └── tasks.db          # Base de datos SQLite (se crea automáticamente)
```

## 🎮 Cómo usar la aplicación

### Crear una nueva tarea:
1. Haz clic en el botón azul flotante (+)
2. Llena el formulario:
   - **Título**: Nombre de la tarea (obligatorio)
   - **Descripción**: Detalles adicionales (opcional)
   - **Prioridad**: Baja, Media o Alta
   - **Fecha de vencimiento**: Cuándo debe estar lista (opcional)
3. Haz clic en "Guardar Tarea"

### Gestionar tareas:
- **Marcar como completada**: Haz clic en el checkbox
- **Editar**: Haz clic en los tres puntos (...) → Editar
- **Eliminar**: Haz clic en los tres puntos (...) → Eliminar

### Filtrar tareas:
- Usa los botones de navegación: "Todas", "Pendientes", "Completadas"
- Haz clic en el botón de filtro para opciones avanzadas

## 🔧 Solución de problemas

### Error: "python no se reconoce como comando"
- Asegúrate de que Python esté instalado correctamente
- Verifica que esté en el PATH del sistema

### Error: "pip no se reconoce como comando"
- Instala pip: `python -m ensurepip --upgrade`
- O usa: `python -m pip install -r requirements.txt`

### Error: "puerto 5000 en uso"
- Cambia el puerto en `app.py` línea 89: `port=5001`
- O cierra otras aplicaciones que usen el puerto 5000

### La página no carga
- Verifica que el servidor esté corriendo (deberías ver mensajes en la terminal)
- Asegúrate de usar la URL correcta: `http://localhost:5000`

## 📚 Conceptos básicos que aprenderás

- **Frontend**: La parte que ves en el navegador (HTML, CSS, JavaScript)
- **Backend**: La parte que procesa datos en el servidor (Python, Flask)
- **Base de datos**: Donde se guardan las tareas (SQLite)
- **API**: Forma de comunicación entre frontend y backend
- **MVC**: Patrón de organización del código (Modelo, Vista, Controlador)
- **Deploy**: Proceso de subir tu aplicación a internet

## 🤝 Contribuir

Si encuentras errores o quieres mejorar el proyecto:
1. Haz una copia del proyecto
2. Realiza tus cambios
3. Prueba que todo funcione
4. Comparte tus mejoras

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso educativo.

---

**¡Disfruta aprendiendo a programar! 🎉** 