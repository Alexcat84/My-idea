/**
 * constants.ts - Fase 3.0: constantes del bucle de entrevista de
 * prototipo_motor.py que no pertenecen a graph.ts (acceso al grafo) ni a
 * compass.ts (brujula semantica).
 */
export const MAX_DEPTH = 15;
export const MAX_SALTOS_SILENCIOSOS_POR_LLAMADA = 3;
export const MAX_REPREGUNTAS_POR_PUNTO = 1;
export const MAX_TURNOS_EXTRA_SIGAMOS_DIRIGIDO = 3;

export type CampoNumericoProyecto =
  | "costo_materiales_unidad"
  | "horas_por_unidad"
  | "valor_hora"
  | "precio_tentativo"
  | "capacidad_semanal"
  | "costos_fijos_mensuales"
  | "unidades_vendidas"
  | "precio_pagado_real";

const CAMPOS_NUMERICOS_PROYECTO_LISTA: CampoNumericoProyecto[] = [
  "costo_materiales_unidad",
  "horas_por_unidad",
  "valor_hora",
  "precio_tentativo",
  "capacidad_semanal",
  "costos_fijos_mensuales",
  "unidades_vendidas",
  "precio_pagado_real",
];
export const CAMPOS_NUMERICOS_PROYECTO = new Set<string>(CAMPOS_NUMERICOS_PROYECTO_LISTA);

export const TIPOS_OFERTA_VALIDOS = new Set(["producto_fisico", "servicio", "digital", "mixto"]);

export const FAMILIA_QUERY_BRUJULA: Record<string, string> = {
  accion_clientes: "validar con clientes reales, conseguir la primera venta, preventa, prueba de pago",
  viabilidad_economica: "costos, precios, punto de equilibrio, rentabilidad, margen, cuanto cobrar",
};
