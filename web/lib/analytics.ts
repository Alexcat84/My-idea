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
  /** Fase 4.1 (V3b): null = core. Los items de mundo YA no se excluyen en la
   * entrada; la capa universal los ignora (sus etapas colisionarian con las del
   * core y le moverian el ritmo al viaje principal) y el desglose los cuenta. */
  dominio?: string | null;
  etapa: number;
  estado: string;
  destacado: boolean;
  completed_at: string | null;
  fecha_base: string | null;
  fecha_base_original: string | null;
  /** texto del ítem, para los hitos de acción de la Celebración */
  texto?: string;
  /** gestor de estados: el porqué de una tarea retirada (estado 'no_aplica') */
  no_aplica_motivo?: string | null;
}

export interface MundoAnalytics {
  dominio: string;
  unlocked_at: string;
  /** Fase 4.2: el usuario dio por terminado este mundo (migración 026). null =
   * abierto. Es el `realizada_at` del mundo: mismo parámetro, misma soberanía. */
  completado_at?: string | null;
  /** Fase 4.2: el porqué del cierre de ESTE mundo, en sus palabras. */
  cierre_motivo?: string | null;
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
  /** Fase 4.2: los planes de los MUNDOS, con su dominio. Un mundo es un
   * subproyecto: tiene sus propios ciclos y su propio plan vigente, y
   * analyticsDeMundo() los mide con la MISMA capa universal que el core. */
  planesMundo?: Array<PlanCoreAnalytics & { dominio: string }>;
  /** Fase 4.0 §3: el modo del camino viaja con la lectura — el bloque de
   * realidad NO habla de cumplimiento si el usuario eligió "a mi ritmo". */
  modoCamino?: "ritmo" | "fechas" | null;
  /** Fase 4.0 §8: el motivo del cierre (projects.cierre_motivo). */
  cierreMotivo?: string | null;
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
  tipo: "chispa" | "claridad" | "plan" | "mundo" | "mundo_completado" | "accion" | "realizada";
  etiqueta: string;
  dominio?: string;
  /** subtítulo dim (canon 09): "La idea nace", "planificado · a tiempo"… */
  subtitulo?: string;
  /** cumplimiento del ítem (solo hitos de acción con fecha_base) */
  cumplimiento?: CumplimientoItem;
}

/** Gestor de estados: una tarea retirada ('no_aplica'), con su porqué en la
 * voz del usuario. Fuera del denominador del avance; el acta y el expediente
 * la nombran aparte. */
export interface RetiradaAnalytics {
  texto: string;
  etapa: number;
  motivo: string | null;
}

export interface CapaUniversal {
  duracionTotalDias: number;
  accionesHechas: number;
  /** X/N del checklist VIGENTE, sobre ACTIVAS (canon 09: "19 de 24 acciones").
   * 'total' excluye las retiradas: el avance nunca se mide sobre lo que el
   * usuario decidió que no aplica. */
  accionesVigente: { hechas: number; total: number };
  /** las tareas retiradas del plan vigente (no_aplica), con su motivo */
  retiradas: RetiradaAnalytics[];
  ritmoAccionesPorSemana: number;
  rachaMasLargaDias: number;
  ciclosDePlan: number;
  mundos: number;
  duracionPorEtapa: Array<{ etapa: number; dias: number }>;
  /** Fase 4.0 §3 (ritmo real): días desde el último avance. null si nunca hubo
   * uno. Un usuario que no toca el checklist en 30 días es otro contexto. */
  diasSinAvance: number | null;
  /** Fase 4.0 §3 (ciclo): cuándo nació el plan vigente y cuánto lleva vivo. */
  planVigenteAt: string | null;
  diasDeVidaPlanVigente: number;
}

/** Fase 4.1 (V3b): un mundo (o el core) con sus conteos de cumplimiento.
 *
 * Fase 4.2: gana la desviación media, las tardías que importan y las
 * replanificaciones — los mismos parámetros que la capa de cumplimiento del
 * viaje principal. No es adorno: el bloque de realidad de un follow-DE-MUNDO
 * REDACTA de aquí, y sin estos campos tendría que recalcularlos por su cuenta
 * (la regla del §6 prohíbe duplicar la lógica del tiempo). */
