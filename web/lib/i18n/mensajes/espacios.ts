/** Campaña "Espacios": la muralla del sin plan (lib/espacios.ts), las pestañas
 * de los espacios (CambiadorEspacios) y el selector de caras (SelectorCara). */
import type { PorIdioma } from "../config";

const es = {
  /** UNA sola frase para toda la casa: la ruta (409) y la pantalla del escaparate. */
  murallaSinPlan: "Primero genera el plan de tu idea: tu mundo de {{mundo}} se construirá sobre él.",
  cambiador: {
    aria: "Los espacios de tu proyecto",
    tuViaje: "Tu viaje",
    anadirMundo: "Añadir un mundo",
    mundo: "Mundo",
  },
  caras: {
    aria: "Las caras de este espacio",
  },
};

const en: typeof es = {
  murallaSinPlan: "First generate your idea's plan: your {{mundo}} world will be built on top of it.",
  cambiador: {
    aria: "Your project's spaces",
    tuViaje: "Your Journey",
    anadirMundo: "Add a world",
    mundo: "World",
  },
  caras: {
    aria: "The views of this space",
  },
};

export const ESPACIOS: PorIdioma<typeof es> = { es, en };
