/**
 * /terminos: los términos de uso, publicado desde docs/legal/ (encargo del fundador del 6 oct 2026, punto 6). Se lee sin cuenta y
 * sin iniciar sesión. En el idioma de la persona si su traducción está publicada (I18N AL DÍA, 7 oct 2026: los once
 * idiomas) y, si no, en español, sin aviso. La revisión profesional queda pendiente: el texto se afina en el .md y se
 * vuelve a sincronizar (scripts/sync_legal_web.py).
 */
import type { Metadata } from "next";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { PaginaPublica } from "@/app/ui/PaginaPublica";
import { idiomaDeCookies } from "@/lib/i18n/servidor";
import { TEXTOS_LEGALES } from "@/lib/legal/textos";
import { idiomaLegal, navPublica } from "@/lib/legal/paginas";

export async function generateMetadata(): Promise<Metadata> {
  return { title: `${navPublica(await idiomaDeCookies()).terminos} | My Idea` };
}

export default async function Pagina() {
  const idioma = await idiomaDeCookies();
  const legal = idiomaLegal(idioma, "terminos");
  return (
    <PaginaPublica idioma={idioma}>
      {/* lang: si cae al español, el lector de pantalla lo lee en español. */}
      <div lang={legal === idioma ? undefined : legal}>
        <ReactMarkdown remarkPlugins={[remarkGfm]}>{TEXTOS_LEGALES.terminos[legal]}</ReactMarkdown>
      </div>
    </PaginaPublica>
  );
}
