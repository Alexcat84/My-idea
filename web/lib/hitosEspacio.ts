/**
 * Campaña "Espacios" — la cara "Tu avance": los HITOS ESTRUCTURALES de un espacio
 * (de datos ya persistidos), como el timeline de La Celebración. Muestra LO MÁS
 * IMPORTANTE (el nacimiento, la claridad, el plan, el cierre), NO cada acción
 * (eso es la bitácora / el Manos a la obra). Cero estadística, cero LLM.
 *
 * Cada espacio cuenta SU historia desde su nacimiento:
 *  - core:  La Chispa → Claridad → Tu Plan → Realizada
 *  - mundo: Tu diagnóstico → Su Plan → Cerrado
 * Los hitos de arranque se muestran solo si YA ocurrieron (traen fecha); el
 * cierre se muestra SIEMPRE como destino: alcanzado si ya cerró, pendiente (gris)
 * si no. Los hitos de un espacio NO incluyen los de otro (ley de lib/espacios).
 */

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

export function hitosDeEspacio(entrada: EntradaAvance): HitoEspacio[] {
  const hitos: HitoEspacio[] = [];
  const arranque = (tipo: TipoHito, etiqueta: string, subtitulo: string, fecha?: string | null) => {
    // Solo si ya ocurrió (trae fecha): no se dibuja un arranque sin fecha, ni se
    // inventa.
    if (fecha) hitos.push({ tipo, etiqueta, subtitulo, fecha, alcanzado: true });
  };

  if (entrada.espacio === "core") {
    arranque("chispa", "La Chispa", "La idea nace", entrada.chispaAt);
    arranque("claridad", "Claridad", "Tu idea, organizada", entrada.claridadAt);
    arranque("plan", "Tu Plan", "Tu plan de acción, listo", entrada.planAt);
  } else {
    arranque("diagnostico", "Tu diagnóstico", "El primer vistazo de este frente", entrada.diagnosticoAt);
    arranque("plan", `El plan de ${entrada.nombre}`, "Listo para ejecutar", entrada.planAt);
  }

  // El cierre: el destino. Siempre presente; verde si ya cerró, gris si falta.
  const cierreAt = entrada.espacio === "core" ? entrada.realizadaAt : entrada.cerradoAt;
  if (entrada.espacio === "core") {
    hitos.push({
      tipo: "cierre",
      etiqueta: cierreAt ? "Realizada" : "El cierre",
      subtitulo: cierreAt ? "Aquí nace tu proyecto" : "Cuando lo sientas real",
      fecha: cierreAt ?? null,
      alcanzado: Boolean(cierreAt),
    });
  } else {
    hitos.push({
      tipo: "cierre",
      etiqueta: cierreAt ? "Cerrado" : "El cierre",
      subtitulo: cierreAt ? "Diste este frente por terminado" : "Cuando lo des por terminado",
      fecha: cierreAt ?? null,
      alcanzado: Boolean(cierreAt),
    });
  }

  return hitos;
}
