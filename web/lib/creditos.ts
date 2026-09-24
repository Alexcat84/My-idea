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
 * - La cortesía de beta está DORMIDA (Catálogo congruente, ANÁLISIS §4): el
 *   fundador siembra a mano; la maquinaria (una vez por cuenta,
 *   beta_courtesy_log) queda sin llamador.
 * - Carrera rara (verificó al inicio, otra pestaña gastó antes de la
 *   entrega): entregar y registrar, nunca cobrar de más ni castigar.
 * - AUD-09 M25 (decisión del fundador, 25 sep 2026): RESERVA al empezar la
 *   sesión, cobro al entregar, liberación si la IA falla (migración 042). La
 *   verificación del inicio ya no solo mira: APARTA el precio con la clave del
 *   cobro (`plan:{sessionId}`). El disponible es el saldo menos lo apartado; así
 *   dos sesiones en paralelo no pasan con saldo para una. La carrera rara queda
 *   para lo que la reserva no cubre (una reserva vencida).
 */
import { createAdminClient } from "./supabase/admin";
import type { ConceptoPrecio } from "./precios";

/**
 * CORTESIA_BETA — DORMIDA desde la fase "Catálogo congruente" (ANÁLISIS §4/§8.3).
 * El otorgamiento automático al primer login se retiró: la beta trabaja con
 * precios REALES y el fundador siembra créditos A MANO (RPC otorgar_creditos,
 * origen 'siembra_beta'; ver docs/BETA_CUENTAS_README.md). Esta constante y
 * `otorgarCortesia` quedan aquí, sin llamador, por si la cortesía PÚBLICA
 * post-lanzamiento se decide con telemetría (candidata preliminar: organizador
 * gratis + un plan de bienvenida). No borrar: es el ancla dormida.
 *
 * La allowlist NO se toca: sigue siendo la puerta de la beta (sin fila en
 * beta_allowlist, registrar/entrar rechazan antes de crear la cuenta).
 */
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

/** AUD-09 M25: cuánto vive una reserva. Cubre una exploración normal de punta
 * a punta; si la sesión se abandona, lo apartado se suelta solo. La entrega
 * renueva la reserva de su clave antes de gastar un token. */
export const MINUTOS_RESERVA = 120;

/** La base aún no tiene la migración 042 (tabla o función ausente). */
function faltaLaReserva(error: { code?: string; message?: string } | null): boolean {
  if (!error) return false;
  if (["PGRST202", "PGRST205", "42P01", "42883"].includes(error.code ?? "")) return true;
  return /credit_reservas|reservar_creditos|resolver_reserva/.test(error.message ?? "");
}

/** Lo apartado por reservas activas y no vencidas (sin contar `excluirClave`,
 * la propia sesión que renueva la suya). */
export async function apartadoDe(userId: string, excluirClave?: string): Promise<number> {
  const admin = createAdminClient();
  let q = admin
    .from("credit_reservas")
    .select("monto")
    .eq("user_id", userId)
    .eq("estado", "activa")
    .gt("expira_at", new Date().toISOString());
  if (excluirClave) q = q.neq("clave", excluirClave);
  const { data, error } = await q;
  if (error) {
    if (faltaLaReserva(error)) {
      console.error("[creditos] falta la migracion 042 (credit_reservas); el disponible es el saldo entero:", error.message);
      return 0;
    }
    throw error;
  }
  return ((data ?? []) as Array<{ monto: number }>).reduce((t, r) => t + r.monto, 0);
}

export interface VerificacionSaldo {
  alcanza: boolean;
  creditos: number;
  /** AUD-09 M25: lo apartado por otras sesiones en curso. */
  apartados?: number;
}

/** La verificación del inicio: ¿alcanza el DISPONIBLE (saldo menos lo apartado
 * por otras sesiones) para esta unidad facturable? */
export async function verificarSaldo(userId: string, monto: number, excluirClave?: string): Promise<VerificacionSaldo> {
  const creditos = await saldoDe(userId);
  const apartados = await apartadoDe(userId, excluirClave);
  return { alcanza: creditos - apartados >= monto, creditos, apartados };
}

/**
 * AUD-09 M25: aparta `monto` con la clave de su cobro, atómico en la base
 * (reservar_creditos bloquea la cuenta). Idempotente por clave: la entrega
 * renueva la reserva de su propia sesión. Sin la migración 042 degrada a la
 * verificación de antes, con el síntoma en el log.
 */
export async function reservarCreditos(
  userId: string,
  clave: string,
  concepto: ConceptoPrecio,
  monto: number
): Promise<{ reservado: boolean; disponible: number }> {
  const admin = createAdminClient();
  const { data, error } = await admin.rpc("reservar_creditos", {
    p_user_id: userId,
    p_clave: clave,
    p_concepto: concepto,
    p_monto: monto,
    p_minutos: MINUTOS_RESERVA,
  });
  if (error) {
    if (faltaLaReserva(error)) {
      console.error("[creditos] falta la migracion 042 (reservar_creditos); se sigue sin apartar:", error.message);
      return { reservado: true, disponible: monto };
    }
    throw error;
  }
  const disponible = data as number;
  return { reservado: disponible >= 0, disponible: Math.max(0, disponible) };
}

/** AUD-09 M25: la reserva de una entrega pasa a 'cobrada' o 'liberada'. Nunca
 * rompe la entrega: si falla, queda en el log y el vencimiento la suelta. */
export async function resolverReserva(clave: string, estado: "cobrada" | "liberada"): Promise<void> {
  try {
    const admin = createAdminClient();
    const { error } = await admin.rpc("resolver_reserva", { p_clave: clave, p_estado: estado });
    if (error) console.error(`[creditos] no se pudo marcar la reserva ${clave} como ${estado}:`, error.message);
  } catch (e) {
    console.error(`[creditos] no se pudo marcar la reserva ${clave} como ${estado}:`, e);
  }
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

/** La cortesía de beta, DORMIDA y sin llamador (CORTESIA_BETA, UNA vez por
 * cuenta, beta_courtesy_log). */
export async function otorgarCortesia(userId: string): Promise<number> {
  const admin = createAdminClient();
  const { data, error } = await admin.rpc("otorgar_cortesia", {
    p_user_id: userId,
    p_monto: CORTESIA_BETA,
  });
  if (error) throw error;
  return data as number;
}

// La regla de concepto del plan vive en precios.ts (fuente única: la usan el
// cobro del servidor Y el precio que pinta la pantalla, AUD-09 H01). Se
// re-exporta aquí para no mover a quien ya la importaba desde creditos.
export { conceptoDelPlan, montoDelPlan } from "./precios";

/** El 402 en palabras de persona (la compuerta del canon 07). Si parte del
 * saldo está apartada por un plan en curso (AUD-09 M25), lo dice. */
export function mensajeSaldoInsuficiente(creditos: number, costo: number, apartados = 0): string {
  const plural = creditos === 1 ? "crédito" : "créditos";
  if (apartados > 0) {
    const verbo = apartados === 1 ? "ya está apartado" : "ya están apartados";
    return `Tienes ${creditos} ${plural} y ${apartados} ${verbo} para un plan que tienes en curso; esto cuesta ${costo}. Tu trabajo queda guardado tal como está.`;
  }
  return `Te quedan ${creditos} ${plural}; esto cuesta ${costo}. Tu trabajo queda guardado tal como está.`;
}
