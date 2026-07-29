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
  /** variante "etapa" (Manos a la Obra): radio 16 y, al abrir, borde verde al
   * 28% — el verde ejecuta marca la etapa en curso. El resto de acordeones no
   * lo llevan (mantienen radio 12 y hairline). */
  variante?: "etapa";
}

export function Acordeon({ titulo, abierto, children, extra, variante }: Props) {
  const esEtapa = variante === "etapa";
  return (
    <details
      open={abierto}
      className={
        "group border bg-surface " +
        (esEtapa
          ? "rounded-panel border-hairline open:border-done/[0.28]"
          : "rounded-cinta border-hairline")
      }
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
