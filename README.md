# Sistema de Bonificaciones

Una aplicación Full Stack para simular bonificaciones en pedidos, desarrollada con **FastAPI** para el backend y **React TypeScript + Vite** para el frontend.

## 🚀 Características

- **Backend**: API REST con FastAPI siguiendo principios SOLID y patrones de diseño
- **Frontend**: Interfaz moderna con React TypeScript
- **Lógica de negocio**: Bonificaciones proporcionales para productos del grupo "JUGOS"
- **Arquitectura**: Clean Architecture con inversión de dependencias
- **Tests**: Cobertura de tests unitarios para la lógica de negocio

## 📋 Lógica de Bonificación

- Solo se consideran productos del grupo **"JUGOS"**
- Por cada **10 unidades** compradas del grupo, se otorgan **2 unidades** de bonificación
- La bonificación se distribuye **proporcionalmente** entre los productos del grupo

### Ejemplo
```json
// Entrada
[
  { "codigo": "PROD_A", "grupo": "JUGOS", "cantidad": 12 },
  { "codigo": "PROD_B", "grupo": "JUGOS", "cantidad": 8 },
  { "codigo": "PROD_C", "grupo": "AGUA", "cantidad": 5 }
]

// Salida
[
  { "codigo": "PROD_A", "bonificacion": 2 },
  { "codigo": "PROD_B", "bonificacion": 2 }
]
```

## 🛠️ Tecnologías Utilizadas

### Backend
- **FastAPI**: Framework web moderno para Python
- **Pydantic**: Validación de datos y serialización
- **Uvicorn**: Servidor ASGI
- **Pytest**: Framework de testing

### Frontend
- **React 18**: Biblioteca de interfaz de usuario
- **TypeScript**: Tipado estático para JavaScript
- **Vite**: Build tool y dev server
- **Axios**: Cliente HTTP para comunicación con la API

## 📦 Instalación y Ejecución

### Prerequisitos
- Python 3.8+
- Node.js 16+
- npm o yarn

### Backend

1. **Navegar al directorio del backend**:
   ```bash
   cd backend
   ```

2. **Crear y activar un entorno virtual**:
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar el servidor**:
   ```bash
   python main.py
   ```
   
   El servidor estará disponible en: `http://localhost:8000`

5. **Ejecutar tests**:
   ```bash
   pytest tests/ -v
   ```

### Frontend

1. **Navegar al directorio del frontend**:
   ```bash
   cd frontend
   ```

2. **Instalar dependencias**:
   ```bash
   npm install
   ```

3. **Ejecutar el servidor de desarrollo**:
   ```bash
   npm run dev
   ```
   
   La aplicación estará disponible en: `http://localhost:5173`

4. **Compilar para producción**:
   ```bash
   npm run build
   ```

### Inicio Rápido con Scripts

```bash
# Backend
./scripts/start-backend.sh

# Frontend (en otra terminal)
./scripts/start-frontend.sh
```

## 🏗️ Arquitectura del Proyecto

### Backend - Clean Architecture

```
backend/
├── app/
│   ├── models/                    # Modelos de datos (Pydantic)
│   ├── domain/
│   │   ├── interfaces/           # Interfaces y contratos
│   │   └── services/            # Lógica de dominio
│   ├── application/
│   │   └── services/            # Servicios de aplicación
│   ├── infrastructure/          # Inyección de dependencias
│   └── api/
│       └── controllers/         # Controladores HTTP
├── tests/                       # Tests unitarios
├── main.py                      # Punto de entrada
└── requirements.txt             # Dependencias
```

### Frontend - Componentes Modulares

```
frontend/
├── src/
│   ├── components/              # Componentes React
│   ├── hooks/                   # Hooks personalizados
│   ├── services/               # Servicios API
│   ├── types/                  # Tipos TypeScript
│   ├── App.tsx                 # Componente principal
│   └── main.tsx                # Punto de entrada
├── index.html                  # Template HTML
└── package.json                # Dependencias y scripts
```

## 🔧 Principios de Diseño Aplicados

### SOLID Principles

1. **Single Responsibility Principle (SRP)**:
   - `JugosBonificacionCalculator`: Solo responsable de calcular bonificaciones
   - `PedidoService`: Solo maneja operaciones de pedidos
   - Cada componente React tiene una responsabilidad específica

2. **Open/Closed Principle (OCP)**:
   - `IBonificacionCalculator`: Interfaz que permite extensión sin modificación
   - Nuevos tipos de calculadores pueden agregarse fácilmente

3. **Liskov Substitution Principle (LSP)**:
   - Cualquier implementación de `IBonificacionCalculator` puede sustituirse

4. **Interface Segregation Principle (ISP)**:
   - Interfaces específicas y cohesivas

5. **Dependency Inversion Principle (DIP)**:
   - `PedidoService` depende de abstracción, no de implementación concreta
   - `DependencyContainer` maneja la inyección de dependencias

### Patrones de Diseño

- **Factory Pattern**: `DependencyContainer` para crear instancias
- **Strategy Pattern**: `IBonificacionCalculator` permite diferentes estrategias de cálculo
- **Dependency Injection**: Inversión de control para dependencias

## 📡 API Endpoints

### POST /api/simular

Simula bonificaciones para un pedido.

**Request Body:**
```json
{
  "productos": [
    {
      "codigo": "string",
      "grupo": "string",
      "cantidad": number
    }
  ]
}
```

**Response:**
```json
{
  "productos_bonificados": [
    {
      "codigo": "string",
      "bonificacion": number
    }
  ]
}
```

**Ejemplo de uso con curl:**
```bash
curl -X POST "http://localhost:8000/api/simular" \
  -H "Content-Type: application/json" \
  -d '{
    "productos": [
      {"codigo": "PROD_A", "grupo": "JUGOS", "cantidad": 12},
      {"codigo": "PROD_B", "grupo": "JUGOS", "cantidad": 8},
      {"codigo": "PROD_C", "grupo": "AGUA", "cantidad": 5}
    ]
  }'
```

## 🧪 Testing

El proyecto incluye tests unitarios para validar la lógica de bonificación:

```bash
cd backend
pytest tests/ -v
```

Los tests cubren:
- Cálculo básico de bonificaciones
- Casos edge (sin productos, cantidades insuficientes)
- Distribución proporcional
- Validación de grupos de productos

## 🌐 Uso de la Aplicación

1. **Abrir la aplicación** en `http://localhost:5173`
2. **Agregar productos** usando el formulario:
   - Código del producto
   - Grupo (JUGOS, AGUA, BEBIDAS, OTROS)
   - Cantidad
3. **Ver productos agregados** en la tabla
4. **Simular bonificaciones** haciendo clic en el botón
5. **Ver resultados** con los productos bonificados

## 🔍 Validaciones y Reglas de Negocio

- Solo productos del grupo "JUGOS" califican para bonificaciones
- Se requieren mínimo 10 unidades para generar bonificación
- La bonificación se calcula por grupos completos de 10 unidades
- La distribución es proporcional a la cantidad de cada producto
- Los productos de otros grupos no afectan el cálculo

## 📈 Posibles Mejoras Futuras

- Persistencia de datos con base de datos
- Autenticación y autorización
- Más tipos de bonificaciones (por producto, por cliente, etc.)
- Dashboard con métricas y reportes
- API de gestión de productos y grupos
- Notificaciones en tiempo real
- Exportación de resultados (PDF, Excel)

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

---

**Desarrollado con ❤️ usando FastAPI y React** 