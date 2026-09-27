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
import { latidoUpstash } from "@/lib/rateLimit";
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

  // El latido diario a Upstash (decisión del fundador, 25 sep 2026): mantiene
  // activa la base del contador y, si no responde, la tarea FALLA (Vercel la
  // marca en rojo) con una alerta en los registros. Sin esa base la IA está
  // detenida (falla cerrada, lib/rateLimit.ts).
  const upstash = await latidoUpstash();
  if (upstash === "caido" || (upstash === "sin_credenciales" && process.env.NODE_ENV === "production")) {
    console.error("[cron/limpiar-invitados] ALERTA: la base del contador (Upstash) no responde; la IA está detenida", { upstash });
    return NextResponse.json({ borradas, upstash }, { status: 500 });
  }
  return NextResponse.json({ borradas, upstash });
}
