/**
 * CONSTRUCCION 2 (decision del fundador, 28 sep 2026, docs/REGLAS_DE_LA_CASA.md): el ADAPTADOR de preguntas.
 *
 * Las preguntas de la cache (preguntas_cache.json) son PREGUNTAS BASE: se escribieron para cualquiera, y muchas vienen
 * de libros pensados para empresas grandes (un jefe, recursos humanos, varios departamentos). La base NO se toca. Toda
 * pregunta que va a salir de la cache, o la generica de un nodo sin pregunta, pasa por aqui: Haiku la dice a ESTA
 * persona (su ficha y lo que ya conto, en el bloque de contexto de 1 hora) y en el idioma de su idea. Cambia la forma,
 * nunca el fondo: devuelve tambien una linea con lo que la pregunta busca, que queda en el evento para que el juez de
 * la prueba de coherencia compare con la base. Sustituye a la traduccion (preguntaEnIdioma): adapta y traduce a la vez.
 *
 * Los cinco caminos por los que una pregunta salia cruda (la entrada a un mundo, la re-eleccion de puerta, el respaldo
 * del interprete, la pregunta dirigida fallida y la copia literal) terminan todos igual: el turno sale con la pregunta
 * de la cache del ultimo nodo de la ruta. Por eso hay un solo embudo, adaptarResultadoTurno, al final del turno.
 *
 * SALIDA SEGURA: si la llamada falla, tarda o devuelve algo que no pasa las comprobaciones, sale la version NEUTRAL de
 * la cache (`pregunta_neutral`, un campo aparte: la base sigue intacta), nunca la base cruda. Mientras un nodo no tenga
 * neutral (se generan en la corrida final), sale una PLANTILLA NEUTRAL generica sin roles supuestos (visto del
 * fundador, 28 sep 2026, punto 1): la generica que nombra el tema por su etiqueta, o, si la etiqueta supone un papel
 * (equipo, jefe, socios), la que no nombra tema. El evento dice cual salio.
 */
import type Anthropic from "@anthropic-ai/sdk";
import { llamarClaude, MODEL_HAIKU, type UsoAcumulado } from "../costmeter";
import { SYSTEM_ADAPTAR_PREGUNTA } from "../prompts";
import type { Locale } from "../i18n/config";
import { contextoDeSesion, type FichaContexto } from "./memoria";
import { etiquetaArbol, obtenerPregunta, resolverId, type Grafo, type NodoGrafo, type PreguntasCache } from "./graph";
import { elegir } from "../i18n/config";
import { MOTOR } from "../i18n/mensajes/motor";
import type { EventoAdaptacionPregunta, EventoInterprete } from "./interprete";

/** Lo que tarda de mas una adaptacion antes de dar paso a la neutral: la persona esta esperando su pregunta. */
export const TIEMPO_MAX_ADAPTADOR_MS = 8000;
/** Cuantos siguientes del nodo viajan como ancla del fondo. */
const MAX_SIGUIENTES = 6;

export type SalidaAdaptador = "adaptada" | "neutral" | "plantilla_neutral";

/** Una etiqueta de nodo que supone un papel o una estructura (la mira en español, que es la del grafo). 100 de las
 * 3.169 etiquetas vivas lo hacen ("Alinea a tu Equipo con el Mapa") al 28 sep 2026. */
const SUPONE_PAPEL = /\b(jef[ea]s?|recursos humanos|directiv\w*|departamento\w*|emplead\w*|equipo\w*|subordinad\w*|gerente\w*|socio\w*|colaborador\w*|junta)\b/i;

export function supuestoDePapel(etiqueta: string): boolean {
  return SUPONE_PAPEL.test(etiqueta);
}

/** La plantilla neutral de un nodo: la generica con su tema si su etiqueta no supone papeles; si los supone, la que
 * no nombra tema. Nunca la base. */
export function plantillaNeutral(nodo: string, n: NodoGrafo, idioma: Locale): string {
  if (supuestoDePapel(n.etiqueta_arbol ?? n.titulo_concepto ?? "")) return elegir(MOTOR, idioma).preguntaNeutralSinTema;
  return obtenerPregunta(nodo, n, {}, idioma);
}

