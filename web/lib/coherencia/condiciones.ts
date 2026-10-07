/**
 * PRUEBA DE COHERENCIA: las condiciones nuevas de la corrida final, encargadas por el fundador sobre
 * docs/auditoria_final/informes/estado_memoria_contexto.md. Funciones puras: el arnes (web/scripts/coherencia.ts) lee
 * la base y les pasa lo leido; aqui no hay red.
 *
 *  1. FICHA: tras el nucleo y tras cada mundo, projects.memoria tiene el papel y el jefe del retrato.
 *  2. HILO: el hilo son las respuestas dadas, con su sesion, en orden, y solo crece por el final.
 *  3. CONTINUIDAD: desde el nucleo (no desde el primer mundo), con TODAS las respuestas del espacio anterior en el
 *     contexto del siguiente; en el primer mundo, ademas, estado vivo y ficha con el papel; en los mundos de
 *     proteccion, el snapshot del nucleo.
 *  4. CONTEXTO: toda llamada a la IA lleva el contexto del proyecto, salvo la lista blanca explicita (organizadores).
 *  5. CACHE: ahorro mayor que 0; lecturas en las sesiones con 2 o mas turnos del interprete; al menos una escritura
 *     de 1 hora por persona; el turno del interprete mas barato que antes.
 *  Salida: dictamen && continuidad && ficha && hilo && contexto && cache.
 *
 * Sin medicion no se cumple: una lista vacia nunca se da por buena.
 */
import type { RegistroLlamada } from "../costmeter";
import type { EntradaHilo, FichaContexto } from "../engine/memoria";
import { esMundoProteccion } from "../espacios";
import { ahorroCache, type Dictamen, type Persona } from "./nucleo";

export interface Veredicto {
  ok: boolean;
  motivos: string[];
}

const veredicto = (motivos: string[]): Veredicto => ({ ok: motivos.length === 0, motivos });

/** Junta varios veredictos: todos ok, o los motivos de todos. Sin nada que juntar no hay medicion: no cumple. */
export function juntar(vs: Veredicto[]): Veredicto {
  if (vs.length === 0) return { ok: false, motivos: ["no hay nada medido"] };
  return veredicto(vs.flatMap((v) => v.motivos));
}

/** 1. La ficha guardada tiene el papel y el jefe del retrato de la persona. */
export function verificarFicha(ficha: FichaContexto | null | undefined, persona: Pick<Persona, "id" | "ficha">, momento: string): Veredicto {
  const donde = `${persona.id}, ${momento}`;
  if (!ficha) return veredicto([`${donde}: no hay ficha en projects.memoria`]);
  const motivos: string[] = [];
  if (ficha.papel !== persona.ficha.papel) motivos.push(`${donde}: la ficha dice papel '${ficha.papel}', el retrato '${persona.ficha.papel}'`);
  if (ficha.tiene_jefe !== persona.ficha.tiene_jefe) {
    motivos.push(`${donde}: la ficha dice tiene_jefe ${ficha.tiene_jefe}, el retrato ${persona.ficha.tiene_jefe}`);
  }
  return veredicto(motivos);
}

export interface RespuestaDada {
  sesion: string;
  respuesta: string;
}

const mismaEntrada = (a: EntradaHilo, b: EntradaHilo) => JSON.stringify(a) === JSON.stringify(b);

/** 2. El hilo son exactamente las respuestas dadas (con su sesion), en orden; y lo que habia antes sigue igual al
 * principio (solo crece por el final). `hiloAntes` es la lectura anterior, o null en la primera. */
export function verificarHilo(hiloAntes: EntradaHilo[] | null, hiloAhora: EntradaHilo[], dadas: RespuestaDada[], momento: string): Veredicto {
  const motivos: string[] = [];
  if (hiloAntes) {
    const prefijo = hiloAhora.length >= hiloAntes.length && hiloAntes.every((e, i) => mismaEntrada(e, hiloAhora[i]));
    if (!prefijo) motivos.push(`${momento}: el hilo no crecio solo al final (cambio lo que ya tenia: ${hiloAntes.length} entradas antes)`);
  }
  if (hiloAhora.length !== dadas.length) {
    motivos.push(`${momento}: el hilo tiene ${hiloAhora.length} entradas y se dieron ${dadas.length} respuestas`);
  }
  const n = Math.min(hiloAhora.length, dadas.length);
  for (let i = 0; i < n; i++) {
    const e = hiloAhora[i];
    const d = dadas[i];
    if (e.respuesta !== d.respuesta || e.sesion !== d.sesion) {
      motivos.push(`${momento}: la entrada ${i + 1} del hilo no es la respuesta ${i + 1} dada (orden, texto o sesion)`);
      break;
    }
  }
  return veredicto(motivos);
}

