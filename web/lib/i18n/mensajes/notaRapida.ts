/** NotaRapida: el atajo de nota de cada actividad (Manos a la Obra y Calendario). */
import type { PorIdioma } from "../config";

const es = {
  verOEditar: "Ver o editar tu nota",
  anadir: "Añadir una nota",
  cerrarNota: "Cerrar la nota",
  tuNota: "Tu nota",
  placeholder: "Lo que necesites recordar…",
  guardar: "Guardar",
  cerrar: "cerrar",
  quitar: "quitar",
};

const en: typeof es = {
  verOEditar: "View or edit your note",
  anadir: "Add a note",
  cerrarNota: "Close the note",
  tuNota: "Your note",
  placeholder: "Anything you need to remember…",
  guardar: "Save",
  cerrar: "close",
  quitar: "remove",
};

export const NOTA_RAPIDA: PorIdioma<typeof es> = { es, en };
