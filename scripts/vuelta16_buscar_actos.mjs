import fs from 'fs';
import { execSync } from 'child_process';

const names = JSON.parse(fs.readFileSync('scripts/_actos_viejos.json', 'utf-8'));

const files = execSync('git ls-files', { maxBuffer: 1024 * 1024 * 50 })
  .toString('utf-8').split('\n').filter(Boolean)
  .filter(f => f !== 'docs/plan/INVENTARIO.jsonl');

const BINARY_EXT = /\.(png|jpg|jpeg|gif|ico|pdf|woff2?|ttf|eot|zip|xlsx|docx|lock)$/i;
const textFiles = files.filter(f => !BINARY_EXT.test(f));

console.log('archivos rastreados (menos INVENTARIO.jsonl):', files.length);
console.log('archivos de texto a barrer:', textFiles.length);

// prepara un regex por nombre con limite de palabra
const nameSet = names.map(n => ({ n, re: new RegExp(`\\b${n.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}\\b`) }));

const hits = new Map(); // nombre -> [ {file, count} ]
for (const n of names) hits.set(n, []);

let filesRead = 0, filesSkipped = 0;
for (const f of textFiles) {
  let content;
  try {
    content = fs.readFileSync(f, 'utf-8');
  } catch (e) {
    filesSkipped++;
    continue;
  }
  filesRead++;
  for (const { n, re } of nameSet) {
    if (content.includes(n)) { // filtro rapido antes del regex
      const matches = content.match(new RegExp(`\\b${n.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}\\b`, 'g'));
      if (matches && matches.length) {
        hits.get(n).push({ file: f, count: matches.length });
      }
    }
  }
}

console.log('archivos leidos:', filesRead, 'saltados (no texto/error):', filesSkipped);

// clasifica sitios: base de datos (master_graph.json, INTRA_DOMINIO_VEREDICTOS.jsonl, RECOMPUTO_3388_COMPONENTES.jsonl)
// contra el resto (docs narrativos, OPERACIONES.jsonl, etc)
const BASE = new Set(['dataset/master_graph.json', 'docs/INTRA_DOMINIO_VEREDICTOS.jsonl', 'docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl']);

let citadoFueraDeInventario = 0;
let citadoSoloEnBase = 0;
let citadoEnNarrativa = 0;
const narrativos = [];

for (const n of names) {
  const list = hits.get(n);
  if (list.length === 0) continue;
  citadoFueraDeInventario++;
  const soloBase = list.every(h => BASE.has(h.file));
  if (soloBase) citadoSoloEnBase++;
  else {
    citadoEnNarrativa++;
    narrativos.push({ nombre: n, sitios: list.filter(h => !BASE.has(h.file)) });
  }
}

console.log('---RESUMEN---');
console.log('citados en algun archivo fuera de INVENTARIO.jsonl:', citadoFueraDeInventario, 'de', names.length);
console.log('de esos, SOLO en archivos base de catalogo (master_graph.json / VEREDICTOS / COMPONENTES):', citadoSoloEnBase);
console.log('de esos, citados TAMBIEN en documentos narrativos (plan, operaciones, actas, etc):', citadoEnNarrativa);
console.log('---NARRATIVOS, con sitio---');
for (const r of narrativos) {
  console.log(r.nombre, '=>', r.sitios.map(s => `${s.file}(${s.count})`).join(', '));
}

fs.writeFileSync('scripts/_actos_citas.json', JSON.stringify({ citadoFueraDeInventario, citadoSoloEnBase, citadoEnNarrativa, narrativos }, null, 1));
