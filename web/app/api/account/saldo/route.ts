/**
 * GET /api/account/saldo — ETAPA 2: el saldo del chip del header (canon 07)
 * y la señal de sesión para la navegación. Lee credit_accounts con el
 * cliente RLS del usuario (policy own-select): cada quien ve solo lo suyo.
 * Para la identidad invisible no hay cuenta de créditos: saldo 0 + la señal
 * de que el login está pendiente.
 */
import { NextResponse } from "next/server";
import { esInvitadoInvisible } from "@/lib/identidad";
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
  const { data } = await supabase.from("credit_accounts").select("creditos_total").maybeSingle();
  return NextResponse.json({
    sesion: true,
    invisible: false,
    email: user.email ?? null,
    saldo: (data as { creditos_total: number } | null)?.creditos_total ?? 0,
  });
}
