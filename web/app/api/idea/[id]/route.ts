/**
 * GET /api/idea/[id] — Fase 3.2: todo lo que la vista de idea necesita
 * para renderizarse desde lo persistido (refresh-proof): el proyecto, su
 * organizador, el último plan, el último reporte, y la entrevista
 * abierta (pregunta pendiente + ruta con títulos reales del grafo para
 * el árbol). RLS garantiza que solo se ve lo propio.
 */
import { NextResponse } from "next/server";
import { PREGUNTA_TIPO_OFERTA } from "@/lib/engine/constants";
import { obtenerProyecto, type EstadoSesionPersistido } from "@/lib/db";
import { cargarGrafo } from "@/lib/engine/graph";
import { preguntasPorTipo } from "@/lib/engine/reporte";
import { nombreDeIdea } from "@/lib/ideas";
import { createClient } from "@/lib/supabase/server";

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

  const { data: sesiones } = await supabase
    .from("sessions")
    .select("id, closed_at, estado_recorrido, created_at")
    .eq("project_id", projectId)
    .order("created_at", { ascending: true });

  const idsSesiones = ((sesiones ?? []) as Array<{ id: string }>).map((s) => s.id);
  const { data: planes } = idsSesiones.length
    ? await supabase
        .from("plans")
        .select("session_id, etiqueta, contenido_md, created_at")
        .in("session_id", idsSesiones)
        .order("created_at", { ascending: true })
    : { data: [] };

  type FilaPlan = { session_id: string; etiqueta: string; contenido_md: string; created_at: string };
  const filas = (planes ?? []) as FilaPlan[];
  const ultimo = (pred: (p: FilaPlan) => boolean) => filas.filter(pred).at(-1) ?? null;
  const organizador = ultimo((p) => p.etiqueta === "organizador");
  const plan = ultimo((p) => ["inicial", "completo", "seguimiento"].includes(p.etiqueta));
  const reporte = ultimo((p) => p.etiqueta === "reporte_numeros");

  // Entrevista abierta: sesión sin cerrar con estado resumible.
  const graph = cargarGrafo();
  let entrevista: {
    session_id: string;
    pregunta: string | null;
    listo_para_plan: boolean;
    ruta: Array<{ id: string; titulo: string; modo: string }>;
  } | null = null;
  for (const s of ((sesiones ?? []) as Array<{
    id: string;
    closed_at: string | null;
    estado_recorrido: EstadoSesionPersistido | null;
  }>).reverse()) {
    if (s.closed_at || !s.estado_recorrido) continue;
    const rec = s.estado_recorrido.recorrido;
    entrevista = {
      session_id: s.id,
      pregunta: rec.preguntaPendiente,
      listo_para_plan: rec.fase === "listo_para_plan",
      ruta: rec.ruta.map((nid, i) => ({
        id: nid,
        titulo: graph[nid]?.titulo_concepto ?? nid,
        modo: rec.modos[i],
      })),
    };
    break;
  }

  // Mini-entrevista de reporte a medias (refresh-proof): reconstruye la
  // pregunta pendiente desde projects.estado_reporte, igual que lo haría
  // el siguiente paso del flujo.
  let reporteEnCurso: { pregunta: string } | null = null;
  if (proyecto.estado_reporte) {
    const e = proyecto.estado_reporte.estado;
    if (e.fase === "clasificando_oferta" || e.fase === "reclasificando_molde") {
      reporteEnCurso = { pregunta: PREGUNTA_TIPO_OFERTA };
    } else {
      const campo = e.faltantesEsenciales[e.idx];
      if (campo) {
        reporteEnCurso = { pregunta: preguntasPorTipo(e.tipoOferta, e.unidadVenta)[campo] };
      }
    }
  }

  return NextResponse.json({
    idea: {
      id: proyecto.id,
      nombre: nombreDeIdea(proyecto.titulo, proyecto.entrada_original),
      entrada_original: proyecto.entrada_original,
      fase_actual: proyecto.fase_actual,
      tipo_oferta: proyecto.tipo_oferta ?? null,
    },
    organizador: organizador && { contenido_md: organizador.contenido_md },
    plan: plan && { etiqueta: plan.etiqueta, contenido_md: plan.contenido_md, created_at: plan.created_at },
    reporte: reporte && { contenido_md: reporte.contenido_md, created_at: reporte.created_at },
    reporte_en_curso: reporteEnCurso,
    entrevista,
  });
}