// Los rotulos de textoContextoProyecto (lib/engine/memoria.ts). La prueba arma sus contextos con la funcion real: si
// el formato cambia, la prueba rompe alli y no en la corrida.
const ROTULO_ESTADO_VIVO = "Estado vivo del proyecto: ";
const ROTULO_FICHA = "Ficha de contexto al abrir esta sesión: ";
const SIN_ESTADO_VIVO = "(aún no hay)";

/** El estado vivo con que abrio la sesion, leido de su contexto; null si no lo hay. */
export function estadoVivoDelContexto(ctx: string | null | undefined): string | null {
  if (!ctx) return null;
  const ini = ctx.indexOf(ROTULO_ESTADO_VIVO);
  if (ini < 0) return null;
  const desde = ini + ROTULO_ESTADO_VIVO.length;
  const fin = ctx.indexOf(`\n${ROTULO_FICHA}`, desde);
  const valor = ctx.slice(desde, fin < 0 ? undefined : fin).trim();
  return valor && valor !== SIN_ESTADO_VIVO ? valor : null;
}

/** La ficha con que abrio la sesion, leida de su contexto (el JSON tras su rotulo); null si no se puede leer. */
export function fichaDelContexto(ctx: string | null | undefined): Partial<FichaContexto> | null {
  if (!ctx) return null;
  const ini = ctx.indexOf(ROTULO_FICHA);
  if (ini < 0) return null;
  const abre = ctx.indexOf("{", ini + ROTULO_FICHA.length);
  if (abre < 0) return null;
  let nivel = 0;
  let enCadena = false;
  for (let i = abre; i < ctx.length; i++) {
    const c = ctx[i];
    if (enCadena) {
      if (c === "\\") i++;
      else if (c === '"') enCadena = false;
      continue;
    }
    if (c === '"') enCadena = true;
    else if (c === "{") nivel++;
    else if (c === "}" && --nivel === 0) {
      try {
        return JSON.parse(ctx.slice(abre, i + 1)) as Partial<FichaContexto>;
      } catch {
        return null;
      }
    }
  }
  return null;
}

export interface PasoDeEspacio {
  persona: Pick<Persona, "id" | "ficha">;
  /** el espacio anterior ('core' para el nucleo) y el que se abre */
  de: string;
  a: string;
  /** el contexto con que abrio el espacio nuevo (estado_recorrido.recorrido.contextoProyecto) */
  contexto: string | null | undefined;
  /** todas las respuestas dadas en el espacio anterior */
  respuestasAnterior: string[];
  /** el paso del nucleo al primer mundo */
  primerMundo: boolean;
  /** estado_recorrido.recorrido.snapshotNucleo del espacio nuevo */
  snapshotNucleo: string | null | undefined;
}

/** 3. Continuidad: el contexto del espacio nuevo trae TODAS las respuestas del anterior; en el primer mundo, ademas,
 * el estado vivo y la ficha con el papel; en los mundos de proteccion, el snapshot del nucleo. */
export function verificarContinuidad(p: PasoDeEspacio): Veredicto {
  const donde = `${p.persona.id}, de ${p.de} a ${p.a}`;
  if (!p.contexto) return veredicto([`${donde}: el espacio abrio sin contexto del proyecto`]);
  const motivos: string[] = [];
  const respuestas = p.respuestasAnterior.map((r) => r.trim()).filter(Boolean);
  if (respuestas.length === 0) {
    motivos.push(`${donde}: el espacio anterior no tiene respuestas que arrastrar (sin medicion)`);
  } else {
    const faltan = respuestas.filter((r) => !p.contexto!.includes(r));
    if (faltan.length > 0) motivos.push(`${donde}: faltan ${faltan.length} de ${respuestas.length} respuestas del espacio anterior en el contexto`);
  }
  if (p.primerMundo) {
    if (!estadoVivoDelContexto(p.contexto)) motivos.push(`${donde}: el primer mundo abrio sin estado vivo`);
    const ficha = fichaDelContexto(p.contexto);
    if (ficha?.papel !== p.persona.ficha.papel) {
      motivos.push(`${donde}: el primer mundo abrio con la ficha en papel '${ficha?.papel ?? "ilegible"}', el retrato '${p.persona.ficha.papel}'`);
    }
  }
  if (esMundoProteccion(p.a) && !p.snapshotNucleo?.trim()) motivos.push(`${donde}: un mundo de proteccion abrio sin el snapshot del nucleo`);
  return veredicto(motivos);
}

/** La lista blanca EXPLICITA: los dos organizadores (el no streaming y el de streaming registran 'organizador').
 * Corren cuando el proyecto acaba de nacer y su memoria esta vacia: no hay contexto que pasar. */
export const COMPONENTES_SIN_CONTEXTO = ["organizador"] as const;

