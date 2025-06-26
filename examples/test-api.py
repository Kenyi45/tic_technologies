#!/usr/bin/env python3
"""
Script de ejemplo para probar la API de bonificaciones
Ejecutar: python examples/test-api.py
"""

import requests
import json


def test_api():
    """Prueba la API con diferentes casos de uso"""
    
    base_url = "http://localhost:8000/api/simular"
    
    # Caso 1: Ejemplo básico del enunciado
    print("=" * 60)
    print("CASO 1: Ejemplo básico del enunciado")
    print("=" * 60)
    
    caso1 = {
        "productos": [
            {"codigo": "PROD_A", "grupo": "JUGOS", "cantidad": 12},
            {"codigo": "PROD_B", "grupo": "JUGOS", "cantidad": 8},
            {"codigo": "PROD_C", "grupo": "AGUA", "cantidad": 5}
        ]
    }
    
    print("Entrada:")
    print(json.dumps(caso1, indent=2, ensure_ascii=False))
    
    try:
        response = requests.post(base_url, json=caso1)
        response.raise_for_status()
        
        print("\nSalida:")
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        print("Asegúrate de que el servidor esté ejecutándose en http://localhost:8000")
        return
    
    # Caso 2: Sin productos JUGOS
    print("\n" + "=" * 60)
    print("CASO 2: Sin productos del grupo JUGOS")
    print("=" * 60)
    
    caso2 = {
        "productos": [
            {"codigo": "PROD_C", "grupo": "AGUA", "cantidad": 20},
            {"codigo": "PROD_D", "grupo": "BEBIDAS", "cantidad": 15}
        ]
    }
    
    print("Entrada:")
    print(json.dumps(caso2, indent=2, ensure_ascii=False))
    
    try:
        response = requests.post(base_url, json=caso2)
        response.raise_for_status()
        
        print("\nSalida:")
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    # Caso 3: Cantidad insuficiente de JUGOS
    print("\n" + "=" * 60)
    print("CASO 3: Cantidad insuficiente de JUGOS")
    print("=" * 60)
    
    caso3 = {
        "productos": [
            {"codigo": "PROD_A", "grupo": "JUGOS", "cantidad": 5},
            {"codigo": "PROD_B", "grupo": "JUGOS", "cantidad": 3}
        ]
    }
    
    print("Entrada:")
    print(json.dumps(caso3, indent=2, ensure_ascii=False))
    
    try:
        response = requests.post(base_url, json=caso3)
        response.raise_for_status()
        
        print("\nSalida:")
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    # Caso 4: Múltiples grupos de bonificación
    print("\n" + "=" * 60)
    print("CASO 4: Múltiples grupos de bonificación")
    print("=" * 60)
    
    caso4 = {
        "productos": [
            {"codigo": "PROD_A", "grupo": "JUGOS", "cantidad": 30},
            {"codigo": "PROD_B", "grupo": "JUGOS", "cantidad": 20}
        ]
    }
    
    print("Entrada:")
    print(json.dumps(caso4, indent=2, ensure_ascii=False))
    
    try:
        response = requests.post(base_url, json=caso4)
        response.raise_for_status()
        
        print("\nSalida:")
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    print("\n" + "=" * 60)
    print("Pruebas completadas!")
    print("=" * 60)


if __name__ == "__main__":
    test_api() 