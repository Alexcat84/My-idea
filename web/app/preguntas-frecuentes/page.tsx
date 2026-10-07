/**
 * /preguntas-frecuentes (encargo del fundador del 6 oct 2026, punto 6), incluida la eliminación de la cuenta. Se lee
 * sin cuenta. En el idioma de la persona, en los once (I18N AL DÍA, 7 oct 2026: catálogo
 * lib/i18n/mensajes/paginasAyuda.ts). Los precios salen de precios.ts (lib/legal/paginas.ts), nunca escritos a mano.
 */
import type { Metadata } from "next";
import { PaginaPublica } from "@/app/ui/PaginaPublica";
import { idiomaDeCookies } from "@/lib/i18n/servidor";
import { preguntasFrecuentes } from "@/lib/legal/paginas";

export async function generateMetadata(): Promise<Metadata> {
  const m = preguntasFrecuentes(await idiomaDeCookies());
  return { title: `${m.titulo} | My Idea`, description: m.descripcion };
}

export default async function PreguntasFrecuentes() {
  const idioma = await idiomaDeCookies();
  const m = preguntasFrecuentes(idioma);
  return (
    <PaginaPublica idioma={idioma}>
      <h1>{m.titulo}</h1>
      <p>{m.intro}</p>
      {m.items.map((it) => (
        <details key={it.p} style={{ margin: "12px 0" }}>
          {/* La pregunta en azul y la respuesta en blanco (fundador, 8 oct 2026). */}
          <summary className="text-accent" style={{ cursor: "pointer", fontWeight: 600 }}>{it.p}</summary>
          <p className="text-ink">{it.r}</p>
        </details>
      ))}
    </PaginaPublica>
  );
}
