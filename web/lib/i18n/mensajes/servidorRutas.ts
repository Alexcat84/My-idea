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

export const RUTAS: PorIdioma<typeof es> = { es };
