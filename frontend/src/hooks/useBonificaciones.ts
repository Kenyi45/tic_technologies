import { useState } from 'react';
import { Producto, ProductoBonificado } from '../types';
import { pedidoService } from '../services/api';

export const useBonificaciones = () => {
  const [productos, setProductos] = useState<Producto[]>([]);
  const [productosBonificados, setProductosBonificados] = useState<ProductoBonificado[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const agregarProducto = (producto: Producto) => {
    setProductos(prev => [...prev, producto]);
  };

  const eliminarProducto = (index: number) => {
    setProductos(prev => prev.filter((_, i) => i !== index));
  };

  const simularBonificaciones = async () => {
    if (productos.length === 0) {
      setError('Debe agregar al menos un producto');
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const response = await pedidoService.simularBonificaciones({ productos });
      setProductosBonificados(response.productos_bonificados);
    } catch (err) {
      setError('Error al simular bonificaciones. Verifique que el servidor esté ejecutándose.');
      console.error('Error:', err);
    } finally {
      setLoading(false);
    }
  };

  const limpiarFormulario = () => {
    setProductos([]);
    setProductosBonificados([]);
    setError(null);
  };

  return {
    productos,
    productosBonificados,
    loading,
    error,
    agregarProducto,
    eliminarProducto,
    simularBonificaciones,
    limpiarFormulario,
  };
}; 