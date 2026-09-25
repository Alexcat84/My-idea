/** DetalleActividad: el cajón "Explorar actividad" (cumplimiento, protección, estado, esfuerzo, fecha y nota). */
import type { PorIdioma } from "../config";

const es = {
  chip: {
    aTiempo: "A tiempo",
    tardia: { one: "Tardía · {{n}} día", other: "Tardía · {{n}} días" },
    adelantada: { one: "Adelantada · {{n}} día", other: "Adelantada · {{n}} días" },
  },
  dialogo: "Detalle de la actividad",
  cerrar: "Cerrar",
  cerrarDetalle: "Cerrar el detalle",
  etapa: "Etapa {{n}}",
  protegida: "Protegida",
  protege: "Protege:",
  protegeRetirada: "la actividad que protegía fue retirada",
  protegeSistemica: "tu negocio entero",
  protegeFueraDelPlan: "una actividad que ya no está en tu plan",
  estado: "Estado",
  elegirEstado: "Elegir estado",
  porQueNoAplica: "¿Por qué no aplica? Para tu propia memoria (opcional).",
  placeholderMotivo: "No corre para esta idea porque…",
  cuandoLoHiciste: "¿Cuándo lo hiciste?",
  cuandoLoHicisteAria: "Cuándo lo hiciste",
  esfuerzo: "Esfuerzo",
  corregir: "corregir",
  dependeDeTerceros: "· depende de terceros",
  estimadoConEspera:
    "Es un estimado de tu trabajo. Esta tarea depende de respuestas de otros: empiézala temprano, que tu fecha ya trae el colchón de esa espera y el tiempo que ellos tarden no se te cuenta.",
  estimado: "Es un estimado para orientarte. Si no calza con tu realidad, corrígelo.",
  cuantoTeToma: "¿Cuánto te toma de verdad?",
  /** el "cancelar" en texto de las ediciones en línea (esfuerzo, fecha); el botón del pie es botonCancelar */
  cancelarEdicion: "cancelar",
  fecha: "Fecha",
  cambiarFecha: "cambiar fecha",
  diasDespues: { one: "{{n}} día después", other: "{{n}} días después" },
  diasAntes: { one: "{{n}} día antes", other: "{{n}} días antes" },
  nuevaFecha: "Nueva fecha: <b>{{fecha}}</b>.",
  hayPosteriores: {
    one: "Hay <b>{{n}}</b> actividad pendiente que sigue.",
    other: "Hay <b>{{n}}</b> actividades pendientes que siguen.",
  },
  lasMuevo: "¿Las muevo también, {{rumbo}} cada una?",
  moverTodas: "Sí, mover todas",
  soloEsta: "Solo esta",
  nuevaFechaObjetivo: "Nueva fecha objetivo",
  yaLaMoviste: "Ya la moviste: la original ({{fecha}}) se conserva en tu historia.",
  siLaMueves: "Si la mueves, la fecha original se conserva en tu historia. No se reescribe nada.",
  tuNota: "Tu nota",
  placeholderNota: "Lo que necesites recordar de esta acción…",
  notaGratis: "Registrar tu nota es gratis, siempre.",
  guardar: "Guardar",
  botonCancelar: "Cancelar",
};

export const DETALLE_ACTIVIDAD: PorIdioma<typeof es> = { es };
