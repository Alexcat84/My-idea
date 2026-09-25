/**
 * D3 (i18n F5): mantiene las etiquetas del riel de cada idioma
 * (lib/i18n/etiquetas/<idioma>.json), derivadas de `etiqueta_arbol` del grafo.
 * El grafo no se toca. Solo se traducen las que FALTAN: al cambiar el grafo,
 * se exporta la diferencia y nada más.
 *
 *   exportar <idioma> <salida.json> [--lote N]   las etiquetas en español que
 *                                                faltan en ese idioma, con el
 *                                                título del concepto de apoyo;
 *                                                con --lote, en archivos de N
 *   validar  <idioma> <entrada.json...>          cada id es un nodo vivo, nada
 *                                                vacío, sin rayas ni ¿¡, corta
 *   aplicar  <idioma> <entrada.json...>          valida y la suma al archivo
 *                                                del idioma (ordenado por id)
 *
 * Formato de exportación: { "<id>": { "etiqueta": "…", "titulo": "…" } }.
 * Formato de la traducción: { "<id>": "<etiqueta en el idioma>" }.
 * Uso (desde web/): npx tsx scripts/i18n/etiquetasRiel.ts exportar ko /tmp/ko.json --lote 400
 */
import { readFileSync, writeFileSync } from "node:fs";
import path from "node:path";
import { cargarGrafo } from "../../lib/engine/graph";
import { validarEtiquetaRiel } from "../../lib/i18n/etiquetasRielValidar";

const DIR = path.join(__dirname, "..", "..", "lib", "i18n", "etiquetas");
const IDIOMAS = ["en", "pt", "fr", "de", "it", "ja", "zh", "ko", "ar", "hi"];

function archivoDe(idioma: string): string {
  if (!IDIOMAS.includes(idioma)) throw new Error(`idioma desconocido: ${idioma}`);
  return path.join(DIR, `${idioma}.json`);
}

function leerJson<T>(ruta: string): T {
  return JSON.parse(readFileSync(ruta, "utf8")) as T;
}

function vivos(): Record<string, { etiqueta: string; titulo: string }> {
  const g = cargarGrafo();
  const fuera: Record<string, { etiqueta: string; titulo: string }> = {};
  for (const [id, n] of Object.entries(g)) {
    if (n.deprecado || !n.etiqueta_arbol) continue;
    fuera[id] = { etiqueta: n.etiqueta_arbol, titulo: n.titulo_concepto };
  }
  return fuera;
}

function exportar(idioma: string, salida: string, lote: number | null) {
  const ya = leerJson<Record<string, string>>(archivoDe(idioma));
  const faltan = Object.entries(vivos()).filter(([id]) => !ya[id]);
  const trozos = lote ? Array.from({ length: Math.ceil(faltan.length / lote) }, (_, i) => faltan.slice(i * lote, (i + 1) * lote)) : [faltan];
  trozos.forEach((trozo, i) => {
    const ruta = trozos.length > 1 ? salida.replace(/\.json$/, `_${String(i + 1).padStart(2, "0")}.json`) : salida;
    writeFileSync(ruta, JSON.stringify(Object.fromEntries(trozo), null, 1) + "\n");
    console.log(`${ruta}: ${trozo.length}`);
  });
  console.log(`faltan ${faltan.length} en ${idioma}`);
}

function leerTraducciones(rutas: string[]): Record<string, string> {
  const junta: Record<string, string> = {};
  for (const r of rutas) Object.assign(junta, leerJson<Record<string, string>>(r));
  return junta;
}

function validar(idioma: string, rutas: string[]): Record<string, string> {
  const vivosIds = vivos();
  const t = leerTraducciones(rutas);
  const errores: string[] = [];
  for (const [id, valor] of Object.entries(t)) {
    if (!vivosIds[id]) errores.push(`${id}: no es un nodo vivo`);
    const e = validarEtiquetaRiel(valor);
    if (e) errores.push(`${id}: ${e} («${valor}»)`);
  }
  if (errores.length) {
    console.error(errores.join("\n"));
    throw new Error(`${errores.length} problemas en ${idioma}`);
  }
  console.log(`${idioma}: ${Object.keys(t).length} etiquetas válidas`);
  return t;
}

function aplicar(idioma: string, rutas: string[]) {
  const t = validar(idioma, rutas);
  const ya = leerJson<Record<string, string>>(archivoDe(idioma));
  const junta = { ...ya, ...t };
  const ordenado = Object.fromEntries(Object.keys(junta).sort().map((k) => [k, junta[k].trim()]));
  writeFileSync(archivoDe(idioma), JSON.stringify(ordenado, null, 1) + "\n");
  console.log(`${idioma}: ${Object.keys(ordenado).length} en total`);
}

const [accion, idioma, ...resto] = process.argv.slice(2);
if (accion === "exportar") {
  const i = resto.indexOf("--lote");
  const lote = i >= 0 ? Number(resto[i + 1]) : null;
  exportar(idioma, resto[0], lote);
} else if (accion === "validar") {
  validar(idioma, resto);
} else if (accion === "aplicar") {
  aplicar(idioma, resto);
} else {
  console.error("uso: exportar <idioma> <salida.json> [--lote N] | validar <idioma> <json...> | aplicar <idioma> <json...>");
  process.exit(1);
}
