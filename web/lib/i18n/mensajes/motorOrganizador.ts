/** El organizador de la idea (lib/engine/organizador.ts): los nombres de las
 * secciones que enciende el árbol que piensa y el markdown del organizador. */
import type { PorIdioma } from "../config";

const es = {
  /** Las secciones en el orden del contrato JSON (SECCIONES_ORGANIZADOR). */
  secciones: {
    idea_en_una_frase: "En una frase",
    etapa_detectada: "Etapa detectada",
    lo_que_ya_tienes_claro: "Lo que ya tienes claro",
    lo_que_estas_asumiendo_sin_saberlo: "Lo que estás asumiendo sin saberlo",
    areas_que_cubriria_tu_plan_completo: "Áreas de tu plan completo",
  },
  /** El markdown del organizador (construirMarkdown). */
  markdown: {
    titulo: "# Organizador de tu idea",
    enUnaFrase: "**En una frase:** {{frase}}",
    etapaDetectada: "**Etapa detectada:** {{etapa}}",
    yaTienesClaro: "## Lo que ya tienes claro",
    estasAsumiendo: "## Lo que estás asumiendo sin saberlo",
    areasDelPlan: "## Áreas que cubriría tu plan completo",
  },
};

const en: typeof es = {
  secciones: {
    idea_en_una_frase: "In one sentence",
    etapa_detectada: "Detected stage",
    lo_que_ya_tienes_claro: "What you're already clear on",
    lo_que_estas_asumiendo_sin_saberlo: "What you're assuming without realizing it",
    areas_que_cubriria_tu_plan_completo: "Areas of your full plan",
  },
  markdown: {
    titulo: "# Your idea organizer",
    enUnaFrase: "**In one sentence:** {{frase}}",
    etapaDetectada: "**Detected stage:** {{etapa}}",
    yaTienesClaro: "## What you're already clear on",
    estasAsumiendo: "## What you're assuming without realizing it",
    areasDelPlan: "## Areas your full plan would cover",
  },
};

export const MOTOR_ORGANIZADOR: PorIdioma<typeof es> = { es, en };
