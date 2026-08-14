import fs from 'fs';

const oldActos = fs.readFileSync('docs/plan/INVENTARIO.jsonl', 'utf-8').split('\n').filter(Boolean).map(l => JSON.parse(l)).filter(d => d.tipo === 'acto');
const ops = fs.readFileSync('docs/plan/OPERACIONES.jsonl', 'utf-8').split('\n').filter(Boolean).map(l => JSON.parse(l));
const comps = fs.readFileSync('docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl', 'utf-8').split('\n').filter(Boolean).map(l => JSON.parse(l));

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
const abiertos36 = comps.filter(c => c.estado === 'ABIERTO' && c.tamano >= 3 && c.tamano <= 6);
const resto36 = abiertos36.filter(c => !c.miembros.some(m => excluirL02.has(m)));
const backlogL03 = new Set(resto36.filter(c => !destejidos.some(o => c.miembros.some(m => o.nodos.includes(m)))).map(c => c.miembros.join('|')));

function operacionesDe(miembros, estado) {
  const set = new Set();
  for (const o of ops) {
    if (o.nodos && o.nodos.length && miembros.some(m => o.nodos.includes(m))) set.add(o.id_op);
  }
  set.add(estado === 'CERRADO' ? 'OP-U-01' : 'OP-U-02');
  if (estado === 'ABIERTO' && backlogL03.has(miembros.join('|'))) set.add('OP-L-03');
  return [...set].sort();
}

// mapa viejo -> sucesor (para saber a cual de los 335 le viaja la nota escrita a mano)
let sucesorDeViejo = new Map();
for (const a of oldActos) {
  const idx = comps.findIndex(c => a.miembros.every(m => c.miembros.includes(m)));
  sucesorDeViejo.set(idx, a);
}

const HANDWRITTEN_NOTA = "tamano 4, y ES EL PRIMER ACTO DEL PLAN CON SU DECISION ESCRITA. No se funde en uno: se funde en DOS y se enlazan. Sobrevive identificar_consejo_asesores (fusion 367, por el paso 6 que entrega el testigo) y sobrevive formalizar_junta_asesora (fusion 328, por DESEMPATE POR CABLEADO con el contenido empatado). El par 1190 SE LIBERA sin cirugia: el superviviente conserva el paso 6, asi que formalizar sigue siendo hijo y la D se confirma. MEDIDO: la cuerda que el grafo ya tenia es la de VUELTA (formalizar hacia identificar); la de ida hay que anadirla.";

const nuevos = [];
let conAntecesor = 0, netoNuevos = 0;
for (let i = 0; i < comps.length; i++) {
  const c = comps[i];
  const miembros = [...c.miembros].sort();
  const nombre = miembros[0];
  const estado = c.estado === 'CERRADO' ? 'repite, acto CERRADO listo para fundir' : 'repite, acto ABIERTO';
  const cobertura = `${c.leidos} de ${c.posibles} pares leidos; ${c.en_cola_sin_leer} en cola; ${c.fuera_de_cola} fuera de cola`;
  const notaMecanica = c.estado === 'CERRADO'
    ? `tamano ${c.tamano}. Sin pares pendientes: no puede crecer.`
    : `tamano ${c.tamano}. Puede crecer: ${c.en_cola_sin_leer} en cola y ${c.fuera_de_cola} fuera de cola.`;

  const viejo = sucesorDeViejo.get(i);
  let nota = notaMecanica + ' REGENERADO EN LA VUELTA 16 sobre docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl al corte 3.388.';
  if (viejo) {
    conAntecesor++;
    if (viejo.nota === HANDWRITTEN_NOTA) {
      nota += ` NOTA ESCRITA A MANO DE LA ENTRADA VIEJA (corte ${viejo.fecha_corte}, nombre viejo "${viejo.nombre}"), TRASLADADA SIN TOCAR: ${viejo.nota}`;
    } else {
      nota += ` Sucede a la entrada vieja "${viejo.nombre}" (corte ${viejo.fecha_corte}); su nota era la misma formula mecanica, no habia texto escrito a mano que trasladar.`;
    }
  } else {
    netoNuevos++;
    nota += ' Sin antecesor en la nomina de 221 del corte 2.117: componente nueva, aparecida entre el 2.117 y el 3.388. Nota no inventada: hueco nombrado, no rellenado.';
  }

  nuevos.push({
    tipo: 'acto',
    nombre,
    miembros,
    forma: 'componente conexa de la relacion gemelo (banco 9.24)',
    cobertura,
    estado,
    operaciones: operacionesDe(miembros, c.estado),
    fecha_corte: '2026-08-13',
    nota,
  });
}

console.log('total componentes:', comps.length, '| con antecesor en los 221:', conAntecesor, '| net nuevos sin antecesor:', netoNuevos);
console.log('suma:', conAntecesor + netoNuevos);

fs.writeFileSync('scripts/_actos_nuevos_335.jsonl', nuevos.map(n => JSON.stringify(n)).join('\n') + '\n');
console.log('escrito scripts/_actos_nuevos_335.jsonl,', nuevos.length, 'lineas');