export interface EntradaAdaptador {
  nodo: string;
  /** la pregunta base de la cache (o la generica del nodo) */
  base: string;
  /** la version neutral de la cache, sin roles supuestos; null si el nodo aun no la tiene */
  neutral: string | null;
  /** la plantilla neutral generica (plantillaNeutral): la salida segura cuando no hay neutral */
  plantilla: string;
  /** las etiquetas de los siguientes entre los que la respuesta ayuda a elegir */
  siguientes: string[];
}

export interface ResultadoAdaptador {
  pregunta: string;
  busca: string | null;
  acumulado: UsoAcumulado;
  salida: SalidaAdaptador;
  fallo?: string;
}

type Comprobacion = { ok: true; pregunta: string; busca: string } | { ok: false; motivo: string };

const SIGNOS_PREGUNTA = /[?？؟]/;

/** Lo que el codigo exige antes de mostrar una adaptada. El fondo (que busque lo mismo) no se puede comprobar aqui:
 * lo mide el juez de la prueba de coherencia con el `busca` de cada evento. */
export function comprobarAdaptada(base: string, salida: string): Comprobacion {
  const ini = salida.indexOf("{");
  const fin = salida.lastIndexOf("}");
  let crudo: unknown;
  try {
    if (ini < 0 || fin < ini) throw new Error("sin objeto");
    crudo = JSON.parse(salida.slice(ini, fin + 1));
  } catch {
    return { ok: false, motivo: "no_json" };
  }
  const o = (crudo ?? {}) as { pregunta?: unknown; busca?: unknown };
  const pregunta = typeof o.pregunta === "string" ? o.pregunta.trim() : "";
  const busca = typeof o.busca === "string" ? o.busca.trim() : "";
  if (!pregunta) return { ok: false, motivo: "vacia" };
  if (SIGNOS_PREGUNTA.test(base) && !SIGNOS_PREGUNTA.test(pregunta)) return { ok: false, motivo: "no_es_pregunta" };
  if (/[—–]/.test(pregunta)) return { ok: false, motivo: "guion_largo" };
  if (pregunta.length > Math.max(2 * base.length, base.length + 200)) return { ok: false, motivo: "demasiado_larga" };
  if (!busca) return { ok: false, motivo: "sin_busca" };
  return { ok: true, pregunta, busca };
}

function conTope<T>(p: Promise<T>, ms: number): Promise<T> {
  let t: ReturnType<typeof setTimeout> | undefined;
  const tope = new Promise<never>((_, rechazar) => {
    t = setTimeout(() => rechazar(new Error(`el adaptador tardo mas de ${ms} ms`)), ms);
  });
  return Promise.race([p, tope]).finally(() => clearTimeout(t));
}

/** Adapta UNA pregunta. Nunca lanza: ante cualquier problema, la salida segura. */
export async function adaptarPregunta(
  client: Anthropic,
  entrada: EntradaAdaptador,
  acumulado: UsoAcumulado,
  opts: { idiomaSalida: string | null; contexto: string | null; tiempoMaxMs?: number }
): Promise<ResultadoAdaptador> {
  const segura = (fallo: string, acc: UsoAcumulado): ResultadoAdaptador =>
    entrada.neutral
      ? { pregunta: entrada.neutral, busca: null, acumulado: acc, salida: "neutral", fallo }
      : { pregunta: entrada.plantilla, busca: null, acumulado: acc, salida: "plantilla_neutral", fallo };
  const turno = JSON.stringify({ pregunta_base: entrada.base, sirve_para_elegir_entre: entrada.siguientes });
  let r: { texto: string; acumulado: UsoAcumulado };
  try {
    r = await conTope(
      llamarClaude(client, SYSTEM_ADAPTAR_PREGUNTA, turno, MODEL_HAIKU, acumulado, {
        maxTokens: 400,
        componente: "adaptador",
        idiomaSalida: opts.idiomaSalida,
        contexto: opts.contexto,
      }),
      opts.tiempoMaxMs ?? TIEMPO_MAX_ADAPTADOR_MS
    );
  } catch (e) {
    const fallo = e instanceof Error ? e.message : String(e);
    console.error(`[adaptador] ${entrada.nodo}: sale la salida segura:`, fallo);
    return segura(fallo, acumulado);
  }
  const c = comprobarAdaptada(entrada.base, r.texto);
  if (!c.ok) {
    console.error(`[adaptador] ${entrada.nodo}: la adaptada no pasa (${c.motivo}); sale la salida segura`);
    return segura(c.motivo, r.acumulado);
  }
  return { pregunta: c.pregunta, busca: c.busca, acumulado: r.acumulado, salida: "adaptada" };
}

