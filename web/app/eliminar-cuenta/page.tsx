/**
 * /eliminar-cuenta: instrucciones públicas para eliminar la cuenta (encargo del fundador del 6 oct 2026, punto 6).
 * Requisito de Google Play: se lee sin la app y sin iniciar sesión (proxy.ts, RUTAS_PUBLICAS). El borrado real vive
 * en el centro de cuenta (/cuenta, «Zona de peligro», /api/cuenta/eliminar). En el idioma de la persona, en los once
 * (I18N AL DÍA, 7 oct 2026: catálogo lib/i18n/mensajes/paginasAyuda.ts, con los rótulos reales del centro de cuenta).
 */
import type { Metadata } from "next";
import { PaginaPublica } from "@/app/ui/PaginaPublica";
import { idiomaDeCookies } from "@/lib/i18n/servidor";
import { eliminarCuenta } from "@/lib/legal/paginas";

export async function generateMetadata(): Promise<Metadata> {
  const m = eliminarCuenta(await idiomaDeCookies());
  return { title: `${m.titulo} | My Idea`, description: m.descripcion };
}

export default async function EliminarCuenta() {
  const idioma = await idiomaDeCookies();
  const m = eliminarCuenta(idioma);
  return (
    <PaginaPublica idioma={idioma}>
      <h1>{m.titulo}</h1>
      <p>{m.intro}</p>
      <h2>{m.comoTitulo}</h2>
      <ol>
        {m.pasos.map((p) => (
          <li key={p}>{p}</li>
        ))}
      </ol>
      <h2>{m.borraTitulo}</h2>
      <ul>
        {m.borra.map((p) => (
          <li key={p}>{p}</li>
        ))}
      </ul>
      <h2>{m.quedaTitulo}</h2>
      <p>{m.queda}</p>
      <h2>{m.sinAccesoTitulo}</h2>
      <p>{m.sinAcceso}</p>
      <h2>{m.sinCuentaTitulo}</h2>
      <p>{m.sinCuenta}</p>
    </PaginaPublica>
  );
}
