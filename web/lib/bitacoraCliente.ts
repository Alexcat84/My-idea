/**
 * bitacoraCliente.ts — Fase 4.8 "La bitácora del cliente": la historia
 * completa de una idea, del inicio al cierre, contada como documento.
 *
 * Es un LECTOR PURO: ensambla la línea de tiempo cronológica ASCENDENTE desde
 * las fuentes que YA existen (proyecto, sesiones, planes, checklist, la
 * bitácora de eventos y los mundos). No escribe nada, no llama al motor, no
 * cuesta créditos.
 *
 * LISTA BLANCA (§7.1, confidencialidad): solo se narran eventos que son
 * HISTORIA DEL USUARIO. La mecánica interna (cobros, vetos del intérprete,
 * telemetría, reversas técnicas) JAMÁS aparece: no es su historia.
 *
 * VOZ: segunda persona, palabras de persona, etiquetas de cara (jamás claves
 * técnicas). Timestamps ABSOLUTOS (fecha completa; la hora solo cuando el mismo
 * día tiene 2+ entradas, como el historial). Los motivos del usuario se citan
 * en su voz entre comillas.
 *
 * HONESTIDAD CON EL PASADO: lo que no quedó registrado en su día simplemente no
 * aparece. Nunca se inventa ni se estima una entrada.
 */
import { fechaHumanaConAno, fechaInputLocal } from "./fechas";

export interface SesionBita {
  created_at: string;
  tipo: string; // gratuito | inicial | seguimiento | reporte
  dominio: string | null;
}

export interface PlanBita {
  etiqueta: string; // organizador | inicial | completo | seguimiento | reporte_numeros
  created_at: string;
  dominio: string | null;
  baseline_confirmada_at: string | null;
}

export interface ItemBita {
  id: string;
  texto: string;
  completed_at: string | null;
  /** dominio del ítem: null/'core' = viaje principal; otro = un mundo. Sirve
   * para etiquetar en la bitácora QUÉ mundo (mapa de lecciones aprendidas). */
  dominio: string | null;
}

export interface EventoBita {
  tipo: string;
  payload: Record<string, unknown>;
  created_at: string;
}

export interface DatosBitacora {
  nombreIdea: string;
  creadaAt: string;
  realizadaAt: string | null;
  sesiones: SesionBita[];
  planes: PlanBita[];
  items: ItemBita[];
  eventos: EventoBita[];
  /** dominio técnico → nombre de cara del mundo (jamás la clave) */
  nombreMundo: (dominio: string) => string;
  /** momento de la descarga (para el rango de fechas del documento) */
  generadoAt: string;
}

/** El peso visual de una entrada (regla de Design). Solo lo usa el render de la
 * página/papel para tamaño y color; el .md ignora el peso (es texto puro). */
export type PesoBitacora = "hito" | "accion" | "retirada" | "cierre";

export interface EntradaBitacora {
  /** ISO del momento; ordena y fija el día/hora en el render */
  fecha: string;
  /** la línea, en voz de persona, sin la fecha (la pone el render) */
  texto: string;
  /** hito (momento estructural), accion (avance diario), retirada (no aplica),
   * cierre (marcó realizada) — el único verde. */
  peso: PesoBitacora;
  /** nombre corto para el mapa de hitos (solo hito/cierre; el resto lo omite) */
  titulo?: string;
  /** El ESPACIO al que pertenece (Fase 3): "core" | clave de mundo | null.
   * `null` = NO-DERIVABLE (evento de ítem cuyo ítem ya no existe y no estampó
   * dominio): visible SOLO en la bitácora global con etiqueta neutra, ausente de
   * todas las específicas. Nunca se inventa pertenencia. Ver `bitacoraDeEspacio`. */
  dominio: string | null;
}

const esCore = (d: string | null | undefined) => !d || d === "core";
const corto = (s: string, max = 90) => {
  const limpio = s.replace(/\s+/g, " ").trim();
  return limpio.length > max ? `${limpio.slice(0, max - 1).trimEnd()}…` : limpio;
};

/** Los tipos de evento de la bitácora que SÍ son historia del usuario. Cualquier
 * otro (cobro_carrera, mundo_incompatible, y todo lo interno o futuro) se cae
 * por defecto: la lista es BLANCA, no negra. */
const EVENTOS_NARRABLES = new Set([
  "modo_camino",
  "item_estado",
  "item_no_aplica",
  "item_reactivada",
  "fecha_movida",
  "fecha_hecho_movida",
  "nota_escrita",
  "mundo_completado",
  "preview_iniciado",
  "preview_completado",
  "preview_a_compra",
  "realizada",
]);

