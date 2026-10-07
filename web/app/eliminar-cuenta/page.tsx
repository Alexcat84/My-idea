/**
 * /eliminar-cuenta: instrucciones públicas para eliminar la cuenta (encargo del fundador del 6 oct 2026, punto 6).
 * Requisito de Google Play: se lee sin la app y sin iniciar sesión (proxy.ts, RUTAS_PUBLICAS). El borrado real vive
 * en el centro de cuenta (/cuenta, «Zona de peligro», /api/cuenta/eliminar).
 */
import type { Metadata } from "next";
import { PaginaPublica } from "@/app/ui/PaginaPublica";
import { idiomaDeCookies } from "@/lib/i18n/servidor";
import { ELIMINAR_CUENTA, idiomaDePagina } from "@/lib/legal/paginas";

export async function generateMetadata(): Promise<Metadata> {
  const m = ELIMINAR_CUENTA[idiomaDePagina(await idiomaDeCookies())];
  return { title: `${m.titulo} | My Idea`, description: m.descripcion };
}

export default async function EliminarCuenta() {
  const idioma = idiomaDePagina(await idiomaDeCookies());
  const m = ELIMINAR_CUENTA[idioma];
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
