/** La Celebración (app/ui/Celebracion.tsx): el timeline del viaje al cerrar la
 * idea, sus estadísticas y sus acciones. */
import type { PorIdioma } from "../config";

const es = {
  error: "algo se atoró de nuestro lado; intenta de nuevo en un momento",
  errorCargar: "no pudimos cargar tu celebración; revisa tu internet e intenta de nuevo",
  errorReabrir: "no pudimos reabrir tu idea; revisa tu internet e intenta de nuevo",
  preparando: "Preparando tu celebración…",
  realizada: "Realizada",
  heroe: "Aquí acaba tu idea y nace tu proyecto",
  proyecto: "Proyecto",
  porQueCerraste: "Por qué la cerraste aquí",
  estadisticasDe: "Estadísticas de {{nombre}}",
  diasDesdeLaChispa: "días desde la chispa",
  ciclosDePlan: "ciclos de plan",
  deTotal: "de {{total}}",
  acciones: "acciones",
  mundosActivados: { one: "mundo activado", other: "mundos activados" },
  aTiempo: "{{n}} a tiempo",
  adelantadas: "{{n}} adelantadas",
  tardias: "{{n}} tardías",
  verAnalisis: "Ver análisis completo →",
  descargarExpediente: "Descargar tu expediente →",
  volverAMisIdeas: "Volver a mis ideas",
  reabriendo: "Reabriendo…",
  reabrir: "Reabrir esta idea",
};

export const CELEBRACION: PorIdioma<typeof es> = { es };
