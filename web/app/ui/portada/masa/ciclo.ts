/**
 * El ciclo de la masa, en funcion pura del tiempo (segundos).
 *
 * Especificacion: la muestra hibrida aprobada por el fundador
 * (particula-hibrida-my-idea.html), con una decision posterior: la figura
 * se forma con la misma materia, sin particulas. Cuatro fases por ciclo:
 *   reposo    -> la masa liquida sola, viva;
 *   disgrega  -> la masa fluye, se estira y se vuelve la figura;
 *   forma     -> la figura sostenida, hecha del mismo liquido;
 *   regresa   -> la figura se funde de vuelta en la masa.
 * `mezcla` es cuanto de figura hay (0 masa, 1 figura). El respaldo de
 * particulas (equipos debiles) usa el mismo ciclo con particulas.
 * Cada ciclo forma la figura siguiente: foco, lente, brujula, escalera, casa.
 *
 * Es puro y sin estado para que el mismo instante se pueda reproducir
 * (capturas, pruebas, cambio de nivel de calidad sin saltos).
 */

export const FASES = {
  reposo: 3.4,
  disgrega: 1.9,
  forma: 2.6,
  regresa: 1.9,
} as const;

export const DURACION_CICLO = FASES.reposo + FASES.disgrega + FASES.forma + FASES.regresa;

export const FIGURAS = ["foco", "lente", "brujula", "escalera", "casa"] as const;
export type NombreFigura = (typeof FIGURAS)[number];

export interface EstadoCiclo {
  /** Respaldo de particulas: 0 = sin masa, 1 = masa completa. */
  liquido: number;
  /** 0 = la masa, 1 = la figura formada. */
  mezcla: number;
}

export function suavizar(x: number): number {
  const k = Math.min(Math.max(x, 0), 1);
  return k * k * (3 - 2 * k);
}

/** Estado dentro de un ciclo; `tc` en [0, DURACION_CICLO). */
export function estadoEnCiclo(tc: number): EstadoCiclo {
  let resto = tc;
  if (resto < FASES.reposo) return { liquido: 1, mezcla: 0 };
  resto -= FASES.reposo;
  if (resto < FASES.disgrega) {
    const b = resto / FASES.disgrega;
    return { liquido: 1 - suavizar(b * 1.1), mezcla: suavizar(b) };
  }
  resto -= FASES.disgrega;
  if (resto < FASES.forma) return { liquido: 0, mezcla: 1 };
  resto -= FASES.forma;
  const k = resto / FASES.regresa;
  return { liquido: suavizar((k - 0.45) / 0.55), mezcla: 1 - suavizar(k) };
}

/** Estado en el tiempo absoluto `t` (segundos desde el arranque). */
export function estadoEn(t: number): EstadoCiclo {
  const tc = ((t % DURACION_CICLO) + DURACION_CICLO) % DURACION_CICLO;
  return estadoEnCiclo(tc);
}

/** Indice de la figura que forma el ciclo en curso. */
export function figuraEn(t: number): number {
  const ciclo = Math.floor(Math.max(t, 0) / DURACION_CICLO);
  return ciclo % FIGURAS.length;
}

/**
 * Giro de la masa sobre su eje vertical (radianes, en [0, 2pi]). Da una
 * vuelta completa por ciclo mientras es masa: arranca al empezar a
 * regresar de la figura, cruza el reposo y cierra la vuelta justo cuando
 * empieza la transformacion. Asi la figura siempre queda de frente y nunca
 * hay que desenrollar el giro. Arranca y frena suave.
 */
export function giroEn(t: number): number {
  const tc = ((t % DURACION_CICLO) + DURACION_CICLO) % DURACION_CICLO;
  const inicioRegreso = FASES.reposo + FASES.disgrega + FASES.forma;
  const ventana = FASES.regresa + FASES.reposo;
  let u: number;
  if (tc >= inicioRegreso) u = (tc - inicioRegreso) / ventana;
  else if (tc < FASES.reposo) u = (tc + FASES.regresa) / ventana;
  else u = 1;
  return 2 * Math.PI * suavizar(u);
}

/** Instantes de referencia de un ciclo, para capturas y pruebas. */
export const MOMENTOS = {
  reposo: FASES.reposo * 0.5,
  mitadTransformacion: FASES.reposo + FASES.disgrega * 0.5,
  figuraFormada: FASES.reposo + FASES.disgrega + FASES.forma * 0.5,
} as const;
