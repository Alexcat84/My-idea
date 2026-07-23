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
  /** lo que se muestra: la etiqueta_arbol (corta, enamora). */
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
          <ol className="relative flex flex-col">
            {nodos.map((n, i) => {
              const esUltimo = i === nodos.length - 1;
              const activo = generando && esUltimo;
              // ¿Hay un punto DESPUÉS de este (real o el hueco "futuro")?
              const conConector = i < nodos.length - 1 || generando;
              return (
                <li
                  key={n.id}
                  className="anima-rail-in relative flex items-start pb-[30px]"
                  style={{ gap: "15px" }}
                  data-transiciona
                >
                  {/* EL CONECTOR — del centro de ESTE punto (top:10px) al del
                      SIGUIENTE. La distancia entre centros de puntos consecutivos
                      es EXACTAMENTE la altura de esta fila (el punto va arriba de
                      la fila con items-start; el punto siguiente está a fila-alto
                      + 10). Por eso top:10 + bottom:-10 lo alcanza para cualquier
                      largo de texto — SIEMPRE QUE las filas vayan pegadas.
                      El bug del riel cortado (jul 2026): la animación railIn
                      dejaba `margin-bottom:30px` en cada fila, 30px que el
                      conector no cruzaba y que el `overflow:hidden` de la propia
                      animación pintaba de negro. La solución no fue estirar el
                      conector (frágil): fue mover esa separación a `pb-[30px]`,
                      padding DENTRO de la fila, que es caja que el conector sí
                      recorre. El punto de abajo queda pegado, y la línea lo toca.
                      Va detrás del punto (su bg negro lo enmascara), canon 04. */}
                  {conConector && (
                    <span
                      aria-hidden
                      className="absolute w-1 rounded-[2px]"
                      style={{
                        left: "8px",
                        top: "10px",
                        bottom: "-10px",
                        background: "linear-gradient(180deg, rgba(77,124,254,0.35), var(--accent))",
                      }}
                    />
                  )}
                  <PuntoRiel activo={activo} lleno={!activo || n.atenuado === true} />
                  <span className={"min-w-0 flex-1" + (n.atenuado ? " opacity-50" : "")}>
                    {/* B4: una línea con elipsis (el fix A ya las acorta con la
                        etiqueta_arbol). El tooltip repite la MISMA etiqueta
                        cuando el texto se corta: el nombre técnico del
                        concepto no se le enseña al usuario ni aquí. */}
                    <span
                      className={
                        "block truncate pt-px text-sm leading-[1.45] " +
                        (esUltimo && !n.atenuado ? "font-semibold text-accent" : "font-medium text-ink")
                      }
                      title={n.label}
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
            {/* canon 04: el riel es memoria; lo futuro no tiene tema, solo el
                punto hueco punteado mientras el motor sigue vivo. Va pegado
                (parte del <ol>, sin pb) para que el conector de la última fila
                real lo toque como a cualquier otro punto. */}
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
