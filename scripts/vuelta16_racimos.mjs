import fs from 'fs';

const cola = fs.readFileSync('docs/INTRA_DOMINIO_VEREDICTOS.jsonl', 'utf-8')
  .split('\n').filter(Boolean).map(l => JSON.parse(l));

const racimos = [
  ["el efectivo contra la ganancia", ["diferencia_ganancia_flujo_caja","profit_vs_cash","cash_is_king"]],
  ["la ecuacion de valor", ["construccion_de_valor_percibido","ecuacion_de_valor","ecuacion_de_valor_cliente","ecuacion_de_valor_venta","prevencion_objeciones_vs_manejo"]],
  ["el sales roadmap", ["customer_validation_sales_roadmap","estrategia_de_ventas","hoja_de_ruta_de_ventas","refinar_sales_roadmap","sales_roadmap","sales_roadmap_vs_sales_force"]],
  ["la competencia entre inversores", ["construccion_de_leverage","estrategia_competencia_vcs","gestion_multiples_term_sheets","leverage_en_negociacion_con_vcs","tecnica_anclaje_negociacion"]],
  ["la junta asesora", ["formalize_advisory_board","formalizar_junta_asesora","identificar_junta_asesores","identificar_consejo_asesores"]],
  ["los cuadrantes de mercado", ["clasificacion_mercados_cadena_suministro","cuatro_capacidades_mercado","cuatro_categorias_desempeno_cadena_suministro","estrategia_cuatro_capacidades_mercado","marco_analisis_mercado_cadena_suministro","modelo_cuadrantes_mercado"]],
  ["build, measure, learn", ["build_measure_learn","ciclo_construir_medir_aprender","ciclo_crear_medir_aprender","desarrollo_en_espiral","design_test_repeat","design_thinking_proceso","startup_como_experimento_cientifico","testing_process_completo"]],
  ["el compromiso contado tres veces", ["obtencion_compromiso","obtencion_de_compromiso","obtencion_compromiso_venta"]],
  ["la seleccion de canal", ["channels_hypothesis_physical","channels_hypothesis_web_mobile","hipotesis_de_canales","seleccion_canal_distribucion","seleccion_canal_fisico"]],
  ["la supervision de la IA", ["alineacion_etica_ia_negocio","comprender_alineacion_etica_ia","comprension_capacidades_limitaciones_ia","human_in_the_loop_ia","invitar_ia_a_todo","jagged_frontier_ia","mitigar_falling_asleep_wheel","principio_humano_en_el_loop","principio_invitar_ia_siempre","riesgo_sobredependencia_ia"]],
  ["la mesa unida de puertas y portafolio", ["asignacion_recursos_en_gates","decision_factory_mentality","equipos_dedicados_de_proyecto","estructura_de_gates","estructura_gates","gates_go_kill_decision_points","gestion_de_portafolio_gates_go_kill","gestion_portafolio_dos_niveles","gestion_portafolio_foco","gestion_portafolio_formal","portfolio_management","requisitos_gates_con_dientes","revision_portafolio_periodica","sistema_gates_go_kill","sistema_gestion_recursos_en_gates","sistema_stage_gate","stage_gate_system"]],
  ["el racimo del pivote", ["decision_pivote_perseverar","pivotar_o_perseverar","pivotar_o_proceder","pivote_estrategico","pivote_o_proceder","pivote_startup","pivotes_e_iteraciones"]],
  ["la serie de Coleman", ["fase_assess","fase_assess_ciclo_cliente","fase_assess_experiencia_cliente","fase_admit","fase_admit_celebracion","fase_affirm_buyers_remorse","fase_activate","fase_activate_primera_impresion","fase_acclimate","fase_acclimate_experiencia_cliente","fase_acclimate_mapa_de_proceso","fase_accomplish","fase_accomplish_experiencia_cliente","fase_adopt","fase_adopt_ciclo_cliente","advocacy_customer_journey","incentivos_no_monetarios_advocacy","fases_de_retencion_de_clientes","ocho_fases_experiencia_cliente","seis_canales_comunicacion_assess","seis_herramientas_comunicacion_fase_activate","seis_herramientas_comunicacion_celebracion","estrategia_multicanal_bienvenida","regalos_estrategicos_personalizados","regalos_estrategicos_sorpresa","sorprender_cliente_estrategico","welcome_call_cliente_veterano","seis_medios_comunicacion_cliente"]],
];

