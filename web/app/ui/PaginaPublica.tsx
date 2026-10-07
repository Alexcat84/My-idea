/**
 * Marco de las páginas públicas legales y de ayuda (encargo del fundador del 6 oct 2026, punto 6): Privacidad,
 * Términos, Cookies, Eliminar tu cuenta y Preguntas frecuentes. Se leen sin cuenta y sin iniciar sesión (proxy.ts,
 * RUTAS_PUBLICAS). Estructura tomada de The Original I Ching (MarketingDocShell).
 */
import Link from "next/link";
import type { ReactNode } from "react";
import { NAV, type IdiomaPagina } from "@/lib/legal/paginas";

const ENLACES = [
  ["/privacidad", "privacidad"],
  ["/terminos", "terminos"],
  ["/cookies", "cookies"],
  ["/eliminar-cuenta", "eliminar"],
  ["/preguntas-frecuentes", "preguntas"],
] as const;

export function PaginaPublica({ idioma, children }: { idioma: IdiomaPagina; children: ReactNode }) {
  const t = NAV[idioma];
  return (
    <main style={{ background: "var(--bg, #fff)", color: "var(--ink, #1a1a1a)", minHeight: "100vh" }}>
      <div style={{ maxWidth: 760, margin: "0 auto", padding: "32px 20px 64px" }}>
        <Link href="/" style={{ fontSize: 14, textDecoration: "none" }}>
          ← {t.inicio}
        </Link>
        <article className="pagina-publica" style={{ lineHeight: 1.6, marginTop: 24 }}>
          {children}
        </article>
        <nav aria-label="My Idea" style={{ display: "flex", flexWrap: "wrap", gap: 16, marginTop: 48, fontSize: 14 }}>
          {ENLACES.map(([href, clave]) => (
            <Link key={href} href={href}>
              {t[clave]}
            </Link>
          ))}
        </nav>
      </div>
    </main>
  );
}
