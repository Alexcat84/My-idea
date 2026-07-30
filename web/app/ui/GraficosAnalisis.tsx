"use client";

/**
 * GraficosAnalisis — los gráficos estadísticos del Análisis del proyecto, todos
 * DETERMINISTAS (de datos ya guardados; cero LLM) y pensados para que un fundador
 * los lea solo, sin jerga. Idioma de color de la casa: verde adelantada/ejecución,
 * azul a tiempo, ámbar tardía; gris lo que falta. Espejo, nunca juez.
 */
const VERDE = "#3FB950";
const AZUL = "#4D7CFE";
const AMBAR = "#E0A64A";
const MESES = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"];

function Titulo({ children, nota }: { children: React.ReactNode; nota?: string }) {
  return (
    <div className="mb-4">
      <p className="text-[13px] font-semibold">{children}</p>
      {nota && <p className="mt-0.5 text-[12px] leading-relaxed text-dim [text-wrap:pretty]">{nota}</p>}
    </div>
  );
}

/** Reparto del cumplimiento: una barra 100% con los tres estados. El más legible:
 * de todo lo que tenía fecha, qué parte fue adelantada / a tiempo / tardía. */
export function RepartoCumplimiento({ aTiempo, adelantadas, tardias }: { aTiempo: number; adelantadas: number; tardias: number }) {
  const total = aTiempo + adelantadas + tardias;
  if (total === 0) return null;
  const seg = [
    { n: adelantadas, color: VERDE, label: "adelantadas" },
    { n: aTiempo, color: AZUL, label: "a tiempo" },
    { n: tardias, color: AMBAR, label: "tardías" },
  ].filter((s) => s.n > 0);
  return (
    <div className="rounded-panel border border-hairline bg-surface-3 p-5 sm:p-6">
      <Titulo nota="De todo lo que tenía fecha, cómo llegaste. La mayor franja es tu tónica.">Reparto de tu cumplimiento</Titulo>
      <div className="flex h-4 w-full overflow-hidden rounded-full">
        {seg.map((s, i) => (
          <div key={i} style={{ width: `${(s.n / total) * 100}%`, background: s.color, marginLeft: i === 0 ? 0 : 2 }} />
        ))}
      </div>
      <div className="mt-4 flex flex-wrap gap-x-5 gap-y-2 text-[12.5px]">
        {seg.map((s, i) => (
          <span key={i} className="flex items-center gap-2 text-dim">
            <span className="h-2.5 w-2.5 rounded-full" style={{ background: s.color }} />
            {s.label} <span className="font-semibold tabular-nums text-ink">{s.n}</span>
            <span className="tabular-nums">· {Math.round((s.n / total) * 100)}%</span>
          </span>
        ))}
      </div>
    </div>
  );
}

/** Ritmo semana a semana: barras de acciones completadas por semana. Tus semanas
 * fuertes y las tranquilas, sin juicio. */
export function RitmoSemanal({ series }: { series: Array<{ semana: number; hechas: number }> }) {
  const max = Math.max(1, ...series.map((s) => s.hechas));
  if (series.length === 0) return null;
  return (
    <div className="rounded-panel border border-hairline bg-surface-3 p-5 sm:p-6">
      <Titulo nota="Cuántas acciones cerraste cada semana desde que empezaste.">Tu ritmo, semana a semana</Titulo>
      <div className="flex items-end gap-1.5 overflow-x-auto" style={{ height: 120 }}>
        {series.map((s) => (
          <div key={s.semana} className="flex min-w-[18px] flex-1 flex-col items-center gap-1.5" title={`Semana ${s.semana}: ${s.hechas}`}>
            <span className="text-[10px] tabular-nums text-dim">{s.hechas > 0 ? s.hechas : ""}</span>
            <div className="flex w-full items-end" style={{ height: 78 }}>
              <div
                className="w-full rounded-[3px]"
                style={{ height: `${(s.hechas / max) * 100}%`, minHeight: s.hechas > 0 ? 3 : 0, background: s.hechas > 0 ? VERDE : "rgba(255,255,255,0.06)" }}
              />
            </div>
            <span className="text-[10px] tabular-nums text-dim">S{s.semana}</span>
          </div>
        ))}
      </div>
    </div>
  );
}