/**
 * El embudo: si el turno sale con la pregunta de la cache del ultimo nodo de la ruta (su base, su neutral o la
 * generica si no tiene), la pasa por el adaptador y deja la adaptada como pendiente y en el historial anti-repeticion
 * (lo que la persona leyo). Una pregunta que ya redacto el interprete no se toca.
 */
export async function adaptarResultadoTurno<
  R extends {
    tipo: string;
    pregunta?: string;
    acumulado: UsoAcumulado;
    estado: {
      ruta: string[];
      idioma?: string;
      contextoProyecto?: string | null;
      ficha?: FichaContexto;
      preguntaPendiente: string | null;
      ultimasPreguntas: string[];
      fallbackEvents: EventoInterprete[];
    };
  },
>(
  client: Anthropic,
  resultado: R,
  datos: { graph: Grafo; preguntasCache: PreguntasCache; idiomaPlantilla: Locale; tiempoMaxMs?: number }
): Promise<R> {
  if (resultado.tipo !== "pregunta" || !resultado.pregunta) return resultado;
  const ultimo = resultado.estado.ruta[resultado.estado.ruta.length - 1];
  if (!ultimo) return resultado;
  const nodo = resolverId(ultimo, datos.graph) ?? ultimo;
  const n = datos.graph[nodo];
  if (!n) return resultado;
  const entradaCache = datos.preguntasCache[nodo];
  const base = obtenerPregunta(nodo, n, datos.preguntasCache, datos.idiomaPlantilla);
  const neutral = typeof entradaCache?.pregunta_neutral === "string" && entradaCache.pregunta_neutral.trim() ? entradaCache.pregunta_neutral : null;
  const mostrada = resultado.pregunta;
  if (mostrada !== base && mostrada !== neutral) return resultado;

  const candidatos = Array.isArray(entradaCache?.candidatos) ? (entradaCache.candidatos as unknown[]) : [];
  const siguientes = candidatos
    .filter((c): c is string => typeof c === "string")
    .map((c) => resolverId(c, datos.graph) ?? c)
    .filter((c) => datos.graph[c])
    .slice(0, MAX_SIGUIENTES)
    .map((c) => etiquetaArbol(c, datos.graph));

  const plantilla = plantillaNeutral(nodo, n, datos.idiomaPlantilla);
  const a = await adaptarPregunta(client, { nodo, base, neutral, plantilla, siguientes }, resultado.acumulado, {
    idiomaSalida: resultado.estado.idioma ?? null,
    contexto: contextoDeSesion(resultado.estado),
    tiempoMaxMs: datos.tiempoMaxMs,
  });
  const evento: EventoAdaptacionPregunta = {
    tipo: "adaptacion_pregunta",
    nodo,
    de: base,
    a: a.pregunta,
    busca: a.busca,
    salida: a.salida,
    ...(a.fallo ? { motivo: a.fallo } : {}),
  };
  return {
    ...resultado,
    pregunta: a.pregunta,
    acumulado: a.acumulado,
    estado: {
      ...resultado.estado,
      preguntaPendiente: a.pregunta,
      ultimasPreguntas: resultado.estado.ultimasPreguntas.map((q) => (q === mostrada ? a.pregunta : q)),
      fallbackEvents: [...resultado.estado.fallbackEvents, evento],
    },
  };
}
