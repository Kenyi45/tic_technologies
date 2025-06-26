from abc import ABC, abstractmethod
from typing import List
from app.models.producto import Producto, ProductoBonificado


class IBonificacionCalculator(ABC):
    """Interfaz para el calculador de bonificaciones"""
    
    @abstractmethod
    def calcular_bonificaciones(self, productos: List[Producto]) -> List[ProductoBonificado]:
        """
        Calcula las bonificaciones para una lista de productos
        
        Args:
            productos: Lista de productos del pedido
            
        Returns:
            Lista de productos con sus bonificaciones
        """
        pass 