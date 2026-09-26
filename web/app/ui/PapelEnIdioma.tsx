"use client";

/**
 * PapelEnIdioma — i18n F6 (D2): el papel de un documento en el idioma del
 * PROYECTO, dentro de una pantalla en el idioma de la INTERFAZ.
 *
 * La regla (lib/i18n/idiomaDocumento.ts): el cuerpo del documento, con sus
 * rótulos, fechas y encabezados, sigue el idioma del proyecto; lo que lo
 * rodea en la pantalla (botones, navegación, el panel de Descargas), la
 * interfaz. Los componentes de papel eligen sus textos con useIdioma(): aquí
 * se les da el idioma del documento, y los botones que viven DENTRO de un
 * documento (el "Empezar con esto" del plan) piden el de la interfaz con
 * useIdiomaInterfaz().
 *
 * También pone `lang` y `dir`: un proyecto en árabe se imprime de derecha a
 * izquierda aunque la interfaz sea español, y la partición de palabras sigue
 * el idioma del texto. El envoltorio es `display: contents` (no altera el
 * diseño) y, si el idioma es el mismo que el de la interfaz o no se sabe, no
 * hay envoltorio: el marcado queda idéntico al de siempre.
 *
 * Y la TIPOGRAFÍA (F4): la Noto de una escritura (ja, zh, ko, ar, hi) se carga
 * solo para su idioma de interfaz, con la clase de next/font en <html>. Un
 * papel en coreano dentro de una interfaz en español necesita la suya: el
 * layout le pasa aquí las clases de cada escritura (TipografiasDeEscritura,
 * solo nombres de clase) y el envoltorio pone la del idioma del documento con
 * `papel-escritura` (globals.css), que vuelve a declarar la familia del cuerpo
 * para que tome la variable nueva. Las fuentes van sin precarga: el navegador
 * baja esa Noto solo cuando un papel en ese idioma se pinta, nadie más.
 */
import { createContext, useContext, type ReactNode } from "react";
import { htmlDir, htmlLang, type ActiveLocale } from "@/lib/i18n/config";
import { IdiomaProvider, useIdioma } from "@/lib/i18n/IdiomaProvider";

const ContextoInterfaz = createContext<ActiveLocale | null>(null);
const ContextoEscrituras = createContext<Record<string, string>>({});

/** Las clases de next/font de cada escritura, que declara el layout. */
export function TipografiasDeEscritura({ clases, children }: { clases: Record<string, string>; children: ReactNode }) {
  return <ContextoEscrituras.Provider value={clases}>{children}</ContextoEscrituras.Provider>;
}

export function PapelEnIdioma({ idioma, children }: { idioma: ActiveLocale | null | undefined; children: ReactNode }) {
  const interfaz = useIdioma();
  const escrituras = useContext(ContextoEscrituras);
  if (!idioma || idioma === interfaz) return <>{children}</>;
  const escritura = escrituras[idioma];
  return (
    <ContextoInterfaz.Provider value={interfaz}>
      <IdiomaProvider idioma={idioma}>
        <div lang={htmlLang(idioma)} dir={htmlDir(idioma)} className={escritura ? `contents ${escritura} papel-escritura` : "contents"}>
          {children}
        </div>
      </IdiomaProvider>
    </ContextoInterfaz.Provider>
  );
}

/** El idioma de la interfaz, también dentro de un papel en otro idioma. */
export function useIdiomaInterfaz(): ActiveLocale {
  const interfaz = useContext(ContextoInterfaz);
  const actual = useIdioma();
  return interfaz ?? actual;
}
