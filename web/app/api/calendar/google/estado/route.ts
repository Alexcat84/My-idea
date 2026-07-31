/**
 * GET /api/calendar/google/estado — para la UI: si el usuario puede conectar,
 * si ya está conectado (y con qué correo) y CÓMO entró (google/email), para
 * elegir el texto: "activar sincronía" (ya usa Google) vs "conectar Google".
 */
import { NextResponse } from "next/server";
import { createClient } from "@/lib/supabase/server";
import { createAdminClient } from "@/lib/supabase/admin";
import { esInvitadoInvisible } from "@/lib/identidad";
import { estadoConexion } from "@/lib/calendarioSync";

export const runtime = "nodejs";

export async function GET() {
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user || esInvitadoInvisible(user)) {
    return NextResponse.json({ disponible: false, conectado: false, email: null, provider: null });
  }
  const admin = createAdminClient();
  const { conectado, email } = await estadoConexion(admin, user.id);
  const provider = (user.app_metadata?.provider as string | undefined) ?? "email";
  return NextResponse.json({ disponible: true, conectado, email, provider });
}
