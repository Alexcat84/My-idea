/**
 * /api/opiniones — las opiniones de los usuarios (decisión del fundador, 8 oct 2026, antes de la beta).
 *
 *   GET  ?sesion=<id>        → { preguntar, tipo? }: si la tarjeta "¿Qué tal salió tu plan?" se muestra para el plan de
 *                              esa entrevista. ?seguimiento=<idea> hace lo mismo para "¿Qué tal va tu idea?".
 *   POST { sesion | seguimiento | general:true, valoracion?, motivo?, texto? } → guarda la opinión. Todo vacío es
 *                              "cerrar sin responder" (se guarda para no volver a preguntar). Los Comentarios y
 *                              sugerencias (general) piden texto y tienen tope diario.
 *   PATCH { id, motivo?, texto? } → después de "Malo", completa esa opinión con el motivo y el texto.
 *
 * Solo cuentas reales: la identidad invisible no ve tarjeta y no guarda. El tipo, la idea y el contexto interno
 * (etiqueta, ciclo, mundo, nodos) los decide el servidor a partir del plan de ESA cuenta (lib/opinionesServidor.ts);
 * el navegador no puede imponerlos ni los recibe. Fallar ruidoso (BANCO §9): si no se puede guardar, error, nunca ok.
 * Prueba: route.test.ts.
 */
import { NextResponse } from "next/server";
import { elegir } from "@/lib/i18n/config";
import { OPINIONES } from "@/lib/i18n/mensajes/opiniones";
import { idiomaDeRequest } from "@/lib/i18n/servidor";
import { avisoLogin, esInvitadoInvisible } from "@/lib/identidad";
import { decidirPregunta, TOPE_ESCRITURAS_DIA, TOPE_GENERALES_DIA, validarOpinion } from "@/lib/opiniones";
import { completarOpinion, eventoDePlan, eventoDeSeguimiento, guardarOpinion, historialDe, type EventoResuelto } from "@/lib/opinionesServidor";
import { limitarPorClave } from "@/lib/rateLimit";
import { createClient } from "@/lib/supabase/server";

const DIA_S = 86_400;

/** Tope general de escrituras por cuenta, con contador atómico (revisión de seguridad, 8 oct 2026). */
async function dentroDelTope(userId: string): Promise<boolean> {
  return (await limitarPorClave(`opiniones:${userId}`, DIA_S, TOPE_ESCRITURAS_DIA)).permitido;
}

const UUID = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;

async function cuentaReal() {
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  return user && !esInvitadoInvisible(user) ? user : null;
}

async function resolver(userId: string, sesion: unknown, seguimiento: unknown): Promise<EventoResuelto | null | "invalido"> {
  if (typeof sesion === "string") return UUID.test(sesion) ? eventoDePlan(userId, sesion) : "invalido";
  if (typeof seguimiento === "string") return UUID.test(seguimiento) ? eventoDeSeguimiento(userId, seguimiento) : "invalido";
  return "invalido";
}

export async function GET(request: Request) {
  const t = elegir(OPINIONES, idiomaDeRequest(request)).servidor;
  const user = await cuentaReal();
  if (!user) return NextResponse.json({ preguntar: false });
  const url = new URL(request.url);
  try {
    const r = await resolver(user.id, url.searchParams.get("sesion") ?? undefined, url.searchParams.get("seguimiento") ?? undefined);
    if (r === "invalido") return NextResponse.json({ preguntar: false, error: t.cuerpoInvalido }, { status: 400 });
    if (!r) return NextResponse.json({ preguntar: false });
    const decision = decidirPregunta(r.evento, await historialDe(user.id), new Date());
    return NextResponse.json(decision.preguntar ? { preguntar: true, tipo: r.evento.tipo } : { preguntar: false });
  } catch (e) {
    console.error("[opiniones] no se pudo decidir la tarjeta:", e);
    return NextResponse.json({ preguntar: false, error: t.noLeido }, { status: 503 });
  }
}

