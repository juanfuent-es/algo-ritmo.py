# 🚀 Deploy en Render.com - TaskMaster

Guía paso a paso para desplegar TaskMaster en Render.com

## 📋 Requisitos Previos

1. **Cuenta en Render.com** (gratuita)
2. **Repositorio en GitHub** con el código de TaskMaster
3. **Git instalado** en tu computadora

## 🔧 Pasos para el Deploy

### Paso 1: Preparar el Repositorio

Asegúrate de que tu repositorio contenga estos archivos:

```
algo-ritmo.py/
├── app.py                 # ✅ Aplicación principal
├── config.py              # ✅ Configuración
├── requirements.txt       # ✅ Dependencias
├── Procfile              # ✅ Comando de inicio
├── render.yaml           # ✅ Configuración de Render
├── runtime.txt           # ✅ Versión de Python
├── models/               # ✅ Modelos de datos
├── templates/            # ✅ Plantillas HTML
├── static/               # ✅ Archivos estáticos
└── database/             # ✅ Directorio de BD
    └── .gitkeep          # ✅ Mantiene el directorio
```

### Paso 2: Conectar con Render

1. Ve a [render.com](https://render.com) y crea una cuenta
2. Haz clic en "New +" → "Web Service"
3. Conecta tu repositorio de GitHub
4. Selecciona el repositorio `algo-ritmo.py`

### Paso 3: Configurar el Servicio

**Configuración automática (recomendada):**
- Render detectará automáticamente que es una aplicación Python
- Usará el archivo `render.yaml` para la configuración

**Configuración manual:**
- **Name:** `algo-ritmo-app`
- **Environment:** `Python`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`
- **Plan:** `Free`

### Paso 4: Variables de Entorno

Render configurará automáticamente estas variables:

```env
PYTHON_VERSION=3.9.16
FLASK_ENV=production
SECRET_KEY=<generado-automáticamente>
SESSION_COOKIE_SECURE=true
```

### Paso 5: Deploy

1. Haz clic en "Create Web Service"
2. Render comenzará el proceso de build
3. Espera a que termine (puede tomar 2-5 minutos)
4. Tu aplicación estará disponible en: `https://tu-app.onrender.com`

## 🔍 Verificar el Deploy

### Endpoint de Salud
Visita: `https://tu-app.onrender.com/health`
Deberías ver: `{"status": "healthy", "message": "TaskMaster API is running"}`

### Aplicación Principal
Visita: `https://tu-app.onrender.com`
Deberías ver la interfaz de TaskMaster

## 🛠️ Solución de Problemas

### Error: "Module not found"
- Verifica que `requirements.txt` contenga todas las dependencias
- Revisa los logs de build en Render

### Error: "Database not found"
- La base de datos se creará automáticamente
- Verifica que el directorio `database/` exista

### Error: "Port already in use"
- Render maneja automáticamente el puerto
- No necesitas configurar el puerto manualmente

### Error: "Secret key not set"
- Render genera automáticamente la SECRET_KEY
- Si persiste, agrega manualmente en las variables de entorno

## 📊 Monitoreo

### Logs
- Ve a tu servicio en Render
- Haz clic en "Logs" para ver los logs en tiempo real

### Métricas
- Render proporciona métricas básicas de uso
- Monitorea el uso de recursos

## 🔄 Actualizaciones

Para actualizar tu aplicación:

1. Haz cambios en tu código local
2. Haz commit y push a GitHub
3. Render detectará automáticamente los cambios
4. Iniciará un nuevo deploy

## 💰 Costos

- **Plan Free:** Gratuito
- **Límites:** 
  - 750 horas/mes
  - Se suspende después de 15 minutos de inactividad
  - Se reactiva automáticamente con la primera petición

## 🔒 Seguridad

- HTTPS automático
- Variables de entorno seguras
- No expongas credenciales en el código

## 📞 Soporte

Si tienes problemas:
1. Revisa los logs en Render
2. Verifica la configuración
3. Consulta la [documentación de Render](https://render.com/docs)

---

**¡Tu TaskMaster estará disponible en internet! 🌐** 