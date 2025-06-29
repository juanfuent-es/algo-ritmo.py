@echo off
echo ========================================
echo    TaskMaster - Instalador Automatico
echo ========================================
echo.

echo Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no esta instalado o no esta en el PATH
    echo.
    echo Por favor instala Python desde: https://www.python.org/downloads/
    echo Asegurate de marcar "Add Python to PATH" durante la instalacion
    echo.
    pause
    exit /b 1
)

echo Python encontrado!
echo.

echo Creando entorno virtual...
python -m venv venv
if errorlevel 1 (
    echo ERROR: No se pudo crear el entorno virtual
    pause
    exit /b 1
)

echo Entorno virtual creado exitosamente!
echo.

echo Activando entorno virtual...
call venv\Scripts\activate
if errorlevel 1 (
    echo ERROR: No se pudo activar el entorno virtual
    pause
    exit /b 1
)

echo Entorno virtual activado!
echo.

echo Instalando dependencias...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: No se pudieron instalar las dependencias
    pause
    exit /b 1
)

echo.
echo ========================================
echo    ¡Instalacion completada!
echo ========================================
echo.
echo Para ejecutar el proyecto:
echo 1. Ejecuta: run.bat
echo 2. Abre tu navegador en: http://localhost:5000
echo.
echo Para detener el servidor: Ctrl+C
echo.
pause 