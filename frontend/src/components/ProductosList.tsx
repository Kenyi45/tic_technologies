import React from 'react';
import { Producto } from '../types';

interface ProductosListProps {
  productos: Producto[];
  onEliminarProducto: (index: number) => void;
}

export const ProductosList: React.FC<ProductosListProps> = ({ productos, onEliminarProducto }) => {
  if (productos.length === 0) {
    return (
      <div className="productos-list">
        <h3>Productos del Pedido</h3>
        <p className="empty-message">No hay productos agregados</p>
      </div>
    );
  }

  return (
    <div className="productos-list">
      <h3>Productos del Pedido ({productos.length})</h3>
      <div className="table-container">
        <table>
          <thead>
            <tr>
              <th>Código</th>
              <th>Grupo</th>
              <th>Cantidad</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {productos.map((producto, index) => (
              <tr key={index}>
                <td>{producto.codigo}</td>
                <td>
                  <span className={`grupo-badge ${producto.grupo.toLowerCase()}`}>
                    {producto.grupo}
                  </span>
                </td>
                <td>{producto.cantidad}</td>
                <td>
                  <button
                    onClick={() => onEliminarProducto(index)}
                    className="btn-danger btn-small"
                  >
                    Eliminar
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}; 