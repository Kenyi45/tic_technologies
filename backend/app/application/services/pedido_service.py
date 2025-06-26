from typing import List
from app.models.producto import Producto, ProductoBonificado
from app.domain.interfaces.bonificacion_calculator import IBonificacionCalculator


class PedidoService:
    """
    Servicio de aplicación para manejar pedidos
    Implementa el principio de inversión de dependencias (DIP)
    """
    
    def __init__(self, bonificacion_calculator: IBonificacionCalculator):
        self._bonificacion_calculator = bonificacion_calculator
    
    def simular_bonificaciones(self, productos: List[Producto]) -> List[ProductoBonificado]:
        """
        Simula las bonificaciones para un pedido
        
        Args:
            productos: Lista de productos del pedido
            
        Returns:
            Lista de productos con bonificaciones
        """
        return self._bonificacion_calculator.calcular_bonificaciones(productos) 