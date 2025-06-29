# 🚀 Deploy en Render.com - TaskMaster

## 📋 Requisitos previos

1. **Cuenta en Render.com** (gratuita)
2. **Repositorio en GitHub** con el código del proyecto
3. **Archivos de configuración** (ya incluidos en el proyecto)

## 🔧 Archivos de configuración incluidos

### `render.yaml`
```yaml
services:
  - type: web
    name: taskmaster-app
    env: python
    plan: free
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
    envVars:
      - key: PYTHON_VERSION
        value: 3.9.16
```

### `requirements.txt`
```
Flask==2.3.3
Werkzeug==2.3.7
gunicorn==21.2.0
```

### `runtime.txt`
```
python-3.9.16
```

### `Procfile`
```
web: gunicorn app:app
```

## 🚀 Pasos para hacer deploy

### Paso 1: Subir código a GitHub
1. Crea un repositorio en GitHub
2. Sube todos los archivos del proyecto
3. Asegúrate de que estén incluidos todos los archivos de configuración

### Paso 2: Conectar con Render.com
1. Ve a [render.com](https://render.com)
2. Crea una cuenta o inicia sesión
3. Haz clic en "New +" → "Web Service"

### Paso 3: Configurar el servicio
1. **Connect Repository**: Conecta tu repositorio de GitHub
2. **Name**: `taskmaster-app` (o el nombre que prefieras)
3. **Environment**: `Python 3`
4. **Build Command**: `pip install -r requirements.txt`
5. **Start Command**: `gunicorn app:app`
6. **Plan**: `Free`

### Paso 4: Variables de entorno (opcional)
Puedes agregar variables de entorno en la sección "Environment Variables":
- `SECRET_KEY`: Una clave secreta para Flask
- `FLASK_ENV`: `production`

### Paso 5: Deploy
1. Haz clic en "Create Web Service"
2. Render comenzará a construir y desplegar tu aplicación
3. Espera unos minutos hasta que aparezca "Live"

## 🌐 Acceder a tu aplicación

Una vez completado el deploy, Render te dará una URL como:
```
https://tu-app-name.onrender.com
```

## 🔧 Solución de problemas comunes

### Error: "Build failed"
- Verifica que todos los archivos estén en el repositorio
- Revisa que `requirements.txt` esté correcto
- Asegúrate de que `app.py` esté en la raíz del proyecto

### Error: "Application failed to start"
- Verifica que el comando de inicio sea correcto: `gunicorn app:app`
- Revisa los logs en Render para ver el error específico

### Error: "Database not found"
- La base de datos SQLite se creará automáticamente
- Verifica que la carpeta `database/` tenga permisos de escritura

### Error: "Port not available"
- Render asigna automáticamente el puerto
- El código ya está configurado para usar `os.environ.get('PORT')`

## 📊 Monitoreo y logs

### Ver logs en tiempo real:
1. Ve a tu servicio en Render
2. Haz clic en "Logs"
3. Puedes ver logs en tiempo real o descargarlos

### Métricas:
- Render te muestra métricas básicas como requests/minuto
- En el plan gratuito tienes limitaciones de uso

## 🔄 Actualizaciones

Para actualizar tu aplicación:
1. Haz cambios en tu código local
2. Sube los cambios a GitHub
3. Render detectará automáticamente los cambios
4. Iniciará un nuevo deploy automáticamente

## 💰 Planes y costos

### Plan Free:
- ✅ 750 horas de ejecución por mes
- ✅ 512 MB RAM
- ✅ 0.1 CPU
- ✅ Sleep después de 15 minutos de inactividad
- ✅ HTTPS incluido
- ✅ Custom domains

### Planes pagos:
- Más recursos
- Sin sleep automático
- Soporte prioritario

## 🎯 Consejos para producción

1. **Variables de entorno**: Usa variables de entorno para configuraciones sensibles
2. **Logs**: Revisa los logs regularmente
3. **Backup**: Considera hacer backup de tu base de datos
4. **Monitoreo**: Configura alertas si es necesario

## 🔗 Enlaces útiles

- [Documentación de Render](https://render.com/docs)
- [Guía de Python en Render](https://render.com/docs/deploy-python)
- [Soporte de Render](https://render.com/docs/help)

---

**¡Tu aplicación estará disponible en la web en minutos! 🌟** 