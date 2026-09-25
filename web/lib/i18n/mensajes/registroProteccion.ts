/** El registro de un mundo de protección (lib/registroProteccion.ts): la
 * severidad y el camino en palabras (fuente única para pantalla y papel) y el
 * documento descargable. Los "## " y "### " son estructura markdown. */
import type { PorIdioma } from "../config";

const es = {
  probabilidad: {
    poco_probable: "poco probable",
    probable: "probable",
    muy_probable: "muy probable",
  },
  dolor: {
    poco: "dolería poco",
    bastante: "dolería bastante",
    mucho: "dolería mucho",
  },
  camino: {
    evitar: "evitarlo",
    mitigar: "reducirlo",
    transferir: "pasárselo a otro",
    aceptar: "aceptarlo con los ojos abiertos",
  },
  severidad: "{{probabilidad}} y {{dolor}}",
  protegidaDesaparecida: "la actividad que protegía ya no está en tu plan",
  negocioEntero: "tu negocio entero",
  registroVacio:
    "No alcancé a enlazar este plan con tus actividades: sus respuestas están en tu plan, pero este registro quedó vacío.",
  documento: {
    titulo: "## Registro de {{mundo}}",
    queTanSerio: "Qué tan serio: {{severidad}}.",
    elCamino: "El camino: {{camino}}.",
    queProtege: "Qué protege: {{protege}}.",
    tuRespuesta: "Tu respuesta: {{respuesta}}",
  },
};

const en: typeof es = {
  probabilidad: {
    poco_probable: "unlikely",
    probable: "likely",
    muy_probable: "very likely",
  },
  dolor: {
    poco: "would hurt a little",
    bastante: "would hurt quite a bit",
    mucho: "would hurt a lot",
  },
  camino: {
    evitar: "avoid it",
    mitigar: "reduce it",
    transferir: "hand it off to someone else",
    aceptar: "accept it with your eyes open",
  },
  severidad: "{{probabilidad}} and {{dolor}}",
  protegidaDesaparecida: "the activity it protected is no longer in your plan",
  negocioEntero: "your whole business",
  registroVacio:
    "I couldn't link this plan to your activities: its answers are in your plan, but this register came out empty.",
  documento: {
    titulo: "## {{mundo}} register",
    queTanSerio: "How serious: {{severidad}}.",
    elCamino: "The path: {{camino}}.",
    queProtege: "What it protects: {{protege}}.",
    tuRespuesta: "Your response: {{respuesta}}",
  },
};

export const REGISTRO_PROTECCION: PorIdioma<typeof es> = { es, en };
