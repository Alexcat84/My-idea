"use client";

/**
 * SelectorCara — campaña "Espacios". El selector SEGMENTADO de las tres caras de
 * un espacio: Plan · Manos a la obra · Tu avance. Ocupa TODO el ancho, dividido
 * en tres iguales. El "knob" activo es una superficie ELEVADA (como un selector
 * físico: poco azul — el azul vive solo en el icono/texto de la cara activa),
 * que se DESLIZA midiendo la celda activa (robusto a 380 y a etiquetas de
 * distinto largo). Su FORMA (cápsula) lo distingue siempre de las
 * pestañas-fichero (angulares) de los espacios.
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
      className="relative flex w-full rounded-[13px] border border-hairline bg-surface-2 p-1"
    >
      <span
        aria-hidden
        className="pointer-events-none absolute bottom-1 top-1 rounded-[10px] border border-white/[0.08] bg-surface shadow-[0_1px_2px_rgba(0,0,0,0.4)] transition-[left,width] duration-300 ease-out"
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
