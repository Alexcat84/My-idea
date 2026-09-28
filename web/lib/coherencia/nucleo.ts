/**
 * PRUEBA DE COHERENCIA (construccion 7, decision del fundador, 28 sep 2026): la parte pura del arnes
 * (web/scripts/coherencia.ts). Aqui no hay red: las personas sinteticas, las trampas plantadas ANTES de ver ninguna
 * pregunta real, el lote ciego para el juez, la cuenta contra el umbral y el ahorro del cache.
 *
 * UMBRAL fijado por el fundador ANTES de medir (28 sep 2026):
 *  - 0 desajustes de papel (suponer un jefe, recursos humanos o un equipo que la persona no tiene, o al reves);
 *  - como mucho 1 desajuste de contexto por cada 10 preguntas;
 *  - al menos el 95 % de las adaptadas fieles a su base;
 *  - el juez caza TODAS las trampas.
 */
import { costoLlamadaUsd, type RegistroLlamada } from "../costmeter";
import { REGLA_CONTEXTO_USUARIO } from "../reglaContextoUsuario";

export interface Persona {
  id: string;
  /** la verdad de la persona: contra esto juzga el juez, no contra lo que la app dedujo */
  ficha: { papel: "dueno" | "empleado"; tiene_jefe: boolean; equipo: string; sector: string; etapa: string };
  idea: string;
  /** lo que sabe y como habla, para el actor que responde */
  retrato: string;
}

export const PERSONAS: Persona[] = [
  {
    id: "sola",
    ficha: { papel: "dueno", tiene_jefe: false, equipo: "trabaja sola, sin empleados ni socios", sector: "repostería casera por encargo", etapa: "validacion" },
    idea: "Hago pasteles por encargo en mi casa y quiero saber si puedo vivir de esto. Trabajo sola.",
    retrato:
      "Marta, 34 años, hace pasteles en la cocina de su casa desde hace un año. Trabaja sola: no tiene empleados, socios ni jefe. Vende unos 12 pasteles al mes a conocidos, a 45 dólares cada uno, y no sabe bien cuánto le cuestan. Su prioridad es saber si le alcanza para dejar su trabajo de medio tiempo en una tienda.",
  },
  {
    id: "dos_empleados",
    ficha: { papel: "dueno", tiene_jefe: false, equipo: "dos empleados recién contratados", sector: "taller de macetas de cemento", etapa: "ejecucion" },
    idea: "Tengo un taller de macetas de cemento y acabo de contratar a dos personas. No sé dirigirlas: termino haciendo yo el trabajo.",
    retrato:
      "Julián, 41 años, dueño de un taller de macetas de cemento desde hace tres años. No tiene jefe ni socios. Hace dos meses contrató a dos ayudantes, Rosa y Leo, y no sabe dirigirlos: les habla solo cuando hay un problema y termina haciendo él el trabajo. Vende unas 60 macetas al mes a viveros. Su prioridad es dirigir a sus dos empleados.",
  },
  {
    id: "empleado_mediana",
    ficha: { papel: "empleado", tiene_jefe: true, equipo: "trabaja en un equipo de 8 dentro de una empresa de 120 personas, con recursos humanos", sector: "distribuidora de alimentos", etapa: "ideacion" },
    idea: "Trabajo como coordinador de almacén en una distribuidora de 120 personas y quiero proponerle a mi jefe un servicio de entregas el mismo día.",
    retrato:
      "Andrés, 29 años, coordinador de almacén en una distribuidora de alimentos de 120 personas. Tiene un jefe (el gerente de operaciones) y la empresa tiene recursos humanos. No es dueño de nada: quiere proponer un proyecto interno de entregas el mismo día. Su prioridad es armar una propuesta que su jefe apruebe.",
  },
];

/** Semilla del sorteo de posiciones del lote ciego, escrita antes de la corrida (28 sep 2026). */
export const SEMILLA_LOTE = 20260928;

export type TipoTrampa = "papel" | "contexto" | "fidelidad";

export interface Trampa {
  persona: string;
  tipo: TipoTrampa;
  /** la pregunta que se le muestra al juez como si fuera real */
  pregunta: string;
  /** solo en las de fidelidad: la base de la que dice venir (y que NO respeta) */
  base?: string;
}

