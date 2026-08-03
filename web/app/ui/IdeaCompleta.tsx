"use client";

/**
 * IdeaCompleta — el nivel GENERAL "La idea completa" (frente post-Fase 3). Un
 * nivel POR ENCIMA de los espacios: el agregado UNIFICADO de toda la idea (total,
 * ritmo, racha), que es la SUMA de la partición exacta (sin doble conteo). El
 * NÚCLEO va distinguido (no una card igual), con sus registros propios, pero
 * cuenta en el total. Cada mundo, su tarjeta. La timeline unificada y el
 * documento reusan la bitácora y el Expediente globales (decisión de gobierno).
 *
 * RUIDO CERO: esta pantalla solo tiene sentido con >=1 mundo; el control que
 * lleva aquí solo aparece entonces. Si se llega sin mundos (deep-link), degrada a
 * un aviso sereno hacia el núcleo.
 */
import { useEffect, useState } from "react";
import type { AgregadoIdea } from "@/lib/analytics";
import catalogo from "@/lib/assets/packs_catalog.json";
import { Tile } from "./GraficosAnalisis";

const PACKS = (catalogo as { packs: Array<{ clave: string; nombre: string; promesa: string }> }).packs;
const nombreDe = (d: string) => (d === "core" ? "Tu viaje" : PACKS.find((p) => p.clave === d)?.nombre ?? d);
const promesaDe = (d: string) => PACKS.find((p) => p.clave === d)?.promesa ?? "";
// color de cada mundo en el desglose (el núcleo es azul; los mundos rotan)
const COLORES = ["#3F9B8E", "#3FB950", "#B48EEA", "#E0A64A", "#4FB0C6", "#E06A9B"];

type Datos = { nombre: string; realizada_at: string | null; agregado: AgregadoIdea };

function Barra({ pct, color }: { pct: number; color: string }) {
  return (
    <div className="mt-2 h-2 overflow-hidden rounded-full bg-surface-2">
      <div className="h-full rounded-full" style={{ width: `${pct}%`, background: color }} />
    </div>
  );
}

export function IdeaCompleta({
  projectId,
  onIrNucleo,
  onIrMundo,
  onIrBitacora,
  onIrDocumentos,
}: {
  projectId: string;
  onIrNucleo: () => void;
  onIrMundo: (dominio: string) => void;
  onIrBitacora: () => void;
  onIrDocumentos: () => void;
}) {
  const [datos, setDatos] = useState<Datos | null>(null);
  const [error, setError] = useState(false);

  useEffect(() => {
    let vivo = true;
    fetch(`/api/project/${projectId}/analisis`)
      .then((r) => (r.ok ? r.json() : Promise.reject(new Error(String(r.status)))))
      .then((d: Datos) => vivo && setDatos(d))
      .catch(() => vivo && setError(true));
    return () => {
      vivo = false;
    };
  }, [projectId]);

  if (error) return <p className="text-sm text-warn">No pudimos cargar la vista de tu idea completa.</p>;
  if (!datos) return <p className="text-dim">Uniendo toda tu idea…</p>;

  const { nombre, agregado: a } = datos;
  const nucleo = a.espacios.find((e) => e.nucleo) ?? a.espacios[0];
  const mundos = a.espacios.filter((e) => !e.nucleo);
  const pct = (h: number, t: number) => (t > 0 ? Math.round((h / t) * 100) : 0);

  // Ruido cero (deep-link sin mundos): esta vista nace con el primer mundo.
  if (mundos.length === 0) {
    return (
      <div className="anima-plan-in">
        <p className="text-[13px] leading-relaxed text-dim [text-wrap:pretty]">
          Esta vista une toda tu idea, y aparece cuando abres tu primer mundo. Por ahora tu idea es tu núcleo.
        </p>
        <button onClick={onIrNucleo} className="mt-3 text-[13px] font-semibold text-accent hover:underline">
          Ir a tu viaje →
        </button>
      </div>
    );
  }

  return (
    <div className="anima-plan-in flex flex-col gap-6">
      <div>
        <p className="text-[11px] font-semibold uppercase tracking-[1.4px] text-done">La idea completa</p>
        <h2 className="mt-1 text-2xl font-bold tracking-tight sm:text-[28px]">{nombre}</h2>
        <p className="mt-2 text-[14px] text-dim [text-wrap:pretty]">
          Todo junto: tu núcleo y {mundos.length === 1 ? "tu mundo" : `tus ${mundos.length} mundos`}, con las métricas
          generales de la idea.
        </p>
      </div>

      {/* LO GENERAL / COMPARTIDO: el agregado, suma sin doble conteo. */}
      <section className="rounded-panel border border-hairline bg-surface-3 p-5 sm:p-6">
        <p className="mb-4 text-[11px] font-semibold uppercase tracking-[1.2px] text-accent">Lo general · toda la idea</p>
        <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
          <Tile valor={`${a.total.hechas} / ${a.total.total}`} etiqueta="acciones de toda la idea" color="var(--accent)" />
          <Tile valor={a.ritmoUnificado.toFixed(1)} etiqueta="ritmo unificado (acc/sem)" color="var(--accent)" />
          <Tile valor={String(a.rachaUnificadaDias)} etiqueta="días de racha (toda la idea)" color="var(--accent)" />
          <Tile valor={String(a.espacios.length)} etiqueta="espacios (núcleo + mundos)" color="var(--accent)" />
        </div>
      </section>

      {/* EL NÚCLEO: distinguido, con sus registros propios; cuenta en el total. */}
      <button
        onClick={onIrNucleo}
        className="flex flex-col gap-2 rounded-panel border border-accent/30 border-l-[3px] border-l-accent bg-accent/[0.06] p-5 text-left transition-colors hover:bg-accent/[0.1]"
      >
        <div className="flex flex-wrap items-center gap-3">
          <span className="rounded-full bg-accent px-2.5 py-0.5 text-[10px] font-extrabold uppercase tracking-[0.8px] text-[#04102C]">
            Núcleo
          </span>
          <span className="text-[16px] font-bold">Tu viaje</span>
          <span className="text-[13px] font-semibold tabular-nums text-dim">
            {nucleo.hechas} de {nucleo.total}
            {nucleo.cerrado ? " · realizada" : " · en marcha"}
          </span>
          <span className="ml-auto text-[12.5px] font-semibold text-accent">Ir al núcleo →</span>
        </div>
        <Barra pct={pct(nucleo.hechas, nucleo.total)} color="var(--accent)" />
        <p className="text-[11.5px] text-dim">El corazón de la idea, con sus registros propios: plan, manos a la obra, avance y bitácora.</p>
      </button>

      {/* LOS MUNDOS: cada uno su tarjeta. */}
      <div className="grid grid-cols-1 gap-3 sm:grid-cols-2">
        {mundos.map((m, i) => {
          const color = COLORES[i % COLORES.length];
          return (
            <button
              key={m.dominio}
              onClick={() => onIrMundo(m.dominio)}
              className="flex flex-col gap-1.5 rounded-panel border border-hairline bg-surface p-5 text-left transition-colors hover:border-accent/[0.34]"
            >
              <div className="flex items-center gap-2">
                <span aria-hidden className="h-2.5 w-2.5 rounded-full" style={{ background: color }} />
                <span className="text-[15px] font-bold">{nombreDe(m.dominio)}</span>
                <span className="ml-auto text-[12.5px] font-semibold text-accent">Ir →</span>
              </div>
              {promesaDe(m.dominio) && <p className="text-[12.5px] leading-snug text-dim [text-wrap:pretty]">{promesaDe(m.dominio)}</p>}
              <span className="text-[12.5px] font-semibold tabular-nums text-dim">
                {m.hechas} de {m.total}
                {m.cerrado ? " · " : ""}
                {m.cerrado && <span className="font-bold text-done">cerrado</span>}
              </span>
              <Barra pct={pct(m.hechas, m.total)} color={color} />
            </button>
          );
        })}
      </div>

      {/* LO UNIFICADO EN UN SOLO LUGAR (reusa la bitácora y el Expediente globales). */}
      <section className="rounded-panel border border-hairline bg-surface p-5">
        <p className="text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">Toda la idea, unificada</p>
        <div className="mt-3 flex flex-wrap gap-3">
          <button onClick={onIrBitacora} className="rounded-[10px] border border-hairline px-4 py-2 text-[13px] font-semibold text-ink hover:border-accent/40">
            Ver la historia completa
          </button>
          <button onClick={onIrDocumentos} className="rounded-[10px] border border-hairline px-4 py-2 text-[13px] font-semibold text-ink hover:border-accent/40">
            Ver el expediente y el análisis
          </button>
        </div>
        <p className="mt-4 text-[12px] leading-relaxed text-dim [text-wrap:pretty]">
          Cada espacio conserva sus registros propios; esto de arriba es lo general: el agregado de toda tu idea, que es la
          <b className="text-ink"> suma de todos los espacios sin contar nada dos veces</b>. El núcleo no es un mundo más: es
          el corazón, pero también cuenta en el total.
        </p>
      </section>
    </div>
  );
}
