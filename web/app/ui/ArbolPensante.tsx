"use client";

/**
 * ArbolPensante — el riel del recorrido (canon 04, docs/diseno-canon,
 * anatomía extraída del HTML: barra de 4px con gradiente azul que crece,
 * puntos de 20px sobre fondo negro con aro hairline, relleno azul
 * inset 4px cuando el nodo quedó conversado, anillo girando mientras el
 * motor piensa el punto actual, silenciosos al 50% con su nota, y rombo
 * azul de 6px para los saltos).
 *
 * REGLA DE ORO intacta: este componente solo RENDERIZA la lista que
 * recibe; quien la llena lo hace exclusivamente con eventos reales del
 * motor. Las animaciones son de ENTRADA de cada evento real (railIn),
 * jamás temporizadores de progreso simulado.
 *
 * Phase 3.7 (C3): altura contenida — el riel no crece infinito; el punto
 * actual queda siempre a la vista (auto-scroll al fondo) y el historial
 * se desliza hacia arriba.
 */
import { useEffect, useRef } from "react";

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
  /** true mientras el motor sigue generando: el último punto gira */
  generando: boolean;
  /** texto de estado bajo el riel ("generando: <label>") */
  etiquetaGenerando?: string;
}

function PuntoRiel({ activo, lleno }: { activo: boolean; lleno: boolean }) {
  return (
    <span aria-hidden className="relative h-5 w-5 shrink-0 rounded-full bg-black">
      {/* aro base hairline (canon: 1.5px rgba(255,255,255,0.14)) */}
      <span
        className="absolute inset-0 box-border rounded-full border-[1.5px]"
        style={{ borderColor: "rgba(255,255,255,0.14)" }}
      />
      {/* anillo girando: el motor está pensando ESTE punto */}
      {activo && (
        <span
          className="anima-spin-ring absolute inset-0 box-border rounded-full border-[2.5px]"
          style={{ borderColor: "rgba(77,124,254,0.2)", borderTopColor: "var(--accent)" }}
        />
      )}
      {/* relleno azul: el punto ya quedó en el recorrido */}
      {lleno && <span className="anima-rail-fill absolute inset-1 rounded-full bg-accent" />}
    </span>
  );
}

export function ArbolPensante({ nodos, generando, etiquetaGenerando }: Props) {
  const marco = useRef<HTMLDivElement>(null);

  // C3: el punto actual siempre a la vista; el historial se desliza.
  useEffect(() => {
    const el = marco.current;
    if (el) el.scrollTo({ top: el.scrollHeight, behavior: "smooth" });
  }, [nodos.length, generando]);

  return (
    <div aria-live="polite">
      <div
        ref={marco}
        className="max-h-[min(60vh,520px)] overflow-y-auto overscroll-contain pr-1"
        style={{ scrollbarWidth: "thin", maskImage: "linear-gradient(180deg, transparent 0, black 18px)" }}
      >
        <div className="relative flex flex-col">
          {/* la barra del canon: 4px, gradiente azul, crece con el riel */}
          {nodos.length > 1 && (
            <span aria-hidden className="absolute bottom-[10px] left-2 top-[10px]">
              <span
                className="block h-full w-1 rounded-[2px]"
                style={{ background: "linear-gradient(180deg, rgba(77,124,254,0.35), var(--accent))" }}
              />
            </span>
          )}
          <ol className="relative flex flex-col">
            {nodos.map((n, i) => {
              const esUltimo = i === nodos.length - 1;
              const activo = generando && esUltimo;
              return (
                <li
                  key={n.id}
                  className="anima-rail-in relative flex items-start"
                  style={{ gap: "15px" }}
                  data-transiciona
                >
                  <PuntoRiel activo={activo} lleno={!activo || n.atenuado === true} />
                  <span className={"min-w-0" + (n.atenuado ? " opacity-50" : "")}>
                    <span
                      className={
                        "block pt-px text-sm leading-[1.45] " +
                        (esUltimo && !n.atenuado ? "font-semibold text-accent" : "font-medium text-ink")
                      }
                    >
                      {n.label}
                    </span>
                    {(n.nota || n.salto) && (
                      <span className="mt-[3px] block text-xs text-dim">
                        {n.salto && (
                          <span
                            aria-hidden
                            className="mr-1.5 inline-block h-1.5 w-1.5 rotate-45 border-[1.5px] border-accent align-baseline"
                          />
                        )}
                        {n.salto ? "fue un salto" : n.nota}
                      </span>
                    )}
                  </span>
                </li>
              );
            })}
            {/* canon 04: el riel es memoria; lo futuro no tiene tema, solo
                el punto hueco punteado mientras el motor sigue vivo */}
            {generando && nodos.length > 0 && (
              <li aria-hidden className="anima-rail-in relative flex items-start" style={{ gap: "15px" }}>
                <span
                  className="h-5 w-5 shrink-0 rounded-full bg-black"
                  style={{ border: "1.5px dashed rgba(166,167,173,0.6)" }}
                />
              </li>
            )}
          </ol>
        </div>
      </div>
      {generando && (
        <p className="mt-2 text-xs text-dim">
          generando{etiquetaGenerando ? `: ${etiquetaGenerando}` : "…"}
        </p>
      )}
    </div>
  );
}
