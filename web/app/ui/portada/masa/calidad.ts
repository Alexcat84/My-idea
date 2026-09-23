/**
 * Niveles de calidad y la regla adaptativa.
 *
 *   alto        escritorio: liquido a resolucion reducida y escalado,
 *               mas pasos de raymarching, AO, bloom, mas particulas.
 *   medio       movil: menos pasos, menos octavas, menos particulas.
 *   bajo        lo minimo con liquido: sin AO ni bloom.
 *   particulas  el respaldo sin liquido (WebGL1, sin three.js).
 *   fija        una imagen quieta, sin WebGL.
 *
 * Durante los primeros segundos se miden los fotogramas; si el nivel no
 * sostiene su minimo se baja uno y se vuelve a medir.
 */

export const NIVELES = ["alto", "medio", "bajo", "particulas", "fija"] as const;
export type Nivel = (typeof NIVELES)[number];
export type NivelLiquido = Extract<Nivel, "alto" | "medio" | "bajo">;

export interface AjustesLiquido {
  /** Pasos maximos del raymarching. */
  pasos: number;
  /** Octavas del fbm de la ondulacion lenta. */
  octavas: number;
  /** Deformacion de dominio completa (3 ejes) o escalar (1 eje). */
  deformacionCompleta: boolean;
  /** Muestras de oclusion ambiental por SDF (0 = sin AO). */
  muestrasAo: number;
  /** Fraccion de la resolucion del lienzo a la que se calcula el liquido. */
  escalaLiquido: number;
  /** Tope del devicePixelRatio del lienzo. */
  dprMaximo: number;
  particulas: number;
  /** Pasos de integracion del ruido de rizo en el vuelo. */
  pasosRizo: number;
  bloom: boolean;
  /** Mediana de fps por debajo de la cual el nivel no se sostiene. */
  fpsMinimo: number;
}

export const AJUSTES: Record<NivelLiquido, AjustesLiquido> = {
  alto: {
    pasos: 72,
    octavas: 3,
    deformacionCompleta: true,
    muestrasAo: 4,
    escalaLiquido: 0.75,
    dprMaximo: 2,
    particulas: 14000,
    pasosRizo: 2,
    bloom: true,
    fpsMinimo: 45,
  },
  medio: {
    pasos: 44,
    octavas: 2,
    deformacionCompleta: false,
    muestrasAo: 2,
    escalaLiquido: 0.6,
    dprMaximo: 1.5,
    particulas: 7000,
    pasosRizo: 1,
    bloom: true,
    fpsMinimo: 38,
  },
  bajo: {
    pasos: 30,
    octavas: 2,
    deformacionCompleta: false,
    muestrasAo: 0,
    escalaLiquido: 0.42,
    dprMaximo: 1,
    particulas: 4000,
    pasosRizo: 1,
    bloom: false,
    fpsMinimo: 28,
  },
};

/** Minimo del respaldo de particulas antes de caer a la imagen fija. */
export const FPS_MINIMO_PARTICULAS = 24;
export const PARTICULAS_RESPALDO = { movil: 5000, escritorio: 11000 } as const;

export function esNivelLiquido(n: Nivel): n is NivelLiquido {
  return n === "alto" || n === "medio" || n === "bajo";
}

export function siguienteNivel(n: Nivel): Nivel {
  const i = NIVELES.indexOf(n);
  return NIVELES[Math.min(i + 1, NIVELES.length - 1)];
}

export function esNivel(valor: string | null | undefined): valor is Nivel {
  return typeof valor === "string" && (NIVELES as readonly string[]).includes(valor);
}

export interface PistasEquipo {
  webgl: boolean;
  webgl2: boolean;
  /** Puntero grueso (tactil) o lado menor de pantalla por debajo de 700 px. */
  movil: boolean;
  nucleos?: number;
  memoriaGb?: number;
  ahorroDatos?: boolean;
  /** WebGL por software (SwiftShader, llvmpipe): no sostiene el liquido. */
  software?: boolean;
}

/** Nivel con el que se arranca antes de medir nada. */
export function nivelInicial(p: PistasEquipo): Nivel {
  if (!p.webgl) return "fija";
  // three.js actual exige WebGL2; el respaldo corre con WebGL1.
  if (!p.webgl2 || p.software) return "particulas";
  const debil = (p.nucleos !== undefined && p.nucleos <= 2) || (p.memoriaGb !== undefined && p.memoriaGb <= 2);
  if (p.ahorroDatos || debil) return p.movil ? "particulas" : "bajo";
  return p.movil ? "medio" : "alto";
}

export type Veredicto = "midiendo" | "sostiene" | "no-sostiene";

/**
 * Mide la mediana de fps de una ventana corta despues de un calentamiento
 * (el primer tramo carga compilacion de shaders y subidas a la GPU).
 */
export class MedidorFps {
  private transcurrido = 0;
  private readonly muestras: number[] = [];
  private veredicto: Veredicto = "midiendo";

  constructor(
    private readonly fpsMinimo: number,
    private readonly calentamientoMs = 700,
    private readonly ventanaMs = 2600,
  ) {}

  /** Registra la duracion de un fotograma (ms) y devuelve el veredicto vigente. */
  registrar(dtMs: number): Veredicto {
    if (this.veredicto !== "midiendo") return this.veredicto;
    // Un salto enorme es una pausa (pestaña oculta, depurador), no un fotograma.
    if (!(dtMs > 0) || dtMs > 1000) return this.veredicto;
    this.transcurrido += dtMs;
    if (this.transcurrido <= this.calentamientoMs) return this.veredicto;
    this.muestras.push(dtMs);
    if (this.transcurrido >= this.calentamientoMs + this.ventanaMs && this.muestras.length >= 8) {
      this.veredicto = this.fpsMediana() >= this.fpsMinimo ? "sostiene" : "no-sostiene";
    }
    return this.veredicto;
  }

  fpsMediana(): number {
    if (this.muestras.length === 0) return 0;
    const orden = [...this.muestras].sort((a, b) => a - b);
    const medio = orden[Math.floor(orden.length / 2)];
    return 1000 / medio;
  }
}
