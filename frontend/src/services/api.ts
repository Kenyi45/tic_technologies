import axios from 'axios';
import { PedidoRequest, BonificacionResponse } from '../types';

const API_BASE_URL = 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const pedidoService = {
  simularBonificaciones: async (request: PedidoRequest): Promise<BonificacionResponse> => {
    const response = await api.post<BonificacionResponse>('/simular', request);
    return response.data;
  },
}; 