/**
 * saldo.ts: la lectura ÚNICA del saldo de créditos con el cliente del usuario
 * (RLS own-select sobre credit_accounts). AUD-09 M21: si la lectura falla,
 * devuelve null y deja rastro; 0 solo cuando de verdad no hay cuenta. Un cero
 * falso es una mentira sobre dinero, y la pantalla no la muestra.
 */
import type { SupabaseClient } from "@supabase/supabase-js";

export async function leerSaldo(supabase: SupabaseClient): Promise<number | null> {
  const { data, error } = await supabase.from("credit_accounts").select("creditos_total").maybeSingle();
  if (error) {
    console.error("[saldo] no se pudo leer credit_accounts:", error);
    return null;
  }
  return (data as { creditos_total: number } | null)?.creditos_total ?? 0;
}
