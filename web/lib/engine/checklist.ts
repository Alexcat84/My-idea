/**
 * checklist.ts — Fase 3.3: deriva el checklist de un plan YA finalizado.
 * Determinístico, cero LLM: el plan es la fuente, el parser es el notario.
 * Formato real de los planes (verificado contra examples/fase2_9_plan_macetas.md
 * y el plan de la mochila WiFi): etapas "## Etapa N: título", pasos como
 * párrafos numerados "1. ..." (a veces con **negrita** inicial), y el bloque
 * "**Esta semana:** ..." una vez por etapa.
 */
import type { ChecklistEstado } from "../dbContract";

export interface ItemDerivado {
  etapa: number;
  orden: number;
  texto: string;
  destacado: boolean; // true = "Esta semana"
}

const RE_ETAPA = /^##\s+Etapa\s+(\d+)\s*:/;
const RE_PASO = /^(\d+)\.\s+(.*)$/;
const RE_SEMANA = /^\*\*Esta semana:?\*\*\s*(.*)$/i;

/** Primera oración del párrafo, sin markdown de énfasis, tope 180 chars. */
function resumirPaso(cuerpo: string): string {
  const plano = cuerpo.replace(/\*\*/g, "").replace(/\s+/g, " ").trim();
  const punto = plano.indexOf(". ");
  const frase = punto > 20 ? plano.slice(0, punto + 1) : plano;
  return frase.length > 180 ? frase.slice(0, 177).trimEnd() + "…" : frase;
}

export function derivarChecklist(markdownPlan: string): ItemDerivado[] {
  const items: ItemDerivado[] = [];
  let etapaActual = 0;
  let orden = 0;
  let pasoAbierto: { numero: number; lineas: string[] } | null = null;

  const cerrarPaso = () => {
    if (pasoAbierto && etapaActual > 0) {
      orden += 1;
      items.push({
        etapa: etapaActual,
        orden,
        texto: resumirPaso(pasoAbierto.lineas.join(" ")),
        destacado: false,
      });
    }
    pasoAbierto = null;
  };

  for (const cruda of markdownPlan.split(/\r?\n/)) {
    const linea = cruda.trimEnd();
    const mEtapa = RE_ETAPA.exec(linea.trim());
    if (mEtapa) {
      cerrarPaso();
      etapaActual = parseInt(mEtapa[1], 10);
      orden = 0;
      continue;
    }
    if (linea.trim().startsWith("## ")) {
      // Encabezado ## que NO es Etapa (ej. la sección de sostenibilidad):
      // se sale del ámbito de etapas; sus numerales no generan ítems.
      cerrarPaso();
      etapaActual = 0;
      continue;
    }
    if (etapaActual === 0) continue; // intro y secciones fuera de etapas

    const mSemana = RE_SEMANA.exec(linea.trim());
    if (mSemana) {
      cerrarPaso();
      orden += 1;
      items.push({
        etapa: etapaActual,
        orden,
        texto: resumirPaso(mSemana[1] || "Esta semana"),
        destacado: true,
      });
      continue;
    }
    const mPaso = RE_PASO.exec(linea.trim());
    if (mPaso) {
      cerrarPaso();
      pasoAbierto = { numero: parseInt(mPaso[1], 10), lineas: [mPaso[2]] };
      continue;
    }
    if (pasoAbierto) {
      if (linea.trim() === "" || linea.startsWith("#") || linea.startsWith("---")) {
        cerrarPaso();
      } else {
        pasoAbierto.lineas.push(linea.trim());
      }
    }
  }
  cerrarPaso();
  return items;
}

export const ESTADO_INICIAL: ChecklistEstado = "pendiente";
