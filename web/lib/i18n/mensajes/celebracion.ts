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

const en: typeof es = {
  error: "something got stuck on our side; try again in a moment",
  errorCargar: "we couldn't load your celebration; check your connection and try again",
  errorReabrir: "we couldn't reopen your idea; check your connection and try again",
  preparando: "Getting your celebration ready…",
  realizada: "Achieved",
  heroe: "This is where your idea ends and your project begins",
  proyecto: "Project",
  porQueCerraste: "Why you closed it here",
  estadisticasDe: "{{nombre}} in numbers",
  diasDesdeLaChispa: "days since the spark",
  ciclosDePlan: "plan cycles",
  deTotal: "of {{total}}",
  acciones: "actions",
  mundosActivados: { one: "world activated", other: "worlds activated" },
  aTiempo: "{{n}} on time",
  adelantadas: "{{n}} early",
  tardias: "{{n}} late",
  verAnalisis: "See the full analysis →",
  descargarExpediente: "Download your Full Record →",
  volverAMisIdeas: "Back to my ideas",
  reabriendo: "Reopening…",
  reabrir: "Reopen this idea",
};

export const CELEBRACION: PorIdioma<typeof es> = { es, en };
