/** /potenciadores: app/potenciadores/page.tsx y ElegirPotenciador.tsx (solo la puerta y el foco; la parrilla vive en PotenciaTuIdea). */
import type { PorIdioma } from "../config";

const es = {
  misIdeas: "Mis ideas /",
  titulo: "Potenciar",
  ideaSinTitulo: "Idea sin título",
  elegirIdea: {
    titulo: "¿Qué idea quieres potenciar?",
    sinIdeas: "Los potenciadores se suman a una idea. Cuando tengas la primera, aquí podrás elegirla.",
    texto: "Elige una y te llevo a sus potenciadores.",
    pista: "Añádele un mundo o revisa sus potenciadores.",
  },
  elegirPotenciador: {
    error: "no pudimos cargar tu idea; intenta de nuevo en un momento",
    cargando: "Cargando tu idea…",
    cambiarIdea: "← Cambiar de idea",
    titulo: "¿Qué potenciador quieres usar?",
    texto: "Para <idea/>. Al aplicarlo queda agregado a tu idea, y sigues desde ahí.",
  },
};

export const POTENCIADORES: PorIdioma<typeof es> = { es };
