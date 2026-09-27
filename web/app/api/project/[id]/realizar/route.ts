/**
 * POST /api/project/[id]/realizar — Fase 3.8 §5: la Celebración.
 * body { accion: 'realizar' | 'reabrir', motivo?: string | null }.
 *
 * 'realizar' sella projects.realizada_at = now() — la idea se vuelve
 * Proyecto. NO exige el checklist al 100% (las ideas reales cierran con
 * pendientes). 'reabrir' pone realizada_at a null. Cada acción deja rastro
 * en project_bitacora (tipo 'realizada', payload {accion, motivo}).
 *
 * Fase 4.0 §8 (el acta de cierre): 'realizar' acepta un `motivo` OPCIONAL —
 * el porqué en las palabras del usuario — que se guarda en
 * projects.cierre_motivo y en el payload de la bitácora. Reglas del §8:
 *  - Cero fricción: sin motivo se cierra igual, como siempre.
 *  - Reabrir NO borra el motivo (la historia no se reescribe): cierre_motivo
 *    sobrevive y la bitácora conserva la secuencia completa de cierres.
 *  - Los ítems pendientes no se tocan: quedan como testigos en la Historia.
 */
import { NextResponse } from "next/server";
import { elegir } from "@/lib/i18n/config";
import { RUTAS } from "@/lib/i18n/mensajes/servidorRutas";
import { SERVIDOR_PROYECTO } from "@/lib/i18n/mensajes/servidorProyecto";
import { idiomaDeRequest } from "@/lib/i18n/servidor";
import { guardarActa, instantaneaDeActa } from "@/lib/acta";
import { calcularAnalytics } from "@/lib/analytics";
import { cargarEntradaAnalytics, LecturaFallidaError, mensajeLecturaFallida } from "@/lib/analyticsEntrada";
import { MAX_LARGO_TEXTO_USUARIO, mensajeTextoLargo } from "@/lib/constants";
import { actualizarProyecto, obtenerProyecto, registrarBitacora } from "@/lib/db";
import { createClient } from "@/lib/supabase/server";

export const runtime = "nodejs";

export async function POST(request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id: projectId } = await params;
  const idioma = idiomaDeRequest(request);
  const r = elegir(RUTAS, idioma);
  const t = elegir(SERVIDOR_PROYECTO, idioma).realizar;

  let body: { accion?: unknown; motivo?: unknown };
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: r.cuerpoJsonInvalido }, { status: 400 });
  }
  if (body.accion !== "realizar" && body.accion !== "reabrir") {
    return NextResponse.json({ error: t.accionInvalida }, { status: 400 });
  }
  const motivoCrudo = typeof body.motivo === "string" ? body.motivo.trim() : null;
  if (motivoCrudo && motivoCrudo.length > MAX_LARGO_TEXTO_USUARIO) {
    return NextResponse.json(
      { error: mensajeTextoLargo(idioma), limite: MAX_LARGO_TEXTO_USUARIO },
      { status: 400 }
    );
  }
  const motivo = motivoCrudo || null;

  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) {
    return NextResponse.json({ error: r.noAutenticado }, { status: 401 });
  }
  const proyecto = await obtenerProyecto(supabase, projectId);
  if (!proyecto) {
    return NextResponse.json({ error: r.ideaNoEncontrada }, { status: 404 });
  }

  const realizada = body.accion === "realizar";
  // AUD-09 M09: una acción que no cambia el estado no deja historia. Reabrir lo
  // que no está cerrado escribía una reapertura falsa; cerrar lo ya cerrado,
  // otro "realizada" (y podía pisar el motivo del primer cierre).
  if (realizada === Boolean(proyecto.realizada_at)) {
    return NextResponse.json({
      realizada_at: proyecto.realizada_at ?? null,
      cierre_motivo: proyecto.cierre_motivo ?? null,
    });
  }
  // AUD-09 (tanda 5): volver a cerrar una idea YA cerrada no reescribe la fecha
  // del primer cierre (la historia no se reescribe). Reabrir sí la limpia: un
  // cierre posterior es un cierre nuevo, y la bitácora guarda los dos.
  const realizadaAt = realizada ? (proyecto.realizada_at ?? new Date().toISOString()) : null;

  // AUD-09 M04 (decisión del fundador, 25 sep 2026): EL ACTA ES UNA FOTO. En
  // un cierre NUEVO se toma la instantánea y se guarda en su propio registro
  // (project_actas) ANTES de sellar el cierre: si la foto no se puede guardar,
  // la idea sigue abierta y se dice. Volver a cerrar tras reabrir guarda otra
  // foto al lado; cerrar una idea ya cerrada no es un cierre nuevo.
  if (realizada && !proyecto.realizada_at && realizadaAt) {
    let analytics;
    try {
      analytics = calcularAnalytics(await cargarEntradaAnalytics(supabase, projectId, proyecto));
    } catch (e) {
      if (e instanceof LecturaFallidaError) return NextResponse.json({ error: mensajeLecturaFallida(idioma) }, { status: 503 });
      throw e;
    }
    const guardada = await guardarActa(supabase, projectId, {
      dominio: "core",
      cerrada_at: realizadaAt,
      cierre_motivo: motivo ?? proyecto.cierre_motivo ?? null,
      instantanea: instantaneaDeActa(analytics, "core"),
    });
    if (!guardada) {
      return NextResponse.json(
        { error: t.noPudeGuardarActa },
        { status: 500 }
      );
    }
  }
  const campos: Record<string, unknown> = { realizada_at: realizadaAt };
  // §8: solo un cierre CON motivo escribe cierre_motivo. Reabrir jamás lo
  // borra, y cerrar sin escribir nada no pisa el motivo de un cierre anterior.
  if (realizada && motivo) campos.cierre_motivo = motivo;
  await actualizarProyecto(supabase, projectId, campos);
  await registrarBitacora(supabase, projectId, "realizada", { accion: body.accion, motivo });

  return NextResponse.json({
    realizada_at: realizadaAt,
    cierre_motivo: realizada ? motivo ?? (proyecto.cierre_motivo ?? null) : (proyecto.cierre_motivo ?? null),
  });
}
