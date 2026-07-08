/**
 * constants.ts - Fase 3.0: constantes del bucle de entrevista de
 * prototipo_motor.py que no pertenecen a graph.ts (acceso al grafo) ni a
 * compass.ts (brujula semantica).
 */
export const MAX_DEPTH = 15;
export const MAX_SALTOS_SILENCIOSOS_POR_LLAMADA = 3;
export const MAX_REPREGUNTAS_POR_PUNTO = 1;
export const MAX_TURNOS_EXTRA_SIGAMOS_DIRIGIDO = 3;
export const MAX_COSECHA = 25;
export const MAX_COSECHA_PRIORIDAD = 8;

export const SECCION_ECONOMICA_TITULO = "¿Puede sostenerse tu idea?";

export const TEXTO_FAMILIA_FALTANTE: Record<string, string> = {
  accion_clientes: "validar con clientes reales (entrevistas, MVP, pruebas de usuario, una venta o preventa real)",
  viabilidad_economica: "si tu idea puede sostenerse economicamente (costos, precios, punto de equilibrio)",
};

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

// Motor v2.2: Reporte de Sostenibilidad (--reporte en el CLI).
export const CAMPOS_ESENCIALES_POR_TIPO: Record<string, CampoNumericoProyecto[]> = {
  producto_fisico: [
    "costo_materiales_unidad",
    "horas_por_unidad",
    "valor_hora",
    "precio_tentativo",
    "capacidad_semanal",
    "costos_fijos_mensuales",
  ],
  servicio: [
    "costo_materiales_unidad",
    "horas_por_unidad",
    "valor_hora",
    "precio_tentativo",
    "capacidad_semanal",
    "costos_fijos_mensuales",
  ],
  digital: ["costos_fijos_mensuales", "costo_materiales_unidad", "precio_tentativo", "unidades_vendidas"],
};

export const MAX_PREGUNTAS_REPORTE = 6;

export const REPORTE_DISCLAIMER =
  "\n\n---\n_Estimaciones basadas en las cifras que tú diste; no sustituyen " +
  "contabilidad formal ni asesoría fiscal, que varían según tu país._";

export const PREGUNTA_TIPO_OFERTA = "¿Qué vendes exactamente y cómo se cobra?";

// Guardian GIGO (Motor v2.2): frases deterministicas que indican que la
// mini-entrevista actual (el "molde" de preguntas del tipo_oferta activo)
// no encaja con el negocio del usuario. Dos apariciones abortan el molde
// y disparan una reclasificacion en vez de seguir insistiendo con
// preguntas que no aplican.
export const FRASES_NO_APLICA_MOLDE = [
  "no funciona asi",
  "no funciona así",
  "no es por pieza",
  "no es por unidad",
  "no vendo por unidades",
  "no aplica",
  "no se cobra asi",
  "no se cobra así",
  "es una suscripcion",
  "es una suscripción",
  "es digital",
  "no tengo piezas",
  "no produzco piezas",
  "no es un producto fisico",
  "no es un producto físico",
  "no fabrico",
];
