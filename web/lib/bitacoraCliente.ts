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

export interface EntradaBitacora {
  /** ISO del momento; ordena y fija el día/hora en el render */
  fecha: string;
  /** la línea, en voz de persona, sin la fecha (la pone el render) */
  texto: string;
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
  "item_no_aplica",
  "item_reactivada",
  "fecha_movida",
  "mundo_completado",
  "preview_iniciado",
  "preview_completado",
  "preview_a_compra",
  "realizada",
]);

/** Ensambla las entradas de la bitácora, en orden cronológico ASCENDENTE. */
export function construirBitacora(d: DatosBitacora): EntradaBitacora[] {
  const E: EntradaBitacora[] = [];
  const push = (fecha: string | null | undefined, texto: string) => {
    if (fecha) E.push({ fecha, texto });
  };
  const textoDe = new Map(d.items.map((i) => [i.id, i.texto]));
  const accion = (id: unknown) => corto(textoDe.get(String(id)) ?? "una actividad");
  const cita = (m: unknown) => (typeof m === "string" && m.trim() ? `: «${m.replace(/\s+/g, " ").trim()}»` : ".");

  // ── Hitos derivados de timestamps existentes ──────────────────────────────
  push(d.creadaAt, "Encendiste la chispa y escribiste tu idea.");

  const coreOrg = d.planes.find((p) => esCore(p.dominio) && p.etiqueta === "organizador");
  push(coreOrg?.created_at, "Ordenaste tu idea y ganaste claridad.");

  const explora = d.sesiones.find((s) => esCore(s.dominio) && s.tipo === "inicial");
  push(explora?.created_at, "Empezaste a explorar tu idea, pregunta por pregunta.");

  const corePlan = d.planes.find((p) => esCore(p.dominio) && (p.etiqueta === "completo" || p.etiqueta === "inicial"));
  push(corePlan?.created_at, "Recibiste tu plan.");

  // Seguimientos (recálculos del plan), numerados por orden cronológico.
  const segs = d.planes
    .filter((p) => esCore(p.dominio) && p.etiqueta === "seguimiento")
    .sort((a, b) => a.created_at.localeCompare(b.created_at));
  segs.forEach((p, i) => push(p.created_at, `Contaste qué pasó y recalculé tu plan (seguimiento ${i + 1}).`));

  // Línea base sellada: un sello por plan que tenga su marca.
  for (const p of d.planes) {
    if (p.baseline_confirmada_at) push(p.baseline_confirmada_at, "Aceptaste tus fechas: tu línea base quedó sellada.");
  }

  // Tus Números, versionados por orden.
  const nums = d.planes
    .filter((p) => p.etiqueta === "reporte_numeros")
    .sort((a, b) => a.created_at.localeCompare(b.created_at));
  nums.forEach((p, i) => push(p.created_at, `Calculaste Tus Números${nums.length > 1 ? ` (versión ${i + 1})` : ""}.`));

  // Planes de mundo generados.
  for (const p of d.planes) {
    if (!esCore(p.dominio) && (p.etiqueta === "inicial" || p.etiqueta === "completo" || p.etiqueta === "seguimiento")) {
      push(p.created_at, `Se generó tu plan de ${d.nombreMundo(p.dominio!)}.`);
    }
  }

  // Cada acción marcada HECHA, con su fecha de realización.
  for (const it of d.items) if (it.completed_at) push(it.completed_at, `Marcaste hecha «${corto(it.texto)}».`);

  // ── Eventos registrados (lista blanca) ────────────────────────────────────
  const huboRealizada = d.eventos.some((e) => e.tipo === "realizada" && (e.payload?.accion ?? "realizar") === "realizar");
  for (const e of d.eventos) {
    if (!EVENTOS_NARRABLES.has(e.tipo)) continue; // internos y futuros: fuera
    const p = e.payload ?? {};
    switch (e.tipo) {
      case "modo_camino": {
        const a = p.a === "fechas" ? "con fechas y recordatorios" : "a tu ritmo";
        push(e.created_at, p.de ? `Cambiaste tu forma de avanzar: ${a}.` : `Elegiste llevar tu camino ${a}.`);
        break;
      }
      case "item_no_aplica":
        push(e.created_at, `Retiraste «${accion(p.item)}»${cita(p.motivo)}`);
        break;
      case "item_reactivada":
        push(e.created_at, `Reactivaste «${accion(p.item)}».`);
        break;
      case "fecha_movida": {
        const n = typeof p.cascada === "number" ? p.cascada : 0;
        const delta = typeof p.delta_dias === "number" ? p.delta_dias : 0;
        const rumbo = delta >= 0 ? `${Math.abs(delta)} ${Math.abs(delta) === 1 ? "día" : "días"} después` : `${Math.abs(delta)} ${Math.abs(delta) === 1 ? "día" : "días"} antes`;
        const cola = n > 0 ? ` y las ${n} siguientes, ${rumbo} cada una.` : ".";
        push(e.created_at, `Moviste la fecha de «${accion(p.item)}»${cola}`);
        break;
      }
      case "mundo_completado": {
        const nombre = d.nombreMundo(String(p.mundo));
        if (p.accion === "reabrir") push(e.created_at, `Reabriste el mundo ${nombre}.`);
        else push(e.created_at, `Completaste el mundo ${nombre}${cita(p.motivo)}`);
        break;
      }
      case "preview_iniciado":
        push(e.created_at, `Exploraste gratis el mundo ${d.nombreMundo(String(p.mundo))}.`);
        break;
      case "preview_completado":
        push(e.created_at, `Tu diagnóstico de ${d.nombreMundo(String(p.mundo))} quedó listo.`);
        break;
      case "preview_a_compra":
        push(e.created_at, `Sumaste el plan completo de ${d.nombreMundo(String(p.mundo))}.`);
        break;
      case "realizada":
        if (p.accion === "reabrir") push(e.created_at, "Reabriste tu idea para seguir trabajándola.");
        else push(e.created_at, `Marcaste tu idea como realizada${cita(p.motivo)}`);
        break;
    }
  }

  // Honestidad con el pasado: si la idea está realizada pero su cierre es de una
  // era sin bitácora, deriva la entrada del timestamp (no se inventa: existe).
  if (d.realizadaAt && !huboRealizada) push(d.realizadaAt, "Marcaste tu idea como realizada.");

  // Orden cronológico ascendente. El sort es estable: a igual instante, se
  // conserva el orden de inserción (hitos derivados antes que eventos sueltos).
  return E.sort((a, b) => a.fecha.localeCompare(b.fecha));
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
