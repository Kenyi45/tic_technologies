import pytest
from app.models.producto import Producto, ProductoBonificado
from app.domain.services.bonificacion_calculator import JugosBonificacionCalculator


class TestJugosBonificacionCalculator:
    """Tests para el calculador de bonificaciones de jugos"""
    
    def setup_method(self):
        """Setup que se ejecuta antes de cada test"""
        self.calculator = JugosBonificacionCalculator()
    
    def test_calcular_bonificaciones_ejemplo_basico(self):
        """Test con el ejemplo básico del enunciado"""
        productos = [
            Producto(codigo="PROD_A", grupo="JUGOS", cantidad=12),
            Producto(codigo="PROD_B", grupo="JUGOS", cantidad=8),
            Producto(codigo="PROD_C", grupo="AGUA", cantidad=5),
        ]
        
        resultado = self.calculator.calcular_bonificaciones(productos)
        
        # Verificar que solo hay 2 productos bonificados (los de JUGOS)
        assert len(resultado) == 2
        
        # Verificar que los códigos sean correctos
        codigos = [producto.codigo for producto in resultado]
        assert "PROD_A" in codigos
        assert "PROD_B" in codigos
        assert "PROD_C" not in codigos
        
        # Verificar bonificación total (20 unidades de JUGOS = 2 grupos de 10 = 4 de bonificación)
        total_bonificacion = sum(producto.bonificacion for producto in resultado)
        assert total_bonificacion == 4
    
    def test_sin_productos_jugos(self):
        """Test cuando no hay productos del grupo JUGOS"""
        productos = [
            Producto(codigo="PROD_C", grupo="AGUA", cantidad=20),
            Producto(codigo="PROD_D", grupo="BEBIDAS", cantidad=15),
        ]
        
        resultado = self.calculator.calcular_bonificaciones(productos)
        
        assert len(resultado) == 0
    
    def test_productos_jugos_insuficientes(self):
        """Test cuando hay productos JUGOS pero no llegan a 10 unidades"""
        productos = [
            Producto(codigo="PROD_A", grupo="JUGOS", cantidad=5),
            Producto(codigo="PROD_B", grupo="JUGOS", cantidad=3),
        ]
        
        resultado = self.calculator.calcular_bonificaciones(productos)
        
        assert len(resultado) == 0
    
    def test_exactamente_10_unidades(self):
        """Test con exactamente 10 unidades de JUGOS"""
        productos = [
            Producto(codigo="PROD_A", grupo="JUGOS", cantidad=10),
        ]
        
        resultado = self.calculator.calcular_bonificaciones(productos)
        
        assert len(resultado) == 1
        assert resultado[0].codigo == "PROD_A"
        assert resultado[0].bonificacion == 2
    
    def test_multiples_grupos_de_10(self):
        """Test con múltiples grupos de 10 unidades"""
        productos = [
            Producto(codigo="PROD_A", grupo="JUGOS", cantidad=25),
        ]
        
        resultado = self.calculator.calcular_bonificaciones(productos)
        
        assert len(resultado) == 1
        assert resultado[0].bonificacion == 4  # 25 // 10 = 2 grupos, 2 * 2 = 4 bonificación
    
    def test_distribucion_proporcional(self):
        """Test de distribución proporcional compleja"""
        productos = [
            Producto(codigo="PROD_A", grupo="JUGOS", cantidad=30),  # 30/50 = 60%
            Producto(codigo="PROD_B", grupo="JUGOS", cantidad=20),  # 20/50 = 40%
        ]
        
        resultado = self.calculator.calcular_bonificaciones(productos)
        
        # 50 unidades total = 5 grupos de 10 = 10 bonificación total
        total_bonificacion = sum(producto.bonificacion for producto in resultado)
        assert total_bonificacion == 10
        
        # Verificar distribución aproximadamente proporcional
        prod_a = next(p for p in resultado if p.codigo == "PROD_A")
        prod_b = next(p for p in resultado if p.codigo == "PROD_B")
        
        assert prod_a.bonificacion == 6  # 60% de 10
        assert prod_b.bonificacion == 4  # 40% de 10
    
    def test_lista_vacia(self):
        """Test con lista vacía de productos"""
        productos = []
        
        resultado = self.calculator.calcular_bonificaciones(productos)
        
        assert len(resultado) == 0
    
    def test_solo_un_producto_jugo_con_bonificacion(self):
        """Test con un solo producto JUGOS que califique para bonificación"""
        productos = [
            Producto(codigo="PROD_UNICO", grupo="JUGOS", cantidad=15),
        ]
        
        resultado = self.calculator.calcular_bonificaciones(productos)
        
        assert len(resultado) == 1
        assert resultado[0].codigo == "PROD_UNICO"
        assert resultado[0].bonificacion == 2  # 15 // 10 = 1 grupo, 1 * 2 = 2 