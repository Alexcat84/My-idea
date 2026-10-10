/**
 * EL TITULO NO AFIRMA NADA DEL NEGOCIO QUE LA PERSONA NO DIJO (decision del fundador, 10 oct 2026). Caso real: «Plan
 * para tu pieza hecha a mano» cuando la persona nunca dijo como fabrica. Una marca de cita no basta (el titulo comparte
 * "pieza" con la respuesta citada), asi que el codigo mira cada palabra con contenido del titulo (cinco letras o mas):
 * tiene que venir de lo que dijo la persona, de los NOMBRES de los temas que recibio el redactor (apoyoDelTitulo, en
 * planRedactor.ts; el cuerpo de los temas no cuenta) o del vocabulario generico de un plan (plan, pasos, valida...). Si
 * alguna no viene de ahi, el titulo pasa al neutro del idioma ("Tu plan de accion"). Medido en los 14 titulos reales de
 * la segunda medicion: cambian 2, «hecha a mano» y «salgan parejas» (la persona hablo de acabado irregular, no de
 * parejas): un falso positivo barato, porque el neutro no afirma nada.
 * Limite declarado: el juicio por palabras se hace solo en espanol (los temas estan en espanol); en otro idioma manda la
 * regla del prompt.
 */
import type { Locale } from "../i18n/config";

const GENERICAS = new Set(
  [
    "primeros", "primeras", "primer", "primera", "pasos", "ordenar", "ordena", "validar", "valida", "decidir", "decide",
    "definir", "define", "calcular", "calcula", "medir", "mejorar", "mejora", "cuidar", "cuida", "proteger", "protege",
    "preparar", "prepara", "organizar", "organiza", "crecer", "crece", "probar", "prueba", "empezar", "empieza",
    "arrancar", "arranca", "comprobar", "comprueba", "confirmar", "confirma", "camino", "siguiente", "etapa", "etapas",
    "cerrar", "cierra", "sostener", "sostiene", "proyecto", "desde", "hasta", "hacia", "entre", "sobre", "nuevo",
    "nueva", "nuevos", "nuevas", "reales", "claro", "clara", "claridad", "mejor", "bueno", "buena", "rumbo", "numeros",
    "accion", "acciones", "ordenado", "ordenada", "paso",
    // Medidos en los 14 titulos reales de la segunda medicion final: palabras sin contenido de negocio.
    "hecho", "falta", "faltan", "alguien", "salir", "salgan", "salga",
  ].map((w) => w.normalize("NFD").replace(/\p{Mn}/gu, ""))
);

const normal = (s: string) => s.normalize("NFD").replace(/\p{Mn}/gu, "").toLowerCase();
const palabras = (s: string) => normal(s).match(/\p{L}{5,}/gu) ?? [];

export function tituloConRespaldo(
  cuerpo: string,
  apoyo: string[],
  tituloNeutro: string,
  idioma: Locale
): { texto: string; cambiado: boolean; sinRespaldo: string[] } {
  const lineas = cuerpo.split("\n");
  const i = lineas.findIndex((l) => /^#\s/.test(l));
  if (i < 0 || idioma !== "es") return { texto: cuerpo, cambiado: false, sinRespaldo: [] };
  const raices = new Set(apoyo.flatMap(palabras).map((w) => w.slice(0, 5)));
  const sinRespaldo = palabras(lineas[i].replace(/^#\s+/, "")).filter((w) => !GENERICAS.has(w) && !raices.has(w.slice(0, 5)));
  if (sinRespaldo.length === 0) return { texto: cuerpo, cambiado: false, sinRespaldo: [] };
  lineas[i] = tituloNeutro;
  return { texto: lineas.join("\n"), cambiado: true, sinRespaldo };
}
