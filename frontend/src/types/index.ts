export interface Producto {
  codigo: string;
  grupo: string;
  cantidad: number;
}

export interface ProductoBonificado {
  codigo: string;
  bonificacion: number;
}

export interface PedidoRequest {
  productos: Producto[];
}

export interface BonificacionResponse {
  productos_bonificados: ProductoBonificado[];
} 