"use client";

/**
 * El aviso de cookies (corrección del fundador, 7 oct 2026): el sitio usa solo cookies necesarias (la sesión de
 * Supabase, también la de la identidad invisible; el verificador de la entrada con Google; el destino tras entrar) y
 * una de preferencia que recuerda el idioma (docs/legal/COOKIES.md). Sin analítica ni publicidad, no hay nada que
 * consentir ni bloquear: un aviso pequeño al pie, en el flujo de la página, que no tapa nada y no se puede "cerrar"
 * porque no estorba. Si algún día entra una cookie que no sea necesaria, este aviso no basta: habrá que pedir permiso.
 * Dónde (8 oct 2026): al pie de la portada y de las páginas públicas, nunca en el layout raíz, porque ahí asomaba en
 * cada transición entre páginas.
 */
import { elegir } from "@/lib/i18n/config";
import { useIdioma } from "@/lib/i18n/IdiomaProvider";
import { CONSENTIMIENTO } from "@/lib/i18n/mensajes/consentimiento";
import { rico } from "@/lib/i18n/rico";

export function AvisoCookies() {
  const t = elegir(CONSENTIMIENTO, useIdioma()).cookies;
  return (
    <p className="px-4 pt-3 text-center text-[11px] leading-[1.5] text-white/40">
      {rico(t.aviso, {
        cookies: (c) => (
          <a href="/cookies" className="underline underline-offset-2 hover:text-white/70">
            {c}
          </a>
        ),
      })}
    </p>
  );
}
