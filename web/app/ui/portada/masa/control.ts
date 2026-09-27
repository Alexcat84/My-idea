/**
 * Contratos de la masa: lo que HeroMasa sabe de un motor montado, lo que
 * el motor three.js necesita (sin DOM: corre igual en el hilo principal o
 * en un worker con OffscreenCanvas) y los mensajes entre hilo y worker.
 */
import type { NivelLiquido } from "./calidad";

export type Aviso = "no-sostiene" | "fallo";

/** Lo que HeroMasa controla, sea cual sea el motor y el hilo. */
export interface ControlMasa {
  pausar(): void;
  reanudar(): void;
  destruir(): void;
  /** Tiempo del ciclo en segundos. */
  tiempo(): number;
}

/** Opciones de montaje desde HeroMasa (lado DOM). */
export interface OpcionesMontaje {
  contenedor: HTMLElement;
  /** Segundos del ciclo con que arranca (continuidad al cambiar de nivel). */
  tiempoInicial: number;
  /** prefers-reduced-motion: un solo fotograma de la masa quieta. */
  reducido: boolean;
  /** Congela el ciclo en este instante (verificacion y capturas). */
  tiempoFijo: number | null;
  /** Medir los primeros segundos y avisar si el nivel no se sostiene. */
  adaptativo: boolean;
  alPrimerFotograma: () => void;
  alAviso: (aviso: Aviso, fps: number) => void;
}

/** Opciones del motor three.js: nada de DOM, para poder correr en un worker. */
export interface OpcionesMotor {
  lienzo: HTMLCanvasElement | OffscreenCanvas;
  /** Contexto WebGL2 ya creado sobre ese lienzo (se paga una sola vez). */
  contexto?: WebGL2RenderingContext;
  /** Tamano del hero en px CSS y devicePixelRatio. */
  ancho: number;
  alto: number;
  dpr: number;
  tiempoInicial: number;
  reducido: boolean;
  tiempoFijo: number | null;
  adaptativo: boolean;
  alPrimerFotograma: () => void;
  alAviso: (aviso: Aviso, fps: number, tiempo: number) => void;
  alFps: (fps: number, tiempo: number) => void;
}

export interface ControlMotor extends ControlMasa {
  redimensionar(ancho: number, alto: number, dpr: number): void;
  /** Posicion del puntero relativa al centro de la ventana, en [-0.5, 0.5]. */
  puntero(x: number, y: number): void;
}

export type MensajeAlTrabajador =
  | {
      tipo: "montar";
      lienzo: OffscreenCanvas;
      nivel: NivelLiquido;
      ancho: number;
      alto: number;
      dpr: number;
      tiempoInicial: number;
      reducido: boolean;
      tiempoFijo: number | null;
      adaptativo: boolean;
    }
  | { tipo: "redimensionar"; ancho: number; alto: number; dpr: number }
  | { tipo: "puntero"; x: number; y: number }
  | { tipo: "pausar" }
  | { tipo: "reanudar" }
  | { tipo: "destruir" };

export type MensajeDelTrabajador =
  /** El worker no pudo crear un contexto WebGL2 sobre OffscreenCanvas. */
  | { tipo: "sin-contexto" }
  /** Hay contexto, pero la GPU es por software: no sostiene el liquido. */
  | { tipo: "software" }
  | { tipo: "montado" }
  | { tipo: "primer-fotograma" }
  | { tipo: "aviso"; aviso: Aviso; fps: number; tiempo: number }
  | { tipo: "fps"; fps: number; tiempo: number }
  | { tipo: "error"; texto: string };
