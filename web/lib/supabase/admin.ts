/**
 * Fase 3.0: cliente Supabase con la service role key -- salta RLS.
 * Equivalente exacto de engine/db.py: create_client(SUPABASE_URL,
 * SUPABASE_SERVICE_ROLE_KEY). SOLO server-side (route handlers), JAMAS
 * importado desde un Client Component: la service role key nunca debe
 * llegar al bundle del navegador. Usado para las mismas operaciones que
 * el CLI hace con privilegio elevado (crear/actualizar proyectos y
 * sesiones en nombre del usuario autenticado, ya verificado por la ruta
 * via el cliente de server.ts antes de llamar a este).
 */
import { createClient as createSupabaseClient, type SupabaseClient } from "@supabase/supabase-js";

let cached: SupabaseClient | null = null;

export function createAdminClient(): SupabaseClient {
  if (cached) return cached;
  cached = createSupabaseClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.SUPABASE_SERVICE_ROLE_KEY!,
    { auth: { autoRefreshToken: false, persistSession: false } }
  );
  return cached;
}
