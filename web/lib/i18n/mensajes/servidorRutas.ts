/** Rutas de /api de proyectos, sesiones y mundos: los rechazos que comparten varias rutas. */
import type { PorIdioma } from "../config";

const es = {
  noAutenticado: "no autenticado",
  ideaNoEncontrada: "idea no encontrada",
  sesionNoEncontrada: "sesión no encontrada",
  cuerpoInvalido: "cuerpo inválido",
  cuerpoInvalidoJson: "cuerpo inválido, se esperaba JSON",
  cuerpoJsonInvalido: "cuerpo JSON inválido",
  mundoNoExiste: "ese mundo no existe",
  faltaTexto: "falta 'texto'",
  projectIdNoString: "'project_id' debe ser un string",
  noPudimosLeerChecklist: "no pudimos leer tu checklist",
  noPudeGuardarFechas:
    "No pude guardar todas tus fechas. Intenta de nuevo: lo que quedó guardado se corrige al reintentar.",
  mundoNoActivado: 'El mundo "{{mundo}}" aún no está activado para esta idea.',
  conversacionTerminada: "Esta conversación ya terminó. Recarga la página para ver lo último.",
  conversacionSinPendiente: "Esta conversación no tiene nada pendiente. Recarga la página para seguir donde quedaste.",
  tusNumerosConPlan: "Tus Números viene incluido con tu plan. Arma tu plan primero y aquí te espero.",
};

const en: typeof es = {
  noAutenticado: "not authenticated",
  ideaNoEncontrada: "idea not found",
  sesionNoEncontrada: "session not found",
  cuerpoInvalido: "invalid body",
  cuerpoInvalidoJson: "invalid body, expected JSON",
  cuerpoJsonInvalido: "invalid JSON body",
  mundoNoExiste: "that world doesn't exist",
  faltaTexto: "missing 'texto'",
  projectIdNoString: "'project_id' must be a string",
  noPudimosLeerChecklist: "we couldn't read your checklist",
  noPudeGuardarFechas:
    "I couldn't save all your dates. Try again: whatever did get saved will be corrected when you retry.",
  mundoNoActivado: 'The world "{{mundo}}" isn\'t activated for this idea yet.',
  conversacionTerminada: "This conversation has already ended. Reload the page to see the latest.",
  conversacionSinPendiente: "This conversation has nothing pending. Reload the page to pick up where you left off.",
  tusNumerosConPlan: "Your Numbers comes included with your plan. Build your plan first and I'll be waiting for you here.",
};

export const RUTAS: PorIdioma<typeof es> = { es, en };
