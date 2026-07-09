/**
 * proxy.ts (Next 16: el middleware renombrado) — Fase 3.2, item 9 del
 * plan original de Fase 3.0: la puerta de sesión de toda la app.
 *
 * Hace dos cosas y nada más: (1) refresca la sesión de Supabase en cada
 * request (patrón @supabase/ssr: sin esto, los Server Components leen
 * cookies vencidas), y (2) redirige a /login cualquier PÁGINA sin
 * usuario autenticado. Las rutas /api/* no pasan por aquí: cada route
 * handler ya verifica auth por sí mismo y responde 401 JSON (un
 * redirect a HTML rompería a los clientes programáticos como vuelo.ts).
 * La allowlist de beta se aplica en el envío del magic link
 * (/api/auth/magic-link): quien no está invitado nunca recibe el enlace,
 * así que nunca llega a tener sesión.
 */
import { createServerClient } from "@supabase/ssr";
import { NextResponse, type NextRequest } from "next/server";

const RUTAS_PUBLICAS = ["/login", "/auth"];

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
  const esPublica = RUTAS_PUBLICAS.some((r) => pathname === r || pathname.startsWith(r + "/"));

  if (!user && !esPublica) {
    const url = request.nextUrl.clone();
    url.pathname = "/login";
    url.search = "";
    return NextResponse.redirect(url);
  }
  if (user && pathname === "/login") {
    const url = request.nextUrl.clone();
    url.pathname = "/";
    url.search = "";
    return NextResponse.redirect(url);
  }

  return response;
}

export const config = {
  // Solo páginas: excluye estáticos, imágenes y /api (auth propia por ruta).
  matcher: ["/((?!api|_next/static|_next/image|favicon.ico|.*\\.(?:svg|png|jpg|jpeg|gif|webp|ico)$).*)"],
};
