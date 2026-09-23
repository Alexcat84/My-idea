/**
 * Lado del hilo principal del motor de liquido. Pone el lienzo en el hero,
 * le pasa tamano y puntero, y lo quita al destruir. Dos caminos:
 *
 *  - worker (lo normal): el lienzo se transfiere como OffscreenCanvas a
 *    masa/trabajador.ts, que crea el contexto y corre three.js en su hilo;
 *  - hilo principal: si no hay OffscreenCanvas, o el worker no logra un
 *    contexto WebGL2 (Safari 16.4 transfiere lienzos pero sin WebGL).
 *
 * Nada de este modulo importa three.js.
 */
import type { NivelLiquido } from "./calidad";
import { ATRIBUTOS_CONTEXTO, esSoftware, nombreGpu } from "./contexto";
import type {
  ControlMasa,
  ControlMotor,
  MensajeAlTrabajador,
  MensajeDelTrabajador,
  OpcionesMontaje,
} from "./control";

/** Por que no hay liquido en este equipo: el siguiente paso es el respaldo. */
export class SinLiquido extends Error {
  constructor(readonly motivo: "sin-contexto" | "software") {
    super(motivo);
  }
}

let trabajadorSinContexto = false;

function hayTrabajador(): boolean {
  return (
    !trabajadorSinContexto &&
    typeof Worker !== "undefined" &&
    typeof OffscreenCanvas !== "undefined" &&
    "transferControlToOffscreen" in HTMLCanvasElement.prototype
  );
}

function ponerLienzo(contenedor: HTMLElement): HTMLCanvasElement {
  const lienzo = document.createElement("canvas");
  lienzo.className = "portada-masa-lienzo";
  lienzo.setAttribute("aria-hidden", "true");
  contenedor.appendChild(lienzo);
  return lienzo;
}

function medir(contenedor: HTMLElement) {
  return { ancho: contenedor.clientWidth, alto: contenedor.clientHeight, dpr: window.devicePixelRatio || 1 };
}

/** Cablea tamano y puntero del hero hacia el motor; devuelve como soltarlos. */
function cablear(
  contenedor: HTMLElement,
  redimensionar: (ancho: number, alto: number, dpr: number) => void,
  puntero: (x: number, y: number) => void,
): () => void {
  const observador = new ResizeObserver(() => {
    const t = medir(contenedor);
    redimensionar(t.ancho, t.alto, t.dpr);
  });
  observador.observe(contenedor);
  const alMover = (ev: PointerEvent) => {
    if (ev.pointerType !== "mouse") return;
    puntero(ev.clientX / window.innerWidth - 0.5, ev.clientY / window.innerHeight - 0.5);
  };
  window.addEventListener("pointermove", alMover, { passive: true });
  return () => {
    observador.disconnect();
    window.removeEventListener("pointermove", alMover);
  };
}

async function enTrabajador(nivel: NivelLiquido, o: OpcionesMontaje): Promise<ControlMasa> {
  const lienzo = ponerLienzo(o.contenedor);
  const fuera = lienzo.transferControlToOffscreen();
  const trabajador = new Worker(new URL("./trabajador.ts", import.meta.url), { type: "module" });
  const enviar = (m: MensajeAlTrabajador, transferir: Transferable[] = []) => trabajador.postMessage(m, transferir);
  let tiempo = o.tiempoInicial;
  const cerrar = () => {
    trabajador.terminate();
    lienzo.remove();
  };

  try {
    await new Promise<void>((listo, fallar) => {
      trabajador.onmessage = (ev: MessageEvent<MensajeDelTrabajador>) => {
        const m = ev.data;
        switch (m.tipo) {
          case "montado":
            listo();
            return;
          case "sin-contexto":
          case "software":
            fallar(new SinLiquido(m.tipo));
            return;
          case "error":
            console.error("[portada] el motor de la masa no arranco:", m.texto);
            fallar(new Error(m.texto));
            return;
          case "primer-fotograma":
            lienzo.style.opacity = "1";
            o.alPrimerFotograma();
            return;
          case "aviso":
            tiempo = m.tiempo;
            o.alAviso(m.aviso, m.fps);
            return;
          case "fps":
            tiempo = m.tiempo;
            o.contenedor.dataset.fps = m.fps.toFixed(0);
            return;
        }
      };
      // El chunk del worker no llego o fallo al evaluarse.
      trabajador.onerror = (ev) => {
        ev.preventDefault();
        fallar(new Error(ev.message || "worker"));
      };
      const t = medir(o.contenedor);
      enviar(
        {
          tipo: "montar",
          lienzo: fuera,
          nivel,
          ...t,
          tiempoInicial: o.tiempoInicial,
          reducido: o.reducido,
          tiempoFijo: o.tiempoFijo,
          adaptativo: o.adaptativo,
        },
        [fuera],
      );
    });
  } catch (error) {
    cerrar();
    throw error;
  }

  const soltar = cablear(
    o.contenedor,
    (ancho, alto, dpr) => enviar({ tipo: "redimensionar", ancho, alto, dpr }),
    (x, y) => enviar({ tipo: "puntero", x, y }),
  );
  return {
    pausar: () => enviar({ tipo: "pausar" }),
    reanudar: () => enviar({ tipo: "reanudar" }),
    destruir() {
      soltar();
      enviar({ tipo: "destruir" });
      cerrar();
    },
    tiempo: () => tiempo,
  };
}

async function enHiloPrincipal(nivel: NivelLiquido, o: OpcionesMontaje): Promise<ControlMasa> {
  const lienzo = ponerLienzo(o.contenedor);
  const contexto = lienzo.getContext("webgl2", ATRIBUTOS_CONTEXTO);
  if (!contexto || esSoftware(nombreGpu(contexto))) {
    contexto?.getExtension("WEBGL_lose_context")?.loseContext();
    lienzo.remove();
    throw new SinLiquido(contexto ? "software" : "sin-contexto");
  }
  let motor: ControlMotor;
  try {
    const { montarMotor } = await import("./motor");
    motor = await montarMotor(nivel, {
      lienzo,
      contexto,
      ...medir(o.contenedor),
      tiempoInicial: o.tiempoInicial,
      reducido: o.reducido,
      tiempoFijo: o.tiempoFijo,
      adaptativo: o.adaptativo,
      alPrimerFotograma: () => {
        lienzo.style.opacity = "1";
        o.alPrimerFotograma();
      },
      alAviso: (aviso, fps) => o.alAviso(aviso, fps),
      alFps: (fps) => {
        o.contenedor.dataset.fps = fps.toFixed(0);
      },
    });
  } catch (error) {
    contexto.getExtension("WEBGL_lose_context")?.loseContext();
    lienzo.remove();
    throw error;
  }
  const soltar = cablear(o.contenedor, motor.redimensionar, motor.puntero);
  return {
    pausar: motor.pausar,
    reanudar: motor.reanudar,
    destruir() {
      soltar();
      motor.destruir();
      lienzo.remove();
    },
    tiempo: motor.tiempo,
  };
}

/** Monta el liquido en un worker si se puede; si no, en el hilo principal. */
export async function montarLiquido(nivel: NivelLiquido, o: OpcionesMontaje): Promise<ControlMasa> {
  if (hayTrabajador()) {
    try {
      return await enTrabajador(nivel, o);
    } catch (error) {
      if (!(error instanceof SinLiquido && error.motivo === "sin-contexto")) throw error;
      // OffscreenCanvas sin WebGL2: se recuerda y se prueba en el hilo principal.
      trabajadorSinContexto = true;
    }
  }
  return enHiloPrincipal(nivel, o);
}