export interface CumplimientoDominio {
  dominio: string;
  aTiempo: number;
  adelantadas: number;
  tardias: number;
  total: number;
  desviacionMediaDias: number;
  tardiasTop: Array<{ texto: string; etapa: number; diasRetraso: number }>;
  replanificados: Array<{ texto: string; etapa: number }>;
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
  /** Fase 4.0 §3 ("las tardías que importan"): los ítems más desviados, de
   * mayor a menor retraso — el motor debe saber DÓNDE se atora el usuario. */
  tardiasTop: Array<{ texto: string; etapa: number; diasRetraso: number }>;
  /** Fase 4.0 §3: CUÁLES movieron su fecha (no solo cuántos): señal de que la
   * línea base era irreal o de que la vida cambió. */
  replanificados: Array<{ texto: string; etapa: number }>;
  /** Fase 4.1 (V3b): el desglose por dominio — core y cada mundo con fechas,
   * con sus propios conteos. La fila extra que admite el canon 11: los mundos
   * dejan de ser invisibles al cumplimiento sin rediseñar la pantalla. */
  porDominio: CumplimientoDominio[];
}

export interface Analytics {
  universal: CapaUniversal;
  cumplimiento: CapaCumplimiento | null;
  hitos: Hito[];
  /** Fase 4.0 §3: se arrastra tal cual para que el bloque de realidad elija su
   * lenguaje (con fechas: cumplimiento; a mi ritmo: solo duraciones y ritmo). */
  modoCamino: "ritmo" | "fechas" | null;
  /** Fase 4.0 §8 (acta de cierre): el porqué del cierre, en las palabras del
   * usuario. null si aún no cerró, o si cerró sin escribir nada. */
  cierreMotivo: string | null;
  /** Fase 4.2: cada mundo medido como el subproyecto que es (su capa universal,
   * su cumplimiento, su cierre). `universal.mundos` es solo el conteo; esto es
   * la lista, que necesitan el desglose del Análisis y el acta del proyecto
   * (§3: cerrar la idea con mundos abiertos es legítimo, y el acta lo DICE). */
  mundos: AnalyticsMundo[];
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

/** null/"core" = el viaje principal (los items previos a la 016 no traen dominio). */
const dominioDe = (i: ItemAnalytics) => i.dominio ?? "core";
const esItemCore = (i: ItemAnalytics) => dominioDe(i) === "core";

/**
 * Fase 4.1 (V3b): el cumplimiento POR DOMINIO. Cuenta cualquier item con fecha
 * base y fecha real, venga del core o de un mundo, agrupado por su dominio. No
 * mira `baseline_confirmada_at` del plan a proposito: los items de mundo entran
 * al MISMO ritual y baseline del proyecto (su plan no se sella), y aun asi su
 * cumplimiento es real y debe contarse.
 */
function cumplimientoPorDominio(items: ItemAnalytics[]): CumplimientoDominio[] {
  const porDom = new Map<string, ItemAnalytics[]>();
  for (const it of items) {
    const d = dominioDe(it);
    porDom.set(d, [...(porDom.get(d) ?? []), it]);
  }
  const filas: CumplimientoDominio[] = [];
  for (const [dominio, delDominio] of porDom) {
    const conFecha = delDominio.filter((i) => i.completed_at && i.fecha_base);
    if (conFecha.length === 0) continue;
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
    filas.push({
      dominio,
      aTiempo,
      adelantadas,
      tardias,
      total: conFecha.length,
      desviacionMediaDias: Math.round((sumaDesv / conFecha.length) * 10) / 10,
      tardiasTop: conFecha
        .filter((i) => clasificarCumplimiento(i.completed_at!, i.fecha_base!) === "tardia")
        .map((i) => ({
          texto: i.texto ?? "",
          etapa: i.etapa,
          diasRetraso: Math.round(difDias(i.fecha_base!, i.completed_at!)),
        }))
        .sort((a, b) => b.diasRetraso - a.diasRetraso)
        .slice(0, 5),
      // Las replanificaciones se cuentan sobre TODO el dominio, no solo sobre
      // lo ya completado: mover la fecha de algo que aún no haces también dice
      // que la línea base era irreal.
      replanificados: delDominio
        .filter((i) => i.fecha_base_original)
        .map((i) => ({ texto: i.texto ?? "", etapa: i.etapa })),
    });
  }
  // core primero; los mundos, alfabeticos: orden estable para la pantalla.
  return filas.sort((a, b) =>
    a.dominio === "core" ? -1 : b.dominio === "core" ? 1 : a.dominio.localeCompare(b.dominio)
  );
}

/**
 * Fase 4.2: LA CAPA UNIVERSAL, de un tramo cualquiera del viaje. Extraída tal
 * cual de calcularAnalytics para que un MUNDO se mida con la misma vara que el
 * viaje principal — un mundo es un subproyecto completo, y su ritmo, su racha y
 * su "X de N" salen de esta función, no de una copia paralela (la regla del §6:
 * prohibido duplicar la lógica del tiempo).
 *
 * `chispa` es el nacimiento del tramo (la idea para el core; el unlock para un
 * mundo) y `fin` su cierre (realizada_at / completado_at, o ahora).
 */
export function capaUniversalDe(
  items: ItemAnalytics[],
  planes: PlanCoreAnalytics[],
  chispa: string,
  fin: string,
  mundos: number
): CapaUniversal {
  const completadas = items.map((i) => i.completed_at).filter((c): c is string => Boolean(c));
  const accionesHechas = completadas.length;
  const duracionTotalDias = Math.max(0, dias(chispa, fin));
  const semanas = duracionTotalDias / 7;
  const ritmo = semanas > 0 ? accionesHechas / semanas : accionesHechas;

  // "X de N acciones" (canon 09): el checklist del plan VIGENTE del tramo.
  const planVigente = [...planes].sort((a, b) => a.created_at.localeCompare(b.created_at)).at(-1);
  const itemsVigente = planVigente ? items.filter((i) => i.plan_id === planVigente.id) : [];
  // Cuentas honestas (gestor de estados): el denominador son las ACTIVAS; las
  // retiradas ('no_aplica') salen del avance y se listan aparte.
  const activasVigente = itemsVigente.filter((i) => i.estado !== "no_aplica");
  const ultimoAvance = completadas.length ? completadas.reduce((a, b) => (a > b ? a : b)) : null;

  return {
    duracionTotalDias,
    accionesHechas,
    accionesVigente: {
      hechas: activasVigente.filter((i) => i.completed_at).length,
      total: activasVigente.length,
    },
    retiradas: itemsVigente
      .filter((i) => i.estado === "no_aplica")
      .map((i) => ({ texto: i.texto ?? "", etapa: i.etapa, motivo: i.no_aplica_motivo ?? null })),
    ritmoAccionesPorSemana: Math.round(ritmo * 10) / 10,
    rachaMasLargaDias: rachaMasLarga(completadas),
    ciclosDePlan: planes.length,
    mundos,
    duracionPorEtapa: duracionPorEtapa(items, chispa),
    diasSinAvance: ultimoAvance ? Math.max(0, dias(ultimoAvance, fin)) : null,
    planVigenteAt: planVigente?.created_at ?? null,
    diasDeVidaPlanVigente: planVigente ? Math.max(0, dias(planVigente.created_at, fin)) : 0,
  };
}

/**
 * Fase 4.2: la lectura de UN MUNDO como el subproyecto que es. Misma capa
 * universal que el core, y su cumplimiento del desglose por dominio (que no
 * mira `baseline_confirmada_at` a propósito: el plan de un mundo nunca se
 * sella, sus ítems se fechan en el ritual del proyecto, y su cumplimiento es
 * real igual).
 *
 * La vida del mundo va de su unlock a su cierre: `duracionTotalDias` cuenta
 * desde que el usuario lo activó, jamás desde la chispa de la idea.
 */
export interface AnalyticsMundo {
  dominio: string;
  universal: CapaUniversal;
  cumplimiento: CumplimientoDominio | null;
  completadoAt: string | null;
  cierreMotivo: string | null;
}

export function analyticsDeMundo(entrada: EntradaAnalytics, dominio: string): AnalyticsMundo | null {
  const mundo = entrada.mundos.find((m) => m.dominio === dominio);
  if (!mundo) return null;
  const items = entrada.items.filter((i) => dominioDe(i) === dominio);
  const planes = (entrada.planesMundo ?? [])
    .filter((p) => p.dominio === dominio && ETIQUETAS_CICLO_PLAN.includes(p.etiqueta))
    .map(({ id, etiqueta, created_at, baseline_confirmada_at }) => ({
      id,
      etiqueta,
      created_at,
      baseline_confirmada_at,
    }));
  const ahora = entrada.ahora ?? new Date().toISOString();
  // El mundo cierra cuando el usuario lo cierra; si la IDEA entera se cerró
  // antes, ese es su horizonte. Un mundo abierto se mide hasta hoy.
  const fin = mundo.completado_at ?? entrada.realizadaAt ?? ahora;
  return {
    dominio,
    universal: capaUniversalDe(items, planes, mundo.unlocked_at, fin, 0),
    cumplimiento: cumplimientoPorDominio(items)[0] ?? null,
    completadoAt: mundo.completado_at ?? null,
    cierreMotivo: mundo.cierre_motivo ?? null,
  };
}

const ETIQUETAS_CICLO_PLAN = ["inicial", "completo", "seguimiento"];

export function calcularAnalytics(entrada: EntradaAnalytics): Analytics {
  const ahora = entrada.ahora ?? new Date().toISOString();
  const chispa = entrada.proyectoCreatedAt;
  const fin = entrada.realizadaAt ?? ahora;

  // Fase 4.1 (V3b): la entrada ya NO excluye los mundos, pero la capa universal
  // SI los ignora: sus etapas colisionarian con las del core en duracionPorEtapa
  // y le moverian el ritmo/la racha al viaje principal. Los mundos se cuentan en
  // el desglose por dominio del cumplimiento.
  const itemsCore = entrada.items.filter(esItemCore);
  // Fase 4.2: la misma capa que mide un mundo (capaUniversalDe) mide el core.
  const universal = capaUniversalDe(itemsCore, entrada.planesCore, chispa, fin, entrada.mundos.length);

  // Capa de cumplimiento: solo si algún plan tiene baseline confirmada.
  let cumplimiento: CapaCumplimiento | null = null;
  const baselinePlan = planBaselineVigente(entrada.planesCore);
  if (baselinePlan) {
    const delPlan = itemsCore.filter((i) => i.plan_id === baselinePlan.id);
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
      // Las tardías que importan: mayor retraso primero, hasta 5.
      tardiasTop: conFecha
        .filter((i) => clasificarCumplimiento(i.completed_at!, i.fecha_base!) === "tardia")
        .map((i) => ({
          texto: i.texto ?? "",
          etapa: i.etapa,
          diasRetraso: Math.round(difDias(i.fecha_base!, i.completed_at!)),
        }))
        .sort((a, b) => b.diasRetraso - a.diasRetraso)
        .slice(0, 5),
      replanificados: delPlan
        .filter((i) => i.fecha_base_original)
        .map((i) => ({ texto: i.texto ?? "", etapa: i.etapa })),
      // V3b: aqui SI entran los mundos, con TODOS los items del proyecto.
      porDominio: cumplimientoPorDominio(entrada.items),
    };
  }

