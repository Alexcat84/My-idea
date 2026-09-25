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

const en: typeof es = {
  errores: {
    conexionCortadaRef:
      "The connection dropped before we could finish. Your text is still here; try again (reference {{id}}).",
    sinId: "no id",
    atorado: "something got stuck; try again",
    cortadaAMedioCamino: "the connection dropped halfway through; your text is still here, try again",
    tardando: "this is taking longer than usual; your text is still here, try again",
    sinConexion: "we couldn't connect; check your internet connection and try again",
  },
  irAMisIdeas: "Go to my ideas",
  organizando: "Organizing your idea…",
  etiquetaChispa: "New idea · The Spark",
  cuentameTuIdea: "Tell me your idea",
  subtitulo: "Type it or dictate it just as you have it in mind. That's all it takes.",
  placeholder: "I want to deliver specialty coffee to homes in my neighborhood…",
  intentarDeNuevo: "Try again",
  sinPlantillas: "No templates or forms. Just your idea, in your own words.",
  continuar: "Continue",
};

export const NUEVA_IDEA: PorIdioma<typeof es> = { es, en };
