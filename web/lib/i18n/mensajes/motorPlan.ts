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
    titulo: "# Tu plan de accion",
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

export const MOTOR_PLAN: PorIdioma<typeof es> = { es };