/** Eventos ligados a un ÍTEM (su dominio se deriva del ítem o de la estampa). */
const EVENTOS_DE_ITEM = new Set(["item_estado", "item_no_aplica", "item_reactivada", "fecha_hecho_movida", "nota_escrita", "fecha_movida"]);
/** Eventos ligados a un MUNDO (su dominio es `payload.mundo`). */
const EVENTOS_DE_MUNDO = new Set(["mundo_completado", "preview_iniciado", "preview_completado", "preview_a_compra"]);

/** Ensambla las entradas de la bitácora, en orden cronológico ASCENDENTE. */
export function construirBitacora(d: DatosBitacora): EntradaBitacora[] {
  const E: EntradaBitacora[] = [];
  // `dominio` etiqueta el espacio de la entrada (Fase 3). Por defecto "core":
  // los hitos derivados del viaje principal lo son; los de mundo/ítem lo pasan.
  const push = (
    fecha: string | null | undefined,
    texto: string,
    peso: PesoBitacora = "accion",
    titulo?: string,
    dominio: string | null = "core",
  ) => {
    if (fecha) E.push({ fecha, texto, peso, titulo, dominio });
  };
  const textoDe = new Map(d.items.map((i) => [i.id, i.texto]));
  const dominioDe = new Map(d.items.map((i) => [i.id, i.dominio]));
  const accion = (id: unknown) => corto(textoDe.get(String(id)) ?? "una actividad");
  // Sufijo de mundo: si el ítem pertenece a un mundo (no al core), la entrada
  // dice EN QUÉ mundo pasó. Así el mapa de lecciones distingue cada carril.
  const sufMundo = (id: unknown) => {
    const dom = dominioDe.get(String(id));
    return dom && !esCore(dom) ? ` · en ${d.nombreMundo(dom)}` : "";
  };
  const ref = (id: unknown) => `«${accion(id)}»${sufMundo(id)}`;
  const cita = (m: unknown) => (typeof m === "string" && m.trim() ? `: «${m.replace(/\s+/g, " ").trim()}»` : ".");

  // ── Hitos derivados de timestamps existentes ──────────────────────────────
  push(d.creadaAt, "Encendiste la chispa y escribiste tu idea.", "hito", "La Chispa");

  const coreOrg = d.planes.find((p) => esCore(p.dominio) && p.etiqueta === "organizador");
  push(coreOrg?.created_at, "Ordenaste tu idea y ganaste claridad.", "hito", "Tu idea ordenada");

  const explora = d.sesiones.find((s) => esCore(s.dominio) && s.tipo === "inicial");
  push(explora?.created_at, "Empezaste a explorar tu idea, pregunta por pregunta.");

  const corePlan = d.planes.find((p) => esCore(p.dominio) && (p.etiqueta === "completo" || p.etiqueta === "inicial"));
  push(corePlan?.created_at, "Recibiste tu plan.", "hito", "Tu Plan");

  // Seguimientos (recálculos del plan), numerados por orden cronológico.
  const segs = d.planes
    .filter((p) => esCore(p.dominio) && p.etiqueta === "seguimiento")
    .sort((a, b) => a.created_at.localeCompare(b.created_at));
  segs.forEach((p, i) => push(p.created_at, `Contaste qué pasó y recalculé tu plan (seguimiento ${i + 1}).`, "hito", `Seguimiento ${i + 1}`));

  // Línea base sellada: un sello por plan que tenga su marca. El sello pertenece
  // al ESPACIO de su plan (Fase 3), no siempre al core.
  for (const p of d.planes) {
    if (p.baseline_confirmada_at)
      push(p.baseline_confirmada_at, "Aceptaste tus fechas: tu línea base quedó sellada.", "hito", "Tu línea base", esCore(p.dominio) ? "core" : p.dominio);
  }

  // Tus Números, versionados por orden. Cada versión pertenece al espacio de su
  // plan (Fase 3); en la práctica es del core, pero se lee del dato, no se asume.
  const nums = d.planes
    .filter((p) => p.etiqueta === "reporte_numeros")
    .sort((a, b) => a.created_at.localeCompare(b.created_at));
  nums.forEach((p, i) =>
    push(p.created_at, `Calculaste Tus Números${nums.length > 1 ? ` (versión ${i + 1})` : ""}.`, "hito", "Tus Números", esCore(p.dominio) ? "core" : p.dominio),
  );

  // Planes de mundo generados (pertenecen a su mundo).
  for (const p of d.planes) {
    if (!esCore(p.dominio) && (p.etiqueta === "inicial" || p.etiqueta === "completo" || p.etiqueta === "seguimiento")) {
      push(p.created_at, `Se generó tu plan de ${d.nombreMundo(p.dominio!)}.`, "hito", d.nombreMundo(p.dominio!), p.dominio!);
    }
  }

  // Cada acción marcada HECHA, con su fecha de realización (y el mundo, si aplica).
  for (const it of d.items)
    if (it.completed_at)
      push(
        it.completed_at,
        `Marcaste hecha «${corto(it.texto)}»${esCore(it.dominio) ? "" : ` · en ${d.nombreMundo(it.dominio!)}`}.`,
        "accion",
        undefined,
        esCore(it.dominio) ? "core" : it.dominio,
      );

  // ── Eventos registrados (lista blanca) ────────────────────────────────────
  const huboRealizada = d.eventos.some((e) => e.tipo === "realizada" && (e.payload?.accion ?? "realizar") === "realizar");
  for (const e of d.eventos) {
    if (!EVENTOS_NARRABLES.has(e.tipo)) continue; // internos y futuros: fuera
    const p = e.payload ?? {};
    // El ESPACIO del evento (Fase 3), sin inventar pertenencia: estampa del
    // payload → JOIN por ítem → mundo directo → core (eventos de proyecto). Un
    // evento de ítem cuyo ítem ya no existe y no estampó dominio es NO-DERIVABLE
    // (null): solo la bitácora global, jamás una específica.
    let domEvento: string | null = "core";
    if (EVENTOS_DE_ITEM.has(e.tipo)) {
      if (typeof p.dominio === "string" && p.dominio) domEvento = esCore(p.dominio) ? "core" : p.dominio;
      else {
        const dom = dominioDe.get(String(p.item));
        domEvento = dom === undefined ? null : esCore(dom) ? "core" : dom;
      }
    } else if (EVENTOS_DE_MUNDO.has(e.tipo)) {
      const m = String(p.mundo);
      domEvento = esCore(m) ? "core" : m;
    }
    const pushE = (fecha: string | null | undefined, texto: string, peso: PesoBitacora = "accion", titulo?: string) =>
      push(fecha, texto, peso, titulo, domEvento);
    switch (e.tipo) {
      case "modo_camino": {
        const a = p.a === "fechas" ? "con fechas y recordatorios" : "a tu ritmo";
        pushE(e.created_at, p.de ? `Cambiaste tu forma de avanzar: ${a}.` : `Elegiste llevar tu camino ${a}.`);
        break;
      }
      case "item_estado": {
        if (p.a === "empezado") pushE(e.created_at, `Empezaste ${ref(p.item)}.`);
        else if (p.a === "en_proceso") pushE(e.created_at, `Pusiste ${ref(p.item)} en proceso.`);
        else if (p.a === "pendiente") pushE(e.created_at, `Devolviste ${ref(p.item)} a pendiente.`);
        break;
      }
      case "item_no_aplica":
        pushE(e.created_at, `Retiraste ${ref(p.item)}${cita(p.motivo)}`, "retirada");
        break;
      case "item_reactivada":
        pushE(e.created_at, `Reactivaste ${ref(p.item)}.`);
        break;
      case "fecha_hecho_movida":
        pushE(e.created_at, `Ajustaste la fecha en que hiciste ${ref(p.item)}.`);
        break;
      case "nota_escrita":
        pushE(e.created_at, `Anotaste algo en ${ref(p.item)}.`);
        break;
      case "fecha_movida": {
        const n = typeof p.cascada === "number" ? p.cascada : 0;
        const delta = typeof p.delta_dias === "number" ? p.delta_dias : 0;
        const rumbo = delta >= 0 ? `${Math.abs(delta)} ${Math.abs(delta) === 1 ? "día" : "días"} después` : `${Math.abs(delta)} ${Math.abs(delta) === 1 ? "día" : "días"} antes`;
        const cola = n > 0 ? ` y las ${n} siguientes, ${rumbo} cada una.` : ".";
        pushE(e.created_at, `Moviste la fecha de ${ref(p.item)}${cola}`);
        break;
      }
      case "mundo_completado": {
        const nombre = d.nombreMundo(String(p.mundo));
        if (p.accion === "reabrir") pushE(e.created_at, `Reabriste el mundo ${nombre}.`);
        else pushE(e.created_at, `Completaste el mundo ${nombre}${cita(p.motivo)}`, "hito", nombre);
        break;
      }
      case "preview_iniciado":
        pushE(e.created_at, `Exploraste gratis el mundo ${d.nombreMundo(String(p.mundo))}.`);
        break;
      case "preview_completado":
        pushE(e.created_at, `Tu diagnóstico de ${d.nombreMundo(String(p.mundo))} quedó listo.`, "hito", d.nombreMundo(String(p.mundo)));
        break;
      case "preview_a_compra":
        pushE(e.created_at, `Sumaste el plan completo de ${d.nombreMundo(String(p.mundo))}.`, "hito", d.nombreMundo(String(p.mundo)));
        break;
      case "realizada":
        if (p.accion === "reabrir") pushE(e.created_at, "Reabriste tu idea para seguir trabajándola.");
        else pushE(e.created_at, `Marcaste tu idea como realizada${cita(p.motivo)}`, "cierre", "Realizado");
        break;
    }
  }

  // Honestidad con el pasado: si la idea está realizada pero su cierre es de una
  // era sin bitácora, deriva la entrada del timestamp (no se inventa: existe).
  if (d.realizadaAt && !huboRealizada) push(d.realizadaAt, "Marcaste tu idea como realizada.", "cierre", "Realizado");

  // Orden cronológico ascendente. El sort es estable: a igual instante, se
  // conserva el orden de inserción (hitos derivados antes que eventos sueltos).
  return E.sort((a, b) => a.fecha.localeCompare(b.fecha));
}