/** 4. Contexto en cada llamada: toda llamada fuera de la lista blanca lo llevo. Un registro que no lo dice (anterior
 * a este campo) cuenta como sin contexto. */
export function verificarContextoPorLlamada(
  llamadas: RegistroLlamada[],
  listaBlanca: readonly string[] = COMPONENTES_SIN_CONTEXTO
): Veredicto & { total: number; conContexto: number } {
  const total = llamadas.length;
  const conContexto = llamadas.filter((l) => l.con_contexto === true).length;
  if (total === 0) return { ok: false, motivos: ["no hay llamadas de la app que medir"], total, conContexto };
  const fuera = llamadas.filter((l) => l.con_contexto !== true && !listaBlanca.includes(l.componente ?? ""));
  if (fuera.length === 0) return { ok: true, motivos: [], total, conContexto };
  const porComponente = new Map<string, number>();
  for (const l of fuera) porComponente.set(l.componente ?? "sin componente", (porComponente.get(l.componente ?? "sin componente") ?? 0) + 1);
  const detalle = [...porComponente].map(([c, n]) => `${c} (${n})`).join(", ");
  return { ok: false, motivos: [`${fuera.length} de ${total} llamadas sin contexto fuera de la lista blanca: ${detalle}`], total, conContexto };
}

export interface SesionMedida {
  persona: string;
  sesion: string;
  llamadas: RegistroLlamada[];
}

/** El componente del interprete en los registros. */
const TURNOS = "turnos";

/** 5. Las cuatro condiciones de cache. `turnoAntesUsd` es la vara del "antes" (el vuelo del 27 sep 2026). */
export function verificarCache(
  sesiones: SesionMedida[],
  personas: string[],
  turnoAntesUsd: number
): Veredicto & { ahorro: number; turnoAhoraUsd: number | null } {
  const motivos: string[] = [];
  const todas = sesiones.flatMap((s) => s.llamadas);
  // 1. ahorro mayor que 0
  const { ahorro } = ahorroCache(todas);
  if (!(ahorro > 0)) motivos.push(`cache: ahorro ${ahorro.toFixed(6)} USD (tiene que ser mayor que 0)`);
  // 2. lecturas en las sesiones con 2 o mas turnos del interprete
  for (const s of sesiones) {
    const turnos = s.llamadas.filter((l) => l.componente === TURNOS);
    if (turnos.length >= 2 && turnos.reduce((a, l) => a + l.cache_read, 0) === 0) {
      motivos.push(`cache: la sesion ${s.sesion} (${s.persona}) tuvo ${turnos.length} turnos del interprete y ninguna lectura de cache`);
    }
  }
  // 3. al menos una escritura de 1 hora por persona
  for (const p of personas) {
    const escrito = sesiones.filter((s) => s.persona === p).flatMap((s) => s.llamadas).reduce((a, l) => a + l.cache_write_1h, 0);
    if (escrito === 0) motivos.push(`cache: ${p} no tiene ninguna escritura de 1 hora`);
  }
  // 4. el turno del interprete, mas barato que antes
  const turnos = todas.filter((l) => l.componente === TURNOS);
  const turnoAhoraUsd = turnos.length ? turnos.reduce((a, l) => a + l.usd, 0) / turnos.length : null;
  if (turnoAhoraUsd === null) motivos.push("cache: no hay turnos del interprete que medir");
  else if (!(turnoAhoraUsd < turnoAntesUsd)) {
    motivos.push(`cache: el turno del interprete cuesta ${turnoAhoraUsd.toFixed(6)} USD, antes ${turnoAntesUsd.toFixed(6)} USD (tiene que salir mas barato)`);
  }
  return { ...veredicto(motivos), ahorro, turnoAhoraUsd };
}

export interface Condiciones {
  dictamen: Dictamen;
  continuidad: Veredicto;
  ficha: Veredicto;
  hilo: Veredicto;
  contexto: Veredicto;
  cache: Veredicto;
}

/** La condicion de salida: dictamen && continuidad && ficha && hilo && contexto && cache. Cada motivo dice de que
 * condicion viene. */
export function condicionDeSalida(c: Condiciones): Dictamen {
  const motivos = [
    ...c.dictamen.motivos.map((m) => `juez: ${m}`),
    ...(["continuidad", "ficha", "hilo", "contexto", "cache"] as const).flatMap((k) =>
      c[k].ok ? [] : c[k].motivos.length ? c[k].motivos.map((m) => `${k}: ${m}`) : [`${k}: no cumple`]
    ),
  ];
  const cumple = c.dictamen.cumple && c.continuidad.ok && c.ficha.ok && c.hilo.ok && c.contexto.ok && c.cache.ok;
  return { cumple, motivos: cumple ? [] : motivos.length ? motivos : ["no cumple"] };
}
