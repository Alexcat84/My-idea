"use client";

/**
 * Acordeon — cinta desplegable (brief 2.4/2.6). <details> nativo:
 * accesible sin JS extra, con el chevron girando en --motion.
 */

interface Props {
  titulo: React.ReactNode;
  abierto?: boolean;
  children: React.ReactNode;
  /** contenido extra alineado a la derecha del título (chips, etc.) */
  extra?: React.ReactNode;
}

export function Acordeon({ titulo, abierto, children, extra }: Props) {
  return (
    <details
      open={abierto}
      className="group rounded-cinta border border-hairline bg-surface"
    >
      <summary className="flex items-center justify-between gap-3 px-5 py-4">
        <span className="font-medium leading-snug">{titulo}</span>
        <span className="flex items-center gap-3">
          {extra}
          <svg
            width="14"
            height="14"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
            aria-hidden
            className="shrink-0 text-dim transition-transform duration-[180ms] group-open:rotate-180"
          >
            <polyline points="6 9 12 15 18 9" />
          </svg>
        </span>
      </summary>
      <div className="border-t border-hairline px-5 py-4 text-[15px] leading-relaxed text-ink">
        {children}
      </div>
    </details>
  );
}
