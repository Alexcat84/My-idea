/**
 * historialCreditos.ts — el historial de movimientos de créditos que ve la
 * persona en /creditos (decisión del fundador, 8 oct 2026: un acceso directo
 * para comprar y administrar los créditos: saldo, compras e historial).
 *
 * Lee el libro (credit_transactions) con el cliente de la persona: la RLS
 * own-select deja ver solo los suyos. Si la lectura falla devuelve null y deja
 * rastro (AUD-09 M21: un historial vacío falso es una mentira sobre dinero; la
 * pantalla dice que no pudo leerlo).
 */
import type { SupabaseClient } from "@supabase/supabase-js";
import type { CREDITOS } from "./i18n/mensajes/creditos";

export interface Movimiento {
  id: number;
  delta: number;
  saldo_resultante: number | null;
  tipo: "grant" | "consumo" | "refund";
  concepto: string | null;
  origen: string | null;
  created_at: string;
}

type TextosHistorial = (typeof CREDITOS)["es"]["historial"];

/** Los últimos movimientos, del más reciente al más antiguo; null si la lectura falla. */
export async function leerHistorial(supabase: SupabaseClient, limite = 30): Promise<Movimiento[] | null> {
  const { data, error } = await supabase
    .from("credit_transactions")
    .select("id, delta, saldo_resultante, tipo, concepto, origen, created_at")
    .order("created_at", { ascending: false })
    .limit(limite);
  if (error) {
    console.error("[historialCreditos] no se pudo leer credit_transactions:", error);
    return null;
  }
  return (data ?? []) as Movimiento[];
}

/** Cómo se nombra un movimiento: una compra, un regalo, lo que se pagó o una devolución. */
export function etiquetaMovimiento(m: Movimiento, t: TextosHistorial): string {
  if (m.tipo === "grant") return m.origen === "revenuecat" ? t.compra : t.otorgados;
  if (m.tipo === "refund") return t.devolucion;
  const conceptos = t.conceptos as Record<string, string>;
  return (m.concepto && conceptos[m.concepto]) || t.consumo;
}