/**
 * La bitácora de UN espacio (Fase 3): filtra las entradas ya etiquetadas por
 * `dominio`. Core = "core"; un mundo = su clave. Las entradas NO-DERIVABLES
 * (`dominio: null`) NUNCA aparecen en una específica — viven solo en la global.
 *
 * PARTICIÓN EXACTA (addendum): unión de todas las específicas = global − {las
 * no-derivables}. Cada entrada derivable cae en exactamente un espacio; ninguna
 * se inventa una pertenencia.
 */
export function bitacoraDeEspacio(entradas: EntradaBitacora[], dominio: string): EntradaBitacora[] {
  const clave = esCore(dominio) ? "core" : dominio;
  return entradas.filter((e) => e.dominio === clave);
}

function hora(iso: string): string {
  const d = new Date(iso);
  return `${String(d.getHours()).padStart(2, "0")}:${String(d.getMinutes()).padStart(2, "0")}`;
}

/** El cuerpo de la secuencia (agrupado por día), sin portada: lo comparten el
 * documento suelto y la sección del expediente. La hora solo aparece en los
 * días con 2+ entradas (regla del historial). `nivel` es el de los subtítulos
 * de día (### suelto; #### bajo el ## del expediente). */
export function bitacoraCuerpo(entradas: EntradaBitacora[], nivel = 3): string[] {
  const l: string[] = [];
  const almo = "#".repeat(nivel);
  const porDia = new Map<string, number>();
  for (const e of entradas) {
    const k = fechaInputLocal(new Date(e.fecha));
    porDia.set(k, (porDia.get(k) ?? 0) + 1);
  }
  let diaAnterior = "";
  for (const e of entradas) {
    const dia = fechaInputLocal(new Date(e.fecha));
    if (dia !== diaAnterior) {
      l.push("");
      l.push(`${almo} ${fechaHumanaConAno(e.fecha)}`);
      l.push("");
      diaAnterior = dia;
    }
    const conHora = (porDia.get(dia) ?? 0) >= 2;
    l.push(`- ${conHora ? `**${hora(e.fecha)}** · ` : ""}${e.texto}`);
  }
  return l;
}

/** El documento markdown de la bitácora: portada + la secuencia. El .md y el
 * PDF salen de aquí (una sola verdad). */
export function bitacoraMarkdown(nombreIdea: string, entradas: EntradaBitacora[], generadoAt: string): string {
  const l: string[] = [];
  l.push(`# La historia de ${nombreIdea}`);
  l.push("");
  if (entradas.length === 0) {
    l.push(`> Generada el ${fechaHumanaConAno(generadoAt)}`);
    l.push("");
    l.push("Tu historia apenas empieza. Cada paso que des irá quedando aquí.");
    l.push("");
    return l.join("\n");
  }
  l.push(`> Del ${fechaHumanaConAno(entradas[0].fecha)} al ${fechaHumanaConAno(entradas[entradas.length - 1].fecha)}`);
  l.push(...bitacoraCuerpo(entradas, 3));
  l.push("");
  return l.join("\n");
}
