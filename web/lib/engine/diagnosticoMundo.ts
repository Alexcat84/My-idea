/**
 * diagnosticoMundo.ts - Fase 4.5 (docs/PREVIEW_MUNDOS_PLAN.md): el redactor
 * del DIAGNOSTICO del preview. Entrada: el recorrido del preview + el estado
 * vivo; salida: el resumen del escaparate (lo que HAY y lo que un plan
 * estructuraria, jamas lo que HARIAS: la frontera del §3).
 *
 * LEY DE CALIDAD (§2.3, decision del fundador, no negociable): corre SIEMPRE
 * en el modelo de calidad plena (Sonnet). El preview es el vendedor del
 * mundo; si la llamada falla NO se degrada a un modelo menor ni a una
 * plantilla: se falla ruidoso y el usuario reintenta (BANCO §9).
 */
import type Anthropic from "@anthropic-ai/sdk";
import { llamarClaude, MODEL, type UsoAcumulado } from "../costmeter";
import { SYSTEM_DIAGNOSTICO_MUNDO } from "../prompts";
import { etiquetaArbol, type Grafo } from "./graph";
import type { EstadoRecorrido } from "./recorrido";

/** Presupuesto propio del diagnostico (§2.3: ~$0.02-0.03 esperado; el tope da
 * margen sin permitir una fuga). Independiente del presupuesto de sesion. */
export const PRESUPUESTO_DIAGNOSTICO_USD = 0.1;

export interface MaterialDiagnostico {
  mundo: { nombre: string; promesa: string };
  estado_vivo: string | null;
  temas_recorridos: string[];
  lo_que_conto: string;
}

/**
 * Arma el material del diagnostico desde la sesion del preview: las etiquetas
 * de arbol de los nodos CONVERSADOS (regla AGENTS.md: la etiqueta enamora) y
 * el perfil acumulado de la entrevista (lo que el usuario conto).
 */
export function materialDiagnostico(
  recorrido: EstadoRecorrido,
  graph: Grafo,
  mundo: { nombre: string; promesa: string },
  estadoVivo: string | null
): MaterialDiagnostico {
  const temas: string[] = [];
  for (let i = 0; i < recorrido.ruta.length; i++) {
    if (recorrido.modos[i] === "silencioso") continue;
    temas.push(etiquetaArbol(recorrido.ruta[i], graph));
  }
  return {
    mundo,
    estado_vivo: estadoVivo,
    temas_recorridos: temas,
    lo_que_conto: recorrido.perfilSesion ?? "",
  };
}

export interface ResultadoDiagnostico {
  resumen: string;
  acumulado: UsoAcumulado;
}

/**
 * UNA llamada Sonnet redacta el diagnostico. Sin respaldo degradado a
 * proposito: un escaparate mediocre vende peor que un "intenta de nuevo"
 * honesto. El llamador decide el mensaje del fallo.
 */
export async function redactarDiagnostico(
  client: Anthropic,
  material: MaterialDiagnostico,
  acumulado: UsoAcumulado
): Promise<ResultadoDiagnostico> {
  const r = await llamarClaude(client, SYSTEM_DIAGNOSTICO_MUNDO, JSON.stringify(material), MODEL, acumulado, {
    maxTokens: 700,
    componente: "diagnostico",
    presupuestoUsd: PRESUPUESTO_DIAGNOSTICO_USD,
  });
  return { resumen: r.texto.trim(), acumulado: r.acumulado };
}
