/**
 * El selector de idioma manual y opcional (decisión del fundador, 25 sep 2026)
 * en las pantallas sin cabecera de esta sección: fijo arriba a la derecha. El
 * idioma lo pone solo la cookie o el navegador; esto es para cambiarlo a mano.
 */
import { SelectorIdioma } from "@/app/ui/SelectorIdioma";

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <>
      <div className="fixed right-4 top-4 z-40">
        <SelectorIdioma compacto />
      </div>
      {children}
    </>
  );
}
