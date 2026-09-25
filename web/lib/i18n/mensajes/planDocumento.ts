/** El plan como documento de acordeones (app/ui/PlanDocumento.tsx) y la
 * etiqueta que agrega su parser (lib/planParser.ts). Los encabezados del
 * markdown que el parser RECONOCE ("Etapa", "Esta semana", "Entregable",
 * "Pasos"...) no viven aquí: son claves de lectura, no texto de pantalla. */
import type { PorIdioma } from "../config";

const es = {
  estaSemana: "Esta semana",
  empezarConEsto: "Empezar con esto",
  pasos: "Pasos",
  entregable: "Entregable",
  generadoDeTuRecorrido: "Generado de tu recorrido",
  etapas: { one: "{{n}} etapa", other: "{{n}} etapas" },
  metaEtapas: "{{etapas}} · cada barra muestra su entregable; despliégala para los pasos y la acción",
  tuPrimeraAccion: "Tu primera acción",
  miBitacora: "Mi bitácora",
  historiaDeTuViaje: "La historia de tu viaje, paso a paso.",
  verMiBitacora: "Ver mi bitácora",
  construidoConTuRecorrido: "Construido con tu recorrido",
  notaRecalculo:
    "¿Cambia algo en el mundo real? Vuelve a la entrevista cuando quieras: el plan se recalcula desde donde estés.",
  /** planParser: el bloque que rescata las cifras en negrita de la sección de números */
  losNumerosQueNecesitas: "Los números que necesitas",
};

export const PLAN_DOCUMENTO: PorIdioma<typeof es> = { es };
