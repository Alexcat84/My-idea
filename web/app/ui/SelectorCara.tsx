"use client";

/**
 * SelectorCara — campaña "Espacios". El selector de las tres caras de un
 * espacio: Plan · Manos a la obra · Tu avance.
 *
 * Calibrado por el fundador (ago 2026, carril C): hueco HUNDIDO (sombra
 * interior, como una ranura tallada) y una LUZ que se desliza a la cara activa
 * con rebote suave, con su filete de cristal arriba y el icono que crece al
 * activarse. La luz mide la celda real, así que aguanta 380 y etiquetas de
 * distinto largo.
 *
 * La luz NO late. El original de referencia pulsaba en bucle; en una
 * herramienta de trabajo, algo que parpadea sin parar en la esquina del ojo
 * compite con lo que el usuario está leyendo. Brilla, pero quieta.
 *
 * Su FORMA (cápsula ancha con ranura) lo distingue siempre de las
 * pestañas-fichero (angulares) que cambian de ESPACIO: aquí se cambia de cara
 * dentro del mismo espacio.
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
  // La luz viaja con TRANSFORM, no con left. El CSS (.cambiador-luz) siempre
  // animo transform y width; mover el elemento con `left` dejaba el salto
  // horizontal fuera de la transicion, asi que la luz se teletransportaba y
  // solo el ancho rebotaba. Cazado por el fundador en su corrida (ago 2026).
  //
  // Y viaja SOLO cuando el usuario cambia de cara: en el montaje y al
  // redimensionar se COLOCA sin transicion, o la luz entraria volando desde el
  // borde izquierdo cada vez que se abre la pantalla.
  const [viaja, setViaja] = useState(false);
  const montado = useRef(false);

  useEffect(() => {
    const medir = () => {
      const el = refs.current[valor];
      if (el) setInd({ left: el.offsetLeft, width: el.offsetWidth });
    };
    setViaja(montado.current);
    montado.current = true;
    medir();
    const alRedimensionar = () => {
      setViaja(false);
      medir();
    };
    window.addEventListener("resize", alRedimensionar);
    return () => window.removeEventListener("resize", alRedimensionar);
  }, [valor, opciones]);

  return (
    <div
      role="tablist"
      aria-label="Las caras de este espacio"
      // La ranura y el cristal viven en globals.css: son piezas compartidas
      // con las tarjetas de acceso del riel, que lucen igual estando quietas.
      // El borde de la ranura es casi negro, no azul: brilla la luz, no el marco.
      className="ranura relative flex w-full rounded-[16px] p-[5px]"
    >
      {/* La luz que viaja a la cara activa. */}
      <span
        aria-hidden
        className="cristal cambiador-luz pointer-events-none absolute bottom-[5px] left-0 top-[5px] z-[1] rounded-[12px]"
        style={{
          transform: `translateX(${ind.left}px)`,
          width: ind.width,
          ...(viaja ? null : { transition: "none" }),
        }}
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
              "relative z-10 flex flex-1 items-center justify-center gap-2 whitespace-nowrap rounded-[12px] px-2 py-2.5 text-[11.5px] font-semibold transition-colors duration-200 sm:px-4 sm:text-[13px] " +
              (activa ? "text-ink" : "text-dim hover:text-[#cfd2d8]")
            }
          >
            <span
              aria-hidden
              className={
                "shrink-0 transition-transform duration-[350ms] ease-[cubic-bezier(.34,1.56,.64,1)] " +
                (activa ? "scale-110" : "")
              }
            >
              {o.icono}
            </span>
            {o.nombre}
          </button>
        );
      })}
    </div>
  );
}
