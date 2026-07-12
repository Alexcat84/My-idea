/**
 * analytics.ts — Fase 3.8 §5/§6: las métricas del proyecto, TODAS calculadas
 * de lo persistido. CERO LLM, cero costo por render. Este módulo es puro:
 * recibe filas ya cargadas y devuelve números; el conteo se prueba contra
 * casos calculados A MANO (regla AGENTS.md), no contra su propia salida.
 *
 * Dos capas (canon 11):
 *  - UNIVERSAL (siempre): duración total, duración real por etapa, ritmo,
 *    racha más larga, ciclos de plan, mundos, e Hitos (el timeline).
 *  - CUMPLIMIENTO (solo con baseline confirmada): a tiempo / adelantadas /
 *    tardías, desviación media, base-vs-real por etapa, replanificaciones.
 *
 * Umbrales del §6: a tiempo = |completed_at − fecha_base| ≤ 1 día;
 * adelantada < −1 día; tardía > +1 día. Tono espejo: las tardías se pintan
 * en ámbar, jamás en rojo (eso lo decide la UI).
 */
const DIA = 86_400_000;

function difDias(desdeIso: string, hastaIso: string): number {
  return (new Date(hastaIso).getTime() - new Date(desdeIso).getTime()) / DIA;
}

/** Días redondeados entre dos instantes (para duraciones que se muestran). */
function dias(desdeIso: string, hastaIso: string): number {
  return Math.round(difDias(desdeIso, hastaIso));
}

export interface PlanCoreAnalytics {
  id: string;
  etiqueta: string;
  created_at: string;
  baseline_confirmada_at: string | null;
}

export interface ItemAnalytics {
  plan_id: string;
  etapa: number;
  estado: string;
  destacado: boolean;
  completed_at: string | null;
  fecha_base: string | null;
  fecha_base_original: string | null;
}

export interface MundoAnalytics {
  dominio: string;
  unlocked_at: string;
}

export interface EntradaAnalytics {
  proyectoCreatedAt: string;
  realizadaAt?: string | null;
  organizadorAt?: string | null;
  /** planes core (inicial/completo/seguimiento), NO el organizador */
  planesCore: PlanCoreAnalytics[];
  /** TODOS los ítems core (de todos los ciclos): el trabajo real del viaje */
  items: ItemAnalytics[];
  mundos: MundoAnalytics[];
  /** ancla de "ahora" para tests deterministas (default: Date.now) */
  ahora?: string;
}

export type CumplimientoItem = "a_tiempo" | "adelantada" | "tardia";

export function clasificarCumplimiento(completedAt: string, fechaBase: string): CumplimientoItem {
  const d = difDias(fechaBase, completedAt); // + = tarde, − = adelantada
  if (Math.abs(d) <= 1 + 1e-6) return "a_tiempo";
  return d > 0 ? "tardia" : "adelantada";
}

export interface Hito {
  fecha: string;
  tipo: "chispa" | "claridad" | "plan" | "mundo" | "accion" | "realizada";
  etiqueta: string;
  dominio?: string;
}

export interface CapaUniversal {
  duracionTotalDias: number;
  accionesHechas: number;
  ritmoAccionesPorSemana: number;
  rachaMasLargaDias: number;
  ciclosDePlan: number;
  mundos: number;
  duracionPorEtapa: Array<{ etapa: number; dias: number }>;
}

export interface CapaCumplimiento {
  aTiempo: number;
  adelantadas: number;
  tardias: number;
  totalConFecha: number;
  pctATiempo: number;
  pctAdelantadas: number;
  pctTardias: number;
  desviacionMediaDias: number;
  replanificaciones: number;
  porEtapa: Array<{ etapa: number; baseDias: number | null; realDias: number | null }>;
}

export interface Analytics {
  universal: CapaUniversal;
  cumplimiento: CapaCumplimiento | null;
  hitos: Hito[];
}

/** El último plan con baseline confirmada (por created_at) — la base VIGENTE
 * de toda lectura de cumplimiento (§4). null si nadie confirmó fechas. */
function planBaselineVigente(planes: PlanCoreAnalytics[]): PlanCoreAnalytics | null {
  return (
    planes
      .filter((p) => p.baseline_confirmada_at)
      .sort((a, b) => a.created_at.localeCompare(b.created_at))
      .at(-1) ?? null
  );
}

/** La racha más larga EN DÍAS: el mayor lapso de una serie de acciones
 * consecutivas (ordenadas por completed_at) donde cada una cae dentro de los
 * 7 días de la anterior. Una sola acción → 0 días. */
