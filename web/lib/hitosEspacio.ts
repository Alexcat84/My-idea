/**
 * Campaña "Espacios" — la cara "Tu avance": los HITOS ESTRUCTURALES de un espacio
 * (de datos ya persistidos), como el timeline de La Celebración. Muestra LO MÁS
 * IMPORTANTE (el nacimiento, la claridad, el plan, el cierre), NO cada acción
 * (eso es la bitácora / el Manos a la obra). Cero estadística, cero LLM.
 *
 * Cada espacio cuenta SU historia desde su nacimiento:
 *  - core:  La Chispa → Claridad → Tu Plan → Realizada
 *  - mundo: Tu diagnóstico → Su Plan → Cerrado
 * Los hitos que ya ocurrieron traen su fecha; los que faltan DESPUÉS del hito
 * actual van pendientes (gris, sin fecha; decisión del fundador, 26 sep 2026). El
 * cierre se muestra SIEMPRE como destino: alcanzado si ya cerró, pendiente (gris)
 * si no. Los hitos de un espacio NO incluyen los de otro (ley de lib/espacios).
 */

import { elegir, LOCALE_BASE, type Locale } from "./i18n/config";
import { interpolar } from "./i18n/interpolar";
import { HITOS } from "./i18n/mensajes/hitos";

export type TipoHito = "chispa" | "claridad" | "plan" | "diagnostico" | "cierre";

export interface HitoEspacio {
  tipo: TipoHito;
  etiqueta: string;
  subtitulo?: string;
  /** ISO si el hito ya ocurrió; null si es un destino aún pendiente (el cierre). */
  fecha: string | null;
  alcanzado: boolean;
}

export interface EntradaAvanceCore {
  espacio: "core";
  chispaAt?: string | null; // projects.created_at
  claridadAt?: string | null; // organizador.created_at
  planAt?: string | null; // plan.created_at
  realizadaAt?: string | null; // projects.realizada_at
}

export interface EntradaAvanceMundo {
  espacio: "mundo";
  nombre: string;
  diagnosticoAt?: string | null; // project_unlocks.resumen_at
  planAt?: string | null; // plan.created_at (del dominio)
  cerradoAt?: string | null; // project_unlocks.completado_at
}

export type EntradaAvance = EntradaAvanceCore | EntradaAvanceMundo;

export function hitosDeEspacio(entrada: EntradaAvance, idioma: Locale = LOCALE_BASE): HitoEspacio[] {
  const t = elegir(HITOS, idioma);
  const hitos: HitoEspacio[] = [];
  const etapas: Array<{ tipo: TipoHito; etiqueta: string; subtitulo: string; fecha?: string | null }> =
    entrada.espacio === "core"
      ? [
          { tipo: "chispa", etiqueta: t.core.chispa, subtitulo: t.core.chispaSub, fecha: entrada.chispaAt },
          { tipo: "claridad", etiqueta: t.core.claridad, subtitulo: t.core.claridadSub, fecha: entrada.claridadAt },
          { tipo: "plan", etiqueta: t.core.plan, subtitulo: t.core.planSub, fecha: entrada.planAt },
        ]
      : [
          { tipo: "diagnostico", etiqueta: t.mundo.diagnostico, subtitulo: t.mundo.diagnosticoSub, fecha: entrada.diagnosticoAt },
          { tipo: "plan", etiqueta: interpolar(t.mundo.plan, { mundo: entrada.nombre }), subtitulo: t.mundo.planSub, fecha: entrada.planAt },
        ];
  // "Tu avance" es un camino (decisión del fundador, 26 sep 2026): lo que ya
  // ocurrió, con su fecha, y DESPUÉS del hito actual, en gris, todo lo que falta.
  // Una etapa ANTERIOR al hito actual que nunca ocurrió no se dibuja: no se
  // inventa un pasado.
  const ultimaAlcanzada = etapas.map((e) => Boolean(e.fecha)).lastIndexOf(true);
  etapas.forEach((e, i) => {
    if (e.fecha) hitos.push({ tipo: e.tipo, etiqueta: e.etiqueta, subtitulo: e.subtitulo, fecha: e.fecha, alcanzado: true });
    else if (i > ultimaAlcanzada) hitos.push({ tipo: e.tipo, etiqueta: e.etiqueta, subtitulo: e.subtitulo, fecha: null, alcanzado: false });
  });

  // El cierre: el destino. Siempre presente; verde si ya cerró, gris si falta.
  const cierreAt = entrada.espacio === "core" ? entrada.realizadaAt : entrada.cerradoAt;
  if (entrada.espacio === "core") {
    hitos.push({
      tipo: "cierre",
      etiqueta: cierreAt ? t.core.realizada : t.core.cierre,
      subtitulo: cierreAt ? t.core.realizadaSub : t.core.cierreSub,
      fecha: cierreAt ?? null,
      alcanzado: Boolean(cierreAt),
    });
  } else {
    hitos.push({
      tipo: "cierre",
      etiqueta: cierreAt ? t.mundo.cerrado : t.mundo.cierre,
      subtitulo: cierreAt ? t.mundo.cerradoSub : t.mundo.cierreSub,
      fecha: cierreAt ?? null,
      alcanzado: Boolean(cierreAt),
    });
  }

  return hitos;
}
