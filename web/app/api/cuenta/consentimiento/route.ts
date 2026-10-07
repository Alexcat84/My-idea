/**
 * /api/cuenta/consentimiento — el consentimiento legal versionado (decisión del fundador, 7 oct 2026; corregida el
 * mismo día: sin modal, se pide en el primer envío de datos y también sin cuenta).
 *
 *   GET  → { identidad, requiere, motivo?, version }: si quien va a enviar sus datos (la identidad invisible de
 *          proxy.ts o una cuenta) tiene que aceptar la versión vigente de los Términos y la Privacidad. La pantalla lo
 *          usa para pintar la línea y el botón "Aceptar y generar"; no decide nada: la guarda está en el servidor.
 *   POST { version, idioma_texto } → guarda la aceptación en aceptaciones_legales (migración 050) para esa identidad,
 *          con la huella de los textos y el motivo que decide el servidor. La invitada también: la adopción la pasa
 *          a la cuenta al crearla (lib/cuentas.ts).
 *
 * Fallar ruidoso, no mentir calladito (BANCO §9, regla P20): si no se puede leer el estado, 503 con su error (nunca
 * un "al día" inventado); si no se puede guardar, 500 y nunca un ok, así la pantalla no envía nada. La versión la
 * decide el servidor: si el navegador acepta una que ya no es la vigente, 409. La ruta conserva su camino de antes
 * (bajo /cuenta) para no romper ninguna pantalla abierta.
 */
import { NextResponse } from "next/server";
import { elegir } from "@/lib/i18n/config";
import { CONSENTIMIENTO } from "@/lib/i18n/mensajes/consentimiento";
import { idiomaDeRequest } from "@/lib/i18n/servidor";
import { esIdiomaTextoLegal, estadoConsentimiento, VERSION_LEGAL } from "@/lib/legal/consentimiento";
import { guardarAceptacion, ultimaVersionAceptada } from "@/lib/legal/aceptacionServidor";
import { createClient } from "@/lib/supabase/server";

/** La identidad que manda la petición, sea la invisible o una cuenta (null si el proxy no pudo acuñar ninguna). */
async function identidad() {
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  return user ?? null;
}

export async function GET(request: Request) {
  const t = elegir(CONSENTIMIENTO, idiomaDeRequest(request)).servidor;
  const user = await identidad();
  // Sin identidad no hay dónde guardar: se pide (el envío también lo rechazará), jamás se da por aceptado.
  if (!user) return NextResponse.json({ identidad: false, requiere: true, motivo: "primera_aceptacion", version: VERSION_LEGAL });
  let ultima: string | null;
  try {
    ultima = await ultimaVersionAceptada(user.id);
  } catch (e) {
    console.error("[cuenta/consentimiento] no se pudo leer la aceptacion; no se finge al dia:", e);
    return NextResponse.json({ identidad: true, error: t.noLeido, version: VERSION_LEGAL }, { status: 503 });
  }
  const { requiere, motivo } = estadoConsentimiento(ultima);
  return NextResponse.json(
    requiere
      ? { identidad: true, requiere, motivo, version: VERSION_LEGAL }
      : { identidad: true, requiere, version: VERSION_LEGAL }
  );
}

export async function POST(request: Request) {
  const t = elegir(CONSENTIMIENTO, idiomaDeRequest(request)).servidor;
  const user = await identidad();
  if (!user) return NextResponse.json({ error: t.sinIdentidad }, { status: 401 });

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

  try {
    await guardarAceptacion(user.id, body.idioma_texto);
  } catch (e) {
    console.error("[cuenta/consentimiento] fallo el guardado de la aceptacion:", e);
    return NextResponse.json({ error: t.noGuardado }, { status: 500 });
  }
  return NextResponse.json({ ok: true, version: VERSION_LEGAL });
}
