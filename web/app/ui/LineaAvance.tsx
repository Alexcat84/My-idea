"use client";

/**
 * LineaAvance — campaña "Espacios", la cara "Tu avance". CALCO del timeline
 * vertical de La Celebración (docs/diseno-canon/09_la_celebracion.html): eje
 * central con degradado azul→verde, filas que ALTERNAN lados (izq/der en
 * escritorio; todo a la derecha del eje en móvil), nodos sobre el eje, y una
 * DIANA para el cierre. ESTÁTICO (sin la animación de dibujarse: esa es la
 * Celebración grande, del proyecto). Muestra LO MÁS IMPORTANTE (los hitos), no
 * cada acción (eso es el Manos a la obra / la bitácora). Cero estadística.
 */
import { fechaHumanaCorta } from "@/lib/fechas";
import type { HitoEspacio } from "@/lib/hitosEspacio";

const AZUL = "#4D7CFE";
const VERDE = "#3FB950";

export function LineaAvance({ hitos }: { hitos: HitoEspacio[] }) {
  // El último hito es el cierre (la diana final); el resto, los arranques.
  const cierre = hitos.at(-1);
  const arranques = hitos.slice(0, -1);
  const total = hitos.length;
  const alcanzados = hitos.filter((h) => h.alcanzado).length;
  const pct = total > 1 ? Math.round(((alcanzados - 1) / (total - 1)) * 100) : 0;

  return (
    <div className="anima-plan-in">
      <p className="text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">Tu avance</p>
      <p className="mb-7 mt-1 text-[13px] leading-relaxed text-dim">Del inicio al cierre, los hitos de este espacio.</p>

      <div className="relative">
        {/* el eje: pista hairline + degradado azul→verde hasta lo alcanzado.
            Central en escritorio (left-1/2), a la izquierda en móvil (20px). */}
        <span className="absolute bottom-0 left-5 top-1 w-[3px] -translate-x-1/2 rounded bg-hairline sm:left-1/2" />
        <span
          className="absolute left-5 top-1 w-[3px] -translate-x-1/2 rounded sm:left-1/2"
          style={{ height: `${pct}%`, background: `linear-gradient(180deg, ${AZUL}, ${VERDE})` }}
        />

        {/* los arranques: filas alternando lado */}
        <div className="flex flex-col gap-[26px] sm:gap-[34px]">
          {arranques.map((h, i) => {
            const izq = i % 2 === 0;
            return (
              <div key={i} className="grid grid-cols-[40px_1fr] items-start sm:grid-cols-[1fr_44px_1fr]">
                <div className="col-start-1 flex justify-center pt-1 sm:col-start-2">
                  <span
                    className="h-[13px] w-[13px] rounded-full border-[3px] border-black"
                    style={{ background: h.alcanzado ? AZUL : "transparent", borderColor: h.alcanzado ? "#000" : undefined }}
                  />
                </div>
                <div
                  className={
                    "col-start-2 " +
                    (izq ? "sm:col-start-1 sm:pr-4 sm:text-right" : "sm:col-start-3 sm:pl-4 sm:text-left")
                  }
                >
                  {h.fecha && <p className="text-[12.5px] text-dim">{fechaHumanaCorta(h.fecha)}</p>}
                  <p className="text-[16px] font-bold leading-[1.4] [text-wrap:pretty]">{h.etiqueta}</p>
                  {h.subtitulo && <p className="mt-1 text-[13px] leading-snug text-dim">{h.subtitulo}</p>}
                </div>
              </div>
            );
          })}
        </div>

        {/* la diana del cierre: verde con brillo si ya cerró; hueca gris si falta */}
        {cierre && (
          <div className="mt-[26px] flex flex-col items-start pl-[7px] sm:mt-[34px] sm:items-center sm:pl-0">
            <span
              className="flex h-[30px] w-[30px] items-center justify-center rounded-full border-[3px]"
              style={
                cierre.alcanzado
                  ? { borderColor: VERDE, boxShadow: "0 0 20px rgba(63,185,80,0.35)" }
                  : { borderColor: "rgba(255,255,255,0.18)" }
              }
            >
              {cierre.alcanzado && <span className="h-3 w-3 rounded-full" style={{ background: VERDE }} />}
            </span>
            <p className={"mt-3 text-[15px] font-extrabold uppercase tracking-[1.5px] " + (cierre.alcanzado ? "text-done" : "text-dim")}>
              {cierre.etiqueta}
            </p>
            {cierre.subtitulo && <p className="mt-1.5 text-[13px] text-dim sm:text-center">{cierre.subtitulo}</p>}
          </div>
        )}
      </div>
    </div>
  );
}
