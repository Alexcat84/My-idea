/**
 * Las GUARDAS DE CONTENIDO como DATOS con versión (encargo del fundador, 28 sep 2026, auditoría final punto 4): la
 * forja las copia para limpiar un pack ANTES de integrarlo con la misma vara que el catálogo.
 *
 * Una sola fuente: el fichero `dataset/metadata/guardas_contenido.json` se GENERA desde aquí
 * (`npx tsx scripts/exportar_guardas.ts`), y `guardasContenido.test.ts` exige que el fichero y el código coincidan. Si
 * cambia una regla, se sube VERSION_GUARDAS y se regenera el fichero; la prueba no deja que diverjan.
 *
 * Lo que va dentro:
 *  - `voz`: las reglas de i18n/frasesProhibidas.ts (id, origen, qué prohíbe, patrones por idioma en sintaxis
 *    ECMAScript con sus flags, y por qué un idioma no tiene equivalente);
 *  - `campos_de_cliente` y `adjudicados`: qué campos de un nodo se barren y las excepciones adjudicadas
 *    (lib/vozDeCliente.ts);
 *  - `glosario`: la tabla de decisiones del glosario (docs/saneamiento/resultados/M11/glosario/DECISIONES.md), que la
 *    auditoría final aplica a todo el catálogo;
 *  - `referencias`: lo interno que la forja lee de su propio fichero, sin copiarlo aquí (los títulos canónicos de los
 *    libros, la vara de fases).
 */
import { readFileSync } from "node:fs";
import path from "node:path";
import { REGLAS_VOZ } from "./i18n/frasesProhibidas";
import { ADJUDICADOS, CAMPOS_DE_CLIENTE } from "./vozDeCliente";

export const VERSION_GUARDAS = "1.0.0";
export const FECHA_GUARDAS = "2026-09-28";

export interface FilaGlosario {
  aparece: string;
  queda: string;
  porque: string;
}

/** Las filas de la tabla del glosario, tal como están en el markdown (sin la cabecera). */
export function leerGlosario(raiz: string): FilaGlosario[] {
  const md = readFileSync(path.join(raiz, "docs", "saneamiento", "resultados", "M11", "glosario", "DECISIONES.md"), "utf8");
  const filas: FilaGlosario[] = [];
  for (const linea of md.split(/\r?\n/)) {
    if (!linea.startsWith("|") || /^\|\s*-/.test(linea) || /^\|\s*Aparece\s*\|/.test(linea)) continue;
    const celdas = linea.split("|").slice(1, -1).map((c) => c.trim());
    if (celdas.length === 3) filas.push({ aparece: celdas[0], queda: celdas[1], porque: celdas[2] });
  }
  return filas;
}

export function guardasContenido(raiz: string) {
  return {
    version: VERSION_GUARDAS,
    fecha: FECHA_GUARDAS,
    nota:
      "Generado desde web/lib/guardasContenido.ts (npx tsx scripts/exportar_guardas.ts desde web/). No se edita a mano: " +
      "web/lib/guardasContenido.test.ts exige que coincida con el codigo. Patrones en sintaxis ECMAScript (en Python, " +
      "el modulo regex, no re, por \\p{L} y los lookbehind).",
    voz: REGLAS_VOZ.map((r) => ({
      id: r.id,
      origen: r.origen,
      que: r.que,
      porIdioma: Object.fromEntries(
        Object.entries(r.porIdioma).map(([idioma, patrones]) => [idioma, patrones.map((p) => ({ patron: p.source, flags: p.flags }))])
      ),
      sinEquivalente: r.sinEquivalente,
    })),
    campos_de_cliente: [...CAMPOS_DE_CLIENTE],
    adjudicados: ADJUDICADOS,
    glosario: leerGlosario(raiz),
    referencias: {
      titulos_canonicos_de_los_libros: "dataset/metadata/fuentes_canonicas.json",
      vara_de_fases: "docs/puente_forja/paso4/vara_fases.md",
      reglas_de_la_casa: "docs/REGLAS_DE_LA_CASA.md",
    },
  };
}