// las 65 lecturas dirigidas del repo, con id (donde el archivo lo da), fuente y pareja
const dirigidas = [
  // primera tanda LD-01..LD-11, LECTURAS_DIRIGIDAS.md
  ["LD-01","formalizar_junta_asesora","identificar_consejo_asesores","D"],
  ["LD-02","channels_hypothesis_physical","channels_hypothesis_web_mobile","D"],
  ["LD-03","channels_hypothesis_web_mobile","seleccion_canal_fisico","A"],
  ["LD-04","evaluacion_tecnologias_disruptivas","explotacion_tecnologias_disruptivas","D"],
  ["LD-05","estrategia_innovacion_producto","estrategia_de_innovacion_producto","D"],
  ["LD-06","project_close_out","reunion_conclusion_proyecto","A"],
  ["LD-07","project_close_out","encuesta_satisfaccion_postproyecto","D"],
  ["LD-08","disenar_tests_pass_fail","diseno_experimentos_hipotesis","D"],
  ["LD-09","refinar_sales_roadmap","evaluacion_vp_ventas","D"],
  ["LD-10","refinar_sales_roadmap","framework_evaluacion_director_ventas","D"],
  ["LD-11","pensamiento_visual","pensamiento_visual_modelos_negocio","D"],
  // segunda tanda, 16 lecturas SIN id publicado en el archivo (se listan sin id LD)
  ["s2-cuad-1","clasificacion_mercados_cadena_suministro","cuatro_capacidades_mercado","D"],
  ["s2-cuad-2","clasificacion_mercados_cadena_suministro","cuatro_categorias_desempeno_cadena_suministro","D"],
  ["s2-cuad-3","cuatro_capacidades_mercado","modelo_cuadrantes_mercado","D"],
  ["s2-cuad-4","cuatro_categorias_desempeno_cadena_suministro","estrategia_cuatro_capacidades_mercado","D"],
  ["s2-cuad-5","cuatro_categorias_desempeno_cadena_suministro","marco_analisis_mercado_cadena_suministro","D"],
  ["s2-cuad-6","cuatro_categorias_desempeno_cadena_suministro","modelo_cuadrantes_mercado","D"],
  ["s2-cuad-7","estrategia_cuatro_capacidades_mercado","marco_analisis_mercado_cadena_suministro","D"],
  ["s2-cuad-8","marco_analisis_mercado_cadena_suministro","modelo_cuadrantes_mercado","A"],
  ["s2-ecu-1","construccion_de_valor_percibido","ecuacion_de_valor_cliente","D"],
  ["s2-ecu-2","construccion_de_valor_percibido","ecuacion_de_valor_venta","A"],
  ["s2-ecu-3","construccion_de_valor_percibido","prevencion_objeciones_vs_manejo","D"],
  ["s2-ecu-4","ecuacion_de_valor","prevencion_objeciones_vs_manejo","D"],
  ["s2-ecu-5","ecuacion_de_valor_venta","prevencion_objeciones_vs_manejo","D"],
  ["s2-ia-1","alineacion_etica_ia_negocio","mitigar_falling_asleep_wheel","D"],
  ["s2-ia-2","alineacion_etica_ia_negocio","riesgo_sobredependencia_ia","D"],
  ["s2-ia-3","principio_humano_en_el_loop","riesgo_sobredependencia_ia","D"],
  // tercera tanda LD-28..LD-31, LD_ADOPT_ADVOCATE.md
  ["LD-28","advocacy_customer_journey","incentivos_no_monetarios_advocacy","D"],
  ["LD-29","advocacy_customer_journey","fase_adopt","D"],
  ["LD-30","fase_adopt","incentivos_no_monetarios_advocacy","D"],
  ["LD-31","fase_adopt_ciclo_cliente","incentivos_no_monetarios_advocacy","D"],
  // cuarta tanda LD-32..LD-57, LD_MESA_UNIDA.md
  ["LD-32","estructura_gates","portfolio_management","D"],
  ["LD-33","estructura_gates","gestion_portafolio_formal","D"],
  ["LD-34","estructura_gates","revision_portafolio_periodica","D"],
  ["LD-35","estructura_gates","gestion_portafolio_dos_niveles","D"],
  ["LD-36","estructura_gates","gestion_de_portafolio_gates_go_kill","D"],
  ["LD-37","estructura_gates","gestion_portafolio_foco","D"],
  ["LD-38","estructura_gates","equipos_dedicados_de_proyecto","D"],
  ["LD-39","estructura_gates","decision_factory_mentality","D"],
  ["LD-40","requisitos_gates_con_dientes","portfolio_management","D"],
  ["LD-41","requisitos_gates_con_dientes","gestion_portafolio_formal","C"],
  ["LD-42","requisitos_gates_con_dientes","revision_portafolio_periodica","D"],
  ["LD-43","requisitos_gates_con_dientes","gestion_portafolio_dos_niveles","C"],
  ["LD-44","requisitos_gates_con_dientes","gestion_de_portafolio_gates_go_kill","D"],
  ["LD-45","requisitos_gates_con_dientes","gestion_portafolio_foco","D"],
  ["LD-46","requisitos_gates_con_dientes","equipos_dedicados_de_proyecto","D"],
  ["LD-47","requisitos_gates_con_dientes","decision_factory_mentality","D"],
  ["LD-48","gates_go_kill_decision_points","portfolio_management","D"],
  ["LD-49","gates_go_kill_decision_points","gestion_portafolio_formal","D"],
  ["LD-50","gates_go_kill_decision_points","revision_portafolio_periodica","D"],
  ["LD-51","gates_go_kill_decision_points","gestion_portafolio_dos_niveles","D"],
  ["LD-52","gates_go_kill_decision_points","gestion_de_portafolio_gates_go_kill","A"],
  ["LD-53","gates_go_kill_decision_points","gestion_portafolio_foco","D"],
  ["LD-54","gates_go_kill_decision_points","equipos_dedicados_de_proyecto","D"],
  ["LD-55","gates_go_kill_decision_points","decision_factory_mentality","D"],
  ["LD-56","sistema_stage_gate","sistema_gates_go_kill","D"],
  ["LD-57","asignacion_recursos_en_gates","sistema_gates_go_kill","D"],
  // quinta/sexta/septima tanda LD-58..LD-65, LD_CADENA.md + LD_ACTO_DE_SEIS.md
  ["LD-58","gates_go_kill_decision_points","requisitos_gates_con_dientes","A"],
  ["LD-59","customer_validation_sell_phase","introduccion_validacion_clientes","D"],
  ["LD-60","gates_go_kill_decision_points","estructura_gates","A"],
  ["LD-61","gates_go_kill_decision_points","estructura_de_gates","A"],
  ["LD-62","gestion_de_portafolio_gates_go_kill","estructura_gates","D"],
  ["LD-63","gestion_de_portafolio_gates_go_kill","estructura_de_gates","D"],
  ["LD-64","sistema_gates_go_kill","estructura_de_gates","A"],
  ["LD-65","requisitos_gates_con_dientes","gestion_de_portafolio_gates_go_kill","D"],
];

