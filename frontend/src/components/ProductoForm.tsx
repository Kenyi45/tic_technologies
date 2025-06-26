import React, { useState } from 'react';
import { Producto } from '../types';

interface ProductoFormProps {
  onAgregarProducto: (producto: Producto) => void;
}

export const ProductoForm: React.FC<ProductoFormProps> = ({ onAgregarProducto }) => {
  const [codigo, setCodigo] = useState('');
  const [grupo, setGrupo] = useState('JUGOS');
  const [cantidad, setCantidad] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!codigo.trim() || !cantidad.trim() || parseInt(cantidad) <= 0) {
      alert('Por favor, complete todos los campos correctamente');
      return;
    }

    const producto: Producto = {
      codigo: codigo.trim().toUpperCase(),
      grupo,
      cantidad: parseInt(cantidad),
    };

    onAgregarProducto(producto);
    
    // Limpiar formulario
    setCodigo('');
    setCantidad('');
  };

  return (
    <div className="producto-form">
      <h3>Agregar Producto</h3>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="codigo">Código del Producto:</label>
          <input
            type="text"
            id="codigo"
            value={codigo}
            onChange={(e) => setCodigo(e.target.value)}
            placeholder="Ej: PROD_A"
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="grupo">Grupo:</label>
          <select
            id="grupo"
            value={grupo}
            onChange={(e) => setGrupo(e.target.value)}
          >
            <option value="JUGOS">JUGOS</option>
            <option value="AGUA">AGUA</option>
            <option value="BEBIDAS">BEBIDAS</option>
            <option value="OTROS">OTROS</option>
          </select>
        </div>

        <div className="form-group">
          <label htmlFor="cantidad">Cantidad:</label>
          <input
            type="number"
            id="cantidad"
            value={cantidad}
            onChange={(e) => setCantidad(e.target.value)}
            min="1"
            placeholder="Ej: 12"
            required
          />
        </div>

        <button type="submit" className="btn-primary">
          Agregar Producto
        </button>
      </form>
    </div>
  );
}; 