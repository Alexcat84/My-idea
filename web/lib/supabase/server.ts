/**
 * Fase 3.0: cliente Supabase para Server Components, Route Handlers y
 * proxy.ts (Next.js 16 -- antes "middleware"). Lee/escribe la sesion via
 * cookies; respeta RLS con el usuario autenticado real. Crear uno nuevo
 * por request (nunca compartir la instancia entre requests).
 */
import { createServerClient } from "@supabase/ssr";
import { cookies } from "next/headers";

export async function createClient() {
  const cookieStore = await cookies();

  return createServerClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    {
      cookies: {
        getAll() {
          return cookieStore.getAll();
        },
        setAll(cookiesToSet) {
          try {
            cookiesToSet.forEach(({ name, value, options }) => cookieStore.set(name, value, options));
          } catch {
            // Llamado desde un Server Component (no puede escribir cookies).
            // Inofensivo si proxy.ts refresca la sesion en cada request.
          }
        },
      },
    }
  );
}
