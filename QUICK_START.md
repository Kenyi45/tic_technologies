# Guía de Inicio Rápido

## 🚀 Ejecución Rápida

### Opción 1: Scripts Automáticos

```bash
# Backend
./scripts/start-backend.sh

# Frontend (en otra terminal)
./scripts/start-frontend.sh
```

### Opción 2: Manual

**Backend:**
```bash
cd backend
python -m venv venv
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate
pip install -r requirements.txt
python main.py
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

## 🧪 Probar la API

```bash
cd examples
pip install -r requirements.txt
python test-api.py
```

## 📱 Usar la Aplicación

1. Backend: http://localhost:8000
2. Frontend: http://localhost:5173
3. Documentación API: http://localhost:8000/docs

## 📋 Ejemplo de Uso

### Entrada:
```json
{
  "productos": [
    {"codigo": "PROD_A", "grupo": "JUGOS", "cantidad": 12},
    {"codigo": "PROD_B", "grupo": "JUGOS", "cantidad": 8},
    {"codigo": "PROD_C", "grupo": "AGUA", "cantidad": 5}
  ]
}
```

### Salida:
```json
{
  "productos_bonificados": [
    {"codigo": "PROD_A", "bonificacion": 2},
    {"codigo": "PROD_B", "bonificacion": 2}
  ]
}
```

## ⚡ Casos de Prueba

- **20 unidades de JUGOS = 4 bonificaciones** (2 grupos de 10)
- **Distribución proporcional**: PROD_A (12/20 = 60%) = 2.4 ≈ 2, PROD_B (8/20 = 40%) = 1.6 ≈ 2
- **Solo grupo JUGOS** recibe bonificaciones
- **Productos AGUA** no califican 