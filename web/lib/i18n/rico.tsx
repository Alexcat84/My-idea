/**
 * Frases con partes marcadas (negritas, énfasis, enlaces, saltos de línea) SIN
 * partirlas en pedazos: el catálogo guarda la frase entera con etiquetas
 * propias ("Tu plan <b>ya está</b> listo", "primera línea<br/>segunda") y aquí
 * cada etiqueta se convierte en su elemento. Así quien traduce ve la oración
 * completa y puede mover la parte marcada donde la pida su idioma (F3).
 *
 * Etiquetas: `<nombre>…</nombre>` (envuelve texto) y `<nombre/>` (sola, como
 * un salto de línea). Sin anidar. Una etiqueta sin componente lanza (fallar
 * ruidoso): el auditor exige las mismas etiquetas en cada idioma.
 */
import { Fragment, type ReactNode } from "react";

export type ComponentesRicos = Record<string, (contenido: ReactNode) => ReactNode>;

const ETIQUETA = /<(\w+)>([\s\S]*?)<\/\1>|<(\w+)\/>/g;

export function rico(texto: string, componentes: ComponentesRicos = {}): ReactNode {
  const partes: ReactNode[] = [];
  let desde = 0;
  let k = 0;
  for (const m of texto.matchAll(ETIQUETA)) {
    if (m.index > desde) partes.push(texto.slice(desde, m.index));
    const nombre = m[1] ?? m[3];
    const componente = componentes[nombre] ?? (nombre === "br" ? () => <br /> : undefined);
    if (!componente) throw new Error(`i18n: la etiqueta <${nombre}> no tiene componente en "${texto}"`);
    partes.push(<Fragment key={k++}>{componente(m[2] ?? null)}</Fragment>);
    desde = m.index + m[0].length;
  }
  if (desde < texto.length) partes.push(texto.slice(desde));
  return partes.length === 1 ? partes[0] : <>{partes}</>;
}

/** Las etiquetas de una frase (para el auditor: deben ser las mismas en cada idioma). */
export function etiquetasDe(texto: string): string[] {
  return [...texto.matchAll(ETIQUETA)].map((m) => m[1] ?? m[3]).sort();
}
