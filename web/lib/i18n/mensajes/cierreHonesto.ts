/** El cierre honesto cuando el motor decide salir (app/ui/CierreHonesto.tsx, canon 12). */
import type { PorIdioma } from "../config";

const es = {
  unAltoHonesto: "Un alto honesto",
  activacionDevuelta: { one: "Activación devuelta · {{n}} crédito", other: "Activación devuelta · {{n}} créditos" },
  porQueEsteMundo: "Por qué este mundo, no ahora",
  loQueVi: "Lo que vi",
  teDevolvimos: {
    one: "Te devolvimos {{n}} crédito de la activación. Nunca pierdes créditos por algo que no te sirvió.",
    other: "Te devolvimos {{n}} créditos de la activación. Nunca pierdes créditos por algo que no te sirvió.",
  },
  volverAManos: "Volver a Manos a la Obra",
  volverAMiIdea: "Volver a mi idea",
  verOtrosMundos: "Ver los otros mundos",
  explorarOtroAngulo: "Explorar otro ángulo de la idea",
  notaMundo: "Tu viaje principal sigue intacto: cerrar este mundo no toca tu idea.",
  notaCamino: "Nada se pierde: tu recorrido y tu Claridad quedan guardados tal como están.",
};

const en: typeof es = {
  unAltoHonesto: "An honest stop",
  activacionDevuelta: { one: "Activation refunded · {{n}} credit", other: "Activation refunded · {{n}} credits" },
  porQueEsteMundo: "Why this world isn't for now",
  loQueVi: "What I saw",
  teDevolvimos: {
    one: "We refunded {{n}} credit from the activation. You never lose credits on something that didn't help you.",
    other: "We refunded {{n}} credits from the activation. You never lose credits on something that didn't help you.",
  },
  volverAManos: "Back to Get to Work",
  volverAMiIdea: "Back to my idea",
  verOtrosMundos: "See the other worlds",
  explorarOtroAngulo: "Explore another angle of the idea",
  notaMundo: "Your main journey is still intact: closing this world doesn't touch your idea.",
  notaCamino: "Nothing is lost: your path and your Clarity stay saved just as they are.",
};

export const CIERRE_HONESTO: PorIdioma<typeof es> = { es, en };
