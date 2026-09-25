/** El sitio entero (app/layout.tsx): metadatos y el sello de versión. El título "My Idea" es la marca y no pasa por aquí. */
import type { PorIdioma } from "../config";

const es = {
  descripcion: "El espacio donde tus ideas se trabajan.",
  /** aria-label del sello de versión al pie de cada página. */
  etiquetaVersion: "versión",
};

export const SITIO: PorIdioma<typeof es> = { es };
