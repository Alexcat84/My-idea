/**
 * avisos.ts - los AVISOS de un nodo en la tarjeta de pregunta (decision del fundador del 26 sep 2026,
 * saneamiento del dataset, tanda 1; docs/POLITICA_MARCO_PAIS.md):
 *   - jurisdiccion (dataset/metadata/jurisdiccion.json): clase B, "Ejemplo de Estados Unidos: busca el
 *     equivalente en tu pais"; clase C, "Aplica si operas o vendes en Estados Unidos". La clase A no avisa.
 *   - vigencia (dataset/metadata/vigencia.json): "Verifica la norma vigente en tu pais: estas reglas cambian con el
 *     tiempo", en los nodos con una norma, un plazo legal, una cifra con fecha o una institucion. Desde el 30 sep 2026
 *     (regla dura del fundador: ningun origen se insinua) el aviso no lleva el ano de la fuente.
 *     REGLA ESTRICTA (fundador, 26 sep 2026): el aviso NUNCA nombra el libro; el libro vive solo en los metadatos.
 * Las listas son CURADAS y se sincronizan como assets (scripts/sync_assets_web.py) en su VISTA WEB: el pais y la
 * clase, y que nodos llevan aviso de vigencia, sin el ano, el libro ni el motivo (NADA INTERNO LLEGA AL NAVEGADOR, fundador, 27 sep 2026).
 * El texto del nodo no se
 * toca: el aviso va aparte, en el idioma de la interfaz. Se resuelve por el mismo resolutor que la etiqueta,
 * asi que una referencia historica avisa lo de quien la representa hoy.
 */
import jurisdiccionJson from "../assets/jurisdiccion.json";
import vigenciaJson from "../assets/vigencia.json";
import { elegir, LOCALE_BASE, type Locale } from "../i18n/config";
import { interpolar } from "../i18n/interpolar";
import { AVISO_NODO, type CodigoPais } from "../i18n/mensajes/avisoNodo";
import { resolverId, type GrafoResoluble } from "./graph";

export type ClasePais = "A" | "B" | "C";
export interface EntradaJurisdiccion {
  pais: CodigoPais | "INT";
  clase: ClasePais;
}
/** La entrada de vigencia no lleva datos en la web: solo marca que el nodo avisa. */
export type EntradaVigencia = Record<string, never>;

export const JURISDICCION = (jurisdiccionJson as unknown as { nodos: Record<string, EntradaJurisdiccion> }).nodos;
export const VIGENCIA_NODOS = (vigenciaJson as unknown as { nodos: Record<string, EntradaVigencia> }).nodos;

export function avisosNodo(nid: string, graph: GrafoResoluble, idioma: Locale = LOCALE_BASE): string[] {
  const real = resolverId(nid, graph) ?? nid;
  const t = elegir(AVISO_NODO, idioma);
  const avisos: string[] = [];
  const j = JURISDICCION[real];
  if (j && (j.clase === "B" || j.clase === "C")) {
    const pais = j.pais === "INT" ? undefined : t.paises[j.pais];
    if (pais) {
      avisos.push(j.clase === "B" ? interpolar(t.claseB, { desde: pais.desde }) : interpolar(t.claseC, { en: pais.en }));
    }
  }
  const v = VIGENCIA_NODOS[real];
  if (v) avisos.push(t.vigencia);
  return avisos;
}
