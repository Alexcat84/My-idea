/**
 * cuentas.ts — ETAPA 2: la adopción de proyectos. El organizador es gratis y
 * sin login (el gancho); sus proyectos nacen bajo la identidad INVISIBLE.
 * Al hacer login, esos proyectos se ADOPTAN: user_id pasa al dueño recién
 * autenticado en TODAS las tablas que lo cargan (projects, sessions, plans;
 * checklist/nodos/unlocks/bitácora/versiones van por project_id y siguen
 * solos).
 *
 * SEGURIDAD (la regla: NADIE adopta el proyecto de otro):
 * - En el login (entrar/registrar/auth-callback): el id anónimo sale de la
 *   SESIÓN que el propio request traía en cookies ANTES de autenticar:
 *   prueba de posesión criptográfica. Jamás de un parámetro.
 * - En el script del fundador (scripts/adoptar_proyectos.ts): corre con la
 *   service-role key en la máquina del fundador, con ids explícitos.
 */
import { createHash } from "node:crypto";
import type { User } from "@supabase/supabase-js";
import { esInvitadoInvisible } from "./identidad";
import { createAdminClient } from "./supabase/admin";

/** Huella sha256 (hex) del email en minúsculas: la llave de
 * cortesia_email_log (migración 029, patrón trial_email_log del I Ching). */
export function huellaDeEmail(email: string): string {
  return createHash("sha256").update(email.trim().toLowerCase()).digest("hex");
}

/** ¿Este correo ya recibió cortesía en una cuenta que luego se borró?
 * (El log por user_id se va con la cascada del borrado; esta huella queda.) */
export async function cortesiaYaDadaAlCorreo(email: string): Promise<boolean> {
  const admin = createAdminClient();
  const { data, error } = await admin
    .from("cortesia_email_log")
    .select("email_hash")
    .eq("email_hash", huellaDeEmail(email))
    .maybeSingle();
  if (error) throw error;
  return data !== null;
}

/**
 * ¿Este correo está invitado a la beta? (beta_allowlist, migración 008, solo
 * legible con service role). Compartido por el envío del código (que filtra
 * ANTES de mandar el correo) y por el callback de Google (que solo puede
 * filtrar DESPUÉS de autenticar, porque el email se conoce al volver).
 * Lanza si la consulta falla: un error de infraestructura jamás debe leerse
 * como "no invitado".
 */
export async function estaEnAllowlist(email: string): Promise<boolean> {
  const admin = createAdminClient();
  const { data, error } = await admin
    .from("beta_allowlist")
    .select("email")
    .eq("email", email.trim().toLowerCase())
    .maybeSingle();
  if (error) throw error;
  return data !== null;
}

/**
 * El acto de la bienvenida tras un login exitoso: la ADOPCIÓN de la identidad
 * invisible. Si el navegador traía un organizador anónimo, sus proyectos pasan
 * al dueño recién autenticado. `anonId` SIEMPRE debe venir de la sesión que el
 * propio request traía en cookies ANTES de verificar (prueba de posesión),
 * jamás de un parámetro, o de la anotación que el servidor dejó al registrar.
 * No bloquea el login si falla: se reintenta, se dice fuerte, queda anotada
 * para el próximo ingreso y el llamador recibe cuántas quedaron pendientes.
 *
 * CORTESÍA RETIRADA (fase "Catálogo congruente", ANÁLISIS §4/§8.3). Ya NO se
 * otorgan créditos automáticos al primer login: la beta trabaja con precios
 * REALES y el fundador siembra créditos A MANO desde Supabase (RPC
 * otorgar_creditos, origen 'siembra_beta') — ver docs/BETA_CUENTAS_README.md.
 * La maquinaria de cortesía (otorgar_cortesia, CORTESIA_BETA, beta_courtesy_log
 * y cortesiaYaDadaAlCorreo) queda DORMIDA, no borrada, por si la cortesía
 * pública post-lanzamiento se decide con telemetría. La allowlist NO se toca:
 * sigue siendo la puerta de la beta.
 */
export async function bienvenidaTrasLogin(real: User, anonId: string | null): Promise<{ pendientes: number }> {
  if (esInvitadoInvisible(real)) return { pendientes: 0 };
  // AUD-09 H07: se adopta en TODO camino de sesión. Además de la identidad que
  // este navegador traía (la cookie), se adoptan las que quedaron anotadas al
  // registrarse (app_metadata, que solo escribe el servidor): así la cuenta
  // confirmada desde otro navegador, o entrada tras recuperar la contraseña,
  // recibe sus ideas igual.
  const anotadas = leerPendientes(real.app_metadata);
  const candidatos = [...new Set([...(anonId && anonId !== real.id ? [anonId] : []), ...anotadas])];
  if (candidatos.length === 0) return { pendientes: 0 };

  const fallidas: string[] = [];
  for (const deId of candidatos) {
    if (!(await adoptarConReintento(deId, real.id))) fallidas.push(deId);
  }
  // Lo que falló queda anotado: el próximo ingreso lo reintenta, venga de
  // donde venga. Lo adoptado se limpia de la lista.
  if (anotadas.length > 0 || fallidas.length > 0) {
    try {
      await guardarPendientes(real.id, fallidas);
    } catch (e) {
      console.error(`[login] no se pudo anotar la adopcion pendiente de ${real.id}:`, e);
    }
  }
  if (fallidas.length > 0) {
    console.error(`[login] ADOPCION PENDIENTE: ${fallidas.length} identidad(es) sin adoptar para ${real.id}`, fallidas);
  }
  return { pendientes: fallidas.length };
}

/** AUD-09 H07: al registrarse, el servidor conoce la identidad invisible del
 * navegador (la cookie: prueba de posesión) y la deja anotada en la cuenta
 * nueva, para adoptarla al confirmar desde cualquier navegador. */
export async function registrarAdopcionPendiente(realId: string, anonId: string): Promise<void> {
  const admin = createAdminClient();
  const { data, error } = await admin.auth.admin.getUserById(realId);
  if (error) throw error;
  const actuales = leerPendientes(data.user?.app_metadata);
  if (actuales.includes(anonId)) return;
  await guardarPendientes(realId, [...actuales, anonId]);
}

const CLAVE_PENDIENTE = "adopcion_pendiente";
const INTENTOS_ADOPCION = 3;

function leerPendientes(appMetadata: Record<string, unknown> | undefined | null): string[] {
  const v = appMetadata?.[CLAVE_PENDIENTE];
  return Array.isArray(v) ? v.filter((x): x is string => typeof x === "string") : [];
}

async function guardarPendientes(realId: string, ids: string[]): Promise<void> {
  const admin = createAdminClient();
  const { data, error: errLeer } = await admin.auth.admin.getUserById(realId);
  if (errLeer) throw errLeer;
  const { error } = await admin.auth.admin.updateUserById(realId, {
    app_metadata: { ...(data.user?.app_metadata ?? {}), [CLAVE_PENDIENTE]: ids },
  });
  if (error) throw error;
}

async function adoptarConReintento(deId: string, aId: string): Promise<boolean> {
  for (let intento = 1; intento <= INTENTOS_ADOPCION; intento += 1) {
    try {
      const adoptados = await adoptarProyectosDeUsuario(deId, aId);
      if (adoptados > 0) console.log(`[login] ${adoptados} proyecto(s) adoptado(s) de ${deId}`);
      return true;
    } catch (e) {
      console.error(`[login] fallo la adopcion de ${deId} (intento ${intento}/${INTENTOS_ADOPCION}):`, e);
    }
  }
  return false;
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
