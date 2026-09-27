/**
 * finDeEntrevista.ts: qué ofrece la pantalla al terminar una entrevista y a
 * qué precio (AUD-09 H01). Pura, sin estado: la usa IdeaView para decidir el
 * botón final y lee el precio de la MISMA regla que usa el cobro del servidor
 * (montoDelPlan en precios.ts), según el espacio y el tipo de sesión.
 *
 *   núcleo (primera o seguimiento) -> plan, al precio de su concepto
 *   mundo, preview                 -> diagnóstico gratis (el plan se compra después)
 *   mundo, seguimiento             -> plan del ciclo, al precio de su concepto
 */
import { montoDelPlan } from "./precios";

export interface FinDeEntrevista {
  /** true: el botón pide el diagnóstico gratis del preview de un mundo. */
  esDiagnostico: boolean;
  /** Créditos que se descontarán a la entrega (0 para el diagnóstico). */
  costo: number;
}

export function finDeEntrevista(dominio: string, esSeguimiento: boolean): FinDeEntrevista {
  const esDiagnostico = dominio !== "core" && !esSeguimiento;
  return { esDiagnostico, costo: esDiagnostico ? 0 : montoDelPlan(dominio, esSeguimiento) };
}
