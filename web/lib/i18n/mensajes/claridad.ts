/** La Claridad (canon 03): la tarjeta del organizador en /nueva y en la idea
 * (app/ui/Claridad.tsx), el botón para explorar y el aviso de precio de La
 * Exploración (lib/avisoExploracion.ts). */
import type { PorIdioma } from "../config";

const es = {
  estoEntendi: "Esto entendí de tu idea",
  loQueYaTienes: "Lo que ya tienes",
  loQueEstasAsumiendo: "Lo que estás asumiendo",
  notaSuposiciones: "Estas suposiciones son exactamente lo que La Exploración pone a prueba, pregunta a pregunta.",
  explorarSuposiciones: "Explorar estas suposiciones",
  avisoPrecioExploracion:
    "La Exploración usa {{n}} créditos, que se cobran solo cuando recibes tu plan. Tu Claridad es gratis y queda guardada para siempre.",
};

export const CLARIDAD: PorIdioma<typeof es> = { es };
