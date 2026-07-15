// Fase 3.1 (caja de vidrio): comando de salud del cerebro. Lee Supabase
// directamente (cliente service-role -- esto es una herramienta de
// operador, no un flujo simulado de usuario como vuelo.ts/probar.ts) y
// agrega: sesiones por tipo, saltos semanticos (tasa + score medio),
// tasa de fallback_auto/abortos GIGO/presupuesto_excedido/
// autodeclaracion_fallida/numero_huerfano/procedencia_invalida, calidad
// media del juez de sesion, y las dos listas de oro: top 20 nodos mas
// usados y los nodos que NINGUNA sesion ha tocado todavia (el mapa del
// conocimiento muerto -- insumo directo para decidir que libros procesar
// despues).
//
// Uso: pnpm salud
import { createClient, type SupabaseClient } from "@supabase/supabase-js";
import { mkdirSync, writeFileSync } from "node:fs";
import path from "node:path";
import { cargarEnvRaiz, ROOT } from "./_shared/http";
import { cargarGrafo } from "../lib/engine/graph";

cargarEnvRaiz();

interface FilaSesion {
  id: string;
  tipo: string;
  presupuesto_excedido: boolean;
  decisiones: Array<Record<string, unknown>> | null;
  calidad: { pertinencia_transiciones?: number } | null;
}

interface FilaProjectNode {
  node_id: string;
}

async function traerTodo<T>(cliente: SupabaseClient, tabla: string, columnas: string): Promise<T[]> {
  const filas: T[] = [];
  const tamañoPagina = 1000;
  let desde = 0;
  while (true) {
    const { data, error } = await cliente
      .from(tabla)
      .select(columnas)
      .range(desde, desde + tamañoPagina - 1);
    if (error) throw error;
    const pagina = (data ?? []) as T[];
    filas.push(...pagina);
    if (pagina.length < tamañoPagina) break;
    desde += tamañoPagina;
  }
  return filas;
}

function porcentaje(parte: number, total: number): string {
  if (total === 0) return "n/a";
  return `${((parte / total) * 100).toFixed(1)}%`;
}

function promedio(valores: number[]): string {
  if (valores.length === 0) return "n/a";
  return (valores.reduce((a, b) => a + b, 0) / valores.length).toFixed(3);
}

function contarEventos(sesiones: FilaSesion[], tipo: string): { total: number; sesionesConEvento: number } {
  let total = 0;
  let sesionesConEvento = 0;
  for (const s of sesiones) {
    const eventos = (s.decisiones ?? []).filter((e) => e.tipo === tipo);
    if (eventos.length > 0) sesionesConEvento++;
    total += eventos.length;
  }
  return { total, sesionesConEvento };
}

