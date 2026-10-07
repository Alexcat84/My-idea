/**
 * La voz de cliente de un NODO (integración del mundo 11, decisiones del
 * fundador del 28 sep 2026): el texto que llega a la IA o a la pantalla no habla
 * con voz de libro ni lleva marcas de auditoría de la extracción. Las reglas son
 * las de i18n/frasesProhibidas.ts (vozDeLibro y marcasInternas); aquí se aplican
 * a los campos de un nodo, que están en español.
 *
 * Los campos son los que llegan a la IA o a la pantalla según
 * docs/fidelidad/CAMPOS_QUE_LLEGAN.md. Lo interno (fuente, fuentes_internas,
 * correcciones, notas_extraccion) no se barre: nunca sale del servidor.
 */
import { faltasDeVoz, type FaltaVoz } from "./i18n/frasesProhibidas";

export const CAMPOS_DE_CLIENTE = [
  "etiqueta_arbol",
  "titulo_concepto",
  "resumen_teorico",
  "pasos_accionables",
  "condiciones_activacion",
  "entregable_esperado",
] as const;

/** Las reglas de voz que se aplican a los campos de un nodo (van a guardas_contenido.json para la forja). */
export const REGLAS_VOZ_DE_NODO = ["vozDeLibro", "marcasInternas"] as const;
const REGLAS = new Set<string>(REGLAS_VOZ_DE_NODO);

/**
 * Lo adjudicado a mano: un texto vivo que usa la palabra en su sentido propio
 * (no como fuente). Clave "node_id.campo", con su motivo.
 */
export const ADJUDICADOS: Readonly<Record<string, string>> = {
  "reglas_de_origen_fta_2.pasos_accionables":
    "\"el capítulo de ROOs del FTA\" es el capítulo de reglas de origen de un tratado comercial, no el de un libro",
  "definicion_calidad_segun_agente.resumen_teorico":
    "\"el autor\" es uno de los agentes que juzgan la calidad de un producto impreso (la planta, el consumidor, el impresor o el autor), no una cita a una fuente",
};

/** Las faltas de voz de cliente de un texto en español. */
export function faltasDeCliente(texto: string): FaltaVoz[] {
  return faltasDeVoz(texto, "es").filter((f) => REGLAS.has(f.regla));
}

export type FaltaNodo = FaltaVoz & { node_id: string; campo: string };

/** Las faltas de un nodo, campo por campo (los campos lista, elemento a elemento). */
export function faltasDeNodo(nodo: Record<string, unknown>): FaltaNodo[] {
  const node_id = String(nodo.node_id ?? "");
  const faltas: FaltaNodo[] = [];
  for (const campo of CAMPOS_DE_CLIENTE) {
    const v = nodo[campo];
    const piezas: Array<[string, unknown]> = Array.isArray(v) ? v.map((x, i) => [`${campo}[${i}]`, x]) : [[campo, v]];
    for (const [donde, t] of piezas) {
      if (typeof t !== "string" || ADJUDICADOS[`${node_id}.${campo}`]) continue;
      for (const f of faltasDeCliente(t)) faltas.push({ ...f, node_id, campo: donde });
    }
  }
  return faltas;
}
