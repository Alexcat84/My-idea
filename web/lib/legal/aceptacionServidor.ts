/**
 * El registro de la aceptación de los Términos y la Privacidad, lado servidor (corrección del fundador, 7 oct 2026).
 * Una sola puerta para leer, guardar, exigir y trasladar la aceptación en aceptaciones_legales (migración 050, ya
 * aplicada: user_id cuelga de auth.users, así que admite la identidad invisible igual que una cuenta). Escribe con
 * service_role: la tabla solo deja leer a su dueño (RLS) y nadie escribe desde el cliente. Sin SQL nuevo.
 *
 * - exigirAceptacionVigente: la guarda de las rutas que envían la idea (el organizador gratuito y el arranque de La
 *   Exploración). Sin la versión vigente aceptada, 428 con `consentimiento_requerido` y nada se envía. Si el registro
 *   no se puede leer, 503: jamás se da por aceptado lo que no se pudo comprobar (fallar ruidoso, BANCO §9).
 * - guardarAceptacion: lo que llama la ruta /api/cuenta/consentimiento y la entrada con cuenta. Lanza si falla.
 * - trasladarAceptaciones: la adopción (lib/cuentas.ts) copia a la cuenta lo que aceptó la identidad invisible, con su
 *   versión, huella, idioma y fecha. La tabla es de solo añadir: se copia, no se mueve.
 */
import { NextResponse } from "next/server";
import { elegir, type Locale } from "@/lib/i18n/config";
import { CONSENTIMIENTO } from "@/lib/i18n/mensajes/consentimiento";
import { createAdminClient } from "@/lib/supabase/admin";
import {
  esIdiomaTextoLegal,
  estadoConsentimiento,
  HUELLA_LEGAL,
  STATUS_SIN_ACEPTACION,
  VERSION_LEGAL,
  type IdiomaTextoLegal,
  type MotivoAceptacion,
} from "./consentimiento";

export const TABLA_ACEPTACIONES = "aceptaciones_legales";

interface FilaAceptacion {
  version: string;
  huella_textos?: string;
  idioma_texto?: string;
  aceptada_at: string;
}

/** Todas las aceptaciones de una identidad, de la más vieja a la más nueva. Lanza si la base falla. */
async function aceptacionesDe(userId: string): Promise<FilaAceptacion[]> {
  const { data, error } = await createAdminClient()
    .from(TABLA_ACEPTACIONES)
    .select("version, huella_textos, idioma_texto, aceptada_at")
    .eq("user_id", userId);
  if (error) throw new Error(error.message);
  return ((data ?? []) as FilaAceptacion[]).slice().sort((a, b) => String(a.aceptada_at).localeCompare(String(b.aceptada_at)));
}

/** La última versión aceptada por esa identidad (null si nunca aceptó). Lanza si la base falla: jamás se adivina. */
export async function ultimaVersionAceptada(userId: string): Promise<string | null> {
  const filas = await aceptacionesDe(userId);
  if (filas.some((f) => f.version === VERSION_LEGAL)) return VERSION_LEGAL;
  return filas.at(-1)?.version ?? null;
}

/** Guarda la aceptación de la versión vigente (nada si ya estaba). Lanza si no se pudo guardar. */
export async function guardarAceptacion(userId: string, idiomaTexto: IdiomaTextoLegal): Promise<void> {
  const ultima = await ultimaVersionAceptada(userId);
  if (ultima === VERSION_LEGAL) return;
  const { error } = await createAdminClient()
    .from(TABLA_ACEPTACIONES)
    .insert({
      user_id: userId,
      version: VERSION_LEGAL,
      huella_textos: HUELLA_LEGAL,
      idioma_texto: idiomaTexto,
      motivo: estadoConsentimiento(ultima).motivo as MotivoAceptacion,
    });
  // 23505: la misma versión ya estaba guardada (doble envío). Es un hecho, no un error.
  if (error && error.code !== "23505") throw new Error(error.message);
}

/** El idioma del texto aceptado si el cuerpo trae la aceptación de la versión VIGENTE (`acepta_legal`); si no, null.
 * Una versión vieja (una pantalla abierta desde antes del cambio) no cuenta: se pedirá en el siguiente envío. */
export function aceptacionDelCuerpo(x: unknown): IdiomaTextoLegal | null {
  const a = x as { version?: unknown; idioma_texto?: unknown } | null | undefined;
  if (!a || a.version !== VERSION_LEGAL || !esIdiomaTextoLegal(a.idioma_texto)) return null;
  return a.idioma_texto;
}

/**
 * La guarda del envío de datos: null si la identidad tiene aceptada la versión vigente; si no, la respuesta que la
 * ruta devuelve tal cual (428 con `consentimiento_requerido`, o 503 si el registro no se pudo leer). Va ANTES de
 * crear la idea, de contar el límite diario y de tocar la IA.
 */
export async function exigirAceptacionVigente(userId: string, idioma: Locale): Promise<NextResponse | null> {
  const t = elegir(CONSENTIMIENTO, idioma).servidor;
  let ultima: string | null;
  try {
    ultima = await ultimaVersionAceptada(userId);
  } catch (e) {
    console.error("[consentimiento] no se pudo leer la aceptacion; no se envia nada:", e);
    return NextResponse.json({ error: t.noLeido }, { status: 503 });
  }
  const { requiere, motivo } = estadoConsentimiento(ultima);
  if (!requiere) return null;
  return NextResponse.json(
    {
      consentimiento_requerido: true,
      motivo,
      version: VERSION_LEGAL,
      error: motivo === "nueva_version" ? t.requeridaNueva : t.requerida,
    },
    { status: STATUS_SIN_ACEPTACION }
  );
}

/**
 * La adopción: copia a la cuenta las aceptaciones de la identidad invisible que la cuenta no tenía, con la misma
 * versión, huella, idioma y fecha (la prueba de qué texto se aceptó y cuándo). El motivo se recalcula contra la
 * historia de la cuenta. Devuelve cuántas copió. Lanza si la base falla (la adopción queda pendiente y se reintenta).
 */
export async function trasladarAceptaciones(deUserId: string, aUserId: string): Promise<number> {
  const delInvitado = await aceptacionesDe(deUserId);
  if (delInvitado.length === 0) return 0;
  const deLaCuenta = await aceptacionesDe(aUserId);
  const versiones = new Set(deLaCuenta.map((f) => f.version));
  let copiadas = 0;
  for (const f of delInvitado) {
    if (versiones.has(f.version)) continue;
    const { error } = await createAdminClient()
      .from(TABLA_ACEPTACIONES)
      .insert({
        user_id: aUserId,
        version: f.version,
        huella_textos: f.huella_textos,
        idioma_texto: f.idioma_texto,
        motivo: versiones.size === 0 ? "primera_aceptacion" : "nueva_version",
        aceptada_at: f.aceptada_at,
      });
    if (error && error.code !== "23505") throw new Error(error.message);
    versiones.add(f.version);
    if (!error) copiadas += 1;
  }
  return copiadas;
}
