"use client";

/**
 * AnalisisProyecto — Fase 3.8 §6 (canon 11): el análisis del proyecto, TODO
 * de lo persistido (cero LLM). Capa universal siempre; capa de cumplimiento
 * solo con baseline confirmada. Tono espejo: las tardías en ÁMBAR, jamás
 * rojo. Botón "Descargar mi informe (.md)".
 */
import { useEffect, useMemo, useState } from "react";
import type { Analytics } from "@/lib/analytics";
import { fechaHumanaCorta } from "@/lib/fechas";
import catalogo from "@/lib/assets/packs_catalog.json";
import { GanttCumplimiento } from "./GanttCumplimiento";
import { MapaHitos } from "./MapaHitos";

interface Respuesta {
  nombre: string;
  tiene_baseline: boolean;
  /** Fase 4.0 §8: el acta de cierre. */
  realizada_at?: string | null;
  cierre_motivo?: string | null;
  analytics: Analytics;
  informe_md: string;
}

const ERROR = "algo se atoró de nuestro lado; intenta de nuevo en un momento";

/** Fase 4.1 (V3b): el mundo se nombra como el usuario lo conoce, jamás por su
 * clave técnica. "core" es el viaje principal. */
const NOMBRE_DOMINIO: Record<string, string> = Object.fromEntries([
  ["core", "Tu viaje principal"],
  ...(catalogo as { packs: Array<{ clave: string; nombre: string }> }).packs.map((p) => [p.clave, p.nombre]),
]);

function Tile({ valor, etiqueta, color }: { valor: string; etiqueta: string; color?: string }) {
  return (
    <div className="flex flex-col items-center justify-center rounded-[14px] border border-hairline bg-surface-3 px-4 py-6 text-center">
      <p className="text-[38px] font-extrabold leading-none tracking-tight tabular-nums" style={color ? { color } : undefined}>
        {valor}
      </p>
      <p className="mt-2 text-[12px] text-dim [text-wrap:balance]">{etiqueta}</p>
    </div>
  );
}

/** Tile compacta de cumplimiento: el número (grande y centrado) lleva el color
 * semántico (verde a tiempo, azul adelantada, ámbar tardía), debajo el
 * porcentaje o la unidad y la etiqueta. Misma familia que la capa universal. */
function TileCumpl({ valor, sufijo, etiqueta, color }: { valor: string; sufijo: string; etiqueta: string; color?: string }) {
  return (
    <div className="flex flex-col items-center justify-center rounded-[14px] border border-hairline bg-surface-3 px-3 py-5 text-center">
      <p className="text-[34px] font-extrabold leading-none tracking-tight tabular-nums" style={color ? { color } : undefined}>
        {valor}
      </p>
      <p className="mt-1.5 text-[12px] font-semibold text-dim tabular-nums">{sufijo}</p>
      <p className="mt-0.5 text-[12px] text-dim [text-wrap:balance]">{etiqueta}</p>
    </div>
  );
}

/** Chip numerado que amarra la leyenda con el diagrama (misma cifra arriba y
 * en la barra), para que el texto no parta el Gantt. */

