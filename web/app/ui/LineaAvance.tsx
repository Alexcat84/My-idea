"use client";

/**
 * LineaAvance — campaña "Espacios", la cara "Tu avance". CALCO del riel de hitos
 * de La Celebración (docs/diseno-canon/09_la_celebracion.html). Reglas del fundador:
 *  - UNA línea CONTINUA (no por tramos: los tramos por fila no empalmaban).
 *  - La línea NUNCA pasa del último punto alcanzado: se mide del primer nodo al
 *    último nodo vivo (o a la meta si hay cierre real) y termina ahí.
 *  - La PUNTA VIVA (el último punto, dónde vas ahora) LATE; si aparece otro
 *    punto, el latido pasa a ese.
 *  - El CIERRE (la meta) solo aparece cuando hay cierre REAL, nunca antes.
 * Se mide con getBoundingClientRect (como el knob del selector) para ser robusto
 * a alturas de fila variables. Eje central (a la izquierda en móvil), hitos
 * alternando lados, nodos que toman el color a su altura (azul del pensar → verde
 * del ejecutar). Lo más importante (los hitos), no cada acción.
 */
import { useEffect, useRef, useState } from "react";
import { fechaHumanaCorta } from "@/lib/fechas";
import type { HitoEspacio, TipoHito } from "@/lib/hitosEspacio";

const AZUL = "#4D7CFE";
const MEDIO = "#3F9B8E";
const VERDE = "#3FB950";
const AZUL_T = "rgba(77,124,254,0.34)";
const MEDIO_T = "rgba(63,155,142,0.34)";
const VERDE_T = "rgba(63,185,80,0.34)";

function colorNodo(tipo: TipoHito): string {
  if (tipo === "cierre") return VERDE;
  if (tipo === "plan") return MEDIO;
  return AZUL; // chispa, claridad, diagnostico
}

export function LineaAvance({ hitos }: { hitos: HitoEspacio[] }) {
  const cierre = hitos.at(-1);
  const arranques = hitos.slice(0, -1);
  const cerrado = cierre?.alcanzado ?? false;
  // La punta viva: el último arranque, mientras el espacio no ha cerrado (ahí
  // termina el riel y ahí late).
  const vivaIndex = cerrado ? -1 : arranques.length - 1;

  const contRef = useRef<HTMLDivElement | null>(null);
  const primeraRef = useRef<HTMLSpanElement | null>(null);
  const ultimaRef = useRef<HTMLSpanElement | null>(null);
  const [linea, setLinea] = useState<{ top: number; height: number } | null>(null);

  useEffect(() => {
    const c = contRef.current;
    if (!c) return;
    const medir = () => {
      const a = primeraRef.current;
      const b = ultimaRef.current;
      if (!a || !b) {
        setLinea(null);
        return;
      }
      const rc = c.getBoundingClientRect();
      const ra = a.getBoundingClientRect();
      const rb = b.getBoundingClientRect();
      const top = ra.top + ra.height / 2 - rc.top;
      const bottom = rb.top + rb.height / 2 - rc.top;
      setLinea({ top, height: Math.max(0, bottom - top) });
    };
    medir();
    // Auto-ajustable a CUALQUIER cambio de alto: puntos nuevos, reflujo por
    // carga de fuente, cambio de ancho del contenedor sin resize de ventana...
    // La línea es absoluta, no altera el alto del contenedor, así que observarlo
    // no crea bucle. (Se conserva el listener de resize por si acaso.)
    const ro = new ResizeObserver(medir);
    ro.observe(c);
    window.addEventListener("resize", medir);
    return () => {
      ro.disconnect();
      window.removeEventListener("resize", medir);
    };
  }, [hitos, cerrado]);

  return (
    <div className="anima-plan-in">
      <p className="text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">Tu avance</p>
      <p className="mb-8 mt-1 text-[13px] leading-relaxed text-dim">Del inicio a donde vas, los hitos de este espacio.</p>

      <div ref={contRef} className="relative mx-auto max-w-[620px]">
        {/* la línea CONTINUA, del primer hito al último alcanzado (nunca más allá) */}
        {linea && linea.height > 0 && (
          <span
            aria-hidden
            className="absolute left-5 w-[4px] -translate-x-1/2 rounded sm:left-1/2"
            style={{
              top: linea.top,
              height: linea.height,
              background: `linear-gradient(to bottom, ${AZUL_T}, ${MEDIO_T} 62%, ${VERDE_T})`,
            }}
          />
        )}

        {arranques.map((h, i) => {
          const izq = i % 2 === 0;
          const color = colorNodo(h.tipo);
          const viva = i === vivaIndex;
          const esUltima = !cerrado && i === arranques.length - 1;
          return (
            <div key={i} className="grid grid-cols-[40px_1fr] pb-8 sm:grid-cols-[1fr_4px_1fr] sm:gap-x-7">
              <div className="relative col-start-1 sm:col-start-2">
                <span
                  ref={(el) => {
                    if (i === 0) primeraRef.current = el;
                    if (esUltima) ultimaRef.current = el;
                  }}
                  className={
                    "absolute left-5 top-[7px] z-[1] h-[13px] w-[13px] -translate-x-1/2 rounded-full sm:left-1/2 " +
                    (viva ? "anima-halo-viva" : "")
                  }
                  style={viva ? { background: color } : { background: color, boxShadow: "0 0 0 4px var(--bg)" }}
                />
              </div>
              <div
                className={
                  "col-start-2 flex min-w-0 flex-col gap-[3px] " +
                  (izq ? "sm:col-start-1 sm:items-end sm:text-right" : "sm:col-start-3 sm:items-start sm:text-left")
                }
              >
                {h.fecha && <span className="text-[13px] text-dim">{fechaHumanaCorta(h.fecha)}</span>}
                <span className="text-[17px] font-bold tracking-[-0.01em] [text-wrap:pretty]">{h.etiqueta}</span>
                {h.subtitulo && <span className="text-[13.5px] leading-snug text-dim [text-wrap:pretty]">{h.subtitulo}</span>}
              </div>
            </div>
          );
        })}

        {/* la META: SOLO cuando hay cierre REAL (nunca antes). */}
        {cerrado && cierre && (
          <div className="relative pt-1">
            <span
              ref={(el) => {
                ultimaRef.current = el;
              }}
              className="absolute left-5 top-1 z-[1] flex h-9 w-9 -translate-x-1/2 items-center justify-center rounded-full text-[17px] leading-none sm:left-1/2"
              style={{ background: "var(--bg)", border: `2.5px solid ${VERDE}`, boxShadow: "0 0 0 5px var(--bg), 0 0 0 12px rgba(63,185,80,0.22)" }}
            >
              🎉
            </span>
            <div className="flex flex-col gap-1 pl-[52px] pt-1 sm:items-center sm:pl-0 sm:pt-[52px] sm:text-center">
              {cierre.fecha && <span className="text-[13px] text-dim">{fechaHumanaCorta(cierre.fecha)}</span>}
              <span className="text-[15px] font-extrabold uppercase tracking-[1.6px] text-done">{cierre.etiqueta}</span>
              {cierre.subtitulo && <span className="text-[14px] text-dim">{cierre.subtitulo}</span>}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
