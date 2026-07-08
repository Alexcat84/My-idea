/**
 * Fase 3.0: cliente Supabase para el navegador (Client Components).
 * Usa las claves publicas (NEXT_PUBLIC_*) y respeta RLS con la sesion del
 * usuario autenticado -- mismo par URL/anon key que ya usa el CLI
 * (engine/db.py: SUPABASE_URL/SUPABASE_ANON_KEY), nunca la service role key.
 */
import { createBrowserClient } from "@supabase/ssr";

export function createClient() {
  return createBrowserClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
  );
}