function rachaMasLarga(completadas: string[]): number {
  if (completadas.length === 0) return 0;
  const orden = [...completadas].sort();
  let inicio = 0;
  let mejor = 0;
  for (let i = 1; i < orden.length; i += 1) {
    if (difDias(orden[i - 1], orden[i]) > 7) inicio = i; // se rompe la racha
    const lapso = dias(orden[inicio], orden[i]);
    if (lapso > mejor) mejor = lapso;
  }
  return mejor;
}

/** Duración real por etapa: secuencial. La frontera de cada etapa es su
 * último completed_at; la duración es desde la frontera anterior (o la chispa
 * para la primera etapa con actividad). Solo etapas con completions. */
function duracionPorEtapa(
  items: ItemAnalytics[],
  chispa: string
): Array<{ etapa: number; dias: number }> {
  const ultimoPorEtapa = new Map<number, string>();
  for (const it of items) {
    if (!it.completed_at) continue;
    const prev = ultimoPorEtapa.get(it.etapa);
    if (!prev || it.completed_at > prev) ultimoPorEtapa.set(it.etapa, it.completed_at);
  }
  const etapas = [...ultimoPorEtapa.keys()].sort((a, b) => a - b);
  const out: Array<{ etapa: number; dias: number }> = [];
  let frontera = chispa;
  for (const etapa of etapas) {
    const fin = ultimoPorEtapa.get(etapa)!;
    out.push({ etapa, dias: Math.max(0, dias(frontera, fin)) });
    frontera = fin;
  }
  return out;
}

export function calcularAnalytics(entrada: EntradaAnalytics): Analytics {
  const ahora = entrada.ahora ?? new Date().toISOString();
  const chispa = entrada.proyectoCreatedAt;
  const fin = entrada.realizadaAt ?? ahora;

  const completadas = entrada.items.map((i) => i.completed_at).filter((c): c is string => Boolean(c));
  const accionesHechas = completadas.length;
  const duracionTotalDias = Math.max(0, dias(chispa, fin));
  const semanas = duracionTotalDias / 7;
  const ritmo = semanas > 0 ? accionesHechas / semanas : accionesHechas;

  const universal: CapaUniversal = {
    duracionTotalDias,
    accionesHechas,
    ritmoAccionesPorSemana: Math.round(ritmo * 10) / 10,
    rachaMasLargaDias: rachaMasLarga(completadas),
    ciclosDePlan: entrada.planesCore.length,
    mundos: entrada.mundos.length,
    duracionPorEtapa: duracionPorEtapa(entrada.items, chispa),
  };

  // Capa de cumplimiento: solo si algún plan tiene baseline confirmada.
  let cumplimiento: CapaCumplimiento | null = null;
  const baselinePlan = planBaselineVigente(entrada.planesCore);
  if (baselinePlan) {
    const delPlan = entrada.items.filter((i) => i.plan_id === baselinePlan.id);
    const conFecha = delPlan.filter((i) => i.completed_at && i.fecha_base);
    let aTiempo = 0;
    let adelantadas = 0;
    let tardias = 0;
    let sumaDesv = 0;
    for (const it of conFecha) {
      const clase = clasificarCumplimiento(it.completed_at!, it.fecha_base!);
      if (clase === "a_tiempo") aTiempo += 1;
      else if (clase === "adelantada") adelantadas += 1;
      else tardias += 1;
      sumaDesv += difDias(it.fecha_base!, it.completed_at!);
    }
    const total = conFecha.length;
    const pct = (n: number) => (total > 0 ? Math.round((n / total) * 100) : 0);

    // Barras gemelas por etapa: días desde la chispa hasta la última fecha
    // base y hasta la última real de cada etapa del plan con baseline.
    const etapas = [...new Set(delPlan.map((i) => i.etapa))].sort((a, b) => a - b);
    const porEtapa = etapas.map((etapa) => {
      const deEtapa = delPlan.filter((i) => i.etapa === etapa);
      const bases = deEtapa.map((i) => i.fecha_base).filter((f): f is string => Boolean(f));
      const reales = deEtapa.map((i) => i.completed_at).filter((c): c is string => Boolean(c));
      const maxIso = (xs: string[]) => (xs.length ? xs.reduce((a, b) => (a > b ? a : b)) : null);
      const baseMax = maxIso(bases);
      const realMax = maxIso(reales);
      return {
        etapa,
        baseDias: baseMax ? Math.max(0, dias(chispa, baseMax)) : null,
        realDias: realMax ? Math.max(0, dias(chispa, realMax)) : null,
      };
    });

    cumplimiento = {
      aTiempo,
      adelantadas,
      tardias,
      totalConFecha: total,
      pctATiempo: pct(aTiempo),
      pctAdelantadas: pct(adelantadas),
      pctTardias: pct(tardias),
      desviacionMediaDias: total > 0 ? Math.round((sumaDesv / total) * 10) / 10 : 0,
      replanificaciones: delPlan.filter((i) => i.fecha_base_original).length,
      porEtapa,
    };
  }

  const hitos = construirHitos(entrada, ahora);
  return { universal, cumplimiento, hitos };
}