/** Constancia: un calendario tipo mapa de calor. Los días con avance se pintan
 * (más verde = más ese día); los blancos son pausas. */
export function Constancia({ dias }: { dias: Array<{ fecha: string; hechas: number }> }) {
  if (dias.length === 0) return null;
  const parse = (f: string) => new Date(`${f}T00:00:00Z`);
  const primero = parse(dias[0].fecha);
  const ultimo = parse(dias[dias.length - 1].fecha).getTime();
  // arrancar el lunes de la primera semana
  const inicio = primero.getTime() - (((primero.getUTCDay() + 6) % 7) * 86_400_000);
  const map = new Map(dias.map((d) => [d.fecha, d.hechas]));
  const maxH = Math.max(...dias.map((d) => d.hechas));
  const celdas: Array<{ iso: string; h: number }> = [];
  for (let ms = inicio; ms <= ultimo; ms += 86_400_000) {
    const iso = new Date(ms).toISOString().slice(0, 10);
    celdas.push({ iso, h: map.get(iso) ?? 0 });
  }
  const semanas: Array<Array<{ iso: string; h: number }>> = [];
  for (let i = 0; i < celdas.length; i += 7) semanas.push(celdas.slice(i, i + 7));
  const color = (h: number) => (h === 0 ? "rgba(255,255,255,0.06)" : `rgba(63,185,80,${0.3 + 0.6 * (h / maxH)})`);
  const etiquetaMes = (semana: Array<{ iso: string; h: number }>) => {
    const d = parse(semana[0].iso);
    return d.getUTCDate() <= 7 ? MESES[d.getUTCMonth()] : "";
  };
  return (
    <div className="rounded-panel border border-hairline bg-surface-3 p-5 sm:p-6">
      <Titulo nota="Cada columna es una semana; cada cuadro, un día. Verde = avanzaste; en blanco, pausaste.">Tu constancia</Titulo>
      <div className="overflow-x-auto">
        <div className="flex gap-1">
          {semanas.map((semana, wi) => (
            <div key={wi} className="flex flex-col gap-1">
              {Array.from({ length: 7 }, (_, di) => {
                const c = semana[di];
                return (
                  <span
                    key={di}
                    className="h-[13px] w-[13px] rounded-[3px]"
                    style={{ background: c ? color(c.h) : "transparent" }}
                    title={c ? `${c.iso}: ${c.h}` : ""}
                  />
                );
              })}
              <span className="mt-0.5 h-3 text-[9px] text-dim">{etiquetaMes(semana)}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

/** Esfuerzo por etapa: barras de acciones activas por etapa (hechas sobre total).
 * Dónde pusiste tu trabajo. */
export function EsfuerzoPorEtapa({
  series,
  nombreEtapa,
}: {
  series: Array<{ etapa: number; total: number; hechas: number }>;
  nombreEtapa: (n: number) => string;
}) {
  const maxTotal = Math.max(1, ...series.map((s) => s.total));
  if (series.length === 0) return null;
  return (
    <div className="rounded-panel border border-hairline bg-surface-3 p-5 sm:p-6">
      <Titulo nota="Cuántas acciones tiene cada etapa y cuántas cerraste. Se ve dónde está el grueso del trabajo.">Dónde pusiste el esfuerzo</Titulo>
      <div className="flex flex-col gap-3.5">
        {series.map((s) => (
          <div key={s.etapa}>
            <div className="mb-1.5 flex items-baseline justify-between gap-3">
              <span className="min-w-0 truncate text-[13.5px]">
                <span className="mr-1.5 font-semibold text-accent tabular-nums">{s.etapa}</span>
                {nombreEtapa(s.etapa)}
              </span>
              <span className="shrink-0 text-[12.5px] tabular-nums text-dim">
                <span className="font-semibold text-ink">{s.hechas}</span> de {s.total}
              </span>
            </div>
            <div className="h-[9px] overflow-hidden rounded-full bg-white/[0.08]" style={{ width: `${(s.total / maxTotal) * 100}%`, minWidth: 40 }}>
              <div className="h-full rounded-full" style={{ width: `${s.total > 0 ? (s.hechas / s.total) * 100 : 0}%`, background: VERDE }} />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
