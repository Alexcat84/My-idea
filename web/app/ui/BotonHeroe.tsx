"use client";

/**
 * BotonHeroe — el botón de los momentos que ABREN CAMINO (decisión del
 * fundador, ago 2026): explorar las suposiciones, armar el plan, comprar el
 * plan de un mundo. Al pasar el ratón, cinco chispas salen disparadas.
 *
 * Por qué la chispa y no otra animación: es la metáfora de la casa. Una idea
 * empieza con una chispa, y este botón es siempre el que enciende algo. Es el
 * único adorno del frente que además SIGNIFICA.
 *
 * REGLA: uno por pantalla, jamás dos. Si hay dos héroes, no hay ninguno, y la
 * jerarquía de la página se cae. Todo lo demás usa BOTON_ESTANDAR.
 *
 * El estilo vive en globals.css (.boton-heroe) porque la animación depende de
 * hover sobre hijos, que las utilidades no cubren. Aquí solo el tamaño y el
 * peso, que sí son de cada sitio.
 */
import type { ReactNode } from "react";
import { BOTON_ESTANDAR } from "@/lib/boton";

/** Las cinco chispas. Decoración pura: aria-hidden, sin capturar el puntero. */
function Chispas() {
  return (
    <>
      {[1, 2, 3, 4, 5].map((n) => (
        <svg key={n} className={`chispa chispa-${n}`} viewBox="0 0 24 24" aria-hidden focusable="false">
          <path d="M12 0l3 9 9 3-9 3-3 9-3-9-9-3 9-3z" />
        </svg>
      ))}
    </>
  );
}

export function BotonHeroe({
  children,
  onClick,
  disabled,
  className = "",
  type = "button",
}: {
  children: ReactNode;
  onClick?: () => void;
  disabled?: boolean;
  /** Tamaño, radio y ancho: son de cada sitio, no del lenguaje. */
  className?: string;
  type?: "button" | "submit";
}) {
  return (
    <button
      type={type}
      onClick={onClick}
      disabled={disabled}
      className={`boton-heroe ${BOTON_ESTANDAR} disabled:opacity-50 ${className}`}
    >
      {children}
      <Chispas />
    </button>
  );
}
