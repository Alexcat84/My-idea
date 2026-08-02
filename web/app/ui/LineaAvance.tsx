"use client";

/**
 * LineaAvance — campaña "Espacios", la cara "Tu avance": un TIMELINE VERTICAL
 * visual de los hitos reales del espacio (de hitosEspacio.ts). Mismo lenguaje
 * que la Celebración (eje + barra azul→verde que sube, nodos sobre el eje, un
 * anillo mayor en el cierre), pero ESTÁTICO — la animación con constelación y
 * pulso es de la Celebración grande, del PROYECTO. Ley de color: el azul piensa
 * (arranque: chispa/claridad/plan/diagnóstico), el verde ejecuta (acciones y
 * cierre alcanzado); el cierre pendiente, hueco gris. Cero estadística.
 */
import { fechaHumanaCorta } from "@/lib/fechas";
import type { HitoEspacio } from "@/lib/hitosEspacio";

const AZUL = "#4D7CFE";
const VERDE = "#3FB950";

function colorNodo(h: HitoEspacio): string {
  if (!h.alcanzado) return "";
  // Arranque = azul (piensa); acción y cierre = verde (ejecuta/celebra).
  return h.tipo === "accion" || h.tipo === "cierre" ? VERDE : AZUL;
}

export function LineaAvance({ hitos }: { hitos: HitoEspacio[] }) {
  const total = hitos.length;
  const alcanzados = hitos.filter((h) => h.alcanzado).length;
  const pct = total > 1 ? (alcanzados - 1) / (total - 1) : alcanzados > 0 ? 1 : 0;

  return (
    <div className="anima-plan-in">
      <div className="mb-6 flex items-baseline justify-between gap-3">
        <div>
          <p className="text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">Tu avance</p>
          <p className="mt-1 text-[13px] leading-relaxed text-dim">Del inicio al cierre, los hitos que has alcanzado.</p>
        </div>
        <span className="shrink-0 text-[13px] font-semibold tabular-nums text-done">
          {alcanzados}/{total}
        </span>
      </div>

      <div className="relative py-1">
        {/* el eje: pista hairline + barra azul→verde que sube hasta lo alcanzado */}
        <span className="absolute bottom-3 left-[9px] top-3 w-[2px] rounded bg-hairline" />
        <span
          className="absolute left-[9px] top-3 w-[2px] rounded bg-gradient-to-b from-accent to-done transition-[height] duration-500 ease-out"
          style={{ height: `calc(${Math.round(pct * 100)}% - 24px)` }}
        />

        <ol className="flex flex-col gap-6">
          {hitos.map((h, i) => {
            const cierre = h.tipo === "cierre";
            const color = colorNodo(h);
            return (
              <li key={i} className="grid grid-cols-[20px_1fr] gap-4">
                {/* el nodo sobre el eje: anillo mayor en el cierre; punto en el resto */}
                <span className="relative flex justify-center pt-0.5">
                  {cierre ? (
                    <span
                      className={
                        "z-10 flex h-5 w-5 items-center justify-center rounded-full border-2 " +
                        (h.alcanzado ? "bg-black" : "border-hairline bg-bg")
                      }
                      style={h.alcanzado ? { borderColor: VERDE } : undefined}
                    >
                      {h.alcanzado && <span className="h-2 w-2 rounded-full" style={{ background: VERDE }} />}
                    </span>
                  ) : (
                    <span className="z-10 mt-1 h-3 w-3 rounded-full ring-4 ring-bg" style={{ background: color }} />
                  )}
                </span>

                {/* contenido: fecha + etiqueta del hito */}
                <div className={cierre && !h.alcanzado ? "opacity-70" : ""}>
                  {h.fecha ? (
                    <p className="text-[12px] text-dim">{fechaHumanaCorta(h.fecha)}</p>
                  ) : (
                    <p className="text-[12px] text-dim/70">tu próxima meta</p>
                  )}
                  <p
                    className={
                      "mt-0.5 leading-snug [text-wrap:pretty] " +
                      (cierre && h.alcanzado
                        ? "text-[15px] font-bold uppercase tracking-wide text-done"
                        : h.alcanzado
                          ? "text-[14.5px] font-medium text-ink"
                          : "text-[14.5px] font-medium text-dim")
                    }
                  >
                    {h.etiqueta}
                  </p>
                </div>
              </li>
            );
          })}
        </ol>
      </div>
    </div>
  );
}
