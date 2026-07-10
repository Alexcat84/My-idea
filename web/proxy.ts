/**
 * proxy.ts (Next 16: el middleware renombrado) — Fase 3.2.
 *
 * DECISIÓN DE PRODUCTO (2026-07-09, fundador): la web es ABIERTA — no un
 * sitio-login. El visitante entra directo a la interfaz; el registro se
 * definirá después. Cómo se logra sin abrir la billetera ni romper el
 * modelo por-usuario (RLS): sesión ANÓNIMA invisible. Si no hay sesión,
 * se crea una con signInAnonymously() (cookies persistentes: las ideas
 * del visitante viven en su navegador), el límite de 5 arranques/día
 * aplica por usuario anónimo, y cuando exista registro, Supabase permite
 * VINCULAR el email a esa misma identidad conservando sus ideas.
 *
 * /login queda vivo pero fuera del flujo (nadie es redirigido ahí); la
 * allowlist sigue protegiendo el magic link para cuando el registro
 * regrese. Requiere "Anonymous sign-ins" habilitado en Supabase Auth; si
 * la creación anónima fallara (toggle apagado, red), se cae al login
 * como último recurso en vez de servir una app rota.
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
    // Web abierta: identidad anónima silenciosa en vez de muro de login.
    const { error } = await supabase.auth.signInAnonymously();
    if (error) {
      const url = request.nextUrl.clone();
      url.pathname = "/login";
      url.search = "";
      return NextResponse.redirect(url);
    }
  }

  return response;
}

export const config = {
  // Solo páginas: excluye estáticos, imágenes y /api (auth propia por ruta).
  matcher: ["/((?!api|_next/static|_next/image|favicon.ico|.*\\.(?:svg|png|jpg|jpeg|gif|webp|ico)$).*)"],
};
