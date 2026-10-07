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

/** Los legales; la ayuda (Preguntas frecuentes) va aparte, en su tarjeta. */
const LEGALES = [
  ["/privacidad", "privacidad"],
  ["/terminos", "terminos"],
  ["/cookies", "cookies"],
  ["/eliminar-cuenta", "eliminar"],
] as const;

// Tinta del TEMA (tokens.css: --text sobre --bg). Antes el marco pedía un
// --ink que no existe y caía en #1a1a1a: texto casi negro sobre el negro.
// Decisión del fundador (8 oct 2026): los legales se leen claros y subrayados,
// y Preguntas frecuentes va en una tarjeta destacada.
export function PaginaPublica({ idioma, children }: { idioma: ActiveLocale; children: ReactNode }) {
  const t = navPublica(idioma);
  return (
    <main className="min-h-screen bg-bg text-ink">
      <div className="mx-auto max-w-[760px] px-5 pb-16 pt-8">
        <Link href="/" className="text-sm text-dim hover:text-ink">
          ← {t.inicio}
        </Link>
        <article className="pagina-publica mt-6 leading-relaxed">{children}</article>
        <nav aria-label="My Idea" className="mt-12 flex flex-col gap-6">
          <Link
            href="/preguntas-frecuentes"
            className="flex items-center gap-4 rounded-panel border border-accent/45 bg-accent/10 px-5 py-4 font-semibold text-ink hover:border-accent/70"
          >
            <span aria-hidden className="flex h-10 w-10 shrink-0 items-center justify-center rounded-full border-[1.5px] border-accent/70 text-[19px] font-bold text-accent">
              ?
            </span>
            <span className="flex-1">{t.preguntas}</span>
            <svg width="16" height="16" viewBox="0 0 12 12" aria-hidden className="shrink-0 rtl:-scale-x-100">
              <path d="M4 2l4 4-4 4" stroke="var(--accent)" strokeWidth="1.6" fill="none" />
            </svg>
          </Link>
          <div className="flex flex-wrap gap-x-6 gap-y-3 border-t border-hairline pt-5 text-[14.5px] font-medium">
            {LEGALES.map(([href, clave]) => (
              <Link key={href} href={href} className="text-ink underline underline-offset-[3px] hover:text-accent">
                {t[clave]}
              </Link>
            ))}
          </div>
        </nav>
      </div>
    </main>
  );
}
