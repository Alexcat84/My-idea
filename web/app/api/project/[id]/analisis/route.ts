/**
 * GET /api/project/[id]/analisis — Fase 3.8 §5/§6: todo el análisis del
 * proyecto calculado de lo persistido (CERO LLM, cero costo por render).
 * Alimenta la pantalla Análisis (capa universal + cumplimiento) y la
 * Celebración (mismos números + el timeline con acciones).
 *
 * Devuelve: nombre, modo_camino, realizada_at, tiene_baseline, analytics
 * (hitos sin acciones), hitosCelebracion (con acciones), informe_md.
 */
import { NextResponse } from "next/server";
import { calcularAnalytics, construirHitos, informeMarkdown } from "@/lib/analytics";
import { cargarEntradaAnalytics } from "@/lib/analyticsEntrada";
import { obtenerProyecto } from "@/lib/db";
import { nombreDeIdea } from "@/lib/ideas";
import { createClient } from "@/lib/supabase/server";

export const runtime = "nodejs";

export async function GET(_request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id: projectId } = await params;

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

  const ahora = new Date().toISOString();
  const entrada = await cargarEntradaAnalytics(supabase, projectId, proyecto, ahora);

  const analytics = calcularAnalytics(entrada);
  const nombre = nombreDeIdea(proyecto.titulo, proyecto.entrada_original);

  return NextResponse.json({
    nombre,
    modo_camino: proyecto.modo_camino ?? null,
    realizada_at: proyecto.realizada_at ?? null,
    tiene_baseline: analytics.cumplimiento !== null,
    analytics,
    hitosCelebracion: construirHitos(entrada, ahora, true),
    informe_md: informeMarkdown(nombre, analytics),
  });
}
