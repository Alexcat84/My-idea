/**
 * seguimientoComposer.ts — Fase 3.3: convierte el ritual de 3 tarjetas
 * (checklist actualizado + detalles + enfoque) en el mensaje "qué ha pasado"
 * que el motor de seguimiento ya sabe recibir. Determinístico y compacto:
 * el usuario nunca redacta su historia dos veces; el sistema la compone.
 * El texto resultante queda auditable en la bitácora de la sesión.
 */
import type { ChecklistEstado } from "../dbContract";

export interface ItemParaComponer {
  etapa: number;
  texto: string;
  destacado: boolean;
  estado: ChecklistEstado;
  nota?: string | null;
}

export interface EntradaSeguimiento {
  items: ItemParaComponer[];
  detalles?: string | null; // "¿Algo más que deba saber?"
  enfoque?: string | null; // "¿Hacia dónde profundizamos?" (null = "No estoy seguro")
  /** Fase 4.0 §3: el BLOQUE DE REALIDAD (construirBloqueRealidad), ya
   * redactado desde analytics.ts. null si no hay nada medido todavía. */
  bloqueRealidad?: string | null;
}

const ETIQUETA: Record<ChecklistEstado, string> = {
  hecho: "HECHO",
  a_medias: "A MEDIAS",
  empezado: "APENAS EMPEZADO",
  pendiente: "SIN EMPEZAR",
};

function lista(items: ItemParaComponer[], estado: ChecklistEstado): string[] {
  return items
    .filter((i) => i.estado === estado)
    .map((i) => `- ${i.texto}${i.nota ? ` (nota: ${i.nota.trim()})` : ""}`);
}

/** Mensaje compacto en el orden que mejor lee el intérprete: logros primero,
 * bloqueos después, contexto extra, y el enfoque declarado al final (la
 * prioridad_declarada del motor se alimenta de esa última línea). */
export function componerMensajeSeguimiento(e: EntradaSeguimiento): string {
  const partes: string[] = ["Desde el último plan, este es mi avance real:"];
  const orden: ChecklistEstado[] = ["hecho", "a_medias", "empezado", "pendiente"];
  for (const estado of orden) {
    const filas = lista(e.items, estado);
    if (filas.length) {
      partes.push(`${ETIQUETA[estado]} (${filas.length}):`, ...filas);
    }
  }
  if (e.items.length === 0) {
    partes.push("(aún no actualicé el checklist; cuéntame desde donde estaba)");
  }
  const detalles = e.detalles?.trim();
  if (detalles) partes.push(`Además: ${detalles}`);
  // Fase 4.0 §3: la realidad medida va ANTES del enfoque — el motor lee el
  // tiempo real (cumplimiento, atascos, ritmo) y no solo lo que marqué.
  const bloque = e.bloqueRealidad?.trim();
  if (bloque) partes.push("", bloque, "");
  const enfoque = e.enfoque?.trim();
  partes.push(
    enfoque
      ? `Lo que más me interesa profundizar ahora: ${enfoque}`
      : "No estoy seguro de hacia dónde profundizar; guíame según mi avance."
  );
  return partes.join("\n");
}
