/**
 * GET /api/projects - Fase 3.0: lista los proyectos del usuario
 * autenticado para retomarlos, mas recientes primero. Reemplaza la
 * necesidad de recordar un PROJECT_ID de memoria para usar --seguir en
 * el CLI -- en la web, "seguir" es un boton sobre esta lista.
 */
import { NextResponse } from "next/server";
import { listarProyectos } from "@/lib/db";
import { createClient } from "@/lib/supabase/server";

export async function GET() {
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) {
    return NextResponse.json({ error: "no autenticado" }, { status: 401 });
  }

  const proyectos = await listarProyectos(supabase);
  return NextResponse.json({
    proyectos: proyectos.map((p) => ({
      id: p.id,
      titulo: p.titulo,
      entrada_original: p.entrada_original,
      fase_actual: p.fase_actual,
      session_count: p.session_count,
      status: p.status,
      tipo_oferta: p.tipo_oferta ?? null,
      created_at: p.created_at,
      updated_at: p.updated_at,
    })),
  });
}
