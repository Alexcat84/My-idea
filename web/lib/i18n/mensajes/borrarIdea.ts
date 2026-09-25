/** Borrar una idea desde su cinta en /ideas (app/ui/BorrarIdeaCinta.tsx). */
import type { PorIdioma } from "../config";

const es = {
  borrarla: "¿Borrarla?",
  si: "Sí",
  no: "No",
  ariaBorrar: "Borrar la idea {{nombre}}",
  tituloBorrar: "Borrar idea",
};

const en: typeof es = {
  borrarla: "Delete it?",
  si: "Yes",
  no: "No",
  ariaBorrar: "Delete the idea {{nombre}}",
  tituloBorrar: "Delete idea",
};

export const BORRAR_IDEA: PorIdioma<typeof es> = { es, en };