/** Trampas sin marca, plantadas ANTES de cualquier corrida: el juez tiene que cazar todas. */
export const TRAMPAS: Trampa[] = [
  { persona: "sola", tipo: "papel", pregunta: "¿Qué le dirías a tu jefe si mañana te pide un informe de cuántos pasteles vendiste?" },
  { persona: "sola", tipo: "papel", pregunta: "¿Cómo reparte hoy el trabajo tu equipo de cocina cuando llegan muchos encargos?" },
  { persona: "sola", tipo: "contexto", pregunta: "Con las tres sucursales que tienes abiertas, ¿cuál vende más pasteles?" },
  {
    persona: "sola",
    tipo: "fidelidad",
    base: "¿Cuánto te cuesta hacer un pastel, contando ingredientes y tu tiempo?",
    pregunta: "¿Qué redes sociales usas para mostrar tus pasteles?",
  },
  { persona: "dos_empleados", tipo: "papel", pregunta: "¿Ya hablaste con recursos humanos para que defina el perfil de Rosa y Leo?" },
  { persona: "dos_empleados", tipo: "papel", pregunta: "¿Qué opina tu jefe de cómo diriges a tus dos ayudantes?" },
  { persona: "dos_empleados", tipo: "contexto", pregunta: "Como trabajas solo en el taller, ¿cuántas macetas alcanzas a hacer tú en una semana?" },
  {
    persona: "dos_empleados",
    tipo: "fidelidad",
    base: "¿Qué esperas exactamente de Rosa y Leo cada semana, y cómo se enteran ellos?",
    pregunta: "¿A qué precio vendes cada maceta a los viveros?",
  },
  { persona: "empleado_mediana", tipo: "papel", pregunta: "Como dueño de la distribuidora, ¿cuánto estás dispuesto a invertir de tu bolsillo?" },
  { persona: "empleado_mediana", tipo: "papel", pregunta: "¿Cuánto te pagas a ti mismo cada mes con lo que deja tu negocio?" },
  { persona: "empleado_mediana", tipo: "contexto", pregunta: "Como trabajas solo desde tu casa, ¿cómo llevarías tú mismo los pedidos?" },
  {
    persona: "empleado_mediana",
    tipo: "fidelidad",
    base: "¿Qué tendría que ver tu jefe en la propuesta para decir que sí?",
    pregunta: "¿Qué tipo de camión compraría la empresa?",
  },
];

/** Una pregunta que la app mostro, tal como se recogio de la corrida. */
export interface PreguntaReal {
  sesion: string;
  espacio: string;
  pregunta: string;
  /** si salio del adaptador: su base y lo que dijo buscar */
  base?: string | null;
}

export interface ItemLote {
  id: string;
  pregunta: string;
  base: string | null;
}

export interface ClaveItem {
  id: string;
  origen: "real" | "trampa";
  tipoTrampa?: TipoTrampa;
  espacio?: string;
  adaptada: boolean;
}

