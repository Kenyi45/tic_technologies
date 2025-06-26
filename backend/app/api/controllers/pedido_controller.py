from fastapi import APIRouter, HTTPException
from typing import List
from app.models.producto import PedidoRequest, BonificacionResponse, ProductoBonificado
from app.infrastructure.dependency_injection import DependencyContainer

router = APIRouter()


@router.post("/simular", response_model=BonificacionResponse)
async def simular_bonificaciones(request: PedidoRequest) -> BonificacionResponse:
    """
    Endpoint para simular bonificaciones de un pedido
    
    Args:
        request: Datos del pedido con productos
        
    Returns:
        Respuesta con productos bonificados
    """
    try:
        # Obtener servicio de pedidos desde el contenedor de dependencias
        pedido_service = DependencyContainer.get_pedido_service()
        
        # Simular bonificaciones
        productos_bonificados = pedido_service.simular_bonificaciones(request.productos)
        
        return BonificacionResponse(productos_bonificados=productos_bonificados)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}") 