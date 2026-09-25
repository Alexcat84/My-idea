"use client";

/**
 * AnalisisProyecto — Fase 3.8 §6 (canon 11): el análisis del proyecto, TODO
 * de lo persistido (cero LLM). Capa universal siempre; capa de cumplimiento
 * solo con baseline confirmada. Tono espejo: las tardías en ÁMBAR, jamás
 * rojo. Botón "Descargar mi informe (.md)".
 */
import { useEffect, useMemo, useState } from "react";
import type { ActaCierre } from "@/lib/acta";
import type { Analytics } from "@/lib/analytics";
import { nombreDeMundo } from "@/lib/catalogoMundos";
import { fechaHumanaCorta } from "@/lib/fechas";
import { elegir } from "@/lib/i18n/config";
import { useIdioma } from "@/lib/i18n/IdiomaProvider";
import { decimal } from "@/lib/i18n/formato";
import { interpolar, plural } from "@/lib/i18n/interpolar";
import { rico } from "@/lib/i18n/rico";
import { ANALISIS } from "@/lib/i18n/mensajes/analisis";
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
  DistribucionEstados,
  Tile,
} from "./GraficosAnalisis";

interface Respuesta {
  nombre: string;
  tiene_baseline: boolean;
  /** Fase 4.0 §8: el acta de cierre. */
  realizada_at?: string | null;
  cierre_motivo?: string | null;
  /** AUD-09 M04: el acta de cada espacio (la FOTO guardada al cerrar). */
  actas?: Record<string, ActaCierre>;
  analytics: Analytics;
  informe_md: string;
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
  dominio,
  nombreEspacio,
}: {
  projectId: string;
  titulos: Record<number, string>;
  onVolver: () => void;
  /** "Todo separado" (T4): si es un mundo, el análisis se scopea a ESE espacio
   * (su capa universal + su cumplimiento con Gantt, de analytics.mundos[dominio]).
   * Sin dominio (o "core") es el análisis del núcleo, como siempre. */
  dominio?: string;
  /** el nombre humano del espacio scopeado (el catálogo lo resuelve el llamador). */
  nombreEspacio?: string;
}) {
  const idioma = useIdioma();
  const tx = elegir(ANALISIS, idioma);
  const t = tx.proyecto;
  const [datos, setDatos] = useState<Respuesta | null>(null);
  const [error, setError] = useState<string | null>(null);
  const esCore = !dominio || dominio === "core";

  useEffect(() => {
    let vivo = true;
    (async () => {
      try {
        const res = await fetch(`/api/project/${projectId}/analisis`);
        if (!res.ok) {
          if (vivo) setError(t.error);
          return;
        }
        if (vivo) setDatos((await res.json()) as Respuesta);
      } catch {
        if (vivo) setError(t.errorConexion);
      }
    })();
    return () => {
      vivo = false;
    };
  }, [projectId, t.error, t.errorConexion]);

  // "Todo separado" (T4): la capa que se pinta es la del ESPACIO en foco — el
  // núcleo, o un mundo de analytics.mundos[dominio]. El mundo trae su capa
  // completa (con Gantt porEtapa) desde T3d; sin `porDominio`, que esta pantalla
  // no pinta, así que el MISMO render sirve para ambos.
  const mundo = esCore ? null : datos?.analytics.mundos.find((m) => m.dominio === dominio) ?? null;

  // El horizonte de la línea de tiempo del Gantt: el mayor fin (base o real).
  const maxBarra = useMemo(() => {
    const c = esCore ? datos?.analytics.cumplimiento : mundo?.cumplimiento;
    if (!c) return 1;
    return Math.max(1, ...c.porEtapa.flatMap((e) => [e.baseFin ?? 0, e.realFin ?? 0]));
  }, [datos, esCore, mundo]);

  if (error) return <p className="text-sm text-warn">{error}</p>;
  if (!datos) return <p className="text-dim">{t.calculando}</p>;
  if (!esCore && !mundo) return <p className="text-sm text-warn">{t.sinEspacio}</p>;

  const a = datos.analytics;
  // El núcleo pinta su capa; un mundo pinta la suya (universal + cumplimiento del
  // propio espacio, su cierre propio). Los hitos del mapa son del proyecto: un
  // mundo no los lleva (su avance vive en su cara "Tu avance").
  const u = esCore ? a.universal : mundo!.universal;
  const c = esCore ? a.cumplimiento : mundo!.cumplimiento;
  const nombre = esCore ? datos.nombre : nombreEspacio ?? datos.nombre;
  const tiene_baseline = esCore ? datos.tiene_baseline : c !== null;
  const realizadaAt = esCore ? datos.realizada_at ?? null : mundo!.completadoAt;
  const cierreMotivo = esCore ? datos.cierre_motivo ?? null : mundo!.cierreMotivo;
  // AUD-09 M04: el acta sale de la instantánea guardada al cerrar este espacio.
  // Si el cierre es de antes de la 040 (sin foto), no se inventa un acta: se
  // muestra el estado actual y se llama así.
  const acta = realizadaAt ? datos.actas?.[esCore ? "core" : (dominio as string)] ?? null : null;
  const hitos = esCore ? a.hitos : [];
  const nombreEtapa = (n: number) => titulos[n] ?? interpolar(tx.comun.etapaN, { n });

  return (
    <div className="flex flex-col gap-8">
      <button onClick={onVolver} className="self-start text-sm text-dim hover:text-ink">
        {t.volver}
      </button>

      {/* Fase 4.0 §8: el acta de cierre encabeza el análisis de un proyecto
          ya cerrado: estado final y el porqué, en la voz del usuario. */}
      {realizadaAt && acta && (
        <section className="rounded-panel border border-done/40 bg-surface p-5">
          <p className="text-[11px] font-semibold uppercase tracking-[1.2px] text-done">{t.actaDeCierre}</p>
          <p className="mt-2 text-[14px]">
            {rico(
              interpolar(t.actaCerrado, {
                fecha: fechaHumanaCorta(acta.cerrada_at, idioma),
                hechas: acta.instantanea.acciones.hechas,
                total: acta.instantanea.acciones.total,
              }),
              { b: (contenido) => <span className="font-semibold">{contenido}</span> }
            )}
          </p>
          {acta.cierre_motivo && (
            <blockquote className="mt-3 border-s-2 border-done/50 ps-3 text-[13.5px] leading-[1.65] text-dim [text-wrap:pretty]">
              {interpolar(t.cita, { motivo: acta.cierre_motivo })}
            </blockquote>
          )}
          {(acta.instantanea.acciones.hechas !== u.accionesVigente.hechas ||
            acta.instantanea.acciones.total !== u.accionesVigente.total) && (
            <p className="mt-3 text-[12.5px] text-dim">
              {interpolar(t.estadoActualLinea, { hechas: u.accionesVigente.hechas, total: u.accionesVigente.total })}
            </p>
          )}
        </section>
      )}
      {realizadaAt && !acta && (
        <section className="rounded-panel border border-done/40 bg-surface p-5">
          <p className="text-[11px] font-semibold uppercase tracking-[1.2px] text-done">{t.estadoActual}</p>
          <p className="mt-2 text-[14px]">
            {rico(
              interpolar(t.estadoCerrado, {
                fecha: fechaHumanaCorta(realizadaAt, idioma),
                hechas: u.accionesVigente.hechas,
                total: u.accionesVigente.total,
              }),
              { b: (contenido) => <span className="font-semibold">{contenido}</span> }
            )}
          </p>
          {cierreMotivo && (
            <blockquote className="mt-3 border-s-2 border-done/50 ps-3 text-[13.5px] leading-[1.65] text-dim [text-wrap:pretty]">
              {interpolar(t.cita, { motivo: cierreMotivo })}
            </blockquote>
          )}
        </section>
      )}

      <header className="flex flex-wrap items-center justify-between gap-4">
        <h2 className="text-2xl font-bold tracking-tight sm:text-[28px]">{interpolar(tx.comun.analisisDe, { nombre })}</h2>
        {/* La descarga del informe vive en "Tus documentos" (centralizado): aquí
            ya no hay botón propio. */}
      </header>

      {/* ── El análisis por CAPAS en acordeones: el usuario despliega lo que
          quiera ver. Cada capa es un reporte visual distinto. ── */}

      {/* Capa 1 — Tu viaje de un vistazo (abierta): avance + cifras + hitos. */}
      <Acordeon
        variante="capa"
        abierto
        titulo={
          <span className="flex items-center gap-2.5 text-[15px] font-semibold">
            <span aria-hidden className="h-2 w-2 rounded-full bg-accent" />
            {t.viajeDeUnVistazo}
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
            cerrada={Boolean(realizadaAt)}
          />
          <div>
            {/* Cifras en color (azul piensa): en blanco no lucían. Medida sin juicio. */}
            <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
              <Tile valor={String(u.duracionTotalDias)} etiqueta={t.diasDuracionTotal} color="var(--accent)" />
              <Tile valor={decimal(idioma, u.ritmoAccionesPorSemana, 1)} etiqueta={t.accionesPorSemana} color="var(--accent)" />
              <Tile valor={String(u.rachaMasLargaDias)} etiqueta={t.diasRacha} color="var(--accent)" />
              <Tile valor={`${u.ciclosDePlan} · ${u.mundos}`} etiqueta={tx.comun.ciclosMundos} color="var(--accent)" />
            </div>
            {u.retiradas.length > 0 && (
              <p className="mt-3 text-[13px] text-dim">
                {rico(interpolar(t.retiradas, { n: u.retiradas.length }), {
                  b: (contenido) => <span className="font-semibold text-ink">{contenido}</span>,
                })}
              </p>
            )}
          </div>
          {hitos.length > 0 && (
            <div className="rounded-panel border border-hairline bg-surface-3 p-5 sm:p-6">
              <MapaHitos
                cerrada={Boolean(realizadaAt)}
                hitos={hitos.map((h) => ({
                  fecha: h.fecha,
                  nombre: h.tipo === "realizada" ? t.realizado : h.etiqueta,
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
              {t.ritmoYEsfuerzo}
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
              {tx.comun.cumplisteFechas}
            </span>
          }
        >
          <div className="flex flex-col gap-5">
            <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
              <TileCumpl valor={String(c.adelantadas)} sufijo={`${c.pctAdelantadas}%`} etiqueta={tx.comun.adelantadas} color="var(--done)" />
              <TileCumpl valor={String(c.aTiempo)} sufijo={`${c.pctATiempo}%`} etiqueta={tx.comun.aTiempo} color="var(--accent)" />
              <TileCumpl valor={String(c.tardias)} sufijo={`${c.pctTardias}%`} etiqueta={tx.comun.tardias} color="var(--warn)" />
              <TileCumpl
                valor={`${c.desviacionMediaDias > 0 ? "+" : ""}${decimal(idioma, c.desviacionMediaDias, 1)}`}
                sufijo={t.dias}
                etiqueta={t.desviacionMedia}
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
                  {rico(
                    interpolar(t.frentePlanInicial, {
                      signo: c.desviacionVsInicialDias > 0 ? "+" : "",
                      dias: decimal(idioma, c.desviacionVsInicialDias, 1),
                      n: c.replanificaciones,
                      replanificaciones: plural(idioma, c.replanificaciones, t.replanificacion),
                    }),
                    { b: (contenido) => <span className="font-semibold text-ink tabular-nums">{contenido}</span> }
                  )}
                </p>
              </div>
            )}

            {c.porEtapa.length > 0 && (
              <GanttCumplimiento
                porEtapa={c.porEtapa}
                maxBarra={maxBarra}
                nombreEtapa={nombreEtapa}
                hoyDias={realizadaAt ? null : u.duracionTotalDias}
                /* P4: el carril SOLO en el Gantt del NÚCLEO. El análisis de un
                   mundo mide SU espacio; cruzarle el carril sería doble lectura. */
                carril={esCore ? a.carrilProteccion ?? [] : []}
                nombreMundo={(d) => nombreDeMundo(d, idioma)}
              />
            )}
          </div>
        </Acordeon>
      )}
    </div>
  );
}