/** PRNG determinista (mulberry32): el mismo lote para la misma semilla. */
export function prng(semilla: number): () => number {
  let a = semilla >>> 0;
  return () => {
    a = (a + 0x6d2b79f5) >>> 0;
    let t = a;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

/** El lote ciego de una persona: sus preguntas reales y sus trampas, barajadas con la semilla, con ids opacos. La
 * clave (que dice que es real y que es trampa) no viaja al juez. */
export function construirLote(
  persona: string,
  reales: PreguntaReal[],
  trampas: Trampa[] = TRAMPAS,
  semilla = SEMILLA_LOTE
): { items: ItemLote[]; clave: ClaveItem[] } {
  const todos: Array<{ item: Omit<ItemLote, "id">; clave: Omit<ClaveItem, "id"> }> = [
    ...reales.map((r) => ({
      item: { pregunta: r.pregunta, base: r.base ?? null },
      clave: { origen: "real" as const, espacio: r.espacio, adaptada: Boolean(r.base) },
    })),
    ...trampas
      .filter((t) => t.persona === persona)
      .map((t) => ({
        item: { pregunta: t.pregunta, base: t.base ?? null },
        clave: { origen: "trampa" as const, tipoTrampa: t.tipo, adaptada: Boolean(t.base) },
      })),
  ];
  const azar = prng(semilla + persona.length);
  for (let i = todos.length - 1; i > 0; i--) {
    const j = Math.floor(azar() * (i + 1));
    [todos[i], todos[j]] = [todos[j], todos[i]];
  }
  return {
    items: todos.map((t, i) => ({ id: `p${i + 1}`, ...t.item })),
    clave: todos.map((t, i) => ({ id: `p${i + 1}`, ...t.clave })),
  };
}

export interface VeredictoItem {
  id: string;
  /** supone un papel o una estructura que la persona no tiene (o le niega uno que si tiene) */
  papel: "ok" | "desajuste";
  /** contradice otro dato de su situacion (sector, tamaño, etapa, lo que ya conto) */
  contexto: "ok" | "desajuste";
  /** solo si trae base: busca lo mismo que la base (su respuesta serviria para elegir lo mismo) */
  fiel: "si" | "no" | null;
}

export interface Metricas {
  preguntasReales: number;
  desajustesPapel: number;
  desajustesContexto: number;
  adaptadasReales: number;
  adaptadasFieles: number;
  trampas: number;
  trampasCazadas: number;
  /** ids de lo que el juez no devolvio: cuenta como no cazada (trampa) o como fallo (real) */
  sinVeredicto: string[];
}

/** La cuenta de un lote contra su clave. Una trampa esta cazada si el juez marca lo que se planto en ella. */
export function contar(veredictos: VeredictoItem[], clave: ClaveItem[]): Metricas {
  const porId = new Map(veredictos.map((v) => [v.id, v]));
  const m: Metricas = {
    preguntasReales: 0,
    desajustesPapel: 0,
    desajustesContexto: 0,
    adaptadasReales: 0,
    adaptadasFieles: 0,
    trampas: 0,
    trampasCazadas: 0,
    sinVeredicto: [],
  };
  for (const c of clave) {
    const v = porId.get(c.id);
    if (!v) m.sinVeredicto.push(c.id);
    if (c.origen === "trampa") {
      m.trampas++;
      const cazada =
        (c.tipoTrampa === "papel" && v?.papel === "desajuste") ||
        (c.tipoTrampa === "contexto" && (v?.contexto === "desajuste" || v?.papel === "desajuste")) ||
        (c.tipoTrampa === "fidelidad" && v?.fiel === "no");
      if (cazada) m.trampasCazadas++;
      continue;
    }
    m.preguntasReales++;
    // sin veredicto, una real cuenta en contra: no se da por buena lo que nadie juzgo
    if (!v || v.papel === "desajuste") m.desajustesPapel++;
    if (v?.contexto === "desajuste") m.desajustesContexto++;
    if (c.adaptada) {
      m.adaptadasReales++;
      if (v?.fiel === "si") m.adaptadasFieles++;
    }
  }
  return m;
}

export function sumarMetricas(ms: Metricas[]): Metricas {
  return ms.reduce(
    (a, m) => ({
      preguntasReales: a.preguntasReales + m.preguntasReales,
      desajustesPapel: a.desajustesPapel + m.desajustesPapel,
      desajustesContexto: a.desajustesContexto + m.desajustesContexto,
      adaptadasReales: a.adaptadasReales + m.adaptadasReales,
      adaptadasFieles: a.adaptadasFieles + m.adaptadasFieles,
      trampas: a.trampas + m.trampas,
      trampasCazadas: a.trampasCazadas + m.trampasCazadas,
      sinVeredicto: [...a.sinVeredicto, ...m.sinVeredicto],
    }),
    { preguntasReales: 0, desajustesPapel: 0, desajustesContexto: 0, adaptadasReales: 0, adaptadasFieles: 0, trampas: 0, trampasCazadas: 0, sinVeredicto: [] }
  );
}

export interface Dictamen {
  cumple: boolean;
  motivos: string[];
}

/** El umbral del fundador, tal cual. Sin preguntas reales no hay medicion: no cumple. */
export function dictaminar(m: Metricas): Dictamen {
  const motivos: string[] = [];
  if (m.preguntasReales === 0) motivos.push("no hay preguntas reales que medir");
  if (m.desajustesPapel > 0) motivos.push(`${m.desajustesPapel} desajuste(s) de papel (umbral 0)`);
  if (m.desajustesContexto * 10 > m.preguntasReales) {
    motivos.push(`${m.desajustesContexto} desajuste(s) de contexto en ${m.preguntasReales} preguntas (umbral 1 por cada 10)`);
  }
  if (m.adaptadasReales > 0 && m.adaptadasFieles < 0.95 * m.adaptadasReales) {
    motivos.push(`${m.adaptadasFieles} de ${m.adaptadasReales} adaptadas fieles (umbral 95 %)`);
  }
  if (m.trampasCazadas < m.trampas) motivos.push(`${m.trampasCazadas} de ${m.trampas} trampas cazadas (umbral todas)`);
  return { cumple: motivos.length === 0, motivos };
}

/** Lo que el cache ahorro en un conjunto de llamadas: su coste sin cache (todo como entrada normal) menos su coste
 * real (lecturas al 10 %, escrituras de 5 min al 125 % y de 1 hora al 200 %). Negativo si el cache costo mas. */
export function ahorroCache(llamadas: RegistroLlamada[]): { conCache: number; sinCache: number; ahorro: number } {
  let conCache = 0;
  let sinCache = 0;
  for (const l of llamadas) {
    conCache += costoLlamadaUsd(l.modelo, l.in, l.out, l.cache_read, l.cache_write_5m, l.cache_write_1h);
    sinCache += costoLlamadaUsd(l.modelo, l.in + l.cache_read + l.cache_write_5m + l.cache_write_1h, l.out);
  }
  return { conCache, sinCache, ahorro: sinCache - conCache };
}

/** Mundo tras mundo: el contexto con que abrio un espacio tiene que traer lo que la persona conto en el anterior. */
export function arrastraLoAnterior(contextoDelSiguiente: string | null, respuestasDelAnterior: string[]): boolean {
  if (!contextoDelSiguiente) return false;
  return respuestasDelAnterior.some((r) => r.trim().length > 0 && contextoDelSiguiente.includes(r.trim()));
}

/** El juez ciego de la prueba (Sonnet). Lleva el criterio de papeles de la regla de la casa 5. */
export const SYSTEM_JUEZ_COHERENCIA = [
  "Eres el juez ciego de una prueba de coherencia de una entrevista de emprendimiento.",
  "Recibes la FICHA VERDADERA de una persona (su papel, si tiene jefe, su equipo, su sector y su etapa) y una lista de",
  "preguntas que se le hicieron. Algunas traen 'base': la pregunta de la que salieron.",
  "",
  "Por CADA pregunta decides tres cosas:",
  "- papel: 'desajuste' si supone un papel o una estructura que la ficha contradice o que la persona no tiene (un jefe",
  "  a quien es dueña de su negocio, recursos humanos, directivos, varios departamentos, un equipo a quien trabaja",
  "  sola), o si le niega uno que si tiene (tratar de dueño a quien es empleado). Preguntarlo en condicional ('si",
  "  tienes a alguien por encima...') o hablar de quien cumple ese papel en su caso es 'ok'.",
  "- contexto: 'desajuste' si contradice otro dato de su situacion (sector, tamaño, etapa, lo que ya se sabe).",
  "- fiel: solo si trae 'base'. 'si' si busca averiguar lo mismo que la base (una respuesta serviria para decidir lo",
  "  mismo), aunque cambie la forma; 'no' si pregunta otra cosa. null si no trae base.",
  "",
  REGLA_CONTEXTO_USUARIO,
  "",
  "Juzga cada pregunta por si misma. No expliques nada. Responde SOLO un array JSON con un objeto por pregunta, con",
  'esta forma exacta: [{"id": "p1", "papel": "ok", "contexto": "ok", "fiel": null}]',
].join("\n");

export function pedidoAlJuez(persona: Persona, items: ItemLote[]): string {
  return JSON.stringify({ ficha_verdadera: persona.ficha, preguntas: items });
}

/** Lee la respuesta del juez; lo que no tenga forma valida se descarta (y cuenta como sin veredicto). */
export function leerVeredictos(texto: string): VeredictoItem[] {
  const ini = texto.indexOf("[");
  const fin = texto.lastIndexOf("]");
  if (ini < 0 || fin < ini) return [];
  let crudo: unknown;
  try {
    crudo = JSON.parse(texto.slice(ini, fin + 1));
  } catch {
    return [];
  }
  if (!Array.isArray(crudo)) return [];
  return crudo.filter(
    (v): v is VeredictoItem =>
      !!v &&
      typeof v === "object" &&
      typeof (v as VeredictoItem).id === "string" &&
      ["ok", "desajuste"].includes((v as VeredictoItem).papel) &&
      ["ok", "desajuste"].includes((v as VeredictoItem).contexto) &&
      [null, "si", "no"].includes((v as VeredictoItem).fiel)
  );
}

/** El actor que responde por la persona sintetica (Haiku): breve, fiel a su retrato, sin inventar lo que no tiene. */
export function systemActor(p: Persona): string {
  return [
    "Eres una persona real respondiendo una entrevista sobre su idea o su negocio. Tu retrato:",
    p.retrato,
    "",
    "Responde cada pregunta en 1 a 3 frases, en español, en primera persona, como hablaría esa persona. Sé fiel a tu",
    "retrato: si te preguntan por algo que no tienes (un jefe, un equipo, recursos humanos), dilo con naturalidad. Si no",
    "sabes un dato, dilo. No hagas preguntas de vuelta ni expliques teoría. Responde solo el texto de tu respuesta.",
  ].join("\n");
}
