"use client";

/**
 * La masa del hero de la portada: un liquido oscuro inestable que se
 * disgrega en particulas, forma una figura y vuelve a fundirse.
 *
 * Este componente no importa three.js ni crea contextos WebGL: decide el
 * nivel de calidad y monta el motor cuando la pagina ya pinto (evento load
 * + reposo del hilo). El liquido corre en un worker con OffscreenCanvas
 * (masa/anfitrion.ts); mientras llega, el hero muestra su fondo CSS, el
 * mismo que pinta el shader, y el lienzo entra en fundido.
 *
 * Niveles: alto -> medio -> bajo -> particulas -> fija (ver masa/calidad.ts).
 * Para verificacion: ?masa=<nivel> fuerza un nivel sin adaptar y
 * ?masa-t=<segundos> congela el ciclo en ese instante.
 */
import { useEffect, useRef } from "react";
import { montarLiquido, SinLiquido } from "./masa/anfitrion";
import { esNivel, esNivelLiquido, nivelInicial, siguienteNivel, type Nivel } from "./masa/calidad";
import type { ControlMasa, OpcionesMontaje } from "./masa/control";

/** Pistas baratas del equipo; lo que depende de la GPU lo averigua el motor. */
function nivelSegunEquipo(): Nivel {
  const nav = navigator as Navigator & { deviceMemory?: number; connection?: { saveData?: boolean } };
  return nivelInicial({
    webgl: true,
    webgl2: true,
    movil:
      window.matchMedia("(pointer: coarse)").matches || Math.min(window.screen.width, window.screen.height) < 700,
    nucleos: nav.hardwareConcurrency,
    memoriaGb: nav.deviceMemory,
    ahorroDatos: nav.connection?.saveData === true,
  });
}

export function HeroMasa() {
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const contenedor = ref.current;
    if (!contenedor) return;
    const parametros = new URLSearchParams(window.location.search);
    const pedido = parametros.get("masa");
    const forzado: Nivel | null = esNivel(pedido) ? pedido : null;
    const tFijoTexto = parametros.get("masa-t");
    const tiempoFijo = tFijoTexto !== null && Number.isFinite(Number(tFijoTexto)) ? Number(tFijoTexto) : null;
    const reducido = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    let control: ControlMasa | null = null;
    let cancelado = false;
    let enPantalla = true;

    const sincronizarPausa = () => {
      if (!control) return;
      if (enPantalla && !document.hidden) control.reanudar();
      else control.pausar();
    };

    const montar = async (nivel: Nivel, tiempoInicial: number): Promise<void> => {
      contenedor.dataset.nivel = nivel;
      if (nivel === "fija") return;
      const opciones: OpcionesMontaje = {
        contenedor,
        tiempoInicial,
        reducido,
        tiempoFijo,
        adaptativo: forzado === null && !reducido && tiempoFijo === null,
        alPrimerFotograma: () => {
          contenedor.dataset.listo = "1";
        },
        alAviso: (_aviso, fps) => {
          if (cancelado || !control) return;
          contenedor.dataset.descartes = `${contenedor.dataset.descartes ?? ""}${nivel}@${fps.toFixed(0)} `;
          const t = control.tiempo();
          control.destruir();
          control = null;
          delete contenedor.dataset.listo;
          void montar(forzado ? "fija" : siguienteNivel(nivel), t);
        },
      };
      try {
        const nuevo = esNivelLiquido(nivel)
          ? await montarLiquido(nivel, opciones)
          : await import("./masa/respaldo").then((m) => m.montarRespaldo(opciones));
        if (cancelado) {
          nuevo.destruir();
          return;
        }
        control = nuevo;
        sincronizarPausa();
      } catch (error) {
        if (cancelado) return;
        // Sin WebGL2 o GPU por software: directo al respaldo de particulas.
        // Shader que no compila o chunk que no llega: un nivel menos.
        const siguiente = forzado ? "fija" : error instanceof SinLiquido ? "particulas" : siguienteNivel(nivel);
        await montar(siguiente, tiempoInicial);
      }
    };

    const arrancar = () => {
      if (!cancelado) void montar(forzado ?? nivelSegunEquipo(), 0);
    };

    // Diferido: nada de esto compite con la primera pintura.
    let espera: number | undefined;
    const alCargar = () => {
      espera =
        typeof window.requestIdleCallback === "function"
          ? window.requestIdleCallback(arrancar, { timeout: 1200 })
          : window.setTimeout(arrancar, 150);
    };
    if (document.readyState === "complete") alCargar();
    else window.addEventListener("load", alCargar, { once: true });

    const observador = new IntersectionObserver(
      (entradas) => {
        enPantalla = entradas.some((e) => e.isIntersecting);
        sincronizarPausa();
      },
      { threshold: 0 },
    );
    observador.observe(contenedor);
    document.addEventListener("visibilitychange", sincronizarPausa);

    return () => {
      cancelado = true;
      window.removeEventListener("load", alCargar);
      if (espera !== undefined) {
        if (typeof window.cancelIdleCallback === "function") window.cancelIdleCallback(espera);
        window.clearTimeout(espera);
      }
      observador.disconnect();
      document.removeEventListener("visibilitychange", sincronizarPausa);
      control?.destruir();
      control = null;
    };
  }, []);

  return (
    <div ref={ref} className="portada-masa" aria-hidden="true">
      <noscript>
        <div className="portada-masa-fija" />
      </noscript>
    </div>
  );
}
