/**
 * El auditor de los catálogos (DISENO §3.1). El tipo PorIdioma ya obliga a que
 * cada idioma ACTIVO exista con las claves del español; esto cierra lo que el
 * tipo no ve:
 *   - un catálogo tiene exactamente los idiomas activos (ni más ni menos);
 *   - cada idioma tiene las mismas claves que el español, en todos los niveles;
 *   - cada traducción conserva los mismos {{marcadores}} y las mismas <etiquetas>;
 *   - ninguna cadena vacía;
 *   - las marcas que no se traducen ("My Idea") aparecen intactas donde el
 *     español las tiene.
 * Puro: lo corre auditor.test.ts sobre todos los archivos de `mensajes/`, así
 * que corre en la suite y en el guardián de commit.
 */
import { ACTIVE_LOCALES, LOCALE_BASE } from "./config";
import { etiquetasDe } from "./rico";

/** Glosario §6: lo que no se traduce en ningún idioma. */
export const MARCAS_INTACTAS = ["My Idea"] as const;

const marcadoresDe = (t: string) => [...t.matchAll(/\{\{(\w+)\}\}/g)].map((m) => m[1]).sort();
const iguales = (a: string[], b: string[]) => a.length === b.length && a.every((x, i) => x === b[i]);

function compararNodo(base: unknown, otro: unknown, ruta: string, idioma: string, fallas: string[]) {
  if (typeof base === "string") {
    if (typeof otro !== "string") return void fallas.push(`${ruta} [${idioma}]: se esperaba texto`);
    if (!otro.trim()) fallas.push(`${ruta} [${idioma}]: cadena vacía`);
    if (!iguales(marcadoresDe(base), marcadoresDe(otro)))
      fallas.push(`${ruta} [${idioma}]: marcadores distintos (${marcadoresDe(otro).join(",")} vs ${marcadoresDe(base).join(",")})`);
    if (!iguales(etiquetasDe(base), etiquetasDe(otro)))
      fallas.push(`${ruta} [${idioma}]: etiquetas distintas (${etiquetasDe(otro).join(",")} vs ${etiquetasDe(base).join(",")})`);
    for (const marca of MARCAS_INTACTAS)
      if (base.includes(marca) && !otro.includes(marca)) fallas.push(`${ruta} [${idioma}]: falta la marca "${marca}"`);
    return;
  }
  if (Array.isArray(base)) {
    if (!Array.isArray(otro) || otro.length !== base.length)
      return void fallas.push(`${ruta} [${idioma}]: se esperaba una lista de ${base.length}`);
    base.forEach((b, i) => compararNodo(b, otro[i], `${ruta}[${i}]`, idioma, fallas));
    return;
  }
  if (base && typeof base === "object") {
    if (!otro || typeof otro !== "object" || Array.isArray(otro))
      return void fallas.push(`${ruta} [${idioma}]: se esperaba un objeto`);
    const kb = Object.keys(base).sort();
    const ko = Object.keys(otro).sort();
    for (const k of kb) if (!ko.includes(k)) fallas.push(`${ruta}.${k} [${idioma}]: falta la clave`);
    for (const k of ko) if (!kb.includes(k)) fallas.push(`${ruta}.${k} [${idioma}]: clave que el español no tiene`);
    for (const k of kb) if (ko.includes(k)) compararNodo((base as Record<string, unknown>)[k], (otro as Record<string, unknown>)[k], `${ruta}.${k}`, idioma, fallas);
    return;
  }
  fallas.push(`${ruta} [${idioma}]: tipo no admitido en un catálogo (${typeof base})`);
}

/** Compara una traducción suelta contra su español (la usa la herramienta de
 * traducción de F3 antes de integrar un idioma que aún no está activo). */
export function compararTraduccion(base: unknown, otro: unknown, ruta: string, idioma: string): string[] {
  const fallas: string[] = [];
  compararNodo(base, otro, ruta, idioma, fallas);
  return fallas;
}

/** Audita un catálogo (`PorIdioma<T>`). Devuelve la lista de fallas (vacía = bien). */
export function auditarCatalogo(nombre: string, catalogo: Record<string, unknown>): string[] {
  const fallas: string[] = [];
  const idiomas = Object.keys(catalogo).sort();
  const activos = [...ACTIVE_LOCALES].sort();
  if (!iguales(idiomas, activos)) fallas.push(`${nombre}: idiomas ${idiomas.join(",")}; se esperaban los activos ${activos.join(",")}`);
  const base = catalogo[LOCALE_BASE];
  if (base === undefined) return [...fallas, `${nombre}: falta el idioma base (${LOCALE_BASE})`];
  // El base contra sí mismo: cadenas vacías y tipos no admitidos.
  for (const idioma of idiomas) compararNodo(base, catalogo[idioma], nombre, idioma, fallas);
  return fallas;
}

/** ¿Este export es un catálogo? (un objeto cuyas claves son todas idiomas activos o de la marca). */
export function pareceCatalogo(x: unknown): x is Record<string, unknown> {
  return !!x && typeof x === "object" && !Array.isArray(x) && LOCALE_BASE in x;
}
