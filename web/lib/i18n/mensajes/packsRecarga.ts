/**
 * Los nombres visibles de las recargas de lib/precios.ts (PACKS) y para qué
 * alcanza cada una. SOLO texto: las cifras viven en precios.ts y solo ahí
 * (AGENTS.md). Las claves son el `clave` de cada pack.
 */
import type { PorIdioma } from "../config";

const es = {
  recarga: { nombre: "Recarga", alcanza: "un seguimiento o un mundo suelto" },
  basico: { nombre: "Básico", alcanza: "tu plan completo, con tus números incluidos" },
  premium: { nombre: "Premium", alcanza: "tu plan y tu primer seguimiento" },
  profesional: { nombre: "Profesional", alcanza: "el viaje entero de una idea" },
};

export const PACKS_RECARGA: PorIdioma<typeof es> = { es };
