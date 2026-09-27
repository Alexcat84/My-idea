/**
 * Worker de la masa: crea el contexto WebGL2 sobre el OffscreenCanvas que
 * le transfiere el hilo principal, sondea la GPU y corre el motor three.js.
 * Asi crear el contexto (100 a 170 ms), evaluar three.js y compilar los
 * shaders no bloquean nunca el hilo de la pagina.
 */
import { ATRIBUTOS_CONTEXTO, esSoftware, nombreGpu } from "./contexto";
import type { ControlMotor, MensajeAlTrabajador, MensajeDelTrabajador } from "./control";
import { montarMotor } from "./motor";

interface AmbitoTrabajador {
  postMessage(mensaje: MensajeDelTrabajador): void;
  onmessage: ((ev: MessageEvent<MensajeAlTrabajador>) => void) | null;
  requestAnimationFrame?: (cb: FrameRequestCallback) => number;
  cancelAnimationFrame?: (id: number) => void;
}

const ambito = globalThis as unknown as AmbitoTrabajador;
const enviar = (m: MensajeDelTrabajador) => ambito.postMessage(m);

// rAF existe en los workers de Chrome, Firefox y Safari reciente; si no, un reloj de 60 Hz.
if (typeof ambito.requestAnimationFrame !== "function") {
  ambito.requestAnimationFrame = (cb) => setTimeout(() => cb(performance.now()), 16) as unknown as number;
  ambito.cancelAnimationFrame = (id) => clearTimeout(id);
}

let motor: ControlMotor | null = null;

ambito.onmessage = async (ev) => {
  const m = ev.data;
  switch (m.tipo) {
    case "montar": {
      const contexto = m.lienzo.getContext("webgl2", ATRIBUTOS_CONTEXTO) as WebGL2RenderingContext | null;
      if (!contexto) {
        enviar({ tipo: "sin-contexto" });
        return;
      }
      if (esSoftware(nombreGpu(contexto))) {
        contexto.getExtension("WEBGL_lose_context")?.loseContext();
        enviar({ tipo: "software" });
        return;
      }
      try {
        motor = await montarMotor(m.nivel, {
          lienzo: m.lienzo,
          contexto,
          ancho: m.ancho,
          alto: m.alto,
          dpr: m.dpr,
          tiempoInicial: m.tiempoInicial,
          reducido: m.reducido,
          tiempoFijo: m.tiempoFijo,
          adaptativo: m.adaptativo,
          alPrimerFotograma: () => enviar({ tipo: "primer-fotograma" }),
          alAviso: (aviso, fps, tiempo) => enviar({ tipo: "aviso", aviso, fps, tiempo }),
          alFps: (fps, tiempo) => enviar({ tipo: "fps", fps, tiempo }),
        });
        enviar({ tipo: "montado" });
      } catch (error) {
        enviar({ tipo: "error", texto: String(error) });
      }
      return;
    }
    case "redimensionar":
      motor?.redimensionar(m.ancho, m.alto, m.dpr);
      return;
    case "puntero":
      motor?.puntero(m.x, m.y);
      return;
    case "pausar":
      motor?.pausar();
      return;
    case "reanudar":
      motor?.reanudar();
      return;
    case "destruir":
      motor?.destruir();
      motor = null;
      return;
  }
};
