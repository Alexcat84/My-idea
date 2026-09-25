/** El redactor del plan (lib/engine/planRedactor.ts): lo que el código escribe en
 * el plan sin la IA. El aviso del plan básico, el plan armado sin IA (ensamblado
 * offline), la etiqueta del plan y el encabezado de lo que aún no cubre. */
import type { PorIdioma } from "../config";

const es = {
  avisoVersionBasica:
    "Esta es una versión básica de tu plan: la armé sin la redacción con IA porque esta conversación llegó a su tope de trabajo. No se te cobró. Puedes regenerarlo completo desde lo que ya me contaste: solo se cobra si la IA lo entrega.",
  /** El plan armado sin la IA (ensamblarOffline). "## Etapa N:" es además el
   * marcador que lee checklist.ts. */
  offline: {
    titulo: "# Tu plan de acción",
    contexto: "## Contexto",
    puntoDePartida: "Punto de partida: {{texto}}",
    loQueSabemos: "Lo que sabemos de tu idea: {{perfil}}",
    etapa: "## Etapa {{n}}: {{concepto}}",
    puntoDeControl: "Punto de control: {{entregable}}",
  },
  etiquetaCompleto: "Plan completo",
  etiquetaInicial: "Plan inicial",
  noCubre: "## Lo que este plan aún no cubre",
};

const en: typeof es = {
  avisoVersionBasica:
    "This is a basic version of your plan: I put it together without the AI write-up because this conversation reached its work limit. You weren't charged. You can regenerate the full plan from what you already told me: you're only charged if the AI delivers it.",
  offline: {
    titulo: "# Your action plan",
    contexto: "## Context",
    puntoDePartida: "Starting point: {{texto}}",
    loQueSabemos: "What we know about your idea: {{perfil}}",
    etapa: "## Stage {{n}}: {{concepto}}",
    puntoDeControl: "Checkpoint: {{entregable}}",
  },
  etiquetaCompleto: "Full plan",
  etiquetaInicial: "Initial plan",
  noCubre: "## What this plan doesn't cover yet",
};

export const MOTOR_PLAN: PorIdioma<typeof es> = { es, en };
