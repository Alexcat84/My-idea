/**
 * EL PLAN DE MUNDO SABE QUE TAREAS DEL NUCLEO ESTAN HECHAS (decision del fundador, 10 oct 2026, noche, punto 2b; caso
 * real 85248377). De cada tarea del nucleo vigente que no esta pendiente viaja el titulo de su tema (la etiqueta de arbol
 * de sus nodos de origen) y su estado; nunca el texto de la tarea, que era del plan y no de la persona. Las tareas sin
 * tema no viajan: sin el texto no habria con que nombrarlas.
 */
import type { ChecklistEstado } from "../dbContract";

export interface TareaNucleo {
  estado: ChecklistEstado;
  completed_at?: string | null;
  nodos_origen?: string[] | null;
}

export interface ActividadNucleoIA {
  temas: string[];
  estado: ChecklistEstado;
}

/** `hasta` (opcional, el guion de medicion): lo hecho despues de esa fecha cuenta como pendiente. */
export function nucleoParaMundo(tareas: TareaNucleo[], tituloDeNodo: (nodeId: string) => string | null, hasta?: string): ActividadNucleoIA[] {
  const out: ActividadNucleoIA[] = [];
  const vistos = new Set<string>();
  for (const t of tareas) {
    if (t.estado === "pendiente") continue;
    if (hasta && t.estado === "hecho" && (!t.completed_at || Date.parse(t.completed_at) > Date.parse(hasta))) continue;
    const temas = [...new Set((t.nodos_origen ?? []).map(tituloDeNodo).filter((x): x is string => Boolean(x)))];
    if (temas.length === 0) continue;
    const clave = `${temas.join("|")}::${t.estado}`;
    if (vistos.has(clave)) continue;
    vistos.add(clave);
    out.push({ temas, estado: t.estado });
  }
  return out;
}
