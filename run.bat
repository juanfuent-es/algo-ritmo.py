@echo off
echo ========================================
echo    TaskMaster - Iniciando Servidor
echo ========================================
echo.

echo Activando entorno virtual...
call venv\Scripts\activate
if errorlevel 1 (
    echo ERROR: No se pudo activar el entorno virtual
    echo Ejecuta primero: install.bat
    pause
    exit /b 1
)

echo Entorno virtual activado!
echo.

echo Iniciando servidor...
echo.
echo ========================================
echo    Servidor iniciado correctamente!
echo ========================================
echo.
echo Abre tu navegador en: http://localhost:5000
echo.
echo Para detener el servidor: Ctrl+C
echo ========================================
echo.

python app.py 