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

export const DOCUMENTOS_PAPEL: PorIdioma<typeof es> = { es };
