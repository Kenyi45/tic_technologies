from typing import List
from app.models.producto import Producto, ProductoBonificado
from app.domain.interfaces.bonificacion_calculator import IBonificacionCalculator


class JugosBonificacionCalculator(IBonificacionCalculator):
    """
    Calculador de bonificaciones específico para productos del grupo JUGOS
    Implementa el principio de responsabilidad única (SRP)
    """
    
    GRUPO_OBJETIVO = "JUGOS"
    UNIDADES_REQUERIDAS = 10
    BONIFICACION_POR_GRUPO = 2
    
    def calcular_bonificaciones(self, productos: List[Producto]) -> List[ProductoBonificado]:
        """
        Calcula bonificaciones para productos del grupo JUGOS
        - Por cada 10 unidades compradas del grupo, otorga 2 de bonificación
        - Reparte la bonificación proporcionalmente entre los productos del grupo
        """
        # Filtrar solo productos del grupo JUGOS
        productos_jugos = self._filtrar_productos_jugos(productos)
        
        if not productos_jugos:
            return []
        
        # Calcular total de unidades del grupo
        total_unidades = sum(producto.cantidad for producto in productos_jugos)
        
        # Calcular bonificación total
        bonificacion_total = self._calcular_bonificacion_total(total_unidades)
        
        if bonificacion_total == 0:
            return []
        
        # Distribuir bonificación proporcionalmente
        return self._distribuir_bonificacion(productos_jugos, total_unidades, bonificacion_total)
    
    def _filtrar_productos_jugos(self, productos: List[Producto]) -> List[Producto]:
        """Filtra productos que pertenecen al grupo JUGOS"""
        return [producto for producto in productos if producto.grupo == self.GRUPO_OBJETIVO]
    
    def _calcular_bonificacion_total(self, total_unidades: int) -> int:
        """Calcula la bonificación total basada en las unidades compradas"""
        grupos_completos = total_unidades // self.UNIDADES_REQUERIDAS
        return grupos_completos * self.BONIFICACION_POR_GRUPO
    
    def _distribuir_bonificacion(self, productos_jugos: List[Producto], 
                               total_unidades: int, bonificacion_total: int) -> List[ProductoBonificado]:
        """Distribuye la bonificación proporcionalmente entre los productos"""
        productos_bonificados = []
        bonificacion_restante = bonificacion_total
        
        for i, producto in enumerate(productos_jugos):
            if i == len(productos_jugos) - 1:
                # Al último producto le asignamos toda la bonificación restante
                # para evitar problemas de redondeo
                bonificacion_producto = bonificacion_restante
            else:
                proporcion = producto.cantidad / total_unidades
                bonificacion_producto = int(bonificacion_total * proporcion)
                bonificacion_restante -= bonificacion_producto
            
            if bonificacion_producto > 0:
                productos_bonificados.append(
                    ProductoBonificado(
                        codigo=producto.codigo,
                        bonificacion=bonificacion_producto
                    )
                )
        
        return productos_bonificados 