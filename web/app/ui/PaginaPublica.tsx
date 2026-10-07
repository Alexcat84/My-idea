/**
 * Marco de las páginas públicas legales y de ayuda (encargo del fundador del 6 oct 2026, punto 6): Privacidad,
 * Términos, Cookies, Eliminar tu cuenta y Preguntas frecuentes. Se leen sin cuenta y sin iniciar sesión (proxy.ts,
 * RUTAS_PUBLICAS). Estructura tomada de The Original I Ching (MarketingDocShell). En los once idiomas (I18N AL DÍA,
 * 7 oct 2026): el pie sale del catálogo lib/i18n/mensajes/paginasAyuda.ts.
 */
import Link from "next/link";
import type { ReactNode } from "react";
import type { ActiveLocale } from "@/lib/i18n/config";
import { navPublica } from "@/lib/legal/paginas";
import { AvisoCookies } from "./AvisoCookies";

const ENLACES = [
  ["/privacidad", "privacidad"],
  ["/terminos", "terminos"],
  ["/cookies", "cookies"],
  ["/eliminar-cuenta", "eliminar"],
  ["/preguntas-frecuentes", "preguntas"],
] as const;

// Tinta del TEMA (tokens.css: --text sobre --bg). Antes el marco pedía un
// --ink que no existe y caía en #1a1a1a: texto casi negro sobre el negro, las
// páginas "opacas" que vio el fundador (8 oct 2026). La barra de enlaces es la
// de siempre; ahora hereda la tinta clara.
export function PaginaPublica({ idioma, children }: { idioma: ActiveLocale; children: ReactNode }) {
  const t = navPublica(idioma);
  return (
    <main className="min-h-screen bg-bg text-ink">
      <div className="mx-auto max-w-[760px] px-5 pb-16 pt-8">
        <Link href="/" className="text-sm text-dim hover:text-ink">
          ← {t.inicio}
        </Link>
        <article className="pagina-publica mt-6 leading-relaxed">{children}</article>
        <nav aria-label="My Idea" style={{ display: "flex", flexWrap: "wrap", gap: 16, marginTop: 48, fontSize: 14 }}>
          {ENLACES.map(([href, clave]) => (
            <Link key={href} href={href}>
              {t[clave]}
            </Link>
          ))}
        </nav>
        <div className="mt-8">
          <AvisoCookies />
        </div>
      </div>
    </main>
  );
}