async function main() {
  const url = process.env.NEXT_PUBLIC_SUPABASE_URL;
  const key = process.env.SUPABASE_SERVICE_ROLE_KEY;
  if (!url || !key) {
    console.error("Faltan NEXT_PUBLIC_SUPABASE_URL / SUPABASE_SERVICE_ROLE_KEY en el entorno.");
    process.exit(1);
  }
  const supabase = createClient(url, key);

  const [sesiones, nodosProyecto] = await Promise.all([
    traerTodo<FilaSesion>(supabase, "sessions", "id, tipo, presupuesto_excedido, decisiones, calidad"),
    traerTodo<FilaProjectNode>(supabase, "project_nodes", "node_id"),
  ]);
  const graph = cargarGrafo();

  const lineas: string[] = [];
  const log = (linea: string = "") => {
    console.log(linea);
    lineas.push(linea);
  };

  log("=".repeat(70));
  log("  SALUD DEL CEREBRO -- La Telaraña del Emprendedor (Fase 3.1)");
  log(`  ${new Date().toISOString()}`);
  log("=".repeat(70));

  const totalSesiones = sesiones.length;
  log(`\nTotal de sesiones: ${totalSesiones}`);
  log("\nSesiones por tipo:");
  const porTipo = new Map<string, number>();
  for (const s of sesiones) porTipo.set(s.tipo, (porTipo.get(s.tipo) ?? 0) + 1);
  for (const [tipo, n] of [...porTipo.entries()].sort((a, b) => b[1] - a[1])) {
    log(`  ${tipo}: ${n} (${porcentaje(n, totalSesiones)})`);
  }

  // --- Saltos semanticos: tasa + score medio de los elegidos ---
  let sesionesConSalto = 0;
  const scoresSaltosElegidos: number[] = [];
  for (const s of sesiones) {
    const turnos = (s.decisiones ?? []).filter((e) => e.tipo === "decision_turno");
    let tuvoSalto = false;
    for (const t of turnos) {
      const decision = t.decision as { es_salto?: boolean; camino?: string[] } | undefined;
      if (!decision?.es_salto) continue;
      tuvoSalto = true;
      const destino = decision.camino?.[0];
      const saltosPosibles = (t.saltos_posibles as Array<{ id: string; afinidad: number }>) ?? [];
      const elegido = saltosPosibles.find((sp) => sp.id === destino);
      if (elegido) scoresSaltosElegidos.push(elegido.afinidad);
    }
    if (tuvoSalto) sesionesConSalto++;
  }
  log(`\nSesiones con al menos un salto semantico: ${sesionesConSalto} (${porcentaje(sesionesConSalto, totalSesiones)})`);
  log(`Score medio (afinidad) de los saltos tomados: ${promedio(scoresSaltosElegidos)} (n=${scoresSaltosElegidos.length})`);

  // --- Tasas de eventos de guardianes / fallbacks ---
  const fallback = contarEventos(sesiones, "fallback_auto");
  const gigo = contarEventos(sesiones, "gigo_abortado");
  const autodeclFallida = contarEventos(sesiones, "autodeclaracion_fallida");
  const numeroHuerfano = contarEventos(sesiones, "numero_huerfano");
  const cifraMercado = contarEventos(sesiones, "cifra_mercado_inventada");
  const sinAcentos = contarEventos(sesiones, "salida_sin_acentos");
  const procedenciaInvalida = contarEventos(sesiones, "procedencia_invalida");
  const sesionesReporte = sesiones.filter((s) => s.tipo === "reporte").length;
  const presupuestoExcedido = sesiones.filter((s) => s.presupuesto_excedido).length;

  log("\nTasas de eventos (% de sesiones con al menos uno, total de ocurrencias):");
  log(`  fallback_auto: ${porcentaje(fallback.sesionesConEvento, totalSesiones)} (${fallback.total} ocurrencias)`);
  log(`  gigo_abortado: ${porcentaje(gigo.sesionesConEvento, sesionesReporte)} de sesiones tipo reporte (${gigo.total} ocurrencias)`);
  log(`  presupuesto_excedido: ${porcentaje(presupuestoExcedido, totalSesiones)}`);
  log(`  autodeclaracion_fallida: ${porcentaje(autodeclFallida.sesionesConEvento, totalSesiones)} (${autodeclFallida.total} ocurrencias)`);
  log(`  numero_huerfano: ${porcentaje(numeroHuerfano.sesionesConEvento, totalSesiones)} (${numeroHuerfano.total} ocurrencias)`);
  log(`  cifra_mercado_inventada: ${porcentaje(cifraMercado.sesionesConEvento, totalSesiones)} (${cifraMercado.total} ocurrencias)`);
  log(`  salida_sin_acentos: ${porcentaje(sinAcentos.sesionesConEvento, totalSesiones)} (${sinAcentos.total} ocurrencias)`);
  log(`  procedencia_invalida: ${porcentaje(procedenciaInvalida.sesionesConEvento, totalSesiones)} (${procedenciaInvalida.total} ocurrencias)`);

  // --- Calidad media del juez de sesion ---
  const puntajesCalidad = sesiones
    .map((s) => s.calidad?.pertinencia_transiciones)
    .filter((v): v is number => typeof v === "number");
  log(`\nSesiones muestreadas por el juez: ${puntajesCalidad.length} (${porcentaje(puntajesCalidad.length, totalSesiones)})`);
  log(`Calidad media (pertinencia_transiciones, 1-5): ${promedio(puntajesCalidad)}`);

  // --- DIGEST POR SESION: la cola de revision (Fase 3.9.1) ---
  // Una señal que nadie lee no es una salvaguarda. Lista CADA sesion con al
  // menos una bandera de la caja de vidrio, para ir directo a leerla con el
  // forense. En la beta esto es la lista de "20 sesiones que revisar".
  const UMBRAL_BRUJULA_FLOJA = 0.4; // el mejor salto posible de la sesion apenas pasa
  const UMBRAL_TURNO_POBRE = 0.35; // un turno donde la brujula tuvo poco material
  interface Bandera {
    sesion: string;
    tipo: string;
    flags: string[];
  }
  const cola: Bandera[] = [];
  for (const s of sesiones) {
    const eventos = s.decisiones ?? [];
    const cuenta = (t: string) => eventos.filter((e) => e.tipo === t).length;
    const flags: string[] = [];
    const add = (tipoEvento: string, etiqueta: string) => {
      const n = cuenta(tipoEvento);
      if (n > 0) flags.push(`${etiqueta}×${n}`);
    };
    add("numero_huerfano", "huerfano");
    add("cifra_mercado_inventada", "cifra-mercado");
    add("salida_sin_acentos", "sin-acentos");
    add("gigo_abortado", "GIGO");
    add("procedencia_invalida", "procedencia");
    add("autodeclaracion_fallida", "autodecl");
    if (s.presupuesto_excedido) flags.push("presupuesto");
    // Brujula floja: el mejor salto posible de TODA la sesion apenas supera el
    // umbral (poco material afin al usuario en el grafo), o varios turnos pobres.
    const turnos = eventos.filter((e) => e.tipo === "decision_turno");
    let mejorAfinidad = 0;
    let turnosPobres = 0;
    for (const t of turnos) {
      const sp = (t.saltos_posibles as Array<{ afinidad: number }> | undefined) ?? [];
      if (sp.length === 0) continue;
      const top = sp.reduce((m, c) => Math.max(m, c.afinidad), 0);
      mejorAfinidad = Math.max(mejorAfinidad, top);
      if (top < UMBRAL_TURNO_POBRE) turnosPobres++;
    }
    // La señal fuerte que pidio el fundador: el MEJOR salto de toda la sesion
    // fue bajo (el grafo tenia poco afin al usuario). El conteo de turnos pobres
    // es secundario y solo se marca si es marcado (>=3), para no ser ruido.
    if (mejorAfinidad > 0 && mejorAfinidad < UMBRAL_BRUJULA_FLOJA) {
      flags.push(`brujula-floja(max ${mejorAfinidad.toFixed(3)})`);
    } else if (turnosPobres >= 3) {
      flags.push(`poco-material(${turnosPobres} turnos <${UMBRAL_TURNO_POBRE})`);
    }
    if (flags.length > 0) cola.push({ sesion: s.id, tipo: s.tipo, flags });
  }
  cola.sort((a, b) => b.flags.length - a.flags.length);
  log(`\n${"=".repeat(70)}`);
  log(`DIGEST POR SESION -- cola de revision: ${cola.length} de ${totalSesiones} con banderas`);
  log("=".repeat(70));
  if (cola.length === 0) {
    log("  (ninguna sesion levanto banderas)");
  } else {
    for (const b of cola) log(`  ${b.sesion} [${b.tipo}]: ${b.flags.join(" · ")}`);
    log("\n  -> lee cada una con: pnpm tsx scripts/forense.ts <session_id>");
  }

  // --- Top 20 nodos mas usados ---
  const usoPorNodo = new Map<string, number>();
  for (const n of nodosProyecto) usoPorNodo.set(n.node_id, (usoPorNodo.get(n.node_id) ?? 0) + 1);
  const top20 = [...usoPorNodo.entries()].sort((a, b) => b[1] - a[1]).slice(0, 20);
  log("\nTop 20 nodos mas usados:");
  top20.forEach(([nid, n], i) => {
    const titulo = graph[nid]?.titulo_concepto ?? nid;
    log(`  ${i + 1}. ${titulo} (${nid}) -- ${n} sesion(es)`);
  });

  // --- Nodos jamas tocados por ninguna sesion (el mapa del conocimiento muerto) ---
  const idsGrafo = Object.keys(graph);
  const idsUsados = new Set(usoPorNodo.keys());
  const nuncaTocados = idsGrafo.filter((nid) => !idsUsados.has(nid));
  log(`\nNodos jamas tocados por ninguna sesion: ${nuncaTocados.length} de ${idsGrafo.length} (${porcentaje(nuncaTocados.length, idsGrafo.length)})`);
  log("  (lista completa guardada en examples/salud_nodos_nunca_tocados.txt)");

  const outDir = path.join(ROOT, "examples");
  mkdirSync(outDir, { recursive: true });
  writeFileSync(
    path.join(outDir, "salud_nodos_nunca_tocados.txt"),
    nuncaTocados.map((nid) => `${nid}\t${graph[nid]?.titulo_concepto ?? ""}`).join("\n") + "\n",
    { encoding: "utf-8" }
  );
  writeFileSync(path.join(outDir, "salud_reporte.txt"), lineas.join("\n") + "\n", { encoding: "utf-8" });
  console.log(`\nReporte completo guardado en examples/salud_reporte.txt`);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
