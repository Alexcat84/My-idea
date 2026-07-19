/**
 * cuentas.ts — ETAPA 2: la adopción de proyectos. El organizador es gratis y
 * sin login (el gancho); sus proyectos nacen bajo la identidad INVISIBLE.
 * Al hacer login, esos proyectos se ADOPTAN: user_id pasa al dueño recién
 * autenticado en TODAS las tablas que lo cargan (projects, sessions, plans;
 * checklist/nodos/unlocks/bitácora/versiones van por project_id y siguen
 * solos).
 *
 * SEGURIDAD (la regla: NADIE adopta el proyecto de otro):
 * - En el login (auth/confirm): el id anónimo sale de la SESIÓN que el
 *   propio request traía en cookies antes de verificar el OTP: prueba de
 *   posesión criptográfica. Jamás de un parámetro.
 * - En el script del fundador (scripts/adoptar_proyectos.ts): corre con la
 *   service-role key en la máquina del fundador, con ids explícitos.
 */
import type { User } from "@supabase/supabase-js";
import { otorgarCortesia } from "./creditos";
import { esInvitadoInvisible } from "./identidad";
import { createAdminClient } from "./supabase/admin";

/**
 * Los dos actos de la bienvenida tras un login exitoso (compartidos por el
 * código de verificación y el enlace legacy):
 * 1. CORTESÍA: 20 créditos al primer login (otorgar_cortesia es una-sola-vez
 *    por cuenta vía beta_courtesy_log; repetirla no re-otorga).
 * 2. ADOPCIÓN: si el navegador traía una identidad invisible (el organizador
 *    anónimo), sus proyectos pasan al dueño recién autenticado. `anonId`
 *    SIEMPRE debe venir de la sesión que el propio request traía en cookies
 *    ANTES de verificar (prueba de posesión), jamás de un parámetro.
 * Ninguno de los dos bloquea el login si falla; ambos se dicen fuerte.
 */
export async function bienvenidaTrasLogin(real: User, anonId: string | null): Promise<void> {
  if (esInvitadoInvisible(real)) return;
  try {
    await otorgarCortesia(real.id);
  } catch (e) {
    console.error("[login] fallo otorgar_cortesia (un invitado sin su cortesia es un bug de dinero):", e);
  }
  if (anonId && anonId !== real.id) {
    try {
      const adoptados = await adoptarProyectosDeUsuario(anonId, real.id);
      if (adoptados > 0) console.log(`[login] ${adoptados} proyecto(s) adoptado(s) de ${anonId}`);
    } catch (e) {
      console.error("[login] fallo la adopcion:", e);
    }
  }
}

/**
 * Mueve TODOS los proyectos de un usuario (la identidad invisible del
 * navegador) al usuario real recién autenticado. Devuelve cuántos proyectos
 * se adoptaron.
 */
export async function adoptarProyectosDeUsuario(deUserId: string, aUserId: string): Promise<number> {
  const admin = createAdminClient();
  const { data: proyectos, error } = await admin.from("projects").select("id").eq("user_id", deUserId);
  if (error) throw error;
  const ids = ((proyectos ?? []) as Array<{ id: string }>).map((p) => p.id);
  if (ids.length === 0) return 0;
  await adoptarProyectosPorIds(deUserId, aUserId, ids);
  return ids.length;
}

/**
 * Mueve proyectos CONCRETOS (por id) de un dueño a otro, en las TRES tablas
 * con user_id propio (001): projects (por id), sessions (por project_id) y
 * plans (por session_id: plans NO tiene project_id — lo cazó el vuelo de
 * dinero). Exige que cada fila pertenezca hoy a `deUserId` (el .eq de cada
 * UPDATE lo garantiza: un id ajeno simplemente no matchea y no se mueve).
 */
export async function adoptarProyectosPorIds(deUserId: string, aUserId: string, projectIds: string[]): Promise<void> {
  const admin = createAdminClient();
  // Las sesiones de esos proyectos, ANTES de mover nada (alimentan el filtro
  // de plans).
  const { data: sesiones, error: errSes } = await admin.from("sessions").select("id").in("project_id", projectIds);
  if (errSes) throw errSes;
  const sessionIds = ((sesiones ?? []) as Array<{ id: string }>).map((s) => s.id);

  const { error: e1 } = await admin.from("projects").update({ user_id: aUserId }).eq("user_id", deUserId).in("id", projectIds);
  if (e1) throw e1;
  const { error: e2 } = await admin.from("sessions").update({ user_id: aUserId }).eq("user_id", deUserId).in("project_id", projectIds);
  if (e2) throw e2;
  if (sessionIds.length > 0) {
    const { error: e3 } = await admin.from("plans").update({ user_id: aUserId }).eq("user_id", deUserId).in("session_id", sessionIds);
    if (e3) throw e3;
  }
}
