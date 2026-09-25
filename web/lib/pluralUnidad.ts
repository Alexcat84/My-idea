/**
 * El plural de la unidad de venta ("vela" -> "velas") que escriben Tus Números
 * y Corregir cifras. Vivía en app/ui/TusNumeros.tsx; sale a lib/ para que
 * Corregir cifras use la misma regla (tanda de errores del español: "{{u}}s"
 * daba "unidads").
 */
import { LOCALE_BASE, type Locale } from "./i18n/config";

/** Plural de la unidad de venta en el idioma de la frase. Español (AUD-09 H12):
 * vocal + s, z -> ces, consonante + es; en una unidad de varias palabras ("kit de velas")
 * se pluraliza la primera. Tanda de errores (24 sep 2026): los extranjerismos en
 * b, c, f, g, k, p, q, t, v, w suman -s ("kits", no "kites") y la aguda con
 * tilde en n/s la pierde ("camiones", no "camiónes"). i18n F3: inglés, portugués, francés e
 * italiano con su regla regular; alemán, japonés, chino, coreano, árabe e hindi
 * dejan la unidad tal cual (sin plural regular: mejor sin plural que inventado). */
export function pluralDe(unidad: string, idioma: Locale = LOCALE_BASE): string {
  const palabras = unidad.trim().split(" ");
  if (!palabras[0]) return unidad;
  const regla = REGLA_PLURAL[idioma];
  if (!regla) return unidad;
  // En inglés el núcleo es la última palabra ("candle kit"), salvo con "of"
  // ("cup of coffee"); en las lenguas romances, la primera ("caja de velas").
  const i = idioma === "en" && !palabras.includes("of") ? palabras.length - 1 : 0;
  palabras[i] = regla(palabras[i]);
  return palabras.join(" ");
}

const REGLA_PLURAL: Record<Locale, ((p: string) => string) | null> = {
  es: (p) => {
    // Aguda con tilde en n/s: la tilde se va al sumar sílaba (camión -> camiones).
    const aguda = p.match(/^(.*)([áéíóúÁÉÍÓÚ])([ns])$/);
    if (aguda) return `${aguda[1]}${aguda[2].normalize("NFD")[0]}${aguda[3]}es`;
    if (/[aeiouáéíóú]$/i.test(p)) return `${p}s`;
    if (/z$/i.test(p)) return `${p.slice(0, -1)}ces`;
    if (/s$/i.test(p)) return p;
    // Consonante final ajena al español (kit, club, chip): -s, no -es (RAE).
    if (/[bcfgkpqtvw]$/i.test(p)) return `${p}s`;
    return `${p}es`;
  },
  en: (p) =>
    /(ss|x|z|ch|sh)$/i.test(p) ? `${p}es` : /[^aeiou]y$/i.test(p) ? `${p.slice(0, -1)}ies` : /s$/i.test(p) ? p : `${p}s`,
  pt: (p) =>
    /ão$/i.test(p)
      ? `${p.slice(0, -2)}ões`
      : /m$/i.test(p)
        ? `${p.slice(0, -1)}ns`
        : /[aeou]l$/i.test(p)
          ? `${p.slice(0, -1)}is`
          : /[rz]$/i.test(p)
            ? `${p}es`
            : /s$/i.test(p)
              ? p
              : `${p}s`,
  fr: (p) => (/[sxz]$/i.test(p) ? p : /(eau|au|eu)$/i.test(p) ? `${p}x` : /al$/i.test(p) ? `${p.slice(0, -2)}aux` : `${p}s`),
  it: (p) =>
    /[cg]a$/i.test(p)
      ? `${p.slice(0, -1)}he`
      : /a$/i.test(p)
        ? `${p.slice(0, -1)}e`
        : /[oe]$/i.test(p)
          ? `${p.slice(0, -1)}i`
          : p,
  de: null,
  ja: null,
  zh: null,
  ko: null,
  ar: null,
  hi: null,
};
