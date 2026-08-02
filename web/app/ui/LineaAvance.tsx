"use client";

/**
 * LineaAvance — campaña "Espacios", la cara "Tu avance". La línea de HITOS reales
 * del espacio (de hitosEspacio.ts): del inicio al cierre. Sobria a propósito — la
 * animación con constelación y pulso es de la Celebración grande, del PROYECTO.
 * Distinción por FORMA además de color: hito alcanzado = punto lleno verde; el
 * cierre pendiente = punto hueco gris (lo que falta). Cero estadística: esto es
 * la historia de hitos, no números (eso vive en Análisis).
 */
import { fechaHumana } from "@/lib/fechas";
import type { HitoEspacio } from "@/lib/hitosEspacio";

export function LineaAvance({ hitos }: { hitos: HitoEspacio[] }) {
  const alcanzados = hitos.filter((h) => h.alcanzado).length;

  return (
    <div className="anima-plan-in">
      <p className="text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">Tu avance</p>
      <p className="mt-1 text-[13px] leading-relaxed text-dim">
        Los hitos que has alcanzado, del inicio al cierre.{" "}
        <span className="font-semibold text-done tabular-nums">{alcanzados}</span> alcanzados.
      </p>

      <ol className="mt-5 ml-1 border-l border-hairline">
        {hitos.map((h, i) => (
          <li key={i} className="relative pb-5 pl-6 last:pb-0">
            <span
              className={
                "absolute -left-[7px] top-0.5 flex h-3.5 w-3.5 items-center justify-center rounded-full " +
                (h.alcanzado ? "bg-done" : "border-2 border-hairline bg-bg")
              }
              aria-hidden
            >
              {h.alcanzado && h.tipo === "cierre" && (
                <svg width="8" height="8" viewBox="0 0 12 12">
                  <path d="M2 6.5l2.5 2.5L10 3.5" fill="none" stroke="#04120A" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round" />
                </svg>
              )}
            </span>
            <p className={"text-[14px] font-semibold leading-snug [text-wrap:pretty] " + (h.alcanzado ? "text-ink" : "text-dim")}>
              {h.etiqueta}
            </p>
            {h.fecha ? (
              <p className="mt-0.5 text-[12px] text-dim">{fechaHumana(h.fecha)}</p>
            ) : (
              <p className="mt-0.5 text-[12px] text-dim/70">tu próxima meta</p>
            )}
          </li>
        ))}
      </ol>
    </div>
  );
}
