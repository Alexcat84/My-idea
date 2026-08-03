/**
 * PATCH /api/project/[id]/modo — el modo del camino POR ESPACIO ("todo separado",
 * migration 032). body {modo_camino: 'ritmo'|'fechas', dominio?: string}. Valida
 * contra MODO_CAMINO (dbContract), persiste en project_modos (project_id,
 * dominio) y deja rastro en la bitácora del proyecto (tipo 'modo_camino', payload
 * {de, a, dominio}). `dominio` por defecto 'core' (compat con el interruptor del
 * core, que llama sin dominio). El core DUAL-LEE su modo actual (project_modos ó
 * projects.modo_camino) para el `de` de la bitácora.
 *
 * Cada espacio elige su modo por su cuenta. Pausar (→'ritmo') JAMÁS borra las
 * fechas ya puestas en los ítems de ese espacio: solo silencia.
 */
import { NextResponse } from "next/server";
import { MODO_CAMINO, type ModoCamino } from "@/lib/dbContract";
import { ESPACIO_CORE, esEspacioCore } from "@/lib/espacios";
import { guardarModoEspacio, obtenerModosPorEspacio, obtenerProyecto, registrarBitacora } from "@/lib/db";
import { createClient } from "@/lib/supabase/server";

export const runtime = "nodejs";

export async function PATCH(request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id: projectId } = await params;

  let body: { modo_camino?: unknown; dominio?: unknown };
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
  const dominio = typeof body.dominio === "string" && body.dominio ? body.dominio : ESPACIO_CORE;

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

  // Modo actual del espacio (dual-read del core en la transición).
  const modos = await obtenerModosPorEspacio(supabase, projectId);
  const anterior = modos[dominio] ?? (esEspacioCore(dominio) ? proyecto.modo_camino ?? null : null);

  if (anterior !== nuevo) {
    await guardarModoEspacio(supabase, projectId, dominio, nuevo);
    await registrarBitacora(supabase, projectId, "modo_camino", { de: anterior, a: nuevo, dominio });
  }

  return NextResponse.json({ modo_camino: nuevo, dominio });
}
