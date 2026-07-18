/**
 * numerosVivo.ts - FASE B (canon 14): la logica PURA del tablero vivo que la
 * ruta usa pero que conviene probar aparte. El veredicto determinista (la
 * frase con su color, sin modelo: los numeros los hace codigo), la
 * comparacion de cifras para decidir si hay una version nueva, y el tope
 * diario de re-narraciones (freno, jamas cobro ni bloqueo del recalculo).
 */
import type { NumerosProyecto } from "./calculadora";
import type { Tablero } from "./tableroNumeros";

/** Re-narraciones del modelo por idea por dia. Es un FRENO de costo, no un
 * cobro: el recalculo determinista es gratis e ilimitado siempre. Ajustable
 * con datos de la beta. */
export const TOPE_RENARRACION_DIA = 5;

/** En palabras de persona cuando se alcanza el tope (amarre del fundador):
 * espejo, sin regano, y deja claro que nada se pierde. */
export const MENSAJE_TOPE_RENARRACION =
  "Por hoy llegamos al limite de relecturas. Tus numeros y tus cambios quedan guardados, el recalculo sigue disponible sin limite, y manana puedes pedir una relectura nueva.";

/** Formatea un entero de dinero al estilo del canon: "$1.200", "$170". */
function pesos(n: number): string {
  const r = Math.round(Math.abs(n));
  return "$" + String(r).replace(/\B(?=(\d{3})+(?!\d))/g, ".");
}

function medio(v: number | { min: number; max: number } | null | undefined): number | null {
  if (v === null || v === undefined) return null;
  return typeof v === "object" ? (v.min + v.max) / 2 : v;
}

/**
 * Las cifras vigentes cambiaron respecto de la ultima version guardada. Solo
 * compara los VALORES declarados (no metadatos como updated_at/session_id).
 * Sin version previa, cuenta como cambio (primera corrida).
 */
export function cifrasCambiaron(actuales: NumerosProyecto, previas: NumerosProyecto | null | undefined): boolean {
  if (!previas) return true;
  const todas = new Set([...Object.keys(actuales), ...Object.keys(previas)]);
  for (const k of todas) {
    const va = actuales[k]?.valor ?? null;
    const vb = previas[k]?.valor ?? null;
    if (JSON.stringify(va) !== JSON.stringify(vb)) return true;
  }
  return false;
}

/**
 * El ciclo de conversión de efectivo (CCE) en palabras de persona: cuántos
 * días tarda tu dinero en volver desde que pagas los materiales. Positivo = la
 * plata queda amarrada; cero = vuelve el mismo día; negativo = cobras antes de
 * pagar y la caja trabaja a tu favor (nunca "malo": es un dato, no una falta).
 * null si aún faltan los datos.
 */
export function fraseCicloCaja(dias: number | null): string | null {
  if (dias === null || dias === undefined) return null;
  const d = Math.round(dias);
  if (d > 0) return `Tu dinero tarda unos ${d} días en volver a tu bolsillo desde que pagas los materiales.`;
  if (d === 0) return "Tu dinero vuelve el mismo día: cobras justo cuando pagas.";
  return `Cobras antes de pagar: tu caja trabaja a favor, con unos ${Math.abs(d)} días de holgura.`;
}

export interface Veredicto {
  tono: "perdida" | "ajuste" | "sano" | "datos";
  frase: string;
  /** El fragmento a resaltar con el color del tono; null si no hay. */
  acento: string | null;
}

/**
 * El veredicto de una frase con su color (canon 14), 100% determinista. La
 * voz respeta el BANCO: sin guiones largos, con acentos, espejo jamas regano
 * (una perdida es un dato, nunca una falta). Ambar = perdida (nunca rojo).
 */
export function veredictoNumeros(tablero: Tablero, unidad?: string | null): Veredicto {
  const u = unidad || "unidad";
  const margen = medio(tablero.margen);
  const margenPct = medio(tablero.margenPct);
  const equilibrio = medio(tablero.puntoEquilibrio);
  const fijos = medio(tablero.fijos);

  if (tablero.estado === "datos" || margen === null) {
    return {
      tono: "datos",
      frase: `Aun me faltan cifras para darte el panorama: cuando completes lo que falta, aqui veras con claridad si cada ${u} te deja ganancia.`,
      acento: null,
    };
  }

  if (tablero.estado === "perdida") {
    const acento = `${pesos(margen)} mas de lo que cobras`;
    return {
      tono: "perdida",
      frase: `Hoy, cada ${u} que vendes te cuesta ${acento}: no es problema de vender mas, es que el precio todavia no cubre lo que te cuesta hacerla.`,
      acento,
    };
  }

  if (tablero.estado === "ajuste") {
    const acento = `${pesos(margen)} por ${u}`;
    const pct = margenPct !== null ? ` (${margenPct}%)` : "";
    return {
      tono: "ajuste",
      frase: `Cada ${u} te deja ${acento}${pct}: ya es ganancia, pero un margen delgado, asi que conviene reforzarlo antes de crecer.`,
      acento,
    };
  }

  // sano
  const acento = `${pesos(margen)} limpios`;
  const cola =
    equilibrio !== null && fijos !== null
      ? `, y con vender ${equilibrio} al mes ya cubres tus ${pesos(fijos)} de gasto fijo: de ahi en adelante, cada ${u} es ganancia`
      : "";
  return {
    tono: "sano",
    frase: `Cada ${u} te deja ${acento}${cola}.`,
    acento,
  };
}
