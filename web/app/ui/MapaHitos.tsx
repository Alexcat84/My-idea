"use client";

/**
 * MapaHitos — el mapa HORIZONTAL de hitos del viaje ("Tus hitos, de un vistazo"):
 * una línea con un punto por hito, su fecha y su nombre debajo, en su columna.
 * El último punto late si la idea sigue abierta; al cerrar, vira a verde. Es el
 * formato que el fundador prefiere para el resumen del Análisis (antes vivía en
 * la bitácora; se movió aquí porque es un análisis real, no un registro).
 */
const AZUL = "#4D7CFE";
const VERDE = "#3FB950";
const MESES = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"];

function fechaMapa(iso: string): string {
  const d = new Date(iso);
  return `${d.getDate()} ${MESES[d.getMonth()]}`;
}

export interface HitoMapa {
  fecha: string;
  nombre: string;
  /** el cierre (Realizado): el único verde */
  cierre?: boolean;
}

export function MapaHitos({ hitos, cerrada }: { hitos: HitoMapa[]; cerrada: boolean }) {
  const N = hitos.length;
  if (N === 0) return null;
  const inset = N > 1 ? 100 / (2 * N) : 50;
  return (
    <div>
      <div className="mb-5 text-[11.5px] font-semibold uppercase tracking-[1.3px] text-dim">Tus hitos, de un vistazo</div>
      <div className="relative overflow-x-auto">
        <div className="relative" style={{ minWidth: N > 6 ? N * 96 : undefined }}>
          <div
            aria-hidden
            style={{
              position: "absolute",
              left: `${inset}%`,
              right: `${inset}%`,
              top: 8,
              height: 2,
              background: cerrada
                ? `linear-gradient(to right, rgba(77,124,254,0.85) 0%, rgba(77,124,254,0.85) 82%, rgba(63,185,80,0.9) 100%)`
                : `rgba(77,124,254,0.85)`,
            }}
          />
          <div className="relative grid items-start" style={{ gridTemplateColumns: `repeat(${N}, 1fr)` }}>
            {hitos.map((h, i) => {
              const esCierre = Boolean(h.cierre);
              const viva = !cerrada && i === N - 1;
              return (
                <div key={i} className="flex flex-col items-center gap-0 px-1 text-center">
                  <div className="flex h-[18px] items-center justify-center">
                    <span
                      className={viva ? "anima-idea-pulse" : undefined}
                      style={{
                        width: esCierre ? 13 : 11,
                        height: esCierre ? 13 : 11,
                        borderRadius: "50%",
                        background: esCierre ? VERDE : AZUL,
                        boxShadow: esCierre ? `0 0 0 4px rgba(63,185,80,0.18)` : undefined,
                      }}
                    />
                  </div>
                  <div className="mt-2.5 text-[11.5px] tabular-nums text-dim">{fechaMapa(h.fecha)}</div>
                  <div className="mt-1 text-[12.5px] font-semibold leading-[1.35]" style={{ color: esCierre ? VERDE : "#F5F6F8" }}>
                    {h.nombre}
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </div>
      <div className="mt-4 text-[11.5px] text-dim">
        Un paso por hito, en el orden en que ocurrieron. Las distancias reales entre fechas viven en la línea de abajo.
      </div>
    </div>
  );
}
