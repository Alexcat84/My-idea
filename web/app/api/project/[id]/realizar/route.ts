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
import { MAX_LARGO_TEXTO_USUARIO } from "@/lib/constants";
import { actualizarProyecto, obtenerProyecto, registrarBitacora } from "@/lib/db";
import { createClient } from "@/lib/supabase/server";

export const runtime = "nodejs";

export async function POST(request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id: projectId } = await params;

  let body: { accion?: unknown; motivo?: unknown };
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: "cuerpo JSON inválido" }, { status: 400 });
  }
  if (body.accion !== "realizar" && body.accion !== "reabrir") {
    return NextResponse.json({ error: "accion inválida; usa 'realizar' o 'reabrir'" }, { status: 400 });
  }
  const motivoCrudo = typeof body.motivo === "string" ? body.motivo.trim() : null;
  if (motivoCrudo && motivoCrudo.length > MAX_LARGO_TEXTO_USUARIO) {
    return NextResponse.json(
      { error: `'motivo' supera el maximo de ${MAX_LARGO_TEXTO_USUARIO} caracteres` },
      { status: 400 }
    );
  }
  const motivo = motivoCrudo || null;

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

  const realizada = body.accion === "realizar";
  const realizadaAt = realizada ? new Date().toISOString() : null;
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
