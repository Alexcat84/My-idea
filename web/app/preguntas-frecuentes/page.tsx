/**
 * /preguntas-frecuentes (encargo del fundador del 6 oct 2026, punto 6), incluida la eliminación de la cuenta. Se lee
 * sin cuenta. Los precios salen de precios.ts (lib/legal/paginas.ts), nunca escritos a mano.
 */
import type { Metadata } from "next";
import { PaginaPublica } from "@/app/ui/PaginaPublica";
import { idiomaDeCookies } from "@/lib/i18n/servidor";
import { idiomaDePagina, PREGUNTAS } from "@/lib/legal/paginas";

export async function generateMetadata(): Promise<Metadata> {
  const m = PREGUNTAS[idiomaDePagina(await idiomaDeCookies())];
  return { title: `${m.titulo} | My Idea`, description: m.descripcion };
}

export default async function PreguntasFrecuentes() {
  const idioma = idiomaDePagina(await idiomaDeCookies());
  const m = PREGUNTAS[idioma];
  return (
    <PaginaPublica idioma={idioma}>
      <h1>{m.titulo}</h1>
      <p>{m.intro}</p>
      {m.items.map((it) => (
        <details key={it.p} style={{ margin: "12px 0" }}>
          <summary style={{ cursor: "pointer", fontWeight: 600 }}>{it.p}</summary>
          <p>{it.r}</p>
        </details>
      ))}
    </PaginaPublica>
  );
}
