/**
 * GET /api/cron/limpiar-invitados — BORRADO REAL (decisión del fundador, 26 sep
 * 2026): las ideas de invitado SIN DUEÑO (escritas con la identidad invisible
 * y nunca adoptadas por una cuenta) se borran solas a los 30 días sin
 * actividad. La corre Vercel a diario (vercel.json) con el secreto CRON_SECRET;
 * sin el secreto configurado falla cerrado. El borrado lo hace la base
 * (limpiar_ideas_de_invitado, migración 044), con el mismo ON DELETE CASCADE
 * que borra todo lo que cuelga de cada idea.
 */
import { NextResponse } from "next/server";
import { createAdminClient } from "@/lib/supabase/admin";

export const DIAS_IDEAS_INVITADO = 30;

export async function GET(request: Request) {
  const secreto = process.env.CRON_SECRET;
  if (!secreto) {
    console.error("[cron/limpiar-invitados] falta CRON_SECRET; no se borra nada");
    return NextResponse.json({ error: "no configurado" }, { status: 503 });
  }
  if (request.headers.get("authorization") !== `Bearer ${secreto}`) {
    return NextResponse.json({ error: "no autorizado" }, { status: 401 });
  }
  const admin = createAdminClient();
  const { data, error } = await admin.rpc("limpiar_ideas_de_invitado", { p_dias: DIAS_IDEAS_INVITADO });
  if (error) {
    console.error("[cron/limpiar-invitados] fallo el borrado:", error);
    return NextResponse.json({ error: "fallo el borrado" }, { status: 500 });
  }
  const borradas = typeof data === "number" ? data : 0;
  console.log(`[cron/limpiar-invitados] ${borradas} idea(s) de invitado sin dueño borradas`);
  return NextResponse.json({ borradas });
}
