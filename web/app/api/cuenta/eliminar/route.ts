/**
 * POST /api/cuenta/eliminar — borra la cuenta COMPLETA (réplica del I Ching
 * api/account/delete): exige la palabra escrita "ELIMINAR", y con 2FA activo
 * exige además el desafío superado en esta sesión. Antes de borrar, si la
 * cuenta recibió cortesía, se escribe la huella del correo
 * (cortesia_email_log): borrar-y-volver no re-otorga los 20. El borrado es
 * UNA llamada admin: todas nuestras tablas cuelgan de auth.users con
 * ON DELETE CASCADE (001/018/020/022/024/029) — la base se limpia sola.
 * (Sin paso RevenueCat: las pasarelas siguen dormidas.)
 */
import { NextResponse } from "next/server";
import { huellaDeEmail } from "@/lib/cuentas";
import {
  AVISO_2FA,
  desafioSuperadoEnSesion,
  estadoSeguridad,
  sesionRealDeCookies,
} from "@/lib/seguridad";
import { createAdminClient } from "@/lib/supabase/admin";

export async function POST(request: Request) {
  const sesion = await sesionRealDeCookies();
  if (!sesion) {
    return NextResponse.json({ error: "necesitas tu cuenta para esto" }, { status: 401 });
  }
  let body: { confirmacion?: unknown };
  try {
    body = await request.json();
  } catch {
    return NextResponse.json({ error: "cuerpo invalido" }, { status: 400 });
  }
  if (String(body.confirmacion ?? "").trim().toUpperCase() !== "ELIMINAR") {
    return NextResponse.json(
      { error: 'Para borrar tu cuenta escribe la palabra "ELIMINAR" tal cual.' },
      { status: 400 }
    );
  }

  const userId = sesion.user.id;
  try {
    const seguridad = await estadoSeguridad(userId);
    if (seguridad.habilitado && !(await desafioSuperadoEnSesion(userId, sesion.sessionId))) {
      return NextResponse.json(AVISO_2FA, { status: 403 });
    }
  } catch (e) {
    console.error("[cuenta/eliminar] no se pudo leer user_seguridad:", e);
  }

  const admin = createAdminClient();

  // La huella de la cortesía ANTES del borrado (después ya no hay fila que
  // consultar). Solo si de verdad la recibió.
  const email = sesion.user.email ?? "";
  if (email) {
    const { data: cortesia } = await admin
      .from("beta_courtesy_log")
      .select("user_id")
      .eq("user_id", userId)
      .maybeSingle();
    if (cortesia) {
      const { error: huellaError } = await admin
        .from("cortesia_email_log")
        .upsert({ email_hash: huellaDeEmail(email) });
      if (huellaError) {
        // Sin huella no se borra: borrar dejaría la puerta del re-otorgo
        // abierta (dinero). Ruidoso y reintentable.
        console.error("[cuenta/eliminar] fallo la huella de cortesia:", huellaError.message);
        return NextResponse.json({ error: "algo se atoró; intenta de nuevo" }, { status: 500 });
      }
    }
  }

  const { error: deleteError } = await admin.auth.admin.deleteUser(userId);
  if (deleteError) {
    console.error("[cuenta/eliminar] fallo el borrado:", deleteError.message);
    return NextResponse.json({ error: "algo se atoró; intenta de nuevo" }, { status: 500 });
  }

  console.log(`[cuenta/eliminar] cuenta ${userId.slice(0, 8)}… borrada por su dueño`);
  return NextResponse.json({ ok: true });
}