export async function POST(request: Request) {
  const idioma = idiomaDeRequest(request);
  const t = elegir(OPINIONES, idioma).servidor;
  const user = await cuentaReal();
  if (!user) return NextResponse.json({ ...avisoLogin(idioma), error: t.noAutenticado }, { status: 401 });

  let body: Record<string, unknown>;
  try {
    body = (await request.json()) as Record<string, unknown>;
  } catch {
    return NextResponse.json({ error: t.cuerpoInvalido }, { status: 400 });
  }
  const v = validarOpinion(body);
  if (!v.ok) return NextResponse.json({ error: t.cuerpoInvalido }, { status: 400 });

  try {
    if (!(await dentroDelTope(user.id))) return NextResponse.json({ error: t.tope }, { status: 429 });
    if (body.general === true) {
      if (!v.texto) return NextResponse.json({ error: t.cuerpoInvalido }, { status: 400 });
      // Contador atómico: contar en la base y luego insertar dejaba pasar peticiones simultáneas.
      if (!(await limitarPorClave(`opiniones-general:${user.id}`, DIA_S, TOPE_GENERALES_DIA)).permitido) {
        return NextResponse.json({ error: t.tope }, { status: 429 });
      }
      const g = await guardarOpinion({ userId: user.id, tipo: "general", objetoId: null, proyectoId: null, ...v, idioma, contexto: {} });
      return NextResponse.json(g === "repetida" ? { ok: true, repetida: true } : { ok: true, id: g.id });
    }
    const r = await resolver(user.id, body.sesion, body.seguimiento);
    if (r === "invalido") return NextResponse.json({ error: t.cuerpoInvalido }, { status: 400 });
    if (!r) return NextResponse.json({ error: t.noEncontrado }, { status: 404 });
    // Solo se guarda si la tarjeta tocaba: así el seguimiento no acumula filas sin fin y un plan no se valora dos veces.
    const decision = decidirPregunta(r.evento, await historialDe(user.id), new Date());
    if (!decision.preguntar) {
      if (decision.razon === "ya_respondida") return NextResponse.json({ ok: true, repetida: true });
      return NextResponse.json({ error: t.noGuardado }, { status: 409 });
    }
    const g = await guardarOpinion({
      userId: user.id,
      tipo: r.evento.tipo,
      objetoId: r.evento.objetoId,
      proyectoId: r.proyectoId,
      valoracion: v.valoracion,
      motivo: v.motivo,
      texto: v.texto,
      idioma,
      contexto: r.contexto,
    });
    return NextResponse.json(g === "repetida" ? { ok: true, repetida: true } : { ok: true, id: g.id });
  } catch (e) {
    console.error("[opiniones] fallo el guardado:", e);
    return NextResponse.json({ error: t.noGuardado }, { status: 500 });
  }
}

export async function PATCH(request: Request) {
  const idioma = idiomaDeRequest(request);
  const t = elegir(OPINIONES, idioma).servidor;
  const user = await cuentaReal();
  if (!user) return NextResponse.json({ ...avisoLogin(idioma), error: t.noAutenticado }, { status: 401 });
  let body: Record<string, unknown>;
  try {
    body = (await request.json()) as Record<string, unknown>;
  } catch {
    return NextResponse.json({ error: t.cuerpoInvalido }, { status: 400 });
  }
  const v = validarOpinion({ valoracion: "malo", motivo: body.motivo ?? null, texto: body.texto ?? null });
  if (!v.ok || typeof body.id !== "string" || !UUID.test(body.id)) return NextResponse.json({ error: t.cuerpoInvalido }, { status: 400 });
  try {
    if (!(await dentroDelTope(user.id))) return NextResponse.json({ error: t.tope }, { status: 429 });
    const hecho = await completarOpinion(user.id, body.id, v.motivo, v.texto);
    return hecho ? NextResponse.json({ ok: true }) : NextResponse.json({ error: t.noEncontrado }, { status: 404 });
  } catch (e) {
    console.error("[opiniones] fallo al completar:", e);
    return NextResponse.json({ error: t.noGuardado }, { status: 500 });
  }
}
