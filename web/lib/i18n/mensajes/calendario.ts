/** El Calendario (modo "con fechas"), su tarjeta de sincronía (SuscripcionCalendario) y el .ics (lib/ics.ts). */
import type { PorIdioma } from "../config";

const es = {
  tuViaje: "Tu viaje",
  /** cabeceras de la rejilla, de lunes a domingo */
  diasCortos: ["LUN", "MAR", "MIÉ", "JUE", "VIE", "SÁB", "DOM"],
  /** los meses abreviados del título de la semana */
  mesesCortos: ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"],
  grupos: {
    vencidas: "Ya pasó y sigue abierto",
    hoy: "Hoy",
    manana: "Mañana",
    semana: "Esta semana",
    proxima: "La próxima semana",
    adelante: "Más adelante",
  },
  relativo: {
    hoy: "hoy",
    manana: "mañana",
    ayer: "ayer",
    haceDias: "hace {{n}} días",
    enDias: "en {{n}} días",
  },
  errorMoverFecha: "No pudimos mover la fecha; revisa tu internet.",
  errorGuardarCambio: "No pudimos guardar el cambio.",
  errorGuardarInternet: "No pudimos guardar; revisa tu internet.",
  etapa: "Etapa {{n}}",
  /** el nombre de la idea en la descripción de los eventos del .ics descargado */
  nombreIdeaIcs: "Mi idea",
  /** "20 abr a 26 abr" */
  rangoSemana: "{{d1}} {{m1}} a {{d2}} {{m2}}",
  loQueViene: "Lo que viene",
  volver: "← Volver",
  calendarioDe: "Calendario de {{nombre}}",
  esteMundo: "este mundo",
  tuCalendario: "Tu calendario",
  mesAnterior: "Mes anterior",
  semanaAnterior: "Semana anterior",
  hoyBoton: "Hoy",
  mesSiguiente: "Mes siguiente",
  semanaSiguiente: "Semana siguiente",
  vistas: { mes: "Mes", semana: "Semana", agenda: "Agenda" },
  bandaVencidas: {
    one: "Una fecha ya pasó y sigue abierta. Puedes moverla al día que te sirva.",
    other: "{{n}} fechas ya pasaron y siguen abiertas. Puedes moverlas al día que te sirva.",
  },
  estadisticasTitulo: "Tus estadísticas",
  estadisticasTexto: "Tu avance, tu ritmo y tu cumplimiento, en gráficos. Aquí planeas; ahí ves cómo vas.",
  verAnalisis: "Ver el análisis",
  sinTareasAdelante: "No tienes tareas con fecha por delante. Cuando pongas fechas a tus tareas, aquí verás qué toca y cuándo.",
  sinFecha: {
    one: "Después de esto, <b>{{n}}</b> tarea sigue sin fecha.",
    other: "Después de esto, <b>{{n}}</b> tareas siguen sin fecha.",
  },
  ponerlesFecha: "Ponerles fecha",
  verDetalle: "Ver el detalle",
  verDetalleTarea: "Ver el detalle de la tarea",
  marcarHecha: "Marcar hecha",
  ponerleFechaNueva: "Ponerle fecha nueva",
  moverFecha: "Mover fecha",
  detalle: "Detalle",
  conNota: "(con nota)",
  yaPaso: "ya pasó",
  /** la marca de vencida tras la etapa, en el panel del día */
  puntoYaPaso: "· ya pasó",
  hecha: "Hecha",
  mover: "Mover",
  sinTareasDia: "No hay tareas con fecha este día. Toca otro día para ver las suyas.",
  verDia: "Ver el {{n}}",
  masChips: "+{{n}} más",
  leyenda: { prevista: "Prevista", hecha: "Hecha", yaPaso: "Ya pasó", hoy: "Hoy" },
  arrastraParaMover: "arrastra para mover",
  /** el mismo aviso al final del title de una tarjeta de la semana */
  puntoArrastraParaMover: "· arrastra para mover",
  marcarPrimeraHecha: "Marcar la primera hecha",
  suscripcion: {
    titulo: "Sincronizar con mi calendario",
    comoFunciona: "Cómo funciona la sincronía",
    cerrar: "Cerrar",
    info: "Te suscribes una sola vez. Después, tus fechas aparecen en el calendario que ya usas (Google, Apple, Outlook…) y se actualizan solas cuando cambias algo aquí. Tu calendario te avisa de cada tarea el mismo día.",
    infoRefresco: "No aparecen al instante: tu calendario se refresca cada cierto tiempo (a veces minutos, a veces horas). Si quieres verlas ya mismo, descarga el archivo.",
    subtitulo: "Ten tus fechas en el calendario que ya usas.",
    suscribir: "Suscribir mi calendario",
    creaCuenta: "Crea tu cuenta para suscribir tu calendario.",
    descargar: "Descargar el archivo (.ics)",
  },
  ics: {
    /** la descripción de cada evento: "Etapa 2 · Mi idea" */
    descripcion: "Etapa {{n}} · {{idea}}",
  },
};

export const CALENDARIO: PorIdioma<typeof es> = { es };
