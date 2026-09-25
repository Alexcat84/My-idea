/** La bitácora del cliente: la página (Bitacora), la de un espacio (BitacoraEspacio) y las
 * líneas y el documento que arma lib/bitacoraCliente.ts. */
import type { PorIdioma } from "../config";

const es = {
  pagina: {
    /** los números en palabra del subtítulo del día, del 1 al 10 */
    numeros: ["un", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez"],
    primerDia: "el día en que empezó todo",
    momentosDia: "{{n}} momentos este día",
    cierre: "Aquí acaba tu idea y nace tu proyecto.",
    errorCarga: "No pudimos cargar tu bitácora. Vuelve a intentarlo en un momento.",
    cargando: "Cargando tu bitácora…",
    /** "del 3 de julio de 2026 al 9 de agosto de 2026" */
    rango: "del {{desde}} al {{hasta}}",
    volver: "← Volver",
    tuHistoria: "Tu historia",
    bitacoraDe: "Bitácora de {{nombre}}",
    esteMundo: "este mundo",
    miBitacora: "Mi bitácora de mi viaje",
    vacia: "Tu historia apenas empieza. Cada paso que des irá quedando aquí: cada estado que cambies, cada fecha que muevas, cada nota.",
    pie: "Esta es tu historia tal como quedó registrada, día por día. Nada se reescribe: si moviste una fecha, la original sigue aquí.",
  },
  espacio: {
    errorCarga: "No pudimos cargar la bitácora de este espacio.",
    cargando: "Cargando la bitácora de este espacio…",
    tuBitacora: "Tu bitácora",
    /** nombre del archivo .md descargado */
    archivo: "Bitácora de {{nombre}}",
    vacia: "Este espacio aún no tiene bitácora. En cuanto registres algo aquí (un estado, una fecha, una nota), su historia empezará a quedar guardada.",
  },
  historia: {
    unaActividad: "una actividad",
    /** una actividad citada: «Llama a un cliente» */
    refCita: "«{{texto}}»",
    /** el motivo del usuario al final de una línea, o el punto si no dio motivo */
    motivoCita: ": «{{motivo}}»",
    punto: ".",
    chispa: "Encendiste la chispa y escribiste tu idea.",
    chispaTitulo: "La Chispa",
    ordenaste: "Ordenaste tu idea y ganaste claridad.",
    ordenasteTitulo: "Tu idea ordenada",
    explorar: "Empezaste a explorar tu idea, pregunta por pregunta.",
    plan: "Recibiste tu plan.",
    planTitulo: "Tu Plan",
    seguimiento: "Contaste qué pasó y recalculé tu plan (seguimiento {{n}}).",
    seguimientoTitulo: "Seguimiento {{n}}",
    lineaBase: "Aceptaste tus fechas: tu línea base quedó sellada.",
    lineaBaseTitulo: "Tu línea base",
    numeros: "Calculaste Tus Números.",
    numerosVersion: "Calculaste Tus Números (versión {{n}}).",
    numerosTitulo: "Tus Números",
    planMundo: "Se generó tu plan de {{mundo}}.",
    modoFechas: "con fechas y recordatorios",
    modoRitmo: "a tu ritmo",
    cambiasteModo: "Cambiaste tu forma de avanzar: {{modo}}.",
    elegisteModo: "Elegiste llevar tu camino {{modo}}.",
    empezaste: "Empezaste {{ref}}.",
    enProceso: "Pusiste {{ref}} en proceso.",
    aPendiente: "Devolviste {{ref}} a pendiente.",
    marcasteHecha: "Marcaste hecha {{ref}}.",
    /** la hecha derivada de completed_at (ítems sin evento) */
    marcasteHechaCita: "Marcaste hecha «{{texto}}».",
    retiraste: "Retiraste {{ref}}{{cita}}",
    reactivaste: "Reactivaste {{ref}}.",
    ajustasteFechaHecho: "Ajustaste la fecha en que hiciste {{ref}}.",
    anotaste: "Anotaste algo en {{ref}}.",
    diasDespues: { one: "{{n}} día después", other: "{{n}} días después" },
    diasAntes: { one: "{{n}} día antes", other: "{{n}} días antes" },
    colaCascada: " y las {{n}} siguientes, {{rumbo}} cada una.",
    movisteFecha: "Moviste la fecha de {{ref}}{{cola}}",
    reabristeMundo: "Reabriste el mundo {{mundo}}.",
    completasteMundo: "Completaste el mundo {{mundo}}{{cita}}",
    exploraste: "Exploraste gratis el mundo {{mundo}}.",
    diagnostico: "Tu diagnóstico de {{mundo}} quedó listo.",
    sumaste: "Sumaste el plan completo de {{mundo}}.",
    reabristeIdea: "Reabriste tu idea para seguir trabajándola.",
    realizadaCita: "Marcaste tu idea como realizada{{cita}}",
    realizada: "Marcaste tu idea como realizada.",
    realizadoTitulo: "Realizado",
    tuViaje: "Tu viaje",
  },
  documento: {
    titulo: "# La historia de {{nombre}}",
    generada: "> Generada el {{fecha}}",
    vacia: "Tu historia apenas empieza. Cada paso que des irá quedando aquí.",
    rango: "> Del {{desde}} al {{hasta}}",
  },
};

export const BITACORA: PorIdioma<typeof es> = { es };
