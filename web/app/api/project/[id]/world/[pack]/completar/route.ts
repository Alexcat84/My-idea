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
import catalogo from "@/lib/assets/packs_catalog.json";
import { MAX_LARGO_TEXTO_USUARIO } from "@/lib/constants";
import { obtenerProyecto, registrarBitacora } from "@/lib/db";
import { createClient } from "@/lib/supabase/server";

export const runtime = "nodejs";

export async function POST(request: Request, { params }: { params: Promise<{ id: string; pack: string }> }) {
  const { id: projectId, pack } = await params;

  const entrada = (catalogo.packs as Array<{ clave: string; nombre: string }>).find((p) => p.clave === pack);
  if (!entrada) {
    return NextResponse.json({ error: "ese mundo no existe" }, { status: 404 });
  }

  let body: { accion?: unknown; motivo?: unknown };
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: "cuerpo JSON inválido" }, { status: 400 });
  }
  if (body.accion !== "completar" && body.accion !== "reabrir") {
    return NextResponse.json({ error: "accion inválida; usa 'completar' o 'reabrir'" }, { status: 400 });
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

  // El muro de siempre: sin fila en project_unlocks el mundo no existe aquí.
  const { data: unlock } = await supabase
    .from("project_unlocks")
    .select("id, cierre_motivo")
    .eq("project_id", projectId)
    .eq("dominio", pack)
    .limit(1);
  if (!unlock || unlock.length === 0) {
    return NextResponse.json(
      { error: `El mundo "${entrada.nombre}" aún no está activado para esta idea.` },
      { status: 403 }
    );
  }
  const motivoPrevio = (unlock[0] as { cierre_motivo?: string | null }).cierre_motivo ?? null;

  const completar = body.accion === "completar";
  const completadoAt = completar ? new Date().toISOString() : null;
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
    return NextResponse.json({ error: "no pudimos guardar; intenta de nuevo" }, { status: 500 });
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
