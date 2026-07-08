/**
 * readiness.ts - Fase 3.0: port TypeScript de engine/plan_readiness.py.
 * Clasifica nodos en familias para el medidor de completitud (Fase 2.2).
 * Clasificacion por palabras clave (sin llamadas a la API), sobre
 * titulo_concepto + resumen_teorico, normalizados (sin acentos,
 * minusculas). En runtime, la web usa el node_families.json ya
 * precalculado (sincronizado por scripts/sync_assets_web.py) via
 * cargarFamilies() -- clasificarGrafo()/clasificarNodo() se conservan
 * para paridad y para poder reclasificar si el dataset cambia.
 */
import nodeFamiliesJson from "./assets/node_families.json";

export const MIN_NODOS_COMPLETA = 5;

// Revisar/ajustar aqui. Coincidencia por substring sobre texto normalizado
// (sin acentos, minusculas) de titulo_concepto + resumen_teorico.
export const KEYWORDS_ACCION_CLIENTES = [
  "entrevista", "voz del cliente", "mvp", "producto minimo viable",
  "prueba de usuario", "pruebas de usuario", "testeo con usuario",
  "validacion con cliente", "desarrollo de clientes", "customer development",
  "customer discovery", "investigacion de usuario", "user research",
  "prototipo", "feedback de cliente", "retroalimentacion de cliente",
  "presentacion del problema", "descubrimiento de clientes",
  "investigacion etnografica", "observacion de campo",
];

export const KEYWORDS_VIABILIDAD_ECONOMICA = [
  "punto de equilibrio", "flujo de caja", "flujo de efectivo",
  "unit economics", "metricas financieras", "modelo de ingresos",
  "estructura de costos", "analisis financiero", "proyeccion financiera",
  "presupuesto operativo", "margen de contribucion", "burn rate", "runway",
  "break even", "break-even", "estado de resultados",
  "inteligencia financiera", "arte de las finanzas", "fuentes de financiamiento",
  "rentabilidad", "numeros del negocio", "precio de venta",
  "estrategia de precios", "modelo de precios",
];

export type Familia = "accion_clientes" | "viabilidad_economica" | "general";

interface NodoGrafo {
  titulo_concepto?: string;
  resumen_teorico?: string;
  [key: string]: unknown;
}

function _normalizar(texto: string): string {
  // NFKD descompone "á" en "a" + U+0301 (acento combinante); el rango
  // ̀-ͯ (Combining Diacritical Marks) es el equivalente en JS
  // de filtrar por unicodedata.combining(c) != 0 en Python.
  return texto
    .toLowerCase()
    .normalize("NFKD")
    .replace(/[̀-ͯ]/g, "");
}

function _coincide(textoNormalizado: string, palabrasClave: string[]): boolean {
  return palabrasClave.some((p) => textoNormalizado.includes(p));
}

export function clasificarNodo(node: NodoGrafo): Familia {
  const texto = _normalizar(`${node.titulo_concepto ?? ""} ${node.resumen_teorico ?? ""}`);
  if (_coincide(texto, KEYWORDS_ACCION_CLIENTES)) return "accion_clientes";
  if (_coincide(texto, KEYWORDS_VIABILIDAD_ECONOMICA)) return "viabilidad_economica";
  return "general";
}

export function clasificarGrafo(graph: Record<string, NodoGrafo>): Record<string, Familia> {
  return Object.fromEntries(Object.entries(graph).map(([nid, n]) => [nid, clasificarNodo(n)]));
}

/** node_families.json ya sincronizado (Fase 3.0) -- equivalente a
 * cargar_families() cuando FAMILIES_PATH.exists() en Python. */
export function cargarFamilies(): Record<string, Familia> {
  return nodeFamiliesJson as Record<string, Familia>;
}

export interface EvaluacionCobertura {
  es_completa: boolean;
  tiene_accion_clientes: boolean;
  tiene_viabilidad_economica: boolean;
  num_nodos: number;
  familias_faltantes: string[];
}

/**
 * Evalua si una ruta esta lista para un plan completo (toca >=1 nodo de
 * accion_clientes y >=1 de viabilidad_economica, con al menos 5 nodos).
 */
export function evaluarRuta(ruta: string[], families: Record<string, Familia>): EvaluacionCobertura {
  const familiasEnRuta = new Set(ruta.map((nid) => families[nid] ?? "general"));
  const tieneAccion = familiasEnRuta.has("accion_clientes");
  const tieneViabilidad = familiasEnRuta.has("viabilidad_economica");
  const esCompleta = tieneAccion && tieneViabilidad && ruta.length >= MIN_NODOS_COMPLETA;
  const faltantes: string[] = [];
  if (!tieneAccion) faltantes.push("validar con clientes reales (entrevistas, MVP, pruebas de usuario)");
  if (!tieneViabilidad)
    faltantes.push("si tu idea puede sostenerse economicamente (costos, precios, punto de equilibrio)");
  if (ruta.length < MIN_NODOS_COMPLETA) faltantes.push("mas profundidad en el recorrido");
  return {
    es_completa: esCompleta,
    tiene_accion_clientes: tieneAccion,
    tiene_viabilidad_economica: tieneViabilidad,
    num_nodos: ruta.length,
    familias_faltantes: faltantes,
  };
}
