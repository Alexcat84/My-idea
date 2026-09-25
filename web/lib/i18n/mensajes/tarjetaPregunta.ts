/** La tarjeta de pregunta de la entrevista (app/ui/TarjetaPregunta.tsx). */
import type { PorIdioma } from "../config";

const es = {
  placeholder: "Cuéntame con tus palabras…",
  responder: "Responder",
  pensando: "Pensando…",
};

const en: typeof es = {
  placeholder: "Tell me in your own words…",
  responder: "Answer",
  pensando: "Thinking…",
};

export const TARJETA_PREGUNTA: PorIdioma<typeof es> = { es, en };