/** El timeline de Hitos (§5/§6), construido SOLO de lo persistido. Con
 * incluirAcciones, cada ítem completado suma su propio hito (Celebración). */
export function construirHitos(entrada: EntradaAnalytics, ahora: string, incluirAcciones = false): Hito[] {
  const hitos: Hito[] = [{ fecha: entrada.proyectoCreatedAt, tipo: "chispa", etiqueta: "La Chispa" }];
  if (entrada.organizadorAt) {
    hitos.push({ fecha: entrada.organizadorAt, tipo: "claridad", etiqueta: "Claridad" });
  }
  const ciclos = [...entrada.planesCore].sort((a, b) => a.created_at.localeCompare(b.created_at));
  ciclos.forEach((p, i) => {
    hitos.push({ fecha: p.created_at, tipo: "plan", etiqueta: `Plan ciclo ${i + 1}` });
  });
  for (const m of entrada.mundos) {
    hitos.push({ fecha: m.unlocked_at, tipo: "mundo", etiqueta: "Mundo activado", dominio: m.dominio });
  }
  if (incluirAcciones) {
    for (const it of entrada.items) {
      if (it.completed_at) hitos.push({ fecha: it.completed_at, tipo: "accion", etiqueta: "Acción completada" });
    }
  }
  if (entrada.realizadaAt) {
    hitos.push({ fecha: entrada.realizadaAt, tipo: "realizada", etiqueta: "Realizada" });
  }
  void ahora;
  return hitos.sort((a, b) => a.fecha.localeCompare(b.fecha));
}

/** El informe descargable (.md), armado del análisis ya calculado. Tono
 * espejo (§6): las tardías se nombran sin regaño. Cero LLM. */
export function informeMarkdown(nombre: string, a: Analytics): string {
  const u = a.universal;
  const l: string[] = [];
  l.push(`# Análisis de ${nombre}`);
  l.push("");
  l.push("## Lo que construiste");
  l.push(`- Duración total: **${u.duracionTotalDias} días**`);
  l.push(`- Acciones completadas: **${u.accionesHechas}**`);
  l.push(`- Ritmo: **${u.ritmoAccionesPorSemana} acciones por semana**`);
  l.push(`- Racha más larga: **${u.rachaMasLargaDias} días**`);
  l.push(`- Ciclos de plan: **${u.ciclosDePlan}** · Mundos: **${u.mundos}**`);
  if (u.duracionPorEtapa.length) {
    l.push("");
    l.push("### Duración real por etapa");
    for (const e of u.duracionPorEtapa) l.push(`- Etapa ${e.etapa}: ${e.dias} días`);
  }
  if (a.cumplimiento) {
    const c = a.cumplimiento;
    l.push("");
    l.push("## Cumplimiento (comparado con tus fechas)");
    l.push(`- A tiempo: **${c.aTiempo}** (${c.pctATiempo}%)`);
    l.push(`- Adelantadas: **${c.adelantadas}** (${c.pctAdelantadas}%)`);
    l.push(`- Tardías: **${c.tardias}** (${c.pctTardias}%)`);
    const signo = c.desviacionMediaDias > 0 ? "+" : "";
    l.push(`- Desviación media sobre lo planificado: **${signo}${c.desviacionMediaDias} días**`);
    if (c.replanificaciones > 0) {
      l.push(`- Moviste la fecha de **${c.replanificaciones}** acciones.`);
      l.push("");
      l.push("Replanificar es parte del método. Ajustar el mapa no es fallar: es seguir con los pies en la tierra.");
    }
  }
  l.push("");
  l.push("## Hitos");
  for (const h of a.hitos) l.push(`- ${h.fecha.slice(0, 10)} · ${h.etiqueta}`);
  l.push("");
  return l.join("\n");
}
