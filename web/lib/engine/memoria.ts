/**
 * PRINCIPIO 1, memoria de contexto de principio a fin (decision del fundador, 28 sep 2026, docs/REGLAS_DE_LA_CASA.md):
 * el contexto completo del usuario viaja SIEMPRE, en cada turno, en cada llamada a la IA, al pasar de una sesion a
 * otra y al abrir cada mundo. Vive en la base, en `projects.memoria` (migracion 049), y se actualiza en cada turno.
 *
 * Dos piezas (el patron de referencia es The Original I Ching: una entrada por turno, solo añadiendo, y un prefijo
 * estable que el cache puede reutilizar):
 *  - la FICHA DE CONTEXTO, estructurada: papel, si tiene jefe, equipo, sector, etapa, prioridad declarada y frases
 *    textuales. La actualiza el interprete en la misma llamada de cada turno (`ficha_update`); un dato desconocido
 *    nunca pisa uno conocido, y las frases solo se añaden;
 *  - el HILO: cada pregunta y cada respuesta de todas las sesiones del proyecto, en orden, solo añadiendo.
 *
 * Al abrir una sesion se fija la foto estable del contexto del proyecto (`textoContextoProyecto`), que viaja con
 * cache de 1 hora; la ficha actual viaja aparte en cada turno (`textoFichaActual`), porque cambia.
 */
import type { PrioridadDeclarada } from "./interprete";

export type Papel = "dueno" | "empleado" | "directivo" | "desconocido";

export interface FichaContexto {
  /** dueno: dueño o fundador de su negocio; empleado: trabaja para otro; directivo: dirige dentro de una empresa. */
  papel: Papel;
  tiene_jefe: boolean | null;
  equipo: { personas: number | null; descripcion: string | null };
  sector: string | null;
  etapa: string | null;
  prioridad_declarada: PrioridadDeclarada | null;
  /** lo que la persona dijo con sus palabras y conviene no perder */
  dijo_textual: string[];
}

export interface EntradaHilo {
  sesion: string;
  dominio: string;
  nodo: string | null;
  pregunta: string | null;
  respuesta: string;
  en: string;
}

export interface MemoriaProyecto {
  version: 1;
  ficha: FichaContexto;
  hilo: EntradaHilo[];
}

export function fichaVacia(): FichaContexto {
  return {
    papel: "desconocido",
    tiene_jefe: null,
    equipo: { personas: null, descripcion: null },
    sector: null,
    etapa: null,
    prioridad_declarada: null,
    dijo_textual: [],
  };
}

const PAPELES: readonly Papel[] = ["dueno", "empleado", "directivo", "desconocido"];
const texto = (v: unknown): string | null => (typeof v === "string" && v.trim() ? v.trim() : null);

/** La ficha con lo nuevo encima. Un dato desconocido, nulo o vacio nunca pisa uno conocido; las frases textuales
 * solo se añaden, sin repetir. */
export function fusionarFicha(base: FichaContexto, parcial: Partial<FichaContexto> | null | undefined): FichaContexto {
  if (!parcial) return base;
  const papel = parcial.papel && PAPELES.includes(parcial.papel) && parcial.papel !== "desconocido" ? parcial.papel : base.papel;
  const personas =
    typeof parcial.equipo?.personas === "number" && Number.isFinite(parcial.equipo.personas) ? parcial.equipo.personas : base.equipo.personas;
  const dijo = [...base.dijo_textual];
  for (const f of parcial.dijo_textual ?? []) {
    const t = texto(f);
    if (t && !dijo.includes(t)) dijo.push(t);
  }
  return {
    papel,
    tiene_jefe: typeof parcial.tiene_jefe === "boolean" ? parcial.tiene_jefe : base.tiene_jefe,
    equipo: { personas, descripcion: texto(parcial.equipo?.descripcion) ?? base.equipo.descripcion },
    sector: texto(parcial.sector) ?? base.sector,
    etapa: texto(parcial.etapa) ?? base.etapa,
    prioridad_declarada:
      parcial.prioridad_declarada && texto(parcial.prioridad_declarada.texto) ? parcial.prioridad_declarada : base.prioridad_declarada,
    dijo_textual: dijo,
  };
}

/** La memoria leida de la base. `{}` (proyectos de antes de la 049) o null se leen como memoria vacia. */
export function memoriaDe(raw: unknown): MemoriaProyecto {
  const r = (raw && typeof raw === "object" ? raw : {}) as Partial<MemoriaProyecto>;
  return {
    version: 1,
    ficha: fusionarFicha(fichaVacia(), r.ficha ?? null),
    hilo: Array.isArray(r.hilo) ? r.hilo : [],
  };
}

export function agregarAlHilo(m: MemoriaProyecto, e: EntradaHilo): MemoriaProyecto {
  return { ...m, hilo: [...m.hilo, e] };
}

const fichaJson = (f: FichaContexto) => JSON.stringify(f, null, 1);

/** La foto ESTABLE del contexto del proyecto al abrir una sesion: la idea, el estado vivo, la ficha y todo lo que
 * la persona conto antes. Determinista (misma memoria, mismo texto): de eso depende que el cache de 1 hora acierte. */
export function textoContextoProyecto(
  m: MemoriaProyecto,
  proyecto: { entradaOriginal: string | null; estadoVivo: string | null }
): string {
  const partes = [
    "CONTEXTO DEL PROYECTO (memoria guardada; no lo repitas, úsalo para hablarle a esta persona de su situación real)",
    `Idea original: ${proyecto.entradaOriginal?.trim() || "(sin idea escrita)"}`,
    `Estado vivo del proyecto: ${proyecto.estadoVivo?.trim() || "(aún no hay)"}`,
    `Ficha de contexto al abrir esta sesión: ${fichaJson(m.ficha)}`,
  ];
  if (m.hilo.length > 0) {
    partes.push("Lo que la persona ya contó, en orden:");
    for (const e of m.hilo) {
      partes.push(`- [${e.dominio}] ${e.pregunta ? `P: ${e.pregunta} ` : ""}R: ${e.respuesta}`);
    }
  }
  return partes.join("\n");
}

/** La ficha de este momento: viaja en cada turno, fuera del cache, y manda sobre la de la foto. */
export function textoFichaActual(f: FichaContexto): string {
  return `FICHA DE CONTEXTO ACTUAL (manda sobre la del contexto guardado): ${fichaJson(f)}`;
}

/** La apertura de una sesion (nucleo, mundo, seguimiento o replanteo): la foto estable del contexto del proyecto y la
 * ficha guardada. Un mundo que se abre recibe asi todo lo del nucleo y de los mundos anteriores. */
export function aperturaDeSesion(proyecto: {
  entrada_original: string | null;
  estado_vivo: string | null;
  memoria?: unknown;
}): { contextoProyecto: string; ficha: FichaContexto } {
  const m = memoriaDe(proyecto.memoria);
  return {
    contextoProyecto: textoContextoProyecto(m, { entradaOriginal: proyecto.entrada_original, estadoVivo: proyecto.estado_vivo }),
    ficha: m.ficha,
  };
}
