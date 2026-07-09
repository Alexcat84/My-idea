"use client";

/**
 * ArbolPensante — la línea punteada vertical que crece y se bifurca
 * (brief 2.4). REGLA DE ORO: este componente solo RENDERIZA la lista que
 * recibe; quien la llena lo hace exclusivamente con eventos reales del
 * motor (secciones del stream, nodos de la ruta, etapas del plan).
 * Aquí no hay temporizadores ni progreso simulado — si no llega evento,
 * no se enciende nada.
 */

export interface NodoArbol {
  id: string;
  label: string;
  /** atenuado: nodos silenciosos ("cubierto por lo que contaste") */
  atenuado?: boolean;
  /** marca sutil distinta para los saltos semánticos */
  salto?: boolean;
  nota?: string;
}

interface Props {
  nodos: NodoArbol[];
  /** true mientras el motor sigue generando: el último punto pulsa */
  generando: boolean;
  /** texto de estado "generando: <label>" */
  etiquetaGenerando?: string;
}

export function ArbolPensante({ nodos, generando, etiquetaGenerando }: Props) {
  return (
    <div aria-live="polite">
      <ol className="relative flex flex-col gap-0">
        {nodos.map((n, i) => {
          const esUltimo = i === nodos.length - 1;
          const activo = generando && esUltimo;
          return (
            <li key={n.id} className="relative flex gap-3 pb-5 last:pb-0" data-transiciona>
              {/* línea punteada hacia el siguiente punto */}
              {!esUltimo && (
                <span
                  aria-hidden
                  className="absolute left-[5px] top-4 h-full border-l border-dashed border-hairline"
                />
              )}
              <span
                aria-hidden
                className={
                  "relative z-10 mt-1.5 h-[11px] w-[11px] shrink-0 rounded-full " +
                  (activo
                    ? "bg-accent animate-pulse"
                    : n.salto
                      ? "border-2 border-accent bg-bg"
                      : n.atenuado
                        ? "border border-hairline bg-surface-2"
                        : "bg-accent")
                }
              />
              <div className="min-w-0">
                <p
                  className={
                    "text-sm leading-snug " + (n.atenuado ? "text-dim" : "text-ink")
                  }
                >
                  {n.label}
                  {n.salto && (
                    <span className="ml-1.5 align-middle text-[10px] uppercase tracking-wide text-accent">
                      salto
                    </span>
                  )}
                </p>
                {n.nota && <p className="text-xs text-dim">{n.nota}</p>}
              </div>
            </li>
          );
        })}
      </ol>
      {generando && (
        <p className="mt-4 text-xs text-dim">
          generando{etiquetaGenerando ? `: ${etiquetaGenerando}` : "…"}
        </p>
      )}
    </div>
  );
}
