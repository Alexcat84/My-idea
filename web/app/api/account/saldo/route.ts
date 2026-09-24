/**
 * GET /api/account/saldo — ETAPA 2: el saldo del chip del header (canon 07)
 * y la señal de sesión para la navegación. Lee credit_accounts con el
 * cliente RLS del usuario (policy own-select): cada quien ve solo lo suyo.
 * Para la identidad invisible no hay cuenta de créditos: saldo 0 + la señal
 * de que el login está pendiente.
 */
import { NextResponse } from "next/server";
import { esInvitadoInvisible } from "@/lib/identidad";
import { leerSaldo } from "@/lib/saldo";
import { createClient } from "@/lib/supabase/server";

export async function GET() {
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) {
    return NextResponse.json({ sesion: false, invisible: true, saldo: null });
  }
  const invisible = esInvitadoInvisible(user);
  if (invisible) {
    return NextResponse.json({ sesion: true, invisible: true, saldo: null });
  }
  // AUD-09 M21: si la lectura falla, saldo null (el chip no muestra un 0 falso).
  const saldo = await leerSaldo(supabase);
  return NextResponse.json({
    sesion: true,
    invisible: false,
    email: user.email ?? null,
    saldo,
    saldo_disponible: saldo !== null,
  });
}
