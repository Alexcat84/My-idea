/**
 * /api/cuenta/consentimiento — el consentimiento legal versionado (decisión del fundador, 7 oct 2026; la idea viene
 * de The Original I Ching: api/auth/legal-consent y el legal_acceptance_current de api/account/me).
 *
 *   GET  → { cuenta, requiere, motivo?, version? }: si esta cuenta real tiene que aceptar la versión vigente de los
 *          Términos y la Privacidad. Sin cuenta real (identidad invisible o sin sesión): { cuenta: false,
 *          requiere: false }, sin tocar la base. La web es abierta: al invitado no se le pide nada, jamás.
 *   POST { version, idioma_texto } → guarda la aceptación en aceptaciones_legales (migración 050), con la huella de
 *          los textos y el motivo que decide el servidor (primera aceptación o versión nueva).
 *
 * Fallar ruidoso, no mentir calladito (BANCO §9, regla P20): si no se puede leer el estado, 503 con su error (nunca
 * un "al día" inventado); si no se puede guardar, 500 y nunca un ok, así la pantalla no da por aceptado lo que no se
 * guardó. La versión la decide el servidor: si el navegador acepta una que ya no es la vigente, 409.
 * Escribe con service_role: la tabla solo deja leer a su dueño (RLS) y nadie escribe desde el cliente.
 */
import { NextResponse } from "next/server";
import { elegir } from "@/lib/i18n/config";
import { CONSENTIMIENTO } from "@/lib/i18n/mensajes/consentimiento";
import { idiomaDeRequest } from "@/lib/i18n/servidor";
import { esIdiomaTextoLegal, estadoConsentimiento, HUELLA_LEGAL, VERSION_LEGAL } from "@/lib/legal/consentimiento";
import { sesionRealDeCookies } from "@/lib/seguridad";
import { createAdminClient } from "@/lib/supabase/admin";

const TABLA = "aceptaciones_legales";

/** La última versión aceptada por la cuenta (null si nunca aceptó). Lanza si la base falla: jamás se adivina. */
async function ultimaVersionAceptada(userId: string): Promise<string | null> {
  const { data, error } = await createAdminClient()
    .from(TABLA)
    .select("version")
    .eq("user_id", userId)
    .order("aceptada_at", { ascending: false })
    .limit(1)
    .maybeSingle();
  if (error) throw new Error(error.message);
  return (data as { version?: string } | null)?.version ?? null;
}

export async function GET(request: Request) {
  const t = elegir(CONSENTIMIENTO, idiomaDeRequest(request)).servidor;
  const sesion = await sesionRealDeCookies();
  if (!sesion) return NextResponse.json({ cuenta: false, requiere: false });
  let ultima: string | null;
  try {
    ultima = await ultimaVersionAceptada(sesion.user.id);
  } catch (e) {
    console.error("[cuenta/consentimiento] no se pudo leer la aceptacion; no se finge al dia:", e);
    return NextResponse.json({ cuenta: true, error: t.noLeido, version: VERSION_LEGAL }, { status: 503 });
  }
  const { requiere, motivo } = estadoConsentimiento(true, ultima);
  return NextResponse.json(
    requiere ? { cuenta: true, requiere, motivo, version: VERSION_LEGAL } : { cuenta: true, requiere, version: VERSION_LEGAL }
  );
}

export async function POST(request: Request) {
  const t = elegir(CONSENTIMIENTO, idiomaDeRequest(request)).servidor;
  const sesion = await sesionRealDeCookies();
  if (!sesion) return NextResponse.json({ error: t.necesitasCuenta }, { status: 401 });

  let body: { version?: unknown; idioma_texto?: unknown };
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: t.cuerpoInvalido }, { status: 400 });
  }
  if (!body || typeof body.version !== "string" || !esIdiomaTextoLegal(body.idioma_texto)) {
    return NextResponse.json({ error: t.cuerpoInvalido }, { status: 400 });
  }
  if (body.version !== VERSION_LEGAL) {
    return NextResponse.json({ error: t.versionVieja, version: VERSION_LEGAL }, { status: 409 });
  }

  const userId = sesion.user.id;
  let ultima: string | null;
  try {
    ultima = await ultimaVersionAceptada(userId);
  } catch (e) {
    console.error("[cuenta/consentimiento] no se pudo leer la aceptacion previa; no se guarda:", e);
    return NextResponse.json({ error: t.noGuardado }, { status: 500 });
  }
  if (ultima === VERSION_LEGAL) return NextResponse.json({ ok: true, version: VERSION_LEGAL });

  const { error } = await createAdminClient().from(TABLA).insert({
    user_id: userId,
    version: VERSION_LEGAL,
    huella_textos: HUELLA_LEGAL,
    idioma_texto: body.idioma_texto,
    motivo: estadoConsentimiento(true, ultima).motivo,
  });
  // 23505: la misma versión ya estaba guardada (doble envío). Es un hecho, no un error.
  if (error && error.code !== "23505") {
    console.error("[cuenta/consentimiento] fallo el guardado de la aceptacion:", error.message);
    return NextResponse.json({ error: t.noGuardado }, { status: 500 });
  }
  return NextResponse.json({ ok: true, version: VERSION_LEGAL });
}
