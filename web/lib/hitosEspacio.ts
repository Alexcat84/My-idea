/**
 * Campaña "Espacios" — la cara "Tu avance": los HITOS reales de un espacio, de
 * datos YA persistidos (cero invención, cero estadística, cero LLM). Puro y
 * testeable; fuente única que comparten LineaAvance (UI) y los tests, para que
 * no envejezcan. Es la historia de hitos, no números (eso vive en Análisis).
 *
 * Regla: cada espacio cuenta SU historia desde su nacimiento.
 *  - core:  La Chispa → Claridad → Tu Plan → cada acción hecha → Realizada
 *  - mundo: Tu diagnóstico → Su Plan → cada acción hecha → Cerrado
 * Los hitos de un espacio NO incluyen los de otro (misma ley que lib/espacios).
 * Los hitos de arranque y las acciones se muestran solo si YA ocurrieron (traen
 * fecha); el cierre se muestra SIEMPRE, como destino: alcanzado si ya cerró,
 * pendiente (gris) si no.
 */

export type TipoHito = "chispa" | "claridad" | "plan" | "diagnostico" | "accion" | "cierre";

export interface HitoEspacio {
  tipo: TipoHito;
  etiqueta: string;
  /** ISO si el hito ya ocurrió; null si es un destino aún pendiente (el cierre). */
  fecha: string | null;
  alcanzado: boolean;
}

/** Un ítem del checklist del espacio (ya scopeado por dominio en la UI). */
export interface ItemAvance {
  texto: string;
  completedAt: string | null;
}

export interface EntradaAvanceCore {
  espacio: "core";
  chispaAt?: string | null; // projects.created_at
  claridadAt?: string | null; // organizador.created_at
  planAt?: string | null; // plan.created_at
  realizadaAt?: string | null; // projects.realizada_at
  items: ItemAvance[];
}

export interface EntradaAvanceMundo {
  espacio: "mundo";
  nombre: string;
  diagnosticoAt?: string | null; // project_unlocks.resumen_at
  planAt?: string | null; // plan.created_at (del dominio)
  cerradoAt?: string | null; // project_unlocks.completado_at
  items: ItemAvance[];
}

export type EntradaAvance = EntradaAvanceCore | EntradaAvanceMundo;

/** Las acciones HECHAS (con fecha real de cumplimiento), en orden cronológico. */
function accionesHechas(items: ItemAvance[]): HitoEspacio[] {
  return items
    .filter((i) => i.completedAt)
    .sort((a, b) => (a.completedAt! < b.completedAt! ? -1 : a.completedAt! > b.completedAt! ? 1 : 0))
    .map((i) => ({ tipo: "accion" as const, etiqueta: i.texto, fecha: i.completedAt, alcanzado: true }));
}

export function hitosDeEspacio(entrada: EntradaAvance): HitoEspacio[] {
  const hitos: HitoEspacio[] = [];
  const arranque = (tipo: TipoHito, etiqueta: string, fecha?: string | null) => {
    // Solo si ya ocurrió (trae fecha): un hito de arranque sin fecha no se
    // dibuja como "pendiente" — habría pasado sin registrar, y no se inventa.
    if (fecha) hitos.push({ tipo, etiqueta, fecha, alcanzado: true });
  };

  if (entrada.espacio === "core") {
    arranque("chispa", "La Chispa", entrada.chispaAt);
    arranque("claridad", "Claridad", entrada.claridadAt);
    arranque("plan", "Tu Plan", entrada.planAt);
  } else {
    arranque("diagnostico", "Tu diagnóstico", entrada.diagnosticoAt);
    arranque("plan", `El plan de ${entrada.nombre}`, entrada.planAt);
  }

  hitos.push(...accionesHechas(entrada.items));

  // El cierre: el destino. Siempre presente; verde si ya cerró, gris si falta.
  const cierreAt = entrada.espacio === "core" ? entrada.realizadaAt : entrada.cerradoAt;
  const cierreEtiqueta = cierreAt
    ? entrada.espacio === "core"
      ? "Realizada"
      : "Cerrado"
    : "El cierre";
  hitos.push({ tipo: "cierre", etiqueta: cierreEtiqueta, fecha: cierreAt ?? null, alcanzado: Boolean(cierreAt) });

  return hitos;
}
