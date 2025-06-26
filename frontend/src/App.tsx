import React from 'react';
import { ProductoForm } from './components/ProductoForm';
import { ProductosList } from './components/ProductosList';
import { BonificacionesResult } from './components/BonificacionesResult';
import { useBonificaciones } from './hooks/useBonificaciones';
import './App.css';

function App() {
  const {
    productos,
    productosBonificados,
    loading,
    error,
    agregarProducto,
    eliminarProducto,
    simularBonificaciones,
    limpiarFormulario,
  } = useBonificaciones();

  return (
    <div className="app">
      <header className="app-header">
        <h1>Sistema de Bonificaciones</h1>
        <p>Simula las bonificaciones para tu pedido</p>
      </header>

      <main className="app-main">
        <div className="container">
          <div className="row">
            <div className="col-md-6">
              <ProductoForm onAgregarProducto={agregarProducto} />
            </div>
            <div className="col-md-6">
              <ProductosList 
                productos={productos} 
                onEliminarProducto={eliminarProducto} 
              />
            </div>
          </div>

          {error && (
            <div className="error-message">
              <p>{error}</p>
            </div>
          )}

          <div className="actions">
            <button 
              onClick={simularBonificaciones}
              className="btn-primary btn-large"
              disabled={loading || productos.length === 0}
            >
              {loading ? 'Calculando...' : 'Simular Bonificaciones'}
            </button>
            
            <button 
              onClick={limpiarFormulario} 
              className="btn-secondary btn-large"
              disabled={loading}
            >
              Limpiar Todo
            </button>
          </div>

          <BonificacionesResult 
            productosBonificados={productosBonificados}
            loading={loading}
          />
        </div>
      </main>

      <footer className="app-footer">
        <p>
          <strong>Lógica de bonificación:</strong> Por cada 10 unidades de productos del grupo "JUGOS", 
          se otorgan 2 unidades de bonificación distribuidas proporcionalmente.
        </p>
      </footer>
    </div>
  );
}

export default App; 