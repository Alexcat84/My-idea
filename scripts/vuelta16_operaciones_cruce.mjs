import fs from 'fs';
import { execFileSync } from 'child_process';

const oldActos = fs.readFileSync('docs/plan/INVENTARIO.jsonl', 'utf-8').split('\n').filter(Boolean).map(l => JSON.parse(l)).filter(d => d.tipo === 'acto');
const ops = fs.readFileSync('docs/plan/OPERACIONES.jsonl', 'utf-8').split('\n').filter(Boolean).map(l => JSON.parse(l));
const comps = fs.readFileSync('docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl', 'utf-8').split('\n').filter(Boolean).map(l => JSON.parse(l));

// backlog OP-L-03 al corte 3.388, calcado del metodo de scripts/loop/backlog_l03_vuelta14.py
const NOMINAS_OP_L_02 = [
  ["customer_validation_sales_roadmap","estrategia_de_ventas","hoja_de_ruta_de_ventas","refinar_sales_roadmap","sales_roadmap","sales_roadmap_vs_sales_force"],
  ["clasificacion_mercados_cadena_suministro","cuatro_capacidades_mercado","cuatro_categorias_desempeno_cadena_suministro","estrategia_cuatro_capacidades_mercado","marco_analisis_mercado_cadena_suministro","modelo_cuadrantes_mercado"],
  ["alineacion_etica_ia_negocio","human_in_the_loop_ia","mitigar_falling_asleep_wheel","principio_humano_en_el_loop","riesgo_sobredependencia_ia"],
  ["construccion_de_valor_percibido","ecuacion_de_valor","ecuacion_de_valor_cliente","ecuacion_de_valor_venta","prevencion_objeciones_vs_manejo"],
  ["channels_hypothesis_physical","channels_hypothesis_web_mobile","hipotesis_de_canales","seleccion_canal_distribucion","seleccion_canal_fisico"],
  ["formalizar_junta_asesora","formalize_advisory_board","identificar_consejo_asesores","identificar_junta_asesores"],
];
const excluirL02 = new Set(NOMINAS_OP_L_02.flat());
const destejidos = ops.filter(o => o.tipo === 'DESTEJIDO');

function backlogL03(comps) {
  const abiertos = comps.filter(c => c.estado === 'ABIERTO' && c.tamano >= 3 && c.tamano <= 6);
  const resto = abiertos.filter(c => !c.miembros.some(m => excluirL02.has(m)));
  const backlog = resto.filter(c => !destejidos.some(o => c.miembros.some(m => o.nodos.includes(m))));
  return new Set(backlog.map(c => c.miembros.join('|')));
}
const backlogKeys = backlogL03(comps);

function operacionesDe(miembros, estadoComp) {
  const set = new Set();
  // overlap con cualquiera de las 69 operaciones que tengan nodos poblados
  for (const o of ops) {
    if (o.nodos && o.nodos.length && miembros.some(m => o.nodos.includes(m))) set.add(o.id_op);
  }
  // clase por estado
  set.add(estadoComp === 'CERRADO' ? 'OP-U-01' : 'OP-U-02');
  // backlog L-03
  if (estadoComp === 'ABIERTO' && backlogKeys.has(miembros.join('|'))) set.add('OP-L-03');
  return [...set].sort();
}

// VERIFICACION: reproducir el operaciones[] de los 221 viejos con este metodo
let iguales = 0, distintos = 0;
const difs = [];
for (const a of oldActos) {
  const comp = comps.find(c => a.miembros.every(m => c.miembros.includes(m)));
  const estadoComp = comp.estado;
  const miembros = a.miembros; // usar la nomina VIEJA para probar contra el operaciones VIEJO
  const calc = operacionesDe(miembros, estadoComp);
  const declarado = [...a.operaciones].sort();
  if (JSON.stringify(calc) === JSON.stringify(declarado)) iguales++;
  else { distintos++; difs.push({ nombre: a.nombre, declarado, calc }); }
}
console.log('reproduccion sobre los 221 viejos (con su propia nomina vieja): iguales', iguales, 'distintos', distintos);
for (const d of difs.slice(0, 40)) {
  console.log(d.nombre, '| declarado:', d.declarado, '| calculado:', d.calc);
}
console.log('...', difs.length, 'diferencias totales');
