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
import { elegir } from "@/lib/i18n/config";
import { RUTAS } from "@/lib/i18n/mensajes/servidorRutas";
import { idiomaDeRequest } from "@/lib/i18n/servidor";
import { actasVigentes } from "@/lib/acta";
import { calcularAnalytics, construirHitos, informeMarkdown } from "@/lib/analytics";
import catalogo from "@/lib/assets/packs_catalog.json";
import { cargarEntradaAnalytics, LecturaFallidaError, MENSAJE_LECTURA_FALLIDA } from "@/lib/analyticsEntrada";
import { obtenerProyecto } from "@/lib/db";
import { nombreDeIdea } from "@/lib/ideas";
import { createClient } from "@/lib/supabase/server";

export const runtime = "nodejs";

export async function GET(request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id: projectId } = await params;
  const r = elegir(RUTAS, idiomaDeRequest(request));

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

  const ahora = new Date().toISOString();
  // AUD-09 M18: una lectura fallida se dice (503), no se pinta en cero.
  let entrada: Awaited<ReturnType<typeof cargarEntradaAnalytics>>;
  try {
    entrada = await cargarEntradaAnalytics(supabase, projectId, proyecto, ahora);
  } catch (e) {
    if (e instanceof LecturaFallidaError) return NextResponse.json({ error: MENSAJE_LECTURA_FALLIDA }, { status: 503 });
    throw e;
  }

  const analytics = calcularAnalytics(entrada);
  const nombre = nombreDeIdea(proyecto.titulo, proyecto.entrada_original);
  // Fase 4.2 §3: el acta nombra los mundos como el usuario los conoce; el
  // catálogo vive aquí porque analytics.ts es puro y no conoce los assets.
  const nombreMundo = (dominio: string) =>
    (catalogo as { packs: Array<{ clave: string; nombre: string }> }).packs.find((p) => p.clave === dominio)
      ?.nombre ?? dominio;

  // AUD-09 M04: el acta de cada espacio es la FOTO guardada al cerrar.
  const actas = await actasVigentes(supabase, projectId);

  return NextResponse.json({
    nombre,
    actas,
    // "Todo separado" (T3): el modo del core, ya dual-read en cargarEntradaAnalytics.
    modo_camino: entrada.modoCamino,
    realizada_at: proyecto.realizada_at ?? null,
    cierre_motivo: proyecto.cierre_motivo ?? null,
    tiene_baseline: analytics.cumplimiento !== null,
    analytics,
    hitosCelebracion: construirHitos(entrada, ahora, true),
    informe_md: informeMarkdown(nombre, analytics, proyecto.realizada_at ?? null, nombreMundo, actas.core ?? null),
  });
}
