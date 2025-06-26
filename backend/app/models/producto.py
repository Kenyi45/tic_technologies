from pydantic import BaseModel
from typing import List


class Producto(BaseModel):
    """Modelo que representa un producto en el pedido"""
    codigo: str
    grupo: str
    cantidad: int


class ProductoBonificado(BaseModel):
    """Modelo que representa un producto con bonificación"""
    codigo: str
    bonificacion: int


class PedidoRequest(BaseModel):
    """Modelo para la request del pedido"""
    productos: List[Producto]


class BonificacionResponse(BaseModel):
    """Modelo para la response de bonificaciones"""
    productos_bonificados: List[ProductoBonificado] 