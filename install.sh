#!/bin/bash

echo "========================================"
echo "   TaskMaster - Instalador Automatico"
echo "========================================"
echo

echo "Verificando Python..."
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python3 no esta instalado"
    echo
    echo "Por favor instala Python desde: https://www.python.org/downloads/"
    echo "O usa tu gestor de paquetes:"
    echo "  Ubuntu/Debian: sudo apt install python3 python3-pip"
    echo "  macOS: brew install python3"
    echo
    exit 1
fi

echo "Python encontrado!"
echo

echo "Creando entorno virtual..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "ERROR: No se pudo crear el entorno virtual"
    exit 1
fi

echo "Entorno virtual creado exitosamente!"
echo

echo "Activando entorno virtual..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "ERROR: No se pudo activar el entorno virtual"
    exit 1
fi

echo "Entorno virtual activado!"
echo

echo "Instalando dependencias..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: No se pudieron instalar las dependencias"
    exit 1
fi

echo
echo "========================================"
echo "   ¡Instalacion completada!"
echo "========================================"
echo
echo "Para ejecutar el proyecto:"
echo "1. Ejecuta: ./run.sh"
echo "2. Abre tu navegador en: http://localhost:5000"
echo
echo "Para detener el servidor: Ctrl+C"
echo 