  const hitos = construirHitos(entrada, ahora);
  return {
    universal,
    cumplimiento,
    hitos,
    modoCamino: entrada.modoCamino ?? null,
    cierreMotivo: entrada.cierreMotivo ?? null,
    mundos: entrada.mundos
      .map((m) => analyticsDeMundo(entrada, m.dominio))
      .filter((m): m is AnalyticsMundo => m !== null),
  };
}

/** El timeline de Hitos (§5/§6), construido SOLO de lo persistido. Con
 * incluirAcciones, cada ítem completado suma su propio hito (Celebración). */
const SUBTITULO_CUMPLIMIENTO: Record<CumplimientoItem, string> = {
  a_tiempo: "planificado · a tiempo",
  adelantada: "planificado · adelantada",
  tardia: "planificado · tardía",
};

export function construirHitos(entrada: EntradaAnalytics, ahora: string, incluirAcciones = false): Hito[] {
  const hitos: Hito[] = [
    { fecha: entrada.proyectoCreatedAt, tipo: "chispa", etiqueta: "La Chispa", subtitulo: "La idea nace" },
  ];
  if (entrada.organizadorAt) {
    hitos.push({ fecha: entrada.organizadorAt, tipo: "claridad", etiqueta: "Claridad", subtitulo: "Tu idea, organizada" });
  }
  const ciclos = [...entrada.planesCore].sort((a, b) => a.created_at.localeCompare(b.created_at));
  ciclos.forEach((p, i) => {
    const subtitulo = i === 0 ? (p.baseline_confirmada_at ? "con línea base" : undefined) : "replanificado con lo aprendido";
    hitos.push({ fecha: p.created_at, tipo: "plan", etiqueta: `Tu Plan · ciclo ${i + 1}`, subtitulo });
  });
  for (const m of entrada.mundos) {
    hitos.push({ fecha: m.unlocked_at, tipo: "mundo", etiqueta: "Mundo activado", dominio: m.dominio });
    // Fase 4.2: un mundo cerrado deja su hito en el timeline del PROYECTO —
    // con su motivo discreto de subtítulo si el usuario escribió uno. El
    // nombre humano lo pone la pantalla desde el catálogo; aquí solo la clave.
    if (m.completado_at) {
      hitos.push({
        fecha: m.completado_at,
        tipo: "mundo_completado",
        etiqueta: "Mundo completado",
        dominio: m.dominio,
        subtitulo: m.cierre_motivo?.replace(/\s+/g, " ").trim() || undefined,
      });
    }
  }
  if (incluirAcciones) {
    for (const it of entrada.items) {
      if (!it.completed_at) continue;
      const cumplimiento =
        it.fecha_base ? clasificarCumplimiento(it.completed_at, it.fecha_base) : undefined;
      hitos.push({
        fecha: it.completed_at,
        tipo: "accion",
        etiqueta: it.texto ?? "Acción completada",
        subtitulo: cumplimiento ? SUBTITULO_CUMPLIMIENTO[cumplimiento] : undefined,
        cumplimiento,
      });
    }
  }
  if (entrada.realizadaAt) {
    hitos.push({ fecha: entrada.realizadaAt, tipo: "realizada", etiqueta: "REALIZADA" });
  }
  void ahora;
  return hitos.sort((a, b) => a.fecha.localeCompare(b.fecha));
}

