/**
 * POST /api/calendar/google/sync — "Sincronizar ahora": vuelve a poner todas
 * las fechas del usuario en su calendario "My Idea". Idempotente; no-op si no
 * está conectado. Red de seguridad además del sync automático por cambio.
 */
import { NextResponse } from "next/server";
import { createClient } from "@/lib/supabase/server";
import { createAdminClient } from "@/lib/supabase/admin";
import { sincronizarUsuario } from "@/lib/calendarioSync";

export const runtime = "nodejs";

export async function POST() {
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) return NextResponse.json({ error: "no autenticado" }, { status: 401 });
  const admin = createAdminClient();
  try {
    await sincronizarUsuario(admin, user.id);
    return NextResponse.json({ ok: true });
  } catch (e) {
    console.error("[gcal/sync]", (e as Error).message);
    return NextResponse.json({ error: "no se pudo sincronizar" }, { status: 502 });
  }
}
