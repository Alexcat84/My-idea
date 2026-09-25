/** La sesión en el encabezado: ui/BotonSalir.tsx y ui/Saludo.tsx. */
import type { PorIdioma } from "../config";

const es = {
  salir: "Salir",
  saludo: {
    manana: "Buenos días",
    tarde: "Buenas tardes",
    noche: "Buenas noches",
    /** El neutro del servidor, que no conoce el huso del visitante. */
    neutro: "Hola",
  },
};

export const SESION: PorIdioma<typeof es> = { es };
