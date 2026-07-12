/**
 * PATCH /api/project/[id]/modo — Fase 3.8 §3: el modo del camino.
 * body {modo_camino: 'ritmo' | 'fechas'}. Valida contra MODO_CAMINO
 * (dbContract), persiste projects.modo_camino y deja rastro en la bitácora
 * del proyecto (tipo 'modo_camino', payload {de, a}) — así la telemetría
 * sabe cuándo alguien enciende, pausa o reactiva las fechas.
 *
 * El interruptor "Fechas y recordatorios: activados/pausados" de Manos a la
 * Obra es este mismo endpoint alternando 'fechas' ↔ 'ritmo'. Pausar
 * (→'ritmo') JAMÁS borra las fechas ya puestas en los ítems: solo silencia.
 */
import { NextResponse } from "next/server";
import { MODO_CAMINO, type ModoCamino } from "@/lib/dbContract";
import { actualizarProyecto, obtenerProyecto, registrarBitacora } from "@/lib/db";
import { createClient } from "@/lib/supabase/server";

export const runtime = "nodejs";

export async function PATCH(request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id: projectId } = await params;

  let body: { modo_camino?: unknown };
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: "cuerpo JSON inválido" }, { status: 400 });
  }
  if (typeof body.modo_camino !== "string" || !(MODO_CAMINO as readonly string[]).includes(body.modo_camino)) {
    return NextResponse.json(
      { error: `modo_camino inválido; usa uno de: ${MODO_CAMINO.join(", ")}` },
      { status: 400 }
    );
  }
  const nuevo = body.modo_camino as ModoCamino;

  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) {
    return NextResponse.json({ error: "no autenticado" }, { status: 401 });
  }
  const proyecto = await obtenerProyecto(supabase, projectId);
  if (!proyecto) {
    return NextResponse.json({ error: "idea no encontrada" }, { status: 404 });
  }

  const anterior = proyecto.modo_camino ?? null;
  if (anterior !== nuevo) {
    await actualizarProyecto(supabase, projectId, { modo_camino: nuevo });
    await registrarBitacora(supabase, projectId, "modo_camino", { de: anterior, a: nuevo });
  }

  return NextResponse.json({ modo_camino: nuevo });
}
