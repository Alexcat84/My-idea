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

const en: typeof es = {
  estaSemana: "This week",
  empezarConEsto: "Start with this",
  pasos: "Steps",
  entregable: "Deliverable",
  generadoDeTuRecorrido: "Generated from your path",
  etapas: { one: "{{n}} stage", other: "{{n}} stages" },
  metaEtapas: "{{etapas}} · each bar shows its deliverable; expand it for the steps and the action",
  tuPrimeraAccion: "Your first action",
  miBitacora: "My Logbook",
  historiaDeTuViaje: "The story of your journey, step by step.",
  verMiBitacora: "See my Logbook",
  construidoConTuRecorrido: "Built from your path",
  notaRecalculo:
    "Something changed in the real world? Go back to the interview whenever you like: the plan recalculates from wherever you are.",
  losNumerosQueNecesitas: "The numbers you need",
};

export const PLAN_DOCUMENTO: PorIdioma<typeof es> = { es, en };
