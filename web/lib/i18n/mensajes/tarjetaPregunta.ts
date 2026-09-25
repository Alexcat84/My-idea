/** La tarjeta de pregunta de la entrevista (app/ui/TarjetaPregunta.tsx). */
import type { PorIdioma } from "../config";

const es = {
  placeholder: "Cuéntame con tus palabras…",
  responder: "Responder",
  pensando: "Pensando…",
};

export const TARJETA_PREGUNTA: PorIdioma<typeof es> = { es };
