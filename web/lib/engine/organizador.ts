/**
 * organizador.ts — Fase 3.2: lo compartido entre POST /api/organizer
 * (JSON, usado por vuelo.ts/probar.ts) y POST /api/organizer/stream
 * (SSE, usado por la UI con el árbol que piensa). Una sola definición
 * del shape, del markdown y de las secciones detectables en el stream.
 */
import { limpiarGuiones } from "../voz";


/** Tope de tokens de salida del organizador. 600 truncaba el JSON de ideas
 * ricas/multi-dominio (auditor HSEQ, etc.) → parseo roto → fallo. 1500 da
 * margen holgado para las 3 listas + las dos frases. Fuente única para las
 * dos puertas del organizador (JSON y SSE). */
export const MAX_TOKENS_ORGANIZADOR = 1500;

export interface OrganizadorData {
  idea_en_una_frase?: string;
  etapa_detectada?: string;
  lo_que_ya_tienes_claro?: string[];
  lo_que_estas_asumiendo_sin_saberlo?: string[];
  areas_que_cubriria_tu_plan_completo?: string[];
}

/**
 * Secciones del organizador en el ORDEN en que el modelo las escribe
 * (el contrato JSON de SYSTEM_ORGANIZADOR). El árbol que piensa enciende
 * cada punto cuando la clave aparece en el stream real — la detección es
 * literal (el modelo acaba de empezar a escribir esa sección), jamás un
 * temporizador.
 */
export const SECCIONES_ORGANIZADOR: ReadonlyArray<{ clave: keyof OrganizadorData; label: string }> = [
  { clave: "idea_en_una_frase", label: "En una frase" },
  { clave: "etapa_detectada", label: "Etapa detectada" },
  { clave: "lo_que_ya_tienes_claro", label: "Lo que ya tienes claro" },
  { clave: "lo_que_estas_asumiendo_sin_saberlo", label: "Lo que estás asumiendo sin saberlo" },
  { clave: "areas_que_cubriria_tu_plan_completo", label: "Áreas de tu plan completo" },
];

/**
 * Sin guiones largos, campo por campo.
 *
 * SYSTEM_ORGANIZADOR ya prohíbe el guion largo, y `llamarClaude` limpia su
 * salida en un punto único... pero la puerta SSE llama a `client.messages
 * .stream()` DIRECTO y se salta ese punto. Por ahí salieron los dos guiones
 * que el fundador cazó en su sesión real: la regla estaba escrita y aun así
 * el texto llegó sucio, porque una regla en el prompt es una petición, no una
 * garantía. La garantía es esta función, aplicada a los datos ANTES de armar
 * el markdown y ANTES de mandarlos al cliente (los dos caminos pasan por
 * aquí).
 */
export function limpiarOrganizador(data: OrganizadorData): OrganizadorData {
  const lista = (xs?: string[]) => xs?.map((x) => limpiarGuiones(x));
  return {
    idea_en_una_frase: data.idea_en_una_frase && limpiarGuiones(data.idea_en_una_frase),
    etapa_detectada: data.etapa_detectada,
    lo_que_ya_tienes_claro: lista(data.lo_que_ya_tienes_claro),
    lo_que_estas_asumiendo_sin_saberlo: lista(data.lo_que_estas_asumiendo_sin_saberlo),
    areas_que_cubriria_tu_plan_completo: lista(data.areas_que_cubriria_tu_plan_completo),
  };
}

export function construirMarkdown(data: OrganizadorData): string {
  const out: string[] = [
    "# Organizador de tu idea",
    "",
    `**En una frase:** ${data.idea_en_una_frase ?? ""}`,
    "",
    `**Etapa detectada:** ${data.etapa_detectada ?? ""}`,
    "",
    "## Lo que ya tienes claro",
  ];
  for (const b of data.lo_que_ya_tienes_claro ?? []) out.push(`- ${b}`);
  out.push("", "## Lo que estás asumiendo sin saberlo");
  for (const b of data.lo_que_estas_asumiendo_sin_saberlo ?? []) out.push(`- ${b}`);
  out.push("", "## Áreas que cubriría tu plan completo");
  for (const b of data.areas_que_cubriria_tu_plan_completo ?? []) out.push(`- ${b}`);
  return out.join("\n");
}
