"use client";

/**
 * El idioma de la interfaz en los componentes del cliente. El layout lo lee de
 * la cookie en el servidor y lo pone aquí; los componentes lo piden con
 * useIdioma() y eligen sus textos con elegir(CATALOGO, idioma). Sin proveedor
 * (una prueba que monta un componente suelto), el idioma base.
 */
import { createContext, useContext, type ReactNode } from "react";
import { LOCALE_BASE, type ActiveLocale } from "./config";

const ContextoIdioma = createContext<ActiveLocale>(LOCALE_BASE);

export function IdiomaProvider({ idioma, children }: { idioma: ActiveLocale; children: ReactNode }) {
  return <ContextoIdioma.Provider value={idioma}>{children}</ContextoIdioma.Provider>;
}

export function useIdioma(): ActiveLocale {
  return useContext(ContextoIdioma);
}
