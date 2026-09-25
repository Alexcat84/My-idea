/** /nueva: La Chispa, la espera del organizador y sus errores (app/nueva/page.tsx).
 * La tarjeta del resultado vive en claridad.ts. */
import type { PorIdioma } from "../config";

const es = {
  errores: {
    conexionCortadaRef:
      "La conexión se cortó antes de terminar. Tu texto sigue aquí; intenta de nuevo (referencia {{id}}).",
    sinId: "sin id",
    atorado: "algo se atoró; intenta de nuevo",
    cortadaAMedioCamino: "la conexión se cortó a medio camino; tu texto sigue aquí, intenta de nuevo",
    tardando: "esto está tardando más de lo normal; tu texto sigue aquí, intenta de nuevo",
    sinConexion: "no pudimos conectar; revisa tu internet e intenta de nuevo",
  },
  irAMisIdeas: "Ir a mis ideas",
  organizando: "Organizando tu idea…",
  etiquetaChispa: "Nueva idea · La Chispa",
  cuentameTuIdea: "Cuéntame tu idea",
  subtitulo: "Escríbela o díctala tal como la tienes en mente. Ese es todo el requisito.",
  placeholder: "Quiero vender café de especialidad a domicilio en mi barrio…",
  intentarDeNuevo: "Intentar de nuevo",
  sinPlantillas: "Sin plantillas ni formularios. Solo tu idea, en tus palabras.",
  continuar: "Continuar",
};

export const NUEVA_IDEA: PorIdioma<typeof es> = { es };
