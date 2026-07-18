/**
 * creditos.ts — ETAPA 2 (docs/CUENTAS_DISENO.md §6): la capa fina sobre las
 * RPC atómicas del ledger (migraciones 020-024, aplicadas). Toda mutación va
 * por la service-role key DESDE EL SERVIDOR (las RPC tienen REVOKE para
 * anon/authenticated); el cliente jamás las llama.
 *
 * Las leyes que esta capa materializa:
 * - Verificar al INICIO, descontar A LA ENTREGA (consumir_creditos atómico,
 *   idempotente por clave: reintentos no doble-cobran).
 * - Saldo insuficiente = rechazo limpio ANTES del esfuerzo (402, en palabras
 *   de persona), nunca a mitad.
 * - El usuario JAMÁS pierde créditos por un fallo del sistema
 *   (reembolsar_creditos + credit_refund_log).
 * - La cortesía (20) se otorga UNA vez por cuenta (beta_courtesy_log).
 * - Carrera rara (verificó al inicio, otra pestaña gastó antes de la
 *   entrega): entregar y registrar, nunca cobrar de más ni castigar.
 */
import { createAdminClient } from "./supabase/admin";
import { PRECIOS, type ConceptoPrecio } from "./precios";

export const CORTESIA_BETA = 20;

/** Saldo actual del usuario (0 si aún no tiene cuenta de créditos). */
export async function saldoDe(userId: string): Promise<number> {
  const admin = createAdminClient();
  const { data, error } = await admin
    .from("credit_accounts")
    .select("creditos_total")
    .eq("user_id", userId)
    .maybeSingle();
  if (error) throw error;
  return (data as { creditos_total: number } | null)?.creditos_total ?? 0;
}

export interface VerificacionSaldo {
  alcanza: boolean;
  creditos: number;
}

/** La verificación del inicio: ¿alcanza para esta unidad facturable? */
export async function verificarSaldo(userId: string, monto: number): Promise<VerificacionSaldo> {
  const creditos = await saldoDe(userId);
  return { alcanza: creditos >= monto, creditos };
}

/**
 * El descuento de la entrega. Devuelve el saldo resultante, o -1 si no
 * alcanzó (la carrera rara: el llamador ENTREGA igual y lo registra).
 * Idempotente por clave: la misma acción cobra una sola vez.
 */
export async function cobrar(
  userId: string,
  concepto: ConceptoPrecio,
  monto: number,
  idempotencyKey: string
): Promise<number> {
  const admin = createAdminClient();
  const { data, error } = await admin.rpc("consumir_creditos", {
    p_user_id: userId,
    p_concepto: concepto,
    p_monto: monto,
    p_idempotency_key: idempotencyKey,
  });
  if (error) throw error;
  return data as number;
}

/** El reembolso: compensa un cobro cuya entrega falló. Queda en credit_refund_log. */
export async function reembolsar(userId: string, monto: number, motivo: string): Promise<number> {
  const admin = createAdminClient();
  const { data, error } = await admin.rpc("reembolsar_creditos", {
    p_user_id: userId,
    p_monto: monto,
    p_motivo: motivo,
  });
  if (error) throw error;
  return data as number;
}

/** La cortesía de beta: 20 créditos, UNA vez por cuenta (beta_courtesy_log). */
export async function otorgarCortesia(userId: string): Promise<number> {
  const admin = createAdminClient();
  const { data, error } = await admin.rpc("otorgar_cortesia", {
    p_user_id: userId,
    p_monto: CORTESIA_BETA,
  });
  if (error) throw error;
  return data as number;
}

/**
 * La regla de concepto del plan (CUENTAS_DISENO §5, actualizada por la 4.5):
 *   core + inicial/completo  → plan_completo (5)
 *   core + seguimiento       → seguimiento (2)
 *   mundo + inicial/completo → mundo_activar (3)  ← el preview fue GRATIS;
 *                              lo que se compra es el PLAN, a la entrega.
 *   mundo + seguimiento      → mundo_seguimiento (2)
 */
export function conceptoDelPlan(dominio: string, esSeguimiento: boolean): ConceptoPrecio {
  if (dominio === "core") return esSeguimiento ? "seguimiento" : "plan_completo";
  return esSeguimiento ? "mundo_seguimiento" : "mundo_activar";
}

export function montoDelPlan(dominio: string, esSeguimiento: boolean): number {
  return PRECIOS[conceptoDelPlan(dominio, esSeguimiento)];
}

/** El 402 en palabras de persona (la compuerta del canon 07). */
export function mensajeSaldoInsuficiente(creditos: number, costo: number): string {
  const plural = creditos === 1 ? "crédito" : "créditos";
  return `Te quedan ${creditos} ${plural}; esto cuesta ${costo}. Tu trabajo queda guardado tal como está.`;
}
