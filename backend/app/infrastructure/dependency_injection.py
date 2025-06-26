from app.domain.interfaces.bonificacion_calculator import IBonificacionCalculator
from app.domain.services.bonificacion_calculator import JugosBonificacionCalculator
from app.application.services.pedido_service import PedidoService


class DependencyContainer:
    """Contenedor de inyección de dependencias"""
    
    @staticmethod
    def get_bonificacion_calculator() -> IBonificacionCalculator:
        """Factory method para obtener el calculador de bonificaciones"""
        return JugosBonificacionCalculator()
    
    @staticmethod
    def get_pedido_service() -> PedidoService:
        """Factory method para obtener el servicio de pedidos"""
        bonificacion_calculator = DependencyContainer.get_bonificacion_calculator()
        return PedidoService(bonificacion_calculator) 