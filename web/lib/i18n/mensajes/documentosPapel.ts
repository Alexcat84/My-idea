/** Los documentos en papel (PDF) estructurados: el resumen "Cómo te fue" del
 * Expediente (app/ui/ResumenPapel.tsx) y la bitácora impresa
 * (app/ui/BitacoraPapel.tsx). */
import type { PorIdioma } from "../config";

const es = {
  resumen: {
    comoTeFue: "Cómo te fue",
    tuProgreso: "Tu progreso hasta aquí",
    diasDeCamino: "días de camino",
    accionesCumplidas: "acciones cumplidas",
    hitosAlcanzados: "hitos alcanzados",
    tuViajeCompleto: "Tu viaje completo",
    cierre: "Aquí acaba tu idea y nace tu proyecto",
    sigueEnMarcha:
      "Tu idea sigue en marcha. Cuando la des por realizada, aquí quedará tu cierre con tus propias palabras.",
    loQueMasTeMovio: "Lo que más te movió el camino",
    loQueQuedoPendiente: "Lo que quedó pendiente",
    /** los meses abreviados del mapa de hitos ("3 may") */
    meses: ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"],
    /** la fecha corta: "3 feb" (i18n F3: el orden lo pone cada idioma) */
    fechaCorta: "{{d}} {{mes}}",
  },
  bitacora: {
    rango:
      "Del {{desde}} al {{hasta}}, día por día, tal como quedó registrado. Si moviste una fecha, la original sigue aquí: nada se reescribe.",
    laSecuencia: "La secuencia de tu viaje",
    pie: "Esta es tu historia tal como quedó registrada, día por día. Puedes descargarla aparte cuando quieras.",
  },
  /** los rótulos del pie de página */
  pieExpediente: "Expediente",
  pieMiBitacora: "Mi bitácora",
};

const en: typeof es = {
  resumen: {
    comoTeFue: "How it went",
    tuProgreso: "Your progress so far",
    diasDeCamino: "days on the road",
    accionesCumplidas: "actions completed",
    hitosAlcanzados: "milestones reached",
    tuViajeCompleto: "Your whole journey",
    cierre: "This is where your idea ends and your project begins",
    sigueEnMarcha:
      "Your idea is still underway. When you call it achieved, your close will be here, in your own words.",
    loQueMasTeMovio: "What moved your journey forward the most",
    loQueQuedoPendiente: "What's still open",
    meses: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    fechaCorta: "{{mes}} {{d}}",
  },
  bitacora: {
    rango:
      "From {{desde}} to {{hasta}}, day by day, just as it was recorded. If you moved a date, the original is still here: nothing gets rewritten.",
    laSecuencia: "The sequence of your journey",
    pie: "This is your story just as it was recorded, day by day. You can download it separately whenever you like.",
  },
  pieExpediente: "Full Record",
  pieMiBitacora: "My Logbook",
};

export const DOCUMENTOS_PAPEL: PorIdioma<typeof es> = { es, en };
