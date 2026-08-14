import fs from 'fs';
import { execFileSync } from 'child_process';

const names = JSON.parse(fs.readFileSync('scripts/_actos_viejos.json', 'utf-8'));

// alcance: SOLO la capa narrativa de planeacion (docs/plan y docs/loop), que es donde
// tendria sentido citar un acto de INVENTARIO.jsonl como objeto que sigue existiendo.
// fuera de alcance a proposito: dataset/, packs/, engine/, web/ (catalogo base, cada id
// vive ahi porque ES un nodo real, no porque cite al acto) y los jsonl mecanicos de
// pares/veredictos/componentes (listan miembros, no citan un nombre de acto).
const allPlan = execFileSync('git', ['ls-files', 'docs/plan', 'docs/loop', 'docs/BANCO_DE_TEXTOS.md'])
  .toString('utf-8').split('\n').filter(Boolean);

const EXCLUIR = new Set([
  'docs/plan/INVENTARIO.jsonl',
  'docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl',
  'docs/plan/ARISTAS_DUPLICADAS.jsonl',
  'docs/plan/COSECHA_RAZONES_D.jsonl',
  'docs/plan/DIFERENCIA_CONTRA_COLA.jsonl',
  'docs/plan/PASO_NODO_CALIBRADO.jsonl',
]);

const scope = allPlan.filter(f => !EXCLUIR.has(f));
console.log('archivos en el alcance narrativo:', scope.length);

const contents = new Map();
for (const f of scope) {
  try { contents.set(f, fs.readFileSync(f, 'utf-8')); } catch (e) { /* skip */ }
}

const hits = new Map();
for (const n of names) hits.set(n, []);

for (const [f, content] of contents) {
  for (const n of names) {
    if (content.includes(n)) {
      const re = new RegExp(`\\b${n.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}\\b`, 'g');
      const m = content.match(re);
      if (m && m.length) hits.get(n).push({ file: f, count: m.length });
    }
  }
}

let citados = 0;
const detalle = [];
for (const n of names) {
  const list = hits.get(n);
  if (list.length) { citados++; detalle.push({ nombre: n, sitios: list }); }
}

console.log('citados en la capa narrativa (docs/plan + docs/loop + BANCO_DE_TEXTOS.md), fuera de INVENTARIO.jsonl:', citados, 'de', names.length);
for (const d of detalle) {
  console.log(d.nombre, '=>', d.sitios.map(s => `${s.file}(${s.count})`).join(', '));
}

fs.writeFileSync('scripts/_actos_citas_narrativa.json', JSON.stringify({ citados, detalle }, null, 1));
