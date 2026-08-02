"use client";

/**
 * SelectorCara — campaña "Espacios". El selector SEGMENTADO (píldora) de las tres
 * caras de un espacio: Plan · Manos a la obra · Tu avance. Estética del switch de
 * referencia, pero de 3 celdas y en tema oscuro: el indicador azul se DESLIZA a
 * la celda activa. Mide la celda activa (offsetLeft/Width), así funciona con
 * etiquetas de distinto largo y a 380 (si no caben, la píldora hace scroll
 * horizontal). Su FORMA (redonda) la distingue siempre de las pestañas-fichero
 * (angulares) de los espacios — dos niveles de navegación, nunca confundibles.
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
      className="relative inline-flex max-w-full overflow-x-auto rounded-full border border-hairline bg-surface-2 p-1 [scrollbar-width:none] [&::-webkit-scrollbar]:hidden"
    >
      <span
        aria-hidden
        className="pointer-events-none absolute bottom-1 top-1 rounded-full bg-accent shadow-[0_1px_2px_rgba(0,0,0,0.35)] transition-[left,width] duration-300 ease-out"
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
              "relative z-10 flex shrink-0 items-center justify-center gap-2 whitespace-nowrap rounded-full px-4 py-2 text-[13px] font-semibold transition-colors duration-200 " +
              (activa ? "text-white" : "text-dim hover:text-ink")
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
