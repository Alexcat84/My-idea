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
import { Acordeon } from "./Acordeon";
import { BarraAvance } from "./BarraAvance";
import {
  RepartoCumplimiento,
  RitmoSemanal,
  AvanceAcumulado,
  EsfuerzoPorEtapa,
  ProyeccionCierre,
  CumplimientoPorMundoBarras,
  DistribucionEstados,
  Tile,
} from "./GraficosAnalisis";

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

/** Una fila del desglose "Tu proyecto completo" (Fase 3, tanda 4): un nivel
 * (el viaje o un mundo, o la suma declarada) con su X de N y su %. Cada acción
 * pertenece a UN solo nivel: el total es la suma, nunca un número mezclado. */
function NivelFila({ nombre, hechas, total, destacado }: { nombre: string; hechas: number; total: number; destacado?: boolean }) {
  const pct = total > 0 ? Math.round((hechas / total) * 100) : 0;
  return (
    <div
      className={
        "flex items-center justify-between gap-3 rounded-[12px] px-3.5 py-2.5 " +
        (destacado ? "border border-accent/25 bg-accent/[0.06]" : "bg-surface")
      }
    >
      <span className={"min-w-0 flex-1 truncate text-[13.5px] " + (destacado ? "font-bold" : "font-semibold")}>{nombre}</span>
      <span className="flex-none text-[12.5px] tabular-nums text-dim">
        {hechas} de {total} · {pct}%
      </span>
    </div>
  );
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

      {/* Fase 3 (tanda 4): "Tu proyecto completo" — DECLARA la composición (core y
          N mundos), cada nivel su avance, el del proyecto = la SUMA declarada, sin
          doble conteo. RUIDO CERO: solo aparece cuando hay mundos. */}
      {a.mundos.length > 0 &&
        (() => {
          const sumHechas = u.accionesVigente.hechas + a.mundos.reduce((s, m) => s + m.universal.accionesVigente.hechas, 0);
          const sumTotal = u.accionesVigente.total + a.mundos.reduce((s, m) => s + m.universal.accionesVigente.total, 0);
          return (
            <section className="rounded-panel border border-hairline bg-surface-3 p-5 sm:p-6">
              <p className="text-[11px] font-semibold uppercase tracking-[1.2px] text-accent">Tu proyecto completo</p>
              <p className="mt-2 text-[14px] leading-relaxed [text-wrap:pretty]">
                Tu proyecto completo: <strong>tu viaje</strong> y{" "}
                <strong>
                  {a.mundos.length} {a.mundos.length === 1 ? "mundo" : "mundos"}
                </strong>
                . Cada nivel avanza por su cuenta; el del proyecto es la <strong>suma</strong> de todos, sin mezclarlos.
              </p>
              <div className="mt-4 flex flex-col gap-2">
                <NivelFila nombre={NOMBRE_DOMINIO.core} hechas={u.accionesVigente.hechas} total={u.accionesVigente.total} />
                {a.mundos.map((m) => (
                  <NivelFila
                    key={m.dominio}
                    nombre={NOMBRE_DOMINIO[m.dominio] ?? m.dominio}
                    hechas={m.universal.accionesVigente.hechas}
                    total={m.universal.accionesVigente.total}
                  />
                ))}
                <NivelFila nombre="Todo el proyecto (suma)" hechas={sumHechas} total={sumTotal} destacado />
              </div>
              <p className="mt-3 text-[12px] leading-relaxed text-dim [text-wrap:pretty]">
                Ninguna acción se cuenta dos veces: cada una pertenece a un solo nivel. El total es la suma declarada, nunca un
                número mezclado.
              </p>
            </section>
          );
        })()}

      {/* ── El análisis por CAPAS en acordeones: el usuario despliega lo que
          quiera ver. Cada capa es un reporte visual distinto. ── */}

      {/* Capa 1 — Tu viaje de un vistazo (abierta): avance + cifras + hitos. */}
      <Acordeon
        variante="capa"
        abierto
        titulo={
          <span className="flex items-center gap-2.5 text-[15px] font-semibold">
            <span aria-hidden className="h-2 w-2 rounded-full bg-accent" />
            Tu viaje de un vistazo
          </span>
        }
      >
        <div className="flex flex-col gap-6">
          {u.accionesVigente.total > 0 && (
            <div className="rounded-[16px] border border-hairline bg-surface px-5 py-[18px]">
              <BarraAvance pct={Math.round((u.accionesVigente.hechas / u.accionesVigente.total) * 100)} />
            </div>
          )}
          {/* La curva de culminación: cuánto del plan llevas cerrado en el tiempo. */}
          <AvanceAcumulado series={u.avancePorSemana} total={u.accionesVigente.total} />
          {/* Candidato: proyección de cierre (a tu ritmo, cuándo terminas). */}
          <ProyeccionCierre
            hechas={u.accionesVigente.hechas}
            total={u.accionesVigente.total}
            ritmoPorSemana={u.ritmoAccionesPorSemana}
            cerrada={Boolean(datos.realizada_at)}
          />
          <div>
            {/* Cifras en color (azul piensa): en blanco no lucían. Medida sin juicio. */}
            <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
              <Tile valor={String(u.duracionTotalDias)} etiqueta="días de duración total" color="var(--accent)" />
              <Tile valor={u.ritmoAccionesPorSemana.toFixed(1)} etiqueta="acciones por semana" color="var(--accent)" />
              <Tile valor={String(u.rachaMasLargaDias)} etiqueta="días de racha más larga" color="var(--accent)" />
              <Tile valor={`${u.ciclosDePlan} · ${u.mundos}`} etiqueta="ciclos · mundos" color="var(--accent)" />
            </div>
            {u.retiradas.length > 0 && (
              <p className="mt-3 text-[13px] text-dim">
                Retiradas (no aplican): <span className="font-semibold text-ink">{u.retiradas.length}</span>. Decidiste que no
                corren para esta idea; quedan en tu expediente con su motivo.
              </p>
            )}
          </div>
          {a.hitos.length > 0 && (
            <div className="rounded-panel border border-hairline bg-surface-3 p-5 sm:p-6">
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
        </div>
      </Acordeon>

      {/* Capa 2 — Tu ritmo y tu esfuerzo: ritmo semanal y esfuerzo por etapa.
          El calendario de constancia se retiró: los días viven en el Calendario,
          fuente única de las fechas. */}
      {(u.accionesHechas > 0 || u.accionesPorEtapa.length > 0) && (
        <Acordeon
          variante="capa"
          titulo={
            <span className="flex items-center gap-2.5 text-[15px] font-semibold">
              <span aria-hidden className="h-2 w-2 rounded-full bg-done" />
              Tu ritmo y tu esfuerzo
            </span>
          }
        >
          <div className="flex flex-col gap-5">
            <RitmoSemanal series={u.avancePorSemana} />
            {/* Candidato: distribución de estados (cómo van tus acciones ahora). */}
            <DistribucionEstados dist={u.distribucionEstados} />
            <EsfuerzoPorEtapa series={u.accionesPorEtapa} nombreEtapa={nombreEtapa} />
          </div>
        </Acordeon>
      )}

      {/* Capa 3 — Cómo cumpliste tus fechas (solo con línea base). */}
      {tiene_baseline && c && (
        <Acordeon
          variante="capa"
          titulo={
            <span className="flex items-center gap-2.5 text-[15px] font-semibold">
              <span aria-hidden className="h-2 w-2 rounded-full bg-warn" />
              Cómo cumpliste tus fechas
            </span>
          }
        >
          <div className="flex flex-col gap-5">
            <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
              <TileCumpl valor={String(c.adelantadas)} sufijo={`${c.pctAdelantadas}%`} etiqueta="adelantadas" color="var(--done)" />
              <TileCumpl valor={String(c.aTiempo)} sufijo={`${c.pctATiempo}%`} etiqueta="a tiempo" color="var(--accent)" />
              <TileCumpl valor={String(c.tardias)} sufijo={`${c.pctTardias}%`} etiqueta="tardías" color="var(--warn)" />
              <TileCumpl
                valor={`${c.desviacionMediaDias > 0 ? "+" : ""}${c.desviacionMediaDias.toFixed(1)}`}
                sufijo="días"
                etiqueta="desviación media"
                color="var(--accent)"
              />
            </div>

            <RepartoCumplimiento aTiempo={c.aTiempo} adelantadas={c.adelantadas} tardias={c.tardias} />

            {/* Capa de honestidad: banda gris con icono neutro. Contexto, no alarma. */}
            {c.replanificaciones > 0 && (
              <div className="flex items-start gap-3 rounded-[14px] border border-hairline px-5 py-4">
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

            {c.porEtapa.length > 0 && (
              <GanttCumplimiento
                porEtapa={c.porEtapa}
                maxBarra={maxBarra}
                nombreEtapa={nombreEtapa}
                hoyDias={datos.realizada_at ? null : u.duracionTotalDias}
              />
            )}

            {c.porDominio.length > 1 && (
              <CumplimientoPorMundoBarras
                filas={c.porDominio.map((d) => ({
                  dominio: d.dominio,
                  nombre: NOMBRE_DOMINIO[d.dominio] ?? d.dominio,
                  adelantadas: d.adelantadas,
                  aTiempo: d.aTiempo,
                  tardias: d.tardias,
                  completado: datos.analytics.mundos.some((m) => m.dominio === d.dominio && m.completadoAt),
                }))}
              />
            )}
          </div>
        </Acordeon>
      )}
    </div>
  );
}
