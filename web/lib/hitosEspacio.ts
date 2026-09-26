/**
 * Campaña "Espacios" — la cara "Tu avance": los HITOS de un espacio (de datos ya
 * persistidos), como el timeline de La Celebración. Es un CAMINO, no un
 * registro: orden cronológico, de la primera etapa hacia la actual y lo que
 * falta. Cero estadística, cero LLM.
 *
 * Cada espacio cuenta SU historia:
 *  - core (decisión del fundador, 26 sep 2026): las SEIS etapas del recorrido,
 *    las mismas del paso a paso y con sus nombres del glosario: La Chispa →
 *    Claridad → La Exploración → Tu Plan → Manos a la Obra → Realizado. La etapa
 *    actual es la de la regla única (lib/etapaIdea.ts). Las alcanzadas llevan
 *    color y su fecha cuando se conoce (sin inventarla: Manos a la Obra solo la
 *    tiene si ya hay una tarea hecha); las que faltan, gris y sin fecha.
 *  - mundo: sus hitos propios, Tu diagnóstico → Su plan → Cerrado; lo que ya
 *    ocurrió con su fecha y, después del hito actual, lo que falta en gris.
 * El cierre es siempre el destino: alcanzado si ya cerró, pendiente (gris) si
 * no. Los hitos de un espacio NO incluyen los de otro (ley de lib/espacios).
 */

import { elegir, LOCALE_BASE, type Locale } from "./i18n/config";
import { interpolar } from "./i18n/interpolar";
import { HITOS } from "./i18n/mensajes/hitos";
import { STEPPER_VIAJE } from "./i18n/mensajes/stepperViaje";

export type TipoHito = "chispa" | "claridad" | "exploracion" | "plan" | "manos" | "diagnostico" | "cierre";

export interface HitoEspacio {
  tipo: TipoHito;
  etiqueta: string;
  subtitulo?: string;
  /** ISO si el hito ya ocurrió y se sabe cuándo; null si falta o no se conoce. */
  fecha: string | null;
  alcanzado: boolean;
}

export interface EntradaAvanceCore {
  espacio: "core";
  /** La etapa actual del recorrido (1..5, lib/etapaIdea.ts); con realizadaAt, la 6. */
  etapa: number;
  chispaAt?: string | null; // projects.created_at
  claridadAt?: string | null; // organizador.created_at
  exploracionAt?: string | null; // la primera sesión de exploración del núcleo
  planAt?: string | null; // plan.created_at
  manosAt?: string | null; // la primera tarea hecha del núcleo
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

  if (entrada.espacio === "core") {
    const nombres = elegir(STEPPER_VIAJE, idioma).etapas;
    const actual = entrada.realizadaAt ? 6 : Math.min(Math.max(entrada.etapa, 1), 5);
    const seis: Array<{ tipo: TipoHito; subtitulo: string; fecha?: string | null }> = [
      { tipo: "chispa", subtitulo: t.core.chispaSub, fecha: entrada.chispaAt },
      { tipo: "claridad", subtitulo: t.core.claridadSub, fecha: entrada.claridadAt },
      { tipo: "exploracion", subtitulo: t.core.exploracionSub, fecha: entrada.exploracionAt },
      { tipo: "plan", subtitulo: t.core.planSub, fecha: entrada.planAt },
      { tipo: "manos", subtitulo: t.core.manosSub, fecha: entrada.manosAt },
      { tipo: "cierre", subtitulo: entrada.realizadaAt ? t.core.realizadaSub : t.core.cierreSub, fecha: entrada.realizadaAt },
    ];
    return seis.map((e, i) => {
      const alcanzado = i + 1 <= actual;
      return { tipo: e.tipo, etiqueta: nombres[i], subtitulo: e.subtitulo, fecha: alcanzado ? (e.fecha ?? null) : null, alcanzado };
    });
  }

  const hitos: HitoEspacio[] = [];
  const etapas: Array<{ tipo: TipoHito; etiqueta: string; subtitulo: string; fecha?: string | null }> = [
    { tipo: "diagnostico", etiqueta: t.mundo.diagnostico, subtitulo: t.mundo.diagnosticoSub, fecha: entrada.diagnosticoAt },
    { tipo: "plan", etiqueta: interpolar(t.mundo.plan, { mundo: entrada.nombre }), subtitulo: t.mundo.planSub, fecha: entrada.planAt },
  ];
  // Lo que ya ocurrió, con su fecha, y DESPUÉS del hito actual, en gris, lo que
  // falta. Una etapa ANTERIOR al hito actual que nunca ocurrió no se dibuja.
  const ultimaAlcanzada = etapas.map((e) => Boolean(e.fecha)).lastIndexOf(true);
  etapas.forEach((e, i) => {
    if (e.fecha) hitos.push({ tipo: e.tipo, etiqueta: e.etiqueta, subtitulo: e.subtitulo, fecha: e.fecha, alcanzado: true });
    else if (i > ultimaAlcanzada) hitos.push({ tipo: e.tipo, etiqueta: e.etiqueta, subtitulo: e.subtitulo, fecha: null, alcanzado: false });
  });
  // El cierre: el destino. Siempre presente; verde si ya cerró, gris si falta.
  hitos.push({
    tipo: "cierre",
    etiqueta: entrada.cerradoAt ? t.mundo.cerrado : t.mundo.cierre,
    subtitulo: entrada.cerradoAt ? t.mundo.cerradoSub : t.mundo.cierreSub,
    fecha: entrada.cerradoAt ?? null,
    alcanzado: Boolean(entrada.cerradoAt),
  });
  return hitos;
}
