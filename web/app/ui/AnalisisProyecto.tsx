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

function Tile({ valor, etiqueta }: { valor: string; etiqueta: string }) {
  return (
    <div className="rounded-panel border border-hairline bg-surface p-5">
      <p className="text-3xl font-bold tracking-tight sm:text-[34px]">{valor}</p>
      <p className="mt-1 text-[12.5px] text-dim">{etiqueta}</p>
    </div>
  );
}

function descargar(nombre: string, md: string) {
  const blob = new Blob([md], { type: "text/markdown;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `analisis-${nombre.replace(/[^\p{L}\p{N}]+/gu, "-").slice(0, 40) || "proyecto"}.md`;
  document.body.appendChild(a);
  a.click();
  a.remove();
  URL.revokeObjectURL(url);
}

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

  const maxBarra = useMemo(() => {
    const c = datos?.analytics.cumplimiento;
    if (!c) return 1;
    return Math.max(1, ...c.porEtapa.flatMap((e) => [e.baseDias ?? 0, e.realDias ?? 0]));
  }, [datos]);

  const maxDur = useMemo(() => {
    const d = datos?.analytics.universal.duracionPorEtapa ?? [];
    return Math.max(1, ...d.map((e) => e.dias));
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
        <button
          onClick={() => descargar(nombre, datos.informe_md)}
          className="rounded-[10px] border border-white/15 px-4 py-2 text-[13px] text-dim hover:border-accent/60 hover:text-ink"
        >
          Descargar mi informe (.md)
        </button>
      </header>

      {/* ── Capa universal ── */}
      <section>
        <p className="mb-4 text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">Capa universal</p>
        <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
          <Tile valor={String(u.duracionTotalDias)} etiqueta="días de duración total" />
          <Tile valor={u.ritmoAccionesPorSemana.toFixed(1)} etiqueta="acciones por semana" />
          <Tile valor={String(u.rachaMasLargaDias)} etiqueta="días de racha más larga" />
          <Tile valor={`${u.ciclosDePlan} · ${u.mundos}`} etiqueta="ciclos · mundos" />
        </div>

        {/* Canon 11: duración con barras (izq) y hitos (der) en dos columnas. */}
        {(u.duracionPorEtapa.length > 0 || a.hitos.length > 0) && (
          <div className="mt-6 flex flex-col gap-4 lg:flex-row lg:items-start">
            {u.duracionPorEtapa.length > 0 && (
              <div className="flex-1 rounded-panel border border-hairline bg-surface p-5">
                <p className="mb-4 text-[13px] font-semibold">Duración real por etapa</p>
                <div className="flex flex-col gap-3.5">
                  {u.duracionPorEtapa.map((e) => (
                    <div key={e.etapa}>
                      <div className="mb-1.5 flex items-baseline justify-between gap-3">
                        <span className="text-[14px]">{nombreEtapa(e.etapa)}</span>
                        <span className="text-[13px] font-semibold text-dim">{e.dias} días</span>
                      </div>
                      <div className="h-2 overflow-hidden rounded bg-white/5">
                        <div
                          className="h-full rounded"
                          style={{ width: `${(e.dias / maxDur) * 100}%`, background: "var(--accent)" }}
                        />
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {a.hitos.length > 0 && (
              <div className="rounded-panel border border-hairline bg-surface p-5 lg:w-[340px] lg:shrink-0">
                <p className="mb-4 text-[13px] font-semibold">Hitos</p>
                <ol className="flex flex-col gap-3 border-l border-hairline pl-4">
                  {a.hitos.map((h, i) => (
                    <li key={i} className="relative">
                      <span
                        className="absolute -left-[21px] top-1.5 h-2 w-2 rounded-full"
                        style={{ background: h.tipo === "realizada" ? "var(--done)" : "var(--accent)" }}
                      />
                      <span className="text-[13px] text-dim">{fechaHumanaCorta(h.fecha)}</span>
                      <span className="ml-2 text-[13.5px]">{h.etiqueta}</span>
                    </li>
                  ))}
                </ol>
              </div>
            )}
          </div>
        )}
      </section>

      {/* ── Capa de cumplimiento (solo con baseline) ── */}
      {tiene_baseline && c && (
        <section>
          <p className="mb-4 text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">
            Capa de cumplimiento · <span className="text-accent">modo fechas</span>
          </p>
          <div className="grid grid-cols-3 gap-3">
            <div className="rounded-panel border border-done/40 bg-surface p-5">
              <p className="text-3xl font-bold text-done">
                {c.aTiempo} <span className="text-lg font-semibold text-dim">· {c.pctATiempo}%</span>
              </p>
              <p className="mt-1 text-[12.5px] text-dim">a tiempo</p>
            </div>
            <div className="rounded-panel border border-accent/40 bg-surface p-5">
              <p className="text-3xl font-bold text-accent">
                {c.adelantadas} <span className="text-lg font-semibold text-dim">· {c.pctAdelantadas}%</span>
              </p>
              <p className="mt-1 text-[12.5px] text-dim">adelantadas</p>
            </div>
            <div className="rounded-panel border border-warn/40 bg-surface p-5">
              <p className="text-3xl font-bold text-warn">
                {c.tardias} <span className="text-lg font-semibold text-dim">· {c.pctTardias}%</span>
              </p>
              <p className="mt-1 text-[12.5px] text-dim">tardías</p>
            </div>
          </div>

          {/* Canon 11: barras gemelas (izq) y desviación + replanificación
              en paneles apilados (der). */}
          <div className="mt-6 flex flex-col gap-4 lg:flex-row lg:items-start">
            {c.porEtapa.length > 0 && (
              <div className="flex-1 rounded-panel border border-hairline bg-surface p-5">
                <div className="mb-3 flex flex-wrap items-baseline justify-between gap-2">
                  <p className="text-[13px] font-semibold">Planificado vs. real por etapa</p>
                  <p className="flex gap-4 text-[11.5px] text-dim">
                    <span className="flex items-center gap-1.5">
                      <span className="h-2 w-4 rounded-sm" style={{ background: "rgba(77,124,254,0.55)" }} /> base
                    </span>
                    <span className="flex items-center gap-1.5">
                      <span className="h-2 w-4 rounded-sm bg-done" /> real
                    </span>
                  </p>
                </div>
                <div className="flex flex-col gap-3">
                  {c.porEtapa.map((e) => {
                    const tardeEtapa = (e.realDias ?? 0) > (e.baseDias ?? 0) + 1;
                    return (
                      <div key={e.etapa}>
                        <p className="mb-1 text-[13px]">{nombreEtapa(e.etapa)}</p>
                        <div className="flex flex-col gap-1">
                          <div className="h-2.5 overflow-hidden rounded bg-white/5">
                            <div
                              className="h-full rounded"
                              style={{ width: `${((e.baseDias ?? 0) / maxBarra) * 100}%`, background: "rgba(77,124,254,0.55)" }}
                            />
                          </div>
                          <div className="h-2.5 overflow-hidden rounded bg-white/5">
                            <div
                              className="h-full rounded"
                              style={{
                                width: `${((e.realDias ?? 0) / maxBarra) * 100}%`,
                                background: tardeEtapa ? "var(--warn)" : "var(--done)",
                              }}
                            />
                          </div>
                        </div>
                      </div>
                    );
                  })}
                </div>
              </div>
            )}

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
              <div className="rounded-panel border border-hairline bg-surface p-5">
                <p className="text-[15px]">
                  <span className="text-2xl font-bold text-ink">
                    {c.desviacionMediaDias > 0 ? "+" : ""}
                    {c.desviacionMediaDias.toFixed(1)}
                  </span>{" "}
                  <span className="text-dim">días · desviación media sobre lo planificado</span>
                </p>
              </div>
              {c.replanificaciones > 0 && (
                <div className="rounded-panel border border-hairline bg-surface p-5">
                  <p className="text-[14px] font-semibold">
                    Moviste la fecha de {c.replanificaciones} {c.replanificaciones === 1 ? "acción" : "acciones"}
                  </p>
                  <p className="mt-2 text-[13.5px] leading-relaxed text-dim">
                    Replanificar es parte del método. Ajustar el mapa no es fallar: es seguir con los pies en la tierra.
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
