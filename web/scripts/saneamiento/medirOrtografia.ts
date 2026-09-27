/**
 * Nivel 1 del saneamiento, criterio 16 (decision del fundador del 27 sep 2026): mide, con el detector de acentos de la
 * casa (lib/detectorAcentos.ts), las faltas de tilde en los textos del dataset que ve el cliente: la etiqueta del riel,
 * las preguntas en cache, y los pasos y el entregable (el plan sin IA los imprime tal cual). Solo lee.
 *
 *   npx tsx scripts/saneamiento/medirOrtografia.ts [salida.json]
 */
import { readdirSync, readFileSync, writeFileSync } from "node:fs";
import path from "node:path";
import { detectarFaltaDeAcentos } from "../../lib/detectorAcentos";

const RAIZ = path.resolve(__dirname, "../../..");
const hallazgos: Array<{ donde: string; faltas: string[]; texto: string }> = [];
const por: Record<string, number> = {};
function mirar(donde: string, tipo: string, texto: unknown): void {
  if (typeof texto !== "string" || !texto) return;
  const f = detectarFaltaDeAcentos(texto);
  if (f.length) {
    hallazgos.push({ donde, faltas: f, texto });
    por[tipo] = (por[tipo] ?? 0) + 1;
  }
}
for (const f of readdirSync(path.join(RAIZ, "dataset/nodos"))) {
  const n = JSON.parse(readFileSync(path.join(RAIZ, "dataset/nodos", f), "utf-8"));
  if (n.deprecado) continue;
  mirar(`${n.node_id}.etiqueta_arbol`, "etiqueta", n.etiqueta_arbol);
  mirar(`${n.node_id}.entregable_esperado`, "entregable", n.entregable_esperado);
  (n.pasos_accionables ?? []).forEach((p: string, i: number) => mirar(`${n.node_id}.pasos_accionables[${i}]`, "paso", p));
}
const cache = JSON.parse(readFileSync(path.join(RAIZ, "engine/preguntas_cache.json"), "utf-8"));
for (const [k, v] of Object.entries(cache as Record<string, { pregunta?: string }>)) mirar(`preguntas_cache:${k}`, "pregunta", v?.pregunta);
console.log("textos con falta de tilde:", hallazgos.length, por);
if (process.argv[2]) writeFileSync(process.argv[2], JSON.stringify(hallazgos, null, 1));
