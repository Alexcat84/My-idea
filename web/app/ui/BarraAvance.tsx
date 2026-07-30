"use client";

/**
 * BarraAvance — la barra de avance del proyecto: el porcentaje grande + una
 * barra con ESCALA (25/50/75/100) y relleno en DEGRADADO que arranca en azul
 * (la iniciación) y se torna verde puro al completar. La comparten Manos a la
 * Obra (dentro de su recuadro) y el Análisis del proyecto (capa universal), para
 * que el avance se lea igual en los dos lugares.
 */
export function BarraAvance({ pct }: { pct: number }) {
  return (
    <div className="flex items-center gap-4">
      <span className="flex-none text-[32px] font-extrabold leading-none tracking-[-1px] text-done tabular-nums">{pct}%</span>
      <div className="flex-1">
        <div className="relative h-4 overflow-hidden rounded-full bg-white/[0.08]">
          {/* relleno: recorta un gradiente azul→verde a lo ancho del riel, así el
              borde que avanza refleja cuánto se completó. */}
          <div
            className="h-full overflow-hidden rounded-full"
            style={{ width: `${pct}%`, animation: "barGrow 1.2s ease-out both" }}
          >
            <div
              className="h-full"
              style={{ width: `${pct > 0 ? 10000 / pct : 100}%`, background: "linear-gradient(to right, #4D7CFE, #3FB950)" }}
            />
          </div>
          {/* divisiones de la escala */}
          {[25, 50, 75].map((p) => (
            <div key={p} className="absolute inset-y-0 w-px bg-white/25" style={{ left: `${p}%` }} />
          ))}
        </div>
        {/* rótulos de la escala */}
        <div className="mt-1.5 flex justify-between text-[10px] tabular-nums text-dim">
          {[0, 25, 50, 75, 100].map((p) => (
            <span key={p}>{p}</span>
          ))}
        </div>
      </div>
    </div>
  );
}
