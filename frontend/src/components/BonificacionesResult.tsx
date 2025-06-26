import React from 'react';
import { ProductoBonificado } from '../types';

interface BonificacionesResultProps {
  productosBonificados: ProductoBonificado[];
  loading: boolean;
}

export const BonificacionesResult: React.FC<BonificacionesResultProps> = ({ 
  productosBonificados, 
  loading 
}) => {
  if (loading) {
    return (
      <div className="bonificaciones-result">
        <h3>Resultado de Bonificaciones</h3>
        <div className="loading">
          <p>Calculando bonificaciones...</p>
        </div>
      </div>
    );
  }

  if (productosBonificados.length === 0) {
    return (
      <div className="bonificaciones-result">
        <h3>Resultado de Bonificaciones</h3>
        <p className="no-bonificaciones">
          No hay bonificaciones aplicables. 
          <br />
          <small>
            Recuerda: Solo productos del grupo "JUGOS" califican para bonificaciones 
            y necesitas al menos 10 unidades para obtener 2 de bonificación.
          </small>
        </p>
      </div>
    );
  }

  const totalBonificaciones = productosBonificados.reduce(
    (total, producto) => total + producto.bonificacion, 
    0
  );

  return (
    <div className="bonificaciones-result">
      <h3>Resultado de Bonificaciones</h3>
      <div className="bonificaciones-summary">
        <p className="total-bonificaciones">
          Total de bonificaciones: <strong>{totalBonificaciones} unidades</strong>
        </p>
      </div>
      
      <div className="table-container">
        <table>
          <thead>
            <tr>
              <th>Código del Producto</th>
              <th>Bonificación</th>
            </tr>
          </thead>
          <tbody>
            {productosBonificados.map((producto, index) => (
              <tr key={index}>
                <td>{producto.codigo}</td>
                <td>
                  <span className="bonificacion-badge">
                    {producto.bonificacion} unidades
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}; 