export function AnalisisProyecto({
  projectId,
  titulos,
  onVolver,
}: {
  projectId: string;
  titulos: Record<number, string>;
  onVolver: () => void;
}) {
  const [datos, setDatos] = useState<Respuesta | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let vivo = true;
    (async () => {
      try {
        const res = await fetch(`/api/project/${projectId}/analisis`);
        if (!res.ok) {
          if (vivo) setError(ERROR);
          return;
        }
        if (vivo) setDatos((await res.json()) as Respuesta);
      } catch {
        if (vivo) setError("no pudimos cargar tu análisis; revisa tu internet e intenta de nuevo");
      }
    })();
    return () => {
      vivo = false;
    };
  }, [projectId]);

  // El horizonte de la línea de tiempo del Gantt: el mayor fin (base o real).
  const maxBarra = useMemo(() => {
    const c = datos?.analytics.cumplimiento;
    if (!c) return 1;
    return Math.max(1, ...c.porEtapa.flatMap((e) => [e.baseFin ?? 0, e.realFin ?? 0]));
  }, [datos]);

  if (error) return <p className="text-sm text-warn">{error}</p>;
  if (!datos) return <p className="text-dim">Calculando tu análisis…</p>;

  const { analytics: a, nombre, tiene_baseline } = datos;
  const u = a.universal;
  const c = a.cumplimiento;
  const nombreEtapa = (n: number) => titulos[n] ?? `Etapa ${n}`;

  return (
    <div className="flex flex-col gap-8">
      <button onClick={onVolver} className="self-start text-sm text-dim hover:text-ink">
        ← Volver
      </button>

      {/* Fase 4.0 §8: el acta de cierre encabeza el análisis de un proyecto
          ya cerrado: estado final y el porqué, en la voz del usuario. */}
      {datos.realizada_at && (
        <section className="rounded-panel border border-done/40 bg-surface p-5">
          <p className="text-[11px] font-semibold uppercase tracking-[1.2px] text-done">Acta de cierre</p>
          <p className="mt-2 text-[14px]">
            Cerrado el {fechaHumanaCorta(datos.realizada_at)} con{" "}
            <span className="font-semibold">
              {a.universal.accionesVigente.hechas} de {a.universal.accionesVigente.total}
            </span>{" "}
            acciones. Lo que quedó pendiente sigue en tu historia, tal cual.
          </p>
          {datos.cierre_motivo && (
            <blockquote className="mt-3 border-l-2 border-done/50 pl-3 text-[13.5px] leading-[1.65] text-dim [text-wrap:pretty]">
              «{datos.cierre_motivo}»
            </blockquote>
          )}
        </section>
      )}

      <header className="flex flex-wrap items-center justify-between gap-4">
        <h2 className="text-2xl font-bold tracking-tight sm:text-[28px]">Análisis de {nombre}</h2>
        {/* La descarga del informe vive en "Tus documentos" (centralizado): aquí
            ya no hay botón propio. */}
      </header>

      {/* ── Capa universal ── */}
      <section>
        <p className="mb-4 text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">Capa universal</p>
        {/* Cifras en color (azul piensa): en blanco no lucían. Es medida sin
            juicio, así que van todas del mismo color. */}
        <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
          <Tile valor={String(u.duracionTotalDias)} etiqueta="días de duración total" color="var(--accent)" />
          <Tile valor={u.ritmoAccionesPorSemana.toFixed(1)} etiqueta="acciones por semana" color="var(--accent)" />
          <Tile valor={String(u.rachaMasLargaDias)} etiqueta="días de racha más larga" color="var(--accent)" />
          <Tile valor={`${u.ciclosDePlan} · ${u.mundos}`} etiqueta="ciclos · mundos" color="var(--accent)" />
        </div>
        {/* Gestor de estados: las retiradas tienen su línea propia. No cuentan
            para el avance ni como tardías; son una decisión, no un fracaso. */}
        {u.retiradas.length > 0 && (
          <p className="mt-3 text-[13px] text-dim">
            Retiradas (no aplican): <span className="font-semibold text-ink">{u.retiradas.length}</span>. Decidiste que no
            corren para esta idea; quedan en tu expediente con su motivo.
          </p>
        )}

        {/* Mapa de hitos HORIZONTAL (el formato que vivía en la bitácora): el
            viaje de un vistazo, un punto por hito. Reemplaza a la lista vertical
            y a "Duración por etapa" (que no se entendía). */}
        {a.hitos.length > 0 && (
          <div className="mt-6 rounded-panel border border-hairline bg-surface-3 p-5 sm:p-6">
            <MapaHitos
              cerrada={Boolean(datos.realizada_at)}
              hitos={a.hitos.map((h) => ({
                fecha: h.fecha,
                nombre: h.tipo === "realizada" ? "Realizado" : h.etiqueta,
                cierre: h.tipo === "realizada",
              }))}
            />
          </div>
        )}
      </section>

      {/* ── Capa de cumplimiento (solo con baseline) ── */}
      {tiene_baseline && c && (
        <section>
          <p className="mb-4 text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">
            Capa de cumplimiento · <span className="text-accent">modo fechas</span>
          </p>
          {/* Indicadores reorganizados: una fila de 4 tiles compactas (a tiempo,
              adelantadas, tardías, desviación media), en la misma familia visual
              que la capa universal. El color vive en el número, no en el borde. */}
          <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
            <TileCumpl valor={String(c.aTiempo)} sufijo={`${c.pctATiempo}%`} etiqueta="a tiempo" color="var(--done)" />
            <TileCumpl valor={String(c.adelantadas)} sufijo={`${c.pctAdelantadas}%`} etiqueta="adelantadas" color="var(--accent)" />
            <TileCumpl valor={String(c.tardias)} sufijo={`${c.pctTardias}%`} etiqueta="tardías" color="var(--warn)" />
            <TileCumpl
              valor={`${c.desviacionMediaDias > 0 ? "+" : ""}${c.desviacionMediaDias.toFixed(1)}`}
              sufijo="días"
              etiqueta="desviación media"
              color="var(--accent)"
            />
          </div>

          {/* Capa de honestidad (Design): una BANDA propia, gris, con icono
              neutro, JUSTO debajo de las tiles de cumplimiento. Dice contra qué
              se mide y por qué replanificar no vuelve tardío a nadie. Nunca
              ámbar ni roja: es contexto, no alarma. Solo si hubo replanificaciones. */}
          {c.replanificaciones > 0 && (
            <div className="mt-4 flex items-start gap-3 rounded-[14px] border border-hairline px-5 py-4">
              <span aria-hidden className="mt-0.5 grid h-[22px] w-[22px] shrink-0 place-items-center rounded-full border border-hairline text-dim">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round">
                  <circle cx="12" cy="12" r="9" />
                  <path d="M12 11v5" />
                  <path d="M12 7.5v.5" />
                </svg>
              </span>
              <p className="text-[13px] leading-relaxed text-dim [text-wrap:pretty]">
                Frente a tu plan inicial:{" "}
                <span className="font-semibold text-ink tabular-nums">
                  {c.desviacionVsInicialDias > 0 ? "+" : ""}
                  {c.desviacionVsInicialDias.toFixed(1)} días
                </span>{" "}
                de desviación media ·{" "}
                <span className="font-semibold text-ink tabular-nums">{c.replanificaciones}</span>{" "}
                replanificación{c.replanificaciones === 1 ? "" : "es"}. El cumplimiento se mide contra tu
                fecha vigente: replanificar es el control de cambios, no una tardanza.
              </p>
            </div>
          )}

          {/* Gantt "Cómo se movió tu camino": pieza calibrada por Design, tres
              vistas (riel fantasma / escalera / dos cintas) con selector de
              preferencia. Datos reales de analytics; cero LLM. HOY solo con el
              proyecto en marcha (días desde la chispa = duración total). */}
          {c.porEtapa.length > 0 && (
            <GanttCumplimiento
              porEtapa={c.porEtapa}
              maxBarra={maxBarra}
              nombreEtapa={nombreEtapa}
              hoyDias={datos.realizada_at ? null : u.duracionTotalDias}
            />
          )}

          {/* Desviación en palabras + cumplimiento por mundo, debajo del diagrama. */}
          <div className="mt-4 flex flex-col gap-4 lg:flex-row lg:items-start">
            <div className="flex flex-col gap-4 lg:w-[340px] lg:shrink-0">
              {/* Fase 4.1 (V3b): la fila extra que admite el canon 11 — el
                  cumplimiento por dominio. Solo aparece cuando hay algún mundo
                  con fechas: en un proyecto solo-core no estorba. */}
              {c.porDominio.length > 1 && (
                <div className="rounded-panel border border-hairline bg-surface p-5">
                  <p className="mb-3 text-[13px] font-semibold">Cumplimiento por mundo</p>
                  <ul className="flex flex-col gap-2.5">
                    {c.porDominio.map((d) => (
                      <li key={d.dominio} className="flex items-baseline justify-between gap-3">
                        <span className="min-w-0 truncate text-[13px]">
                          {NOMBRE_DOMINIO[d.dominio] ?? d.dominio}
                          {/* Fase 4.2: el mundo que ya tuvo su final lo dice
                              aquí también, sin cambiar el resto de la fila. */}
                          {datos.analytics.mundos.some((m) => m.dominio === d.dominio && m.completadoAt) && (
                            <span className="ml-2 text-[11px] font-semibold text-done">Completado</span>
                          )}
                        </span>
                        <span className="shrink-0 text-[12.5px] tabular-nums">
                          <span className="font-semibold text-done">{d.aTiempo}</span>
                          <span className="text-dim"> · </span>
                          <span className="font-semibold text-accent">{d.adelantadas}</span>
                          <span className="text-dim"> · </span>
                          <span className="font-semibold text-warn">{d.tardias}</span>
                        </span>
                      </li>
                    ))}
                  </ul>
                  <p className="mt-3 border-t border-hairline pt-2.5 text-[11.5px] text-dim">
                    a tiempo · adelantadas · tardías
                  </p>
                </div>
              )}
            </div>
          </div>
        </section>
      )}
    </div>
  );
}
