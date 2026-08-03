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
import catalogo from "@/lib/assets/packs_catalog.json";
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
  // Fase 4.2 §3: el acta nombra los mundos como el usuario los conoce; el
  // catálogo vive aquí porque analytics.ts es puro y no conoce los assets.
  const nombreMundo = (dominio: string) =>
    (catalogo as { packs: Array<{ clave: string; nombre: string }> }).packs.find((p) => p.clave === dominio)
      ?.nombre ?? dominio;

  return NextResponse.json({
    nombre,
    modo_camino: proyecto.modo_camino ?? null,
    realizada_at: proyecto.realizada_at ?? null,
    cierre_motivo: proyecto.cierre_motivo ?? null,
    tiene_baseline: analytics.cumplimiento !== null,
    analytics,
    hitosCelebracion: construirHitos(entrada, ahora, true),
    informe_md: informeMarkdown(nombre, analytics, proyecto.realizada_at ?? null, nombreMundo),
  });
}
