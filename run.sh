#!/bin/bash

echo "========================================"
echo "   TaskMaster - Iniciando Servidor"
echo "========================================"
echo

echo "Activando entorno virtual..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "ERROR: No se pudo activar el entorno virtual"
    echo "Ejecuta primero: ./install.sh"
    exit 1
fi

echo "Entorno virtual activado!"
echo

echo "Iniciando servidor..."
echo
echo "========================================"
echo "   Servidor iniciado correctamente!"
echo "========================================"
echo
echo "Abre tu navegador en: http://localhost:5000"
echo
echo "Para detener el servidor: Ctrl+C"
echo "========================================"
echo

python app.py 