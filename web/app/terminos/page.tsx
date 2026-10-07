/**
 * /terminos: los términos de uso, publicado desde docs/legal/ (encargo del fundador del 6 oct 2026, punto 6). Se lee sin cuenta y
 * sin iniciar sesión. Español y francés; cualquier otro idioma lee el español con un aviso. La revisión profesional
 * queda pendiente: el texto se afina en el .md y se vuelve a sincronizar (scripts/sync_legal_web.py).
 */
import type { Metadata } from "next";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { PaginaPublica } from "@/app/ui/PaginaPublica";
import { idiomaDeCookies } from "@/lib/i18n/servidor";
import { TEXTOS_LEGALES } from "@/lib/legal/textos";
import { idiomaDePagina, idiomaLegal, NAV } from "@/lib/legal/paginas";

export async function generateMetadata(): Promise<Metadata> {
  const idioma = idiomaDePagina(await idiomaDeCookies());
  return { title: `${NAV[idioma].terminos} | My Idea` };
}

export default async function Pagina() {
  const idioma = await idiomaDeCookies();
  const legal = idiomaLegal(idioma);
  const pagina = idiomaDePagina(idioma);
  return (
    <PaginaPublica idioma={pagina}>
      {idioma !== legal && <p style={{ fontSize: 14, opacity: 0.75 }}>{NAV[pagina].soloEsFr}</p>}
      <ReactMarkdown remarkPlugins={[remarkGfm]}>{TEXTOS_LEGALES.terminos[legal]}</ReactMarkdown>
    </PaginaPublica>
  );
}
