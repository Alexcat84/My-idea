/**
 * GET /api/project/[id]/bitacora — Fase 4.8: las entradas de la bitácora en
 * JSON, para la PÁGINA en vivo (verla antes de imprimir). Misma fuente que el
 * documento .md/PDF: una sola historia. Cero motor, cero créditos.
 */
import { NextResponse } from "next/server";
import { cargarEntradasBitacora } from "@/lib/bitacoraDatos";
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
  if (!user) return NextResponse.json({ error: "no autenticado" }, { status: 401 });
  const proyecto = await obtenerProyecto(supabase, projectId);
  if (!proyecto) return NextResponse.json({ error: "idea no encontrada" }, { status: 404 });

  const nombre = nombreDeIdea(proyecto.titulo, proyecto.entrada_original);
  const entradas = await cargarEntradasBitacora(supabase, projectId, proyecto, nombre);

  return NextResponse.json({ nombre, entradas });
}
