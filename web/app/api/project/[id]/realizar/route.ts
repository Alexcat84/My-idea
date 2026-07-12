/**
 * POST /api/project/[id]/realizar — Fase 3.8 §5: la Celebración.
 * body { accion: 'realizar' | 'reabrir' }.
 *
 * 'realizar' sella projects.realizada_at = now() — la idea se vuelve
 * Proyecto. NO exige el checklist al 100% (las ideas reales cierran con
 * pendientes). 'reabrir' pone realizada_at a null. Cada acción deja rastro
 * en project_bitacora (tipo 'realizada', payload {accion}).
 */
import { NextResponse } from "next/server";
import { actualizarProyecto, obtenerProyecto, registrarBitacora } from "@/lib/db";
import { createClient } from "@/lib/supabase/server";

export const runtime = "nodejs";

export async function POST(request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id: projectId } = await params;

  let body: { accion?: unknown };
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: "cuerpo JSON inválido" }, { status: 400 });
  }
  if (body.accion !== "realizar" && body.accion !== "reabrir") {
    return NextResponse.json({ error: "accion inválida; usa 'realizar' o 'reabrir'" }, { status: 400 });
  }

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

  const realizadaAt = body.accion === "realizar" ? new Date().toISOString() : null;
  await actualizarProyecto(supabase, projectId, { realizada_at: realizadaAt });
  await registrarBitacora(supabase, projectId, "realizada", { accion: body.accion });

  return NextResponse.json({ realizada_at: realizadaAt });
}