/** El informe descargable (.md), armado del análisis ya calculado. Tono
 * espejo (§6): las tardías se nombran sin regaño. Cero LLM. */
/** Fase 4.0 §8: con `realizadaAt`, el informe abre con su ACTA DE CIERRE
 * (estado final + el motivo del usuario) antes de las estadísticas.
 *
 * Fase 4.2 §3 (jerarquía honesta): el acta dice en qué estado quedaron los
 * mundos. Cerrar el proyecto con mundos abiertos es LEGÍTIMO — la soberanía del
 * usuario manda —, y por eso mismo el acta no lo esconde: "Calidad y Confianza:
 * 3 de 5 (60%), abierta". El nombre humano lo resuelve quien llama
 * (`nombreMundo`); este módulo es puro y no conoce el catálogo. */
export function informeMarkdown(
  nombre: string,
  a: Analytics,
  realizadaAt?: string | null,
  nombreMundo: (dominio: string) => string = (d) => d
): string {
  const u = a.universal;
  const l: string[] = [];
  l.push(`# Análisis de ${nombre}`);
  l.push("");
  if (realizadaAt) {
    l.push("## Acta de cierre");
    l.push(`- Estado final: **Proyecto realizado** el ${realizadaAt.slice(0, 10)}`);
    l.push(
      `- Acciones al cerrar: **${u.accionesVigente.hechas} de ${u.accionesVigente.total}**` +
        (u.accionesVigente.total > 0
          ? ` (${Math.round((u.accionesVigente.hechas / u.accionesVigente.total) * 100)}%)`
          : "")
    );
    for (const m of a.mundos) {
      const v = m.universal.accionesVigente;
      const pct = v.total > 0 ? ` (${Math.round((v.hechas / v.total) * 100)}%)` : "";
      const estado = m.completadoAt ? `completado el ${m.completadoAt.slice(0, 10)}` : "abierta";
      l.push(`- ${nombreMundo(m.dominio)}: **${v.hechas} de ${v.total}**${pct}, ${estado}`);
    }
    if (a.cierreMotivo) {
      l.push("");
      l.push("### Por qué la cerraste aquí");
      l.push(`> ${a.cierreMotivo.replace(/\s+/g, " ").trim()}`);
    }
    l.push("");
  }
  l.push("## Lo que construiste");
  l.push(`- Duración total: **${u.duracionTotalDias} días**`);
  l.push(`- Acciones completadas: **${u.accionesHechas}** de **${u.accionesVigente.total}** activas`);
  l.push(`- Ritmo: **${u.ritmoAccionesPorSemana} acciones por semana**`);
  l.push(`- Racha más larga: **${u.rachaMasLargaDias} días**`);
  l.push(`- Ciclos de plan: **${u.ciclosDePlan}** · Mundos: **${u.mundos}**`);
  // Gestor de estados: las retiradas se nombran aparte, con su porqué en la voz
  // del usuario. No son fracaso ni pendiente: son una decisión que cuenta.
  if (u.retiradas.length) {
    l.push("");
    l.push(`### Retiradas (no aplican): ${u.retiradas.length}`);
    for (const r of u.retiradas) {
      l.push(`- ${r.texto}${r.motivo ? ` — ${r.motivo.replace(/\s+/g, " ").trim()}` : ""}`);
    }
  }
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
