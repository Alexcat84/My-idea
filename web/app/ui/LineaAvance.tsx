"use client";

/**
 * LineaAvance — campaña "Espacios", la cara "Tu avance". CALCO del riel de hitos
 * de La Celebración (Entrega 3 de CD, docs/diseno-canon/09_la_celebracion.html):
 * eje CENTRAL con trazo translúcido azul→verde (a la izquierda en móvil), hitos
 * que ALTERNAN lados, nodos de 13px que toman el color a su altura (azul del
 * pensar → verde del ejecutar), la punta VIVA con su anillo (dónde vas ahora), y
 * la META de 36px (🎉 verde si cerró; gris si aún no) con su rótulo debajo.
 * ESTÁTICO: los latidos (halos animados) son de la Celebración grande, del
 * proyecto. Muestra LO MÁS IMPORTANTE (los hitos), no cada acción.
 */
import { fechaHumanaCorta } from "@/lib/fechas";
import type { HitoEspacio, TipoHito } from "@/lib/hitosEspacio";

const AZUL = "#4D7CFE";
const MEDIO = "#3F9B8E";
const VERDE = "#3FB950";
const ANILLO = "var(--bg)"; // el recorte del nodo (separa del trazo): el fondo
const TRAZA =
  "linear-gradient(to bottom, rgba(77,124,254,0.34) 0%, rgba(77,124,254,0.34) 24%, rgba(63,155,142,0.34) 44%, rgba(63,185,80,0.34) 62%, rgba(63,185,80,0.34) 100%)";

// El nodo toma el color del trazo a su altura: el pensar (azul) vira al ejecutar
// (verde). El plan es el pivote (medio).
function colorNodo(tipo: TipoHito): string {
  if (tipo === "plan") return MEDIO;
  return AZUL; // chispa, claridad, diagnostico
}

export function LineaAvance({ hitos }: { hitos: HitoEspacio[] }) {
  const cierre = hitos.at(-1);
  const arranques = hitos.slice(0, -1);
  const cerrado = cierre?.alcanzado ?? false;
  // La punta viva: el último hito alcanzado, mientras el espacio no ha cerrado.
  const vivaIndex = cerrado ? -1 : arranques.length - 1;

  return (
    <div className="anima-plan-in">
      <p className="text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">Tu avance</p>
      <p className="mb-8 mt-1 text-[13px] leading-relaxed text-dim">Del inicio al cierre, los hitos de este espacio.</p>

      <div className="relative mx-auto max-w-[620px]">
        {/* el trazo: central en escritorio, a la izquierda en móvil. Translúcido
            (los nodos a color pleno resaltan). Termina en el centro de la meta. */}
        <span
          aria-hidden
          className="absolute left-5 top-[7px] w-[4px] -translate-x-1/2 rounded sm:left-1/2"
          style={{ bottom: 18, background: TRAZA }}
        />

        {arranques.map((h, i) => {
          const izq = i % 2 === 0;
          const color = colorNodo(h.tipo);
          const viva = i === vivaIndex;
          return (
            <div key={i} className="grid grid-cols-[40px_1fr] pb-8 sm:grid-cols-[1fr_4px_1fr] sm:gap-x-7">
              <div className="relative col-start-1 sm:col-start-2">
                <span
                  className="absolute left-5 top-[7px] h-[13px] w-[13px] -translate-x-1/2 rounded-full sm:left-1/2"
                  style={{
                    background: color,
                    boxShadow: viva
                      ? `0 0 0 4px ${ANILLO}, 0 0 0 7px rgba(77,124,254,0.32)`
                      : `0 0 0 4px ${ANILLO}`,
                  }}
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

        {/* la META (el cierre): nodo de 36px con 🎉 verde si cerró, gris si falta.
            En escritorio va centrado; en móvil, sobre el eje de la izquierda. */}
        {cierre && (
          <div className="grid grid-cols-[40px_1fr] items-center sm:grid-cols-1 sm:justify-items-center">
            <div className="relative col-start-1 h-9 sm:col-start-1 sm:h-auto">
              <span
                className="absolute left-5 top-0 flex h-9 w-9 -translate-x-1/2 items-center justify-center rounded-full text-[17px] leading-none sm:static sm:translate-x-0"
                style={
                  cierre.alcanzado
                    ? { background: "var(--bg)", border: `2.5px solid ${VERDE}`, boxShadow: `0 0 0 5px ${ANILLO}, 0 0 0 12px rgba(63,185,80,0.22)` }
                    : { background: "var(--bg)", border: "2.5px solid rgba(255,255,255,0.20)", boxShadow: `0 0 0 5px ${ANILLO}, 0 0 0 12px rgba(255,255,255,0.05)`, filter: "grayscale(1)", opacity: 0.8 }
                }
              >
                {cierre.alcanzado ? "🎉" : ""}
              </span>
            </div>
            <div className="col-start-2 flex flex-col gap-1 sm:col-start-1 sm:mt-4 sm:items-center sm:text-center">
              {cierre.fecha && <span className="text-[13px] text-dim">{fechaHumanaCorta(cierre.fecha)}</span>}
              <span className={"text-[15px] font-extrabold uppercase tracking-[1.6px] " + (cierre.alcanzado ? "text-done" : "text-dim")}>
                {cierre.etiqueta}
              </span>
              {cierre.subtitulo && <span className="text-[14px] text-dim">{cierre.subtitulo}</span>}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
