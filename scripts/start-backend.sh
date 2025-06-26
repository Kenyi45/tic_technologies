#!/bin/bash
echo "Iniciando Backend - Sistema de Bonificaciones"
echo "=========================================="
cd backend
if [ ! -d "venv" ]; then
    echo "Creando entorno virtual..."
    python3 -m venv venv
fi
echo "Activando entorno virtual..."
source venv/bin/activate
echo "Instalando dependencias..."
pip install -r requirements.txt
echo "Iniciando servidor FastAPI..."
python main.py 