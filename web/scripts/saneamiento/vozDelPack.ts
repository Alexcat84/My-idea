// Integración del mundo 11 (decisiones del fundador, 28 sep 2026): la guarda de voz
// de cliente (lib/vozDeCliente.ts: voz de libro y marcas de auditoría) sobre un pack
// ANTES de integrarlo. La prueba de vitest barre el grafo vivo; este script barre la
// carpeta del pack y sale con 1 si algo cae, para ver la guarda en rojo primero y en
// verde tras la limpieza.
//
// Uso (desde web/):  npx tsx scripts/saneamiento/vozDelPack.ts [../packs/primer_equipo/nodos]
import { readdirSync, readFileSync } from "node:fs";
import path from "node:path";
import { faltasDeNodo } from "../../lib/vozDeCliente";

const dir = path.resolve(process.argv[2] ?? path.join(__dirname, "..", "..", "..", "packs", "primer_equipo", "nodos"));
const nodos = readdirSync(dir).filter((f) => f.endsWith(".json"));
const faltas = nodos.flatMap((f) => faltasDeNodo(JSON.parse(readFileSync(path.join(dir, f), "utf8"))));
const porRegla: Record<string, Set<string>> = {};
const porCampo: Record<string, number> = {};
for (const f of faltas) {
  (porRegla[f.regla] ??= new Set()).add(f.node_id);
  const campo = f.campo.replace(/\[\d+\]$/, "");
  porCampo[campo] = (porCampo[campo] ?? 0) + 1;
}
const nodosConFalta = new Set(faltas.map((f) => f.node_id));
console.log(`voz de cliente sobre ${dir}: ${nodos.length} nodos, ${nodosConFalta.size} con alguna falta, ${faltas.length} faltas`);
for (const [r, s] of Object.entries(porRegla)) console.log(`  ${r}: ${s.size} nodos`);
for (const [c, n] of Object.entries(porCampo)) console.log(`  ${c}: ${n} faltas`);
for (const f of faltas.slice(0, 15)) console.log(`    ${f.node_id}.${f.campo} [${f.regla}] "${f.texto}"`);
process.exit(faltas.length ? 1 : 0);
