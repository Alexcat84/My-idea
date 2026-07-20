/**
 * GET /auth/confirm — LEGACY: el destino del enlace magico. Desde jul 2026 el
 * acceso oficial es por CODIGO (POST /api/auth/verificar-codigo); esta ruta
 * queda viva por si un template viejo o un correo rezagado trae un enlace
 * valido: jamas una puerta muerta. Verifica el token_hash con
 * Supabase (deja la sesión en cookies vía el cliente de server.ts) y manda
 * al usuario a sus ideas. Si el enlace venció o ya se usó, vuelve al login
 * con un aviso en palabras de persona.
 *
 * ETAPA 2, dos actos al confirmar:
 * 1. ADOPCIÓN: si el request traía la sesión de una identidad invisible (el
 *    organizador anónimo), sus proyectos pasan al dueño recién autenticado.
 *    La prueba de posesión es la PROPIA cookie: el id anónimo se lee de la
 *    sesión que este request carga ANTES de verificar el OTP, jamás de un
 *    parámetro. Nadie puede adoptar el proyecto de otro.
 * 2. CORTESÍA: 20 créditos al primer login (otorgar_cortesia es una-sola-vez
 *    por cuenta vía beta_courtesy_log; llamarla de nuevo no re-otorga). El
 *    enlace solo se envió a correos de la allowlist (magic-link route).
 */
import { NextResponse } from "next/server";
import type { EmailOtpType } from "@supabase/supabase-js";
import { bienvenidaTrasLogin } from "@/lib/cuentas";
import { esInvitadoInvisible } from "@/lib/identidad";
import { estadoSeguridad } from "@/lib/seguridad";
import { createClient } from "@/lib/supabase/server";

export async function GET(request: Request) {
  const url = new URL(request.url);
  const tokenHash = url.searchParams.get("token_hash");
  const type = url.searchParams.get("type") as EmailOtpType | null;

  if (tokenHash && type) {
    const supabase = await createClient();

    // La identidad que este navegador traía ANTES del login (si la traía).
    const {
      data: { user: previo },
    } = await supabase.auth.getUser();
    const anonId = previo && esInvitadoInvisible(previo) ? previo.id : null;

    const { error } = await supabase.auth.verifyOtp({ type, token_hash: tokenHash });
    if (!error) {
      const {
        data: { user: real },
      } = await supabase.auth.getUser();
      if (real) await bienvenidaTrasLogin(real, anonId);
      // Centro de cuenta: con 2FA activo, el login sigue con el desafío.
      if (real) {
        try {
          const seguridad = await estadoSeguridad(real.id);
          if (seguridad.habilitado) {
            return NextResponse.redirect(
              new URL(`/login?desafio=1&metodo=${seguridad.metodo ?? "totp"}`, url.origin)
            );
          }
        } catch (e) {
          console.error("[confirm] no se pudo leer user_seguridad:", e);
        }
      }
      return NextResponse.redirect(new URL("/ideas", url.origin));
    }
  }
  return NextResponse.redirect(new URL("/login?enlace=vencido", url.origin));
}
