/**
 * chequeo_acentos_canon.ts — Fase Canon 2.0: la vara se audita con el mismo
 * rigor que la app. Corre `detectarFaltaDeAcentos` sobre el COPY VISIBLE de los
 * HTML del canon (fuera de <style>/<script>/comentarios y de las etiquetas) y
 * cuenta las tildes. Es un PASO OBLIGATORIO de toda adopción de canon: si Design
 * entrega un pase de acentos incompleto, la vara no debe nacer violando su
 * propia ley de voz (regla del fundador, jul 2026 — esta vez cazó 13 residuales
 * que el "acentos verificados" del auditor dejó pasar).
 *
 * Uso: npx tsx scripts/chequeo_acentos_canon.ts [ruta-a-carpeta-de-canon]
 *   sin argumento, audita docs/diseno-canon (el canon adoptado).
 * Sale con código 1 si encuentra faltas en el copy visible.
 */
import fs from "node:fs";
import path from "node:path";
import { detectarFaltaDeAcentos } from "../lib/detectorAcentos";
import { ROOT } from "./_shared/http";

const DIR = process.argv[2] ?? path.join(ROOT, "docs", "diseno-canon");

/** Copy visible: sin <style>/<script>/comentarios ni etiquetas. Los valores de
 * atributos (data-screen-label, class) desaparecen con su etiqueta. Los
 * comentarios del diseñador NO son texto de pantalla y se excluyen. */
function copyVisible(html: string): string {
  return html
    .replace(/<!--[\s\S]*?-->/g, " ")
    .replace(/<style[\s\S]*?<\/style>/gi, " ")
    .replace(/<script[\s\S]*?<\/script>/gi, " ")
    .replace(/<[^>]+>/g, " ")
    .replace(/&[a-z]+;/gi, " ")
    .replace(/&#\d+;/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

const TILDES = /[áéíóúñüÁÉÍÓÚÑÜ]/g;
const files = fs.readdirSync(DIR).filter((f) => f.endsWith(".html")).sort();

let totalTildes = 0;
const fallas: Array<{ archivo: string; token: string; contexto: string }> = [];
for (const f of files) {
  const copy = copyVisible(fs.readFileSync(path.join(DIR, f), "utf-8"));
  totalTildes += (copy.match(TILDES) ?? []).length;
  for (const tok of detectarFaltaDeAcentos(copy)) {
    const i = copy.toLowerCase().indexOf(tok);
    fallas.push({ archivo: f, token: tok, contexto: copy.slice(Math.max(0, i - 35), i + tok.length + 35) });
  }
}

console.log(`canon: ${DIR}`);
console.log(`HTML auditados: ${files.length} · tildes en copy visible: ${totalTildes}\n`);
if (fallas.length === 0) {
  console.log("LIMPIO: el copy visible del canon respeta su ley de voz (cero faltas de acento).");
  process.exit(0);
}
console.log(`FALTAS DE ACENTO EN COPY VISIBLE: ${fallas.length}`);
for (const h of fallas) console.log(`  ${h.archivo} [${h.token}]  …${h.contexto}…`);
process.exit(1);
