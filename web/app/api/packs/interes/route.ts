/**
 * POST /api/packs/interes — Fase 3.2 (brief sección 4): registra el
 * click en un candado de mundo HSEQ. Telemetría de demanda pura: en beta
 * los packs son fachada, y estos clicks son el oro para decidir cuál se
 * lanza primero. El navegador nunca toca pack_clicks directo: la ruta
 * verifica al usuario y escribe con la service role (RLS sin policies).
 */
import { NextResponse } from "next/server";
import { PACK_CLICKS_PACK, type PackClave } from "@/lib/dbContract";
import { createAdminClient } from "@/lib/supabase/admin";
import { createClient } from "@/lib/supabase/server";

export async function POST(request: Request) {
  let body: unknown;
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: "cuerpo invalido" }, { status: 400 });
  }
  const pack = (body as { pack?: unknown } | null)?.pack;
  const projectId = (body as { project_id?: unknown } | null)?.project_id;
  if (typeof pack !== "string" || !(PACK_CLICKS_PACK as readonly string[]).includes(pack)) {
    return NextResponse.json({ error: "pack desconocido" }, { status: 400 });
  }
  if (projectId !== undefined && typeof projectId !== "string") {
    return NextResponse.json({ error: "'project_id' debe ser un string" }, { status: 400 });
  }

  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) {
    return NextResponse.json({ error: "no autenticado" }, { status: 401 });
  }

  const admin = createAdminClient();
  const { error } = await admin.from("pack_clicks").insert({
    user_id: user.id,
    project_id: projectId ?? null,
    pack: pack as PackClave,
  });
  if (error) {
    // La telemetría jamás rompe la experiencia: se responde ok igual y
    // el fallo queda en el log del servidor.
    console.warn("pack_clicks insert fallo:", error.message);
  }
  return NextResponse.json({ ok: true });
}
