/**
 * VERIFICADOR DE PLANES (decision del fundador, corrida final, 8 oct 2026). Implementado SIN desplegar: solo corre con
 * VERIFICADOR_PLAN=1 en el entorno.
 *
 * Antes de entregar un plan (nucleo, mundo, replanteamiento o seguimiento: todos pasan por la ruta del plan), una
 * llamada a Sonnet 5.5 compara cada afirmacion con lo que dijo la persona y con sus nodos (SYSTEM_VERIFICADOR_PLAN) y
 * propone quitar frases o convertirlas en pregunta. El codigo manda:
 *  - solo se aplican frases citadas TAL CUAL en el plan (una sola vez), nunca un titulo;
 *  - una "pregunta" tiene que ser la misma frase vuelta pregunta (con sus palabras); si no lo es, la frase se quita:
 *    nunca entra texto nuevo;
 *  - si se propone quitar mas del 20 % de las frases, no se aplica nada y el plan queda marcado para revision;
 *  - si la llamada falla, el plan sale igual y el fallo queda registrado (el cobro no cambia: lo fija la entrega).
 */
import type Anthropic from "@anthropic-ai/sdk";
import { llamarClaude, MODEL_SONNET, type UsoAcumulado } from "../costmeter";
import { parsearJson } from "../parseJson";
import { SYSTEM_VERIFICADOR_PLAN } from "../prompts";

export interface CorreccionPlan {
  frase: string;
  accion: "quitar" | "pregunta";
  pregunta?: string;
  motivo?: string;
}

export const TOPE_QUITAR = 0.2;

export function verificadorActivo(): boolean {
  return process.env.VERIFICADOR_PLAN === "1";
}

const esTitulo = (linea: string) => /^\s*#/.test(linea);
const esRotulo = (linea: string) => /^\s*_[^_]+_\s*$/.test(linea);

/** Las oraciones del cuerpo del plan (sin titulos ni rotulos), que es lo que se puede verificar. */
export function frasesDelPlan(markdown: string): string[] {
  const frases: string[] = [];
  for (const linea of markdown.split("\n")) {
    if (!linea.trim() || esTitulo(linea) || esRotulo(linea)) continue;
    const texto = linea.replace(/^\s*(?:[-*]|\d+\.)\s+/, "").replace(/^\*\*[^*]+\*\*\s*/, "");
    for (const f of texto.match(/[^.!?]+[.!?]+(?:["»”)]+)?|[^.!?]+$/g) ?? []) {
      const limpia = f.trim();
      if (limpia.length > 3) frases.push(limpia);
    }
  }
  return frases;
}

const palabras = (t: string) =>
  new Set(
    t
      .normalize("NFD")
      .replace(/\p{Diacritic}/gu, "")
      .toLowerCase()
      .match(/\p{L}{4,}/gu) ?? []
  );

/** ¿La "pregunta" es la misma frase vuelta pregunta? Lleva signo de pregunta y conserva al menos 6 de cada 10
 * palabras de la frase. */
function esLaMismaComoPregunta(frase: string, pregunta: string | undefined): boolean {
  if (!pregunta || !pregunta.includes("?")) return false;
  const de = palabras(frase);
  if (de.size === 0) return false;
  const a = palabras(pregunta);
  let comunes = 0;
  for (const p of de) if (a.has(p)) comunes += 1;
  return comunes / de.size >= 0.6;
}

export function aplicarCorrecciones(
  markdown: string,
  correcciones: CorreccionPlan[]
): { markdown: string; aplicadas: number; ignoradas: number; revision: boolean; quitadas: number } {
  const lineas = markdown.split("\n");
  const validas: Array<{ frase: string; reemplazo: string }> = [];
  let ignoradas = 0;
  for (const c of correcciones) {
    const frase = (c.frase ?? "").trim();
    const linea = frase ? lineas.findIndex((l) => l.includes(frase)) : -1;
    const unaSola = frase ? markdown.split(frase).length === 2 : false;
    if (linea < 0 || !unaSola || esTitulo(lineas[linea]) || esRotulo(lineas[linea])) {
      ignoradas += 1;
      continue;
    }
    const reemplazo = c.accion === "pregunta" && esLaMismaComoPregunta(frase, c.pregunta) ? c.pregunta!.trim() : "";
    validas.push({ frase, reemplazo });
  }
  const quitadas = validas.filter((v) => !v.reemplazo).length;
  const total = frasesDelPlan(markdown).length;
  if (total > 0 && quitadas / total > TOPE_QUITAR) {
    return { markdown, aplicadas: 0, ignoradas, revision: true, quitadas };
  }
  let out = markdown;
  for (const v of validas) out = out.replace(v.frase, v.reemplazo);
  // Lo que queda vacio se limpia: espacios dobles, una linea de lista sin texto y un rotulo en negrita que se quedo
  // sin su frase ("**Primera acción:**" solo, cuando antes llevaba texto).
  const originales = new Set(lineas.map((l) => l.trim()));
  out = out
    .split("\n")
    .map((l) => l.replace(/(\S) {2,}/g, "$1 ").replace(/\s+$/, ""))
    .filter((l) => !/^\s*(?:[-*]|\d+\.)$/.test(l))
    .filter((l) => !(/^\s*\*\*[^*]+:\*\*$/.test(l) && !originales.has(l.trim())))
    .join("\n");
  return { markdown: out, aplicadas: validas.length, ignoradas, revision: false, quitadas };
}

export interface EntradaVerificador {
  markdown: string;
  nodos: Array<{ id: string; etiqueta: string; pasos: string[]; entregable: string }>;
  respuestas: string[];
}

export interface ResultadoVerificador {
  markdown: string;
  acumulado: UsoAcumulado;
  correcciones: CorreccionPlan[];
  aplicadas: number;
  ignoradas: number;
  revision: boolean;
  fallo: string | null;
}

export async function verificarPlan(
  client: Anthropic,
  entrada: EntradaVerificador,
  acumulado: UsoAcumulado,
  opts: { presupuestoUsd: number; contexto: string | null; idiomaSalida?: string | null }
): Promise<ResultadoVerificador> {
  try {
    const r = await llamarClaude(
      client,
      SYSTEM_VERIFICADOR_PLAN,
      JSON.stringify({ plan: entrada.markdown, nodos: entrada.nodos, respuestas_de_la_persona: entrada.respuestas }),
      MODEL_SONNET,
      acumulado,
      {
        maxTokens: 2000,
        componente: "verificador_plan",
        presupuestoUsd: opts.presupuestoUsd,
        contexto: opts.contexto,
        idiomaSalida: opts.idiomaSalida ?? null,
      }
    );
    const data = parsearJson<{ correcciones?: CorreccionPlan[] }>(r.texto);
    const correcciones = (Array.isArray(data?.correcciones) ? data.correcciones : []).filter(
      (c) => c && typeof c.frase === "string" && (c.accion === "quitar" || c.accion === "pregunta")
    );
    const ap = aplicarCorrecciones(entrada.markdown, correcciones);
    return {
      markdown: ap.markdown,
      acumulado: r.acumulado,
      correcciones,
      aplicadas: ap.aplicadas,
      ignoradas: ap.ignoradas,
      revision: ap.revision,
      fallo: null,
    };
  } catch (e) {
    return {
      markdown: entrada.markdown,
      acumulado,
      correcciones: [],
      aplicadas: 0,
      ignoradas: 0,
      revision: false,
      fallo: e instanceof Error ? e.message : String(e),
    };
  }
}
