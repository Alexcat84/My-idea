/**
 * proxy.ts (Next 16: el middleware renombrado; corre en runtime Node).
 *
 * REGLA DE PRODUCTO (fundador, 2026-07-09): la web es ABIERTA. Cualquier
 * visitante entra y usa lo básico sin restricciones; NINGÚN camino
 * termina en una pantalla de login, jamás. El signup/login real llegará
 * en una fase futura (al generar reportes) y podrá VINCULARSE a la
 * identidad silenciosa del visitante conservando sus ideas.
 *
 * Cómo se sostiene sin abrir la billetera ni romper el modelo por
 * usuario (RLS): toda visita sin sesión recibe una identidad invisible
 * en cookies. Cadena de bootstrap, de mejor a último recurso:
 *   1. signInAnonymously() — si el proyecto Supabase tiene el toggle
 *      "Anonymous sign-ins" activo (trae rate-limit por IP de fábrica).
 *   2. Usuario invitado creado con la service role key (visitante-<uuid>
 *      @invitado.my-idea.local, contraseña aleatoria descartada tras el
 *      login) — no depende de ningún toggle del dashboard.
 *   3. Si hasta eso falla (outage), el visitante PASA igual: la página
 *      carga y solo las acciones que escriben fallarán con mensaje
 *      humano. Nunca un muro.
 * El costo queda cuidado por el límite de 5 arranques/día por usuario
 * (lib/rateLimit.ts). /login existe pero está fuera de todo flujo.
 */
import { createServerClient } from "@supabase/ssr";
import { NextResponse, type NextRequest } from "next/server";
import { createAdminClient } from "@/lib/supabase/admin";

// "/" exacta = landing pública (Fase 3.4): se sirve sin crear sesión —
// así los crawlers no acuñan usuarios invitados; la identidad invisible
// nace al entrar a /nueva (CTA "Comenzar").
const RUTAS_PUBLICAS = ["/login", "/auth"];
const esRutaPublica = (pathname: string) =>
  pathname === "/" || RUTAS_PUBLICAS.some((r) => pathname === r || pathname.startsWith(r + "/"));

export async function proxy(request: NextRequest) {
  let response = NextResponse.next({ request });

  const supabase = createServerClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    {
      cookies: {
        getAll() {
          return request.cookies.getAll();
        },
        setAll(cookiesToSet) {
          cookiesToSet.forEach(({ name, value }) => request.cookies.set(name, value));
          response = NextResponse.next({ request });
          cookiesToSet.forEach(({ name, value, options }) => response.cookies.set(name, value, options));
        },
      },
    }
  );

  // getUser() (no getSession): valida el JWT contra Supabase y refresca
  // la cookie si hace falta — nunca confiar en la cookie sin validar.
  const {
    data: { user },
  } = await supabase.auth.getUser();

  const { pathname } = request.nextUrl;

  if (!user && !esRutaPublica(pathname)) {
    const { error } = await supabase.auth.signInAnonymously();
    if (error) {
      try {
        const email = `visitante-${crypto.randomUUID()}@invitado.my-idea.local`;
        const password = crypto.randomUUID() + crypto.randomUUID();
        const admin = createAdminClient();
        const creado = await admin.auth.admin.createUser({
          email,
          password,
          email_confirm: true,
          user_metadata: { invitado: true },
        });
        if (!creado.error) {
          await supabase.auth.signInWithPassword({ email, password });
        }
      } catch {
        // Último recurso: dejar pasar sin sesión (regla: nunca un muro).
      }
    }
  }

  return response;
}

export const config = {
  // Solo páginas: excluye estáticos, imágenes y /api (auth propia por ruta).
  matcher: ["/((?!api|_next/static|_next/image|favicon.ico|.*\\.(?:svg|png|jpg|jpeg|gif|webp|ico)$).*)"],
};
