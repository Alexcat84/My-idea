"use client";

/**
 * SelectorCara — campaña "Espacios". El selector SEGMENTADO de las tres caras de
 * un espacio: Plan · Manos a la obra · Tu avance. A todo el ancho, en tres
 * iguales. Se lee CLARAMENTE como un selector: pista recesada oscura con borde
 * visible (contorno), divisores internos en los tercios (interno), y un "knob"
 * ELEVADO (superficie más clara + borde + sombra) que se DESLIZA a la celda
 * activa midiéndola (robusto a 380 y a etiquetas de distinto largo). El azul
 * vive solo en el icono/texto de la cara activa. Su FORMA (cápsula) lo distingue
 * siempre de las pestañas-fichero (angulares) de los espacios.
 */
import { useEffect, useRef, useState, type ReactNode } from "react";

export type Cara = "plan" | "manos" | "avance";

export function SelectorCara({
  valor,
  onCambio,
  opciones,
}: {
  valor: Cara;
  onCambio: (c: Cara) => void;
  opciones: { id: Cara; nombre: string; icono: ReactNode }[];
}) {
  const refs = useRef<Record<string, HTMLButtonElement | null>>({});
  const [ind, setInd] = useState<{ left: number; width: number }>({ left: 0, width: 0 });

  useEffect(() => {
    const medir = () => {
      const el = refs.current[valor];
      if (el) setInd({ left: el.offsetLeft, width: el.offsetWidth });
    };
    medir();
    window.addEventListener("resize", medir);
    return () => window.removeEventListener("resize", medir);
  }, [valor, opciones]);

  return (
    <div
      role="tablist"
      aria-label="Las caras de este espacio"
      className="relative flex w-full rounded-[13px] border border-white/[0.14] bg-surface-3 p-1"
    >
      {/* divisores internos (los tercios): dan lectura de "segmentado" */}
      <span aria-hidden className="pointer-events-none absolute bottom-2.5 left-1/3 top-2.5 w-px bg-white/[0.08]" />
      <span aria-hidden className="pointer-events-none absolute bottom-2.5 left-2/3 top-2.5 w-px bg-white/[0.08]" />

      {/* el knob elevado que se desliza a la celda activa */}
      <span
        aria-hidden
        className="pointer-events-none absolute bottom-1 top-1 z-[1] rounded-[10px] border border-white/[0.18] bg-surface-2 shadow-[0_2px_5px_rgba(0,0,0,0.55)] transition-[left,width] duration-300 ease-out"
        style={{ left: ind.left, width: ind.width }}
      />

      {opciones.map((o) => {
        const activa = o.id === valor;
        return (
          <button
            key={o.id}
            ref={(el) => {
              refs.current[o.id] = el;
            }}
            role="tab"
            aria-selected={activa}
            onClick={() => onCambio(o.id)}
            className={
              "relative z-10 flex flex-1 items-center justify-center gap-2 whitespace-nowrap rounded-[10px] px-2 py-2.5 text-[11.5px] font-semibold transition-colors duration-200 sm:px-4 sm:text-[13px] " +
              (activa ? "text-accent" : "text-dim hover:text-ink")
            }
          >
            <span aria-hidden className="shrink-0">
              {o.icono}
            </span>
            {o.nombre}
          </button>
        );
      })}
    </div>
  );
}
