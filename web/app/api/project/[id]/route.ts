/**
 * DELETE /api/project/[id] — borra UNA idea completa (centro de cuenta,
 * réplica del patrón de borrado de chats del I Ching). El borrado corre con
 * la sesión del PROPIO usuario: RLS (projects_own, FOR ALL) garantiza que
 * nadie borra la idea de otro, y las cascadas de la 001/018 (sessions,
 * plans, nodos, checklist, unlocks, bitácora, versiones) limpian el resto.
 * Con 2FA activo exige el desafío superado (es destructivo e irreversible).
 */
import { NextResponse } from "next/server";
import { AVISO_LOGIN, esInvitadoInvisible } from "@/lib/identidad";
import { AVISO_2FA, faltaSegundoFactor } from "@/lib/seguridad";
import { createClient } from "@/lib/supabase/server";

export async function DELETE(_request: Request, { params }: { params: Promise<{ id: string }> }) {
  const { id: projectId } = await params;

  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) {
    return NextResponse.json({ error: "no autenticado" }, { status: 401 });
  }
  if (esInvitadoInvisible(user)) {
    return NextResponse.json(AVISO_LOGIN, { status: 401 });
  }
  if (await faltaSegundoFactor()) {
    return NextResponse.json(AVISO_2FA, { status: 403 });
  }

  // RLS: si la idea no es suya (o no existe), el select no la ve — misma
  // respuesta en ambos casos, sin filtrar existencia ajena.
  const { data: proyecto } = await supabase.from("projects").select("id").eq("id", projectId).maybeSingle();
  if (!proyecto) {
    return NextResponse.json({ error: "idea no encontrada" }, { status: 404 });
  }

  const { error } = await supabase.from("projects").delete().eq("id", projectId);
  if (error) {
    console.error("[project/delete] fallo:", error.message);
    return NextResponse.json({ error: "algo se atoró; intenta de nuevo" }, { status: 500 });
  }
  return NextResponse.json({ ok: true });
}
