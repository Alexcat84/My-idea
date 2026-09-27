/**
 * numerosVivo.ts - FASE B (canon 14): la logica PURA del tablero vivo que la
 * ruta usa pero que conviene probar aparte. El veredicto determinista (la
 * frase con su color, sin modelo: los numeros los hace codigo), la
 * comparacion de cifras para decidir si hay una version nueva, y el tope
 * diario de re-narraciones (freno, jamas cobro ni bloqueo del recalculo).
 */
import type { NumerosProyecto } from "./calculadora";
import type { Tablero } from "./tableroNumeros";
import { elegir, LOCALE_BASE, type Locale } from "./i18n/config";
import { dinero } from "./i18n/formato";
import { interpolar } from "./i18n/interpolar";
import { MOTOR_NUMEROS } from "./i18n/mensajes/motorNumeros";

/** Re-narraciones del modelo por idea por dia. Es un FRENO de costo, no un
 * cobro: el recalculo determinista es gratis e ilimitado siempre. Ajustable
 * con datos de la beta. */
export const TOPE_RENARRACION_DIA = 5;

/** En palabras de persona cuando se alcanza el tope (amarre del fundador):
 * espejo, sin regano, y deja claro que nada se pierde. El texto vive en el
 * catálogo; la constante es su valor base (quien la muestra elige por idioma). */
export function mensajeTopeRenarracion(idioma: Locale = LOCALE_BASE): string {
  return elegir(MOTOR_NUMEROS, idioma).vivo.topeRenarracion;
}
export const MENSAJE_TOPE_RENARRACION = mensajeTopeRenarracion(LOCALE_BASE);

/** Un entero de dinero al estilo del canon, SIN signo: "$1.200", "$170" (el
 * valor absoluto: la frase ya dice si es pérdida). dinero() de formato.ts. */
function pesos(n: number, idioma: Locale): string {
  return dinero(idioma, Math.abs(n));
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
export function fraseCicloCaja(dias: number | null, idioma: Locale = LOCALE_BASE): string | null {
  if (dias === null || dias === undefined) return null;
  const t = elegir(MOTOR_NUMEROS, idioma).vivo;
  const d = Math.round(dias);
  if (d > 0) return interpolar(t.cicloPositivo, { d });
  if (d === 0) return t.cicloCero;
  return interpolar(t.cicloNegativo, { d: Math.abs(d) });
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
export function veredictoNumeros(tablero: Tablero, unidad?: string | null, idioma: Locale = LOCALE_BASE): Veredicto {
  const t = elegir(MOTOR_NUMEROS, idioma).vivo;
  const u = unidad || t.unidadPorDefecto;
  const margen = medio(tablero.margen);
  const margenPct = medio(tablero.margenPct);
  const equilibrio = medio(tablero.puntoEquilibrio);
  const fijos = medio(tablero.fijos);

  if (tablero.estado === "datos" || margen === null) {
    return {
      tono: "datos",
      frase: interpolar(t.datos, { u }),
      acento: null,
    };
  }

  if (tablero.estado === "perdida") {
    const acento = interpolar(t.perdidaAcento, { monto: pesos(margen, idioma) });
    return {
      tono: "perdida",
      frase: interpolar(t.perdida, { u, acento }),
      acento,
    };
  }

  if (tablero.estado === "ajuste") {
    const acento = interpolar(t.ajusteAcento, { monto: pesos(margen, idioma), u });
    const pct = margenPct !== null ? interpolar(t.ajustePct, { pct: String(margenPct) }) : "";
    return {
      tono: "ajuste",
      frase: interpolar(t.ajuste, { u, acento, pct }),
      acento,
    };
  }

  // sano
  const acento = interpolar(t.sanoAcento, { monto: pesos(margen, idioma) });
  const cola =
    equilibrio !== null && fijos !== null
      ? interpolar(t.sanoCola, { equilibrio: String(equilibrio), fijos: pesos(fijos, idioma), u })
      : "";
  return {
    tono: "sano",
    frase: interpolar(t.sano, { u, acento, cola }),
    acento,
  };
}
