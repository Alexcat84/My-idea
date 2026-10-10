/**
 * COMPROBADOR PASO CONTRA NODO (decision del fundador, 10 oct 2026, punto 3). Apagado salvo COMPROBADOR_PASOS=1.
 *
 * Cada paso del plan termina con la marca del tema del que sale (regla 6-bis); validarCitas la valida y devuelve el par
 * (etapa, paso, temas). Antes de entregar el plan, una llamada a Sonnet 5.5 recibe cada paso SOLO con su tema (nombre,
 * pasos, entregable: lo mismo que recibio el redactor) y dice cuales lo contradicen (SYSTEM_COMPROBADOR_PASOS). El codigo:
 *  - solo quita pasos, nunca reescribe: la linea del paso sale y la lista se renumera;
 *  - solo quita si la frase del tema que se da como prueba esta en el tema tal cual (el tema de ese paso);
 *  - si se propone quitar mas del 30 % de los pasos juzgados (y mas de uno), no aplica nada y queda para revision;
 *  - si la llamada falla, el plan sale igual y el fallo queda registrado.
 * Los pasos sin tema valido no se juzgan.
 */
import type Anthropic from "@anthropic-ai/sdk";
import { llamarClaude, MODEL_SONNET, type UsoAcumulado } from "../costmeter";
import { parsearJson } from "../parseJson";
import { SYSTEM_COMPROBADOR_PASOS } from "../prompts";
import type { PasoCitado } from "./citarOCallar";

export const TOPE_QUITAR_PASOS = 0.3;

export function comprobadorPasosActivo(): boolean {
  return process.env.COMPROBADOR_PASOS === "1";
}

export interface TemaParaComprobar {
  id: string;
  etiqueta: string;
  pasos: string[];
  entregable: string;
}

const RE_ETAPA = /^##\s+Etapa\s+(\d+)/i;
const RE_PASO = /^(\s*)(\d+)([.)])(\s+)(.*)$/;

/** Los pasos del markdown por clave "etapa.paso" (el numero tal como esta escrito), con su linea. */
export function pasosDelPlan(markdown: string): Map<string, { linea: number; texto: string }> {
  const out = new Map<string, { linea: number; texto: string }>();
  let etapa = 0;
  markdown.split("\n").forEach((l, i) => {
    if (/^##\s/.test(l)) etapa = Number(l.match(RE_ETAPA)?.[1] ?? 0);
    const m = etapa > 0 ? l.match(RE_PASO) : null;
    if (m) out.set(`${etapa}.${m[2]}`, { linea: i, texto: m[5].trim() });
  });
  return out;
}

/** Quita las lineas de esos pasos y renumera cada lista que toco (1, 2, 3... en el orden que quedan). */
export function quitarPasos(markdown: string, claves: string[]): string {
  const pasos = pasosDelPlan(markdown);
  const fuera = new Set(claves.map((c) => pasos.get(c)?.linea).filter((x): x is number => x !== undefined));
  if (fuera.size === 0) return markdown;
  const out: string[] = [];
  let siguiente = 0;
  for (const [i, l] of markdown.split("\n").entries()) {
    if (fuera.has(i)) continue;
    const m = l.match(RE_PASO);
    if (m) {
      siguiente += 1;
      out.push(`${m[1]}${siguiente}${m[3]}${m[4]}${m[5]}`);
    } else {
      if (l.trim() !== "") siguiente = 0;
      out.push(l);
    }
  }
  return out.join("\n");
}

const normal = (s: string) =>
  s.normalize("NFD").replace(/\p{Mn}/gu, "").toLowerCase().replace(/[^\p{L}\p{N}]+/gu, " ").trim();

export interface ResultadoComprobador {
  markdown: string;
  acumulado: UsoAcumulado;
  juzgados: number;
  propuestas: Array<{ clave: string; nodo: string; lo_que_ensena: string; motivo?: string }>;
  quitados: string[];
  ignorados: number;
  revision: boolean;
  fallo: string | null;
}

export async function comprobarPasos(
  client: Anthropic,
  entrada: { markdown: string; pasosCitados: PasoCitado[]; nodos: TemaParaComprobar[] },
  acumulado: UsoAcumulado,
  opts: { presupuestoUsd: number; idiomaSalida?: string | null }
): Promise<ResultadoComprobador> {
  const base: ResultadoComprobador = { markdown: entrada.markdown, acumulado, juzgados: 0, propuestas: [], quitados: [], ignorados: 0, revision: false, fallo: null };
  const temas = new Map(entrada.nodos.map((n) => [n.id, n]));
  const pasos = pasosDelPlan(entrada.markdown);
  const pares = entrada.pasosCitados
    .map((p) => ({ clave: `${p.etapa}.${p.numero}`, paso: pasos.get(`${p.etapa}.${p.numero}`)?.texto, temas: p.nodos.filter((id) => temas.has(id)) }))
    .filter((p): p is { clave: string; paso: string; temas: string[] } => Boolean(p.paso) && p.temas.length > 0);
  if (pares.length === 0) return base;
  base.juzgados = pares.length;
  try {
    const usados = [...new Set(pares.flatMap((p) => p.temas))];
    const r = await llamarClaude(
      client,
      SYSTEM_COMPROBADOR_PASOS,
      JSON.stringify({
        temas: usados.map((id) => {
          const t = temas.get(id)!;
          return { id, nombre: t.etiqueta, pasos: t.pasos, entregable: t.entregable };
        }),
        pasos: pares.map((p) => ({ clave: p.clave, paso: p.paso, temas: p.temas })),
      }),
      MODEL_SONNET,
      acumulado,
      { maxTokens: 2000, componente: "comprobador_pasos", presupuestoUsd: opts.presupuestoUsd, idiomaSalida: opts.idiomaSalida ?? null }
    );
    base.acumulado = r.acumulado;
    const data = parsearJson<{ contradicen?: ResultadoComprobador["propuestas"] }>(r.texto);
    base.propuestas = (Array.isArray(data?.contradicen) ? data.contradicen : []).filter(
      (c) => c && typeof c.clave === "string" && typeof c.nodo === "string" && typeof c.lo_que_ensena === "string"
    );
    const validas: string[] = [];
    for (const c of base.propuestas) {
      const par = pares.find((p) => p.clave === c.clave);
      const tema = par && par.temas.includes(c.nodo) ? temas.get(c.nodo) : undefined;
      const prueba = normal(c.lo_que_ensena);
      const textoTema = tema ? normal([tema.etiqueta, ...tema.pasos, tema.entregable].join(" ")) : "";
      if (!tema || prueba.length < 8 || !textoTema.includes(prueba) || validas.includes(c.clave)) {
        base.ignorados += 1;
        continue;
      }
      validas.push(c.clave);
    }
    if (validas.length > Math.max(1, Math.floor(pares.length * TOPE_QUITAR_PASOS))) {
      base.revision = true;
      return base;
    }
    base.quitados = validas;
    base.markdown = quitarPasos(entrada.markdown, validas);
    return base;
  } catch (e) {
    return { ...base, fallo: e instanceof Error ? e.message : String(e) };
  }
}
