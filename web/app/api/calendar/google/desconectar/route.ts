/**
 * POST /api/calendar/google/desconectar — quita la sincronía: borra el
 * calendario dedicado "My Idea" (con todos sus eventos), el mapa y la conexión.
 */
import { NextResponse } from "next/server";
import { createClient } from "@/lib/supabase/server";
import { createAdminClient } from "@/lib/supabase/admin";
import { desconectar } from "@/lib/calendarioSync";

export const runtime = "nodejs";

export async function POST() {
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) return NextResponse.json({ error: "no autenticado" }, { status: 401 });
  const admin = createAdminClient();
  await desconectar(admin, user.id);
  return NextResponse.json({ ok: true });
}
