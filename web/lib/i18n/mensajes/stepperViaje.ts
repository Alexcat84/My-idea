/** El stepper del viaje (app/ui/Stepper.tsx): los seis hitos (términos de marca
 * del glosario) y la etiqueta accesible del riel. */
import type { PorIdioma } from "../config";

const es = {
  etapas: ["La Chispa", "Claridad", "La Exploración", "Tu Plan", "Manos a la Obra", "Realizado"],
  ariaEtapa: "Etapa {{etapa}} de {{total}}: {{nombre}}",
};

const en: typeof es = {
  etapas: ["The Spark", "Clarity", "Exploration", "Your Plan", "Get to Work", "Achieved"],
  ariaEtapa: "Stage {{etapa}} of {{total}}: {{nombre}}",
};

export const STEPPER_VIAJE: PorIdioma<typeof es> = { es, en };
