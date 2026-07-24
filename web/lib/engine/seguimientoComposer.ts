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
  /** gestor de estados: el porqué de una tarea retirada (estado no_aplica) */
  noAplicaMotivo?: string | null;
}

/** Una fila cruda de checklist_items, como la devuelve la consulta del follow. */
export interface FilaChecklist {
  plan_id: string;
  /** null = core (los ítems anteriores a la migración 016 no lo traen). */
  dominio?: string | null;
  etapa: number;
  orden?: number;
  texto: string;
  destacado: boolean;
  estado: ChecklistEstado;
  nota?: string | null;
  no_aplica_motivo?: string | null;
  created_at: string;
}

/**
 * Fase 4.1 (V4, auditoría de paridad de mundos): los ítems del ÚLTIMO plan DE
 * UN DOMINIO. Antes se tomaba el plan del ítem más reciente FUERA CUAL FUERA su
 * dominio: si el usuario acababa de explorar un mundo, "Contar qué pasó"
 * componía su "mi avance real" con el checklist del MUNDO mientras el bloque de
 * realidad llevaba cumplimiento core.
 *
 * Fase 4.2: el dominio es parámetro. Ya no hay un solo follow — cada mundo
 * activo tiene el suyo, y cada uno compone con SUS ítems. `dominio` "core" cubre
 * también los ítems previos a la migración 016, que no lo traen.
 *
 * Ordena por su cuenta a propósito: no depende de que quien la llama haya
 * ordenado la consulta, y así el test la puede ejercitar de verdad.
 */
export function itemsDelUltimoPlanDe(filas: FilaChecklist[], dominio: string): ItemParaComponer[] {
  const delDominio = filas.filter((f) =>
    dominio === "core" ? !f.dominio || f.dominio === "core" : f.dominio === dominio
  );
  if (delDominio.length === 0) return [];
  const masReciente = [...delDominio].sort((a, b) => b.created_at.localeCompare(a.created_at))[0];
  return delDominio
    .filter((f) => f.plan_id === masReciente.plan_id)
    .sort((a, b) => a.etapa - b.etapa || (a.orden ?? 0) - (b.orden ?? 0))
    .map((f) => ({
      etapa: f.etapa,
      texto: f.texto,
      destacado: f.destacado,
      estado: f.estado,
      nota: f.nota ?? null,
      noAplicaMotivo: f.no_aplica_motivo ?? null,
    }));
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
  en_proceso: "EN PROCESO",
  empezado: "APENAS EMPEZADO",
  pendiente: "SIN EMPEZAR",
  no_aplica: "RETIRADA (no aplica)",
};

function lista(items: ItemParaComponer[], estado: ChecklistEstado): string[] {
  return items
    .filter((i) => i.estado === estado)
    .map((i) => `- ${i.texto}${i.nota ? ` (nota: ${i.nota.trim()})` : ""}`);
}

/** Mensaje compacto en el orden que mejor lee el intérprete: logros primero,
 * bloqueos después, contexto extra, y el enfoque declarado al final (la
 * prioridad_declarada del motor se alimenta de esa última línea).
 *
 * Gestor de estados: las RETIRADAS (no_aplica) NO se componen como pendientes.
 * Van en su propia sección, marcadas para que el intérprete no las vuelva a
 * proponer: retirar una tarea es una decisión del usuario, no un olvido. */
export function componerMensajeSeguimiento(e: EntradaSeguimiento): string {
  const partes: string[] = ["Desde el último plan, este es mi avance real:"];
  const orden: ChecklistEstado[] = ["hecho", "en_proceso", "empezado", "pendiente"];
  for (const estado of orden) {
    const filas = lista(e.items, estado);
    if (filas.length) {
      partes.push(`${ETIQUETA[estado]} (${filas.length}):`, ...filas);
    }
  }
  const retiradas = e.items
    .filter((i) => i.estado === "no_aplica")
    .map((i) => `- ${i.texto}${i.noAplicaMotivo ? ` (porque: ${i.noAplicaMotivo.trim()})` : ""}`);
  if (retiradas.length) {
    partes.push(
      `${ETIQUETA.no_aplica} (${retiradas.length}) — decidí que no corren para esta idea; NO las vuelvas a proponer:`,
      ...retiradas
    );
  }
  const activas = e.items.filter((i) => i.estado !== "no_aplica");
  if (activas.length === 0 && e.items.length > 0) {
    partes.push("(retiré todas las tareas del plan; propón desde cero según lo que te cuento)");
  } else if (e.items.length === 0) {
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
