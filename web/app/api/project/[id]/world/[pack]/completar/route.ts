/**
 * POST /api/project/[id]/world/[pack]/completar — Fase 4.2: EL CIERRE DE MUNDO,
 * el acta en miniatura. body { accion: 'completar' | 'reabrir', motivo?: string }.
 *
 * Espejo exacto de /realizar (el acta del proyecto, Fase 4.0 §8) porque un
 * mundo es un subproyecto completo y merece los mismos parámetros:
 *  - NO exige el checklist del mundo al 100%: cerrar es soberanía del usuario.
 *  - Los ítems pendientes NO se tocan: quedan como testigos de la historia.
 *  - El motivo es OPCIONAL (cero fricción: se cierra sin escribir nada).
 *  - Reversible ('reabrir' pone completado_at a null) y reabrir JAMÁS borra el
 *    motivo: la historia no se reescribe. La bitácora conserva la secuencia
 *    completa de cierres de este mundo (tipo 'mundo_completado').
 *
 * Jerarquía honesta (§3): completar un mundo NO cierra la idea, ni siquiera
 * completándolos todos. Esta ruta jamás toca projects.realizada_at — el cierre
 * del proyecto es un acto aparte, del usuario, en su propia pantalla.
 */
import { NextResponse } from "next/server";
import { elegir } from "@/lib/i18n/config";
import { interpolar } from "@/lib/i18n/interpolar";
import { RUTAS } from "@/lib/i18n/mensajes/servidorRutas";
import { SERVIDOR_MUNDOS } from "@/lib/i18n/mensajes/servidorMundos";
import { idiomaDeRequest } from "@/lib/i18n/servidor";
import { guardarActa, instantaneaDeActa } from "@/lib/acta";
import { calcularAnalytics } from "@/lib/analytics";
import { cargarEntradaAnalytics, LecturaFallidaError, mensajeLecturaFallida } from "@/lib/analyticsEntrada";
import catalogo from "@/lib/assets/packs_catalog.json";
import { nombreDeMundo } from "@/lib/catalogoMundos";
import { MAX_LARGO_TEXTO_USUARIO, mensajeTextoLargo } from "@/lib/constants";
import { obtenerProyecto, registrarBitacora } from "@/lib/db";
import { createClient } from "@/lib/supabase/server";

export const runtime = "nodejs";

export async function POST(request: Request, { params }: { params: Promise<{ id: string; pack: string }> }) {
  const { id: projectId, pack } = await params;
  const idioma = idiomaDeRequest(request);
  const r = elegir(RUTAS, idioma);
  const t = elegir(SERVIDOR_MUNDOS, idioma).completar;

  const entrada = (catalogo.packs as Array<{ clave: string; nombre: string }>).find((p) => p.clave === pack);
  if (!entrada) {
    return NextResponse.json({ error: r.mundoNoExiste }, { status: 404 });
  }

  let body: { accion?: unknown; motivo?: unknown };
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: r.cuerpoJsonInvalido }, { status: 400 });
  }
  if (body.accion !== "completar" && body.accion !== "reabrir") {
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

  // El muro de siempre: sin fila en project_unlocks el mundo no existe aquí.
  const { data: unlock } = await supabase
    .from("project_unlocks")
    .select("id, cierre_motivo, completado_at")
    .eq("project_id", projectId)
    .eq("dominio", pack)
    .limit(1);
  if (!unlock || unlock.length === 0) {
    return NextResponse.json(
      { error: interpolar(r.mundoNoActivado, { mundo: nombreDeMundo(entrada.clave, idioma) }) },
      { status: 403 }
    );
  }
  const motivoPrevio = (unlock[0] as { cierre_motivo?: string | null }).cierre_motivo ?? null;

  const completar = body.accion === "completar";
  // AUD-09: completar un mundo YA completado no reescribe la fecha del primer
  // cierre (hermano del M08 del proyecto); reabrir la limpia.
  const completadoPrevio = (unlock[0] as { completado_at?: string | null }).completado_at ?? null;
  const completadoAt = completar ? (completadoPrevio ?? new Date().toISOString()) : null;

  // AUD-09 M04: el acta en miniatura del mundo es una FOTO. En un cierre NUEVO
  // se guarda la instantánea ANTES de sellarlo; si no se puede, no se cierra.
  if (completar && !completadoPrevio && completadoAt) {
    let analytics;
    try {
      analytics = calcularAnalytics(await cargarEntradaAnalytics(supabase, projectId, proyecto));
    } catch (e) {
      if (e instanceof LecturaFallidaError) return NextResponse.json({ error: mensajeLecturaFallida(idioma) }, { status: 503 });
      throw e;
    }
    const guardada = await guardarActa(supabase, projectId, {
      dominio: pack,
      cerrada_at: completadoAt,
      cierre_motivo: motivo ?? motivoPrevio,
      instantanea: instantaneaDeActa(analytics, pack),
    });
    if (!guardada) {
      return NextResponse.json(
        { error: interpolar(t.noPudeGuardarActa, { mundo: nombreDeMundo(entrada.clave, idioma) }) },
        { status: 500 }
      );
    }
  }
  const campos: Record<string, unknown> = { completado_at: completadoAt };
  // Solo un cierre CON motivo escribe cierre_motivo. Reabrir jamás lo borra, y
  // cerrar sin escribir nada no pisa el motivo de un cierre anterior.
  if (completar && motivo) campos.cierre_motivo = motivo;

  const { error } = await supabase
    .from("project_unlocks")
    .update(campos)
    .eq("project_id", projectId)
    .eq("dominio", pack);
  if (error) {
    return NextResponse.json({ error: t.noPudimosGuardar }, { status: 500 });
  }
  await registrarBitacora(supabase, projectId, "mundo_completado", {
    mundo: pack,
    accion: body.accion,
    motivo,
  });

  return NextResponse.json({
    dominio: pack,
    completado_at: completadoAt,
    cierre_motivo: completar ? motivo ?? motivoPrevio : motivoPrevio,
  });
}