console.log("total dirigidas en el instrumento:", dirigidas.length);

const key = (a,b) => [a,b].sort().join("~~");

function combn2(n){ return n*(n-1)/2; }

let out = [];
for (const [nombre, miembros] of racimos) {
  const posibles = combn2(miembros.length);
  const memberSet = new Set(miembros);

  const colaMatches = cola.filter(v => memberSet.has(v.nodo_a) && memberSet.has(v.nodo_b));
  const colaKeys = new Set(colaMatches.map(v => key(v.nodo_a, v.nodo_b)));

  const dirMatches = dirigidas.filter(([id,a,b,c]) => memberSet.has(a) && memberSet.has(b));
  // dedupe por pareja (mismo par, distinto id)
  const dirByKey = new Map();
  for (const [id,a,b,c] of dirMatches) {
    const k = key(a,b);
    if (!dirByKey.has(k)) dirByKey.set(k, []);
    dirByKey.get(k).push([id,c]);
  }
  const dirUniqueKeys = [...dirByKey.keys()];
  // dirigida que ya esta en cola no suma cobertura
  const dirNuevas = dirUniqueKeys.filter(k => !colaKeys.has(k));
  const dirYaEnCola = dirUniqueKeys.filter(k => colaKeys.has(k));

  // reparto de clases: cola + dirigidas nuevas (si alguna pareja tiene mas de un id, todas coinciden en clase segun lo verificado)
  const clases = {A:0,B:0,C:0,D:0};
  for (const v of colaMatches) clases[v.clase] = (clases[v.clase]||0)+1;
  for (const k of dirNuevas) {
    const entries = dirByKey.get(k);
    const clasesDeEsePar = new Set(entries.map(e=>e[1]));
    if (clasesDeEsePar.size > 1) {
      console.log("ALERTA: mismo par con clases distintas en dirigidas", k, entries);
    }
    const c = entries[0][1];
    clases[c] = (clases[c]||0)+1;
  }

  const cobertura = colaMatches.length + dirNuevas.length;

  out.push({
    nombre, n: miembros.length, posibles,
    cola: colaMatches.length,
    dirigidas_unicas_en_nomina: dirUniqueKeys.length,
    dirigidas_ya_en_cola: dirYaEnCola.length,
    dirigidas_nuevas: dirNuevas.length,
    cobertura,
    clases,
    dirigidas_nuevas_ids: dirNuevas.map(k => dirByKey.get(k).map(e=>e[0]).join("/")),
  });
}

for (const r of out) {
  console.log(JSON.stringify(r));
}
