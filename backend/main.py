from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.controllers import pedido_controller

# Crear instancia de FastAPI
app = FastAPI(
    title="Sistema de Bonificaciones",
    description="API para simular bonificaciones en pedidos",
    version="1.0.0"
)

# Configurar CORS para permitir requests del frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Puerto por defecto de Vite
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas
app.include_router(pedido_controller.router, prefix="/api", tags=["pedidos"])

@app.get("/")
async def root():
    """Endpoint de prueba"""
    return {"message": "Sistema de Bonificaciones API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 