"use client";

/**
 * EstadisticasEspacio — campaña "Espacios", Fase 3 (tanda 2). Las estadísticas
 * de UN espacio dentro de su cara "Tu avance": la CAPA UNIVERSAL que
 * `analyticsDeMundo`/`calcularAnalytics` YA calcula (ritmo, racha, duración,
 * X de N, ritmo semanal y esfuerzo por etapa). Cero recálculo aquí: recibe la
 * `CapaUniversal` ya lista y REUSA los mismos tiles y gráficas del Análisis del
 * proyecto (misma vara mide el proyecto y cada espacio).
 *
 * Alcance deliberado (BANCO §7.1 enmendado): aquí va el progreso del ESPACIO. El
 * cumplimiento de fechas y el "core + N mundos, sin doble conteo" son métricas
 * del PROYECTO GLOBAL y viven en Análisis, no aquí. Los hitos ya los pinta la
 * LineaAvance arriba: esto es su lectura numérica, no los repite.
 */
import type { CapaUniversal } from "@/lib/analytics";
import { elegir } from "@/lib/i18n/config";
import { useIdioma } from "@/lib/i18n/IdiomaProvider";
import { decimal } from "@/lib/i18n/formato";
import { interpolar, plural } from "@/lib/i18n/interpolar";
import { rico } from "@/lib/i18n/rico";
import { ANALISIS } from "@/lib/i18n/mensajes/analisis";
import { BarraAvance } from "./BarraAvance";
import { DistribucionEstados, EsfuerzoPorEtapa, RitmoSemanal, Tile } from "./GraficosAnalisis";

export function EstadisticasEspacio({ universal, titulos }: { universal: CapaUniversal; titulos: Record<number, string> }) {
  const idioma = useIdioma();
  const tx = elegir(ANALISIS, idioma);
  const t = tx.estadisticas;
  const u = universal;
  const nombreEtapa = (n: number) => titulos[n] ?? interpolar(tx.comun.etapaN, { n });

  // Aún sin plan ni acciones: nada que medir todavía (mensaje sereno, sin ruido).
  if (u.accionesVigente.total === 0 && u.accionesHechas === 0) {
    return (
      <p className="text-[13px] leading-relaxed text-dim [text-wrap:pretty]">{t.sinDatos}</p>
    );
  }

  return (
    <div className="mt-6 flex flex-col gap-6">
      <p className="text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">{t.titulo}</p>

      {u.accionesVigente.total > 0 && (
        <div className="rounded-[16px] border border-hairline bg-surface px-5 py-[18px]">
          <BarraAvance pct={Math.round((u.accionesVigente.hechas / u.accionesVigente.total) * 100)} />
        </div>
      )}

      {/* Las cifras del espacio (azul piensa), misma tile que el Análisis. */}
      <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
        <Tile valor={String(u.duracionTotalDias)} etiqueta={t.diasDuracion} color="var(--accent)" />
        <Tile valor={decimal(idioma, u.ritmoAccionesPorSemana, 1)} etiqueta={t.accionesPorSemana} color="var(--accent)" />
        <Tile valor={String(u.rachaMasLargaDias)} etiqueta={t.diasRacha} color="var(--accent)" />
        <Tile valor={String(u.ciclosDePlan)} etiqueta={plural(idioma, u.ciclosDePlan, t.cicloDePlan)} color="var(--accent)" />
      </div>

      {u.retiradas.length > 0 && (
        <p className="text-[13px] text-dim">
          {rico(interpolar(t.retiradas, { n: u.retiradas.length }), {
            b: (c) => <span className="font-semibold text-ink">{c}</span>,
          })}
        </p>
      )}

      {u.accionesHechas > 0 && (
        <>
          <RitmoSemanal series={u.avancePorSemana} />
          <DistribucionEstados dist={u.distribucionEstados} />
        </>
      )}
      {u.accionesPorEtapa.length > 0 && <EsfuerzoPorEtapa series={u.accionesPorEtapa} nombreEtapa={nombreEtapa} />}
    </div>
  );
}
