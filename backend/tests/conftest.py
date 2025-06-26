"""
Configuración de pytest para asegurar que las importaciones funcionen correctamente
"""
import sys
import os

# Agregar el directorio raíz del backend al Python path
backend_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if backend_root not in sys.path:
    sys.path.insert(0, backend_root) 