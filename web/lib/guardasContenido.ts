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
 *  - `campos_de_cliente`, `reglas_voz_de_nodo` (desde la 1.1.0) y `adjudicados`: qué campos de un nodo se barren, con
 *    qué reglas de voz, y las excepciones adjudicadas (lib/vozDeCliente.ts);
 *  - `glosario`: la tabla de decisiones del glosario (docs/saneamiento/resultados/M11/glosario/DECISIONES.md), que la
 *    auditoría final aplica a todo el catálogo;
 *  - `procedencia` (desde la 1.1.0, 7 oct 2026, PROXIMOS_PASOS §6 punto 3): las pautas de lib/pautasProcedencia.ts
 *    (prefijo y atribución genérica en los once idiomas, método con persona, formas de nombre propio), cada una con
 *    su origen, qué barre, dónde se cumple en el catálogo y sus fixtures `caza` y `no_caza`;
 *  - `referencias`: lo interno que la forja lee de su propio fichero, sin copiarlo aquí (los títulos canónicos de los
 *    libros, la vara de fases).
 */
import { readFileSync } from "node:fs";
import path from "node:path";
import { REGLAS_VOZ } from "./i18n/frasesProhibidas";
import { ADJUDICADOS, CAMPOS_DE_CLIENTE, REGLAS_VOZ_DE_NODO } from "./vozDeCliente";
import { PAUTAS_PROCEDENCIA } from "./pautasProcedencia";

// 1.0.0 (28 sep 2026): voz, campos de cliente, adjudicados y glosario.
// 1.1.0 (7 oct 2026): las pautas de procedencia (PROXIMOS_PASOS §6, punto 3) y qué reglas de voz van a los nodos.
export const VERSION_GUARDAS = "1.1.0";
export const FECHA_GUARDAS = "2026-10-07";

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
      "el modulo regex, no re, por \\p{L} y los lookbehind). Ojo con \\b: en JS solo ve ASCII y en Python ve Unicode; " +
      "las pautas de procedencia se escribieron y se prueban con el de su origen (prefijo, atribucion y persona en JS; " +
      "nombre propio en Python), y cada pauta trae sus fixtures caza y no_caza para comprobar el motor que las use. " +
      "En procedencia, los exentos se quitan del texto antes de buscar, y no_aplica_en dice en que campos no se aplica " +
      "un patron.",
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
    reglas_voz_de_nodo: [...REGLAS_VOZ_DE_NODO],
    adjudicados: ADJUDICADOS,
    glosario: leerGlosario(raiz),
    procedencia: PAUTAS_PROCEDENCIA,
    referencias: {
      titulos_canonicos_de_los_libros: "dataset/metadata/fuentes_canonicas.json",
      vara_de_fases: "docs/puente_forja/paso4/vara_fases.md",
      reglas_de_la_casa: "docs/REGLAS_DE_LA_CASA.md",
    },
  };
}
