/** SelectorEstado: las etiquetas de cara de los cinco estados de una tarea y el menú para elegirlos.
 * Las CLAVES de `etiquetas` son los valores de la base (checklist_items.estado): no se traducen. */
import type { PorIdioma } from "../config";

const es = {
  etiquetas: {
    pendiente: "sin empezar",
    empezado: "apenas empezada",
    en_proceso: "en proceso",
    hecho: "hecha",
    no_aplica: "no aplica",
  },
  /** title del disparador: "Estado: hecha · tocar para elegir" */
  tituloDisparador: "Estado: {{estado}} · tocar para elegir",
  /** aria-label del disparador: "hecha. Tocar para elegir el estado" */
  ariaDisparador: "{{estado}}. Tocar para elegir el estado",
  cerrarMenu: "Cerrar el menú de estado",
  comoVa: "¿Cómo va esta tarea?",
  porQueNoAplica: "¿Por qué no aplica?",
  paraTuMemoria: "Para tu propia memoria. Puedes dejarlo en blanco.",
  placeholderMotivo: "No corre para esta idea porque…",
  retirarTarea: "Retirar tarea",
  volver: "volver",
};

const en: typeof es = {
  etiquetas: {
    pendiente: "not started",
    empezado: "just started",
    en_proceso: "in progress",
    hecho: "done",
    no_aplica: "doesn't apply",
  },
  tituloDisparador: "Status: {{estado}} · tap to choose",
  ariaDisparador: "{{estado}}. Tap to choose the status",
  cerrarMenu: "Close the status menu",
  comoVa: "How's this task going?",
  porQueNoAplica: "Why doesn't it apply?",
  paraTuMemoria: "Just for your own memory. You can leave it blank.",
  placeholderMotivo: "It doesn't apply to this idea because…",
  retirarTarea: "Set task aside",
  volver: "back",
};

export const ESTADOS_TAREA: PorIdioma<typeof es> = { es, en };
