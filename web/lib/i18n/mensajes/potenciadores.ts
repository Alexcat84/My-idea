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

const en: typeof es = {
  misIdeas: "My ideas /",
  titulo: "Power up",
  ideaSinTitulo: "Untitled idea",
  elegirIdea: {
    titulo: "Which idea do you want to power up?",
    sinIdeas: "Power-ups are added to an idea. Once you have your first one, you'll be able to pick it here.",
    texto: "Pick one and I'll take you to its power-ups.",
    pista: "Add a world to it or check out its power-ups.",
  },
  elegirPotenciador: {
    error: "we couldn't load your idea; try again in a moment",
    cargando: "Loading your idea…",
    cambiarIdea: "← Switch idea",
    titulo: "Which power-up do you want to use?",
    texto: "For <idea/>. Once you apply it, it's added to your idea and you pick up from there.",
  },
};

export const POTENCIADORES: PorIdioma<typeof es> = { es, en };
