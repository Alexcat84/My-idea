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

function Titulo({ children, nota }: { children: React.ReactNode; nota?: string }) {
  return (
    <div className="mb-4">
      <p className="text-[13px] font-semibold">{children}</p>
      {nota && <p className="mt-0.5 text-[12px] leading-relaxed text-dim [text-wrap:pretty]">{nota}</p>}
    </div>
  );
}

/** Reparto del cumplimiento: un gráfico CIRCULAR (dona) con los tres estados.
 * De todo lo que tenía fecha, qué parte fue adelantada / a tiempo / tardía. */
export function RepartoCumplimiento({ aTiempo, adelantadas, tardias }: { aTiempo: number; adelantadas: number; tardias: number }) {
  const total = aTiempo + adelantadas + tardias;
  if (total === 0) return null;
  const seg = [
    { n: adelantadas, color: VERDE, label: "adelantadas" },
    { n: aTiempo, color: AZUL, label: "a tiempo" },
    { n: tardias, color: AMBAR, label: "tardías" },
  ];
  const R = 46;
  const CIRC = 2 * Math.PI * R;
  const conValor = seg.filter((s) => s.n > 0);
  const gap = conValor.length > 1 ? 3 : 0; // hueco entre gajos (si hay más de uno)
  let offset = 0;
  return (
    <div className="rounded-panel border border-hairline bg-surface-3 p-5 sm:p-6">
      <Titulo nota="De todo lo que tenía fecha, cómo llegaste. El gajo más grande es tu tónica.">Reparto de tu cumplimiento</Titulo>
      <div className="flex flex-wrap items-center gap-x-8 gap-y-5">
        <svg width="128" height="128" viewBox="0 0 128 128" className="shrink-0">
          <g transform="rotate(-90 64 64)">
            {conValor.map((s, i) => {
              const largo = (s.n / total) * CIRC;
              const visible = Math.max(0, largo - gap);
              const el = (
                <circle
                  key={i}
                  cx="64"
                  cy="64"
                  r={R}
                  fill="none"
                  stroke={s.color}
                  strokeWidth="16"
                  strokeDasharray={`${visible} ${CIRC - visible}`}
                  strokeDashoffset={-offset}
                  strokeLinecap={conValor.length === 1 ? "butt" : "round"}
                />
              );
              offset += largo;
              return el;
            })}
          </g>
          <text x="64" y="60" textAnchor="middle" fontSize="26" fontWeight="800" fill="#F5F6F8" style={{ fontVariantNumeric: "tabular-nums" }}>
            {total}
          </text>
          <text x="64" y="79" textAnchor="middle" fontSize="10.5" fill="#6F7076">
            con fecha
          </text>
        </svg>
        <div className="flex flex-col gap-3">
          {seg.map((s, i) => (
            <div key={i} className="flex items-center gap-2.5 text-[13px]">
              <span className="h-3 w-3 shrink-0 rounded-[3px]" style={{ background: s.color }} />
              <span className="text-dim">{s.label}</span>
              <span className="font-semibold tabular-nums text-ink">{s.n}</span>
              <span className="tabular-nums text-dim">· {Math.round((s.n / total) * 100)}%</span>
            </div>
          ))}
        </div>
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

const NOMBRE_MES = [
  "enero", "febrero", "marzo", "abril", "mayo", "junio",
  "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre",
];
const DOW = ["L", "M", "X", "J", "V", "S", "D"];

/** Constancia: un CALENDARIO real (mes a mes), con el número de cada día y el
 * color por cuánto avanzaste ese día. Verde = avanzaste; gris tenue = pausaste.
 * Al pasar el cursor sobre un día se ve la fecha y cuántas acciones cerraste. */
export function Constancia({ dias }: { dias: Array<{ fecha: string; hechas: number }> }) {
  if (dias.length === 0) return null;
  const map = new Map(dias.map((d) => [d.fecha, d.hechas]));
  const maxH = Math.max(...dias.map((d) => d.hechas));
  const parse = (f: string) => new Date(`${f}T00:00:00Z`);
  const primero = parse(dias[0].fecha);
  const ultimo = parse(dias[dias.length - 1].fecha);

  // meses que abarca el viaje, del primero al último día con avance
  const meses: Array<{ y: number; m: number }> = [];
  let y = primero.getUTCFullYear();
  let m = primero.getUTCMonth();
  while (y < ultimo.getUTCFullYear() || (y === ultimo.getUTCFullYear() && m <= ultimo.getUTCMonth())) {
    meses.push({ y, m });
    if (++m > 11) {
      m = 0;
      y++;
    }
  }

  const nivel = (h: number) => (h === 0 ? 0 : Math.min(4, 1 + Math.floor((h / maxH) * 3.001)));
  const fondo = (n: number) => (n === 0 ? "rgba(255,255,255,0.04)" : `rgba(63,185,80,${[0, 0.28, 0.5, 0.72, 0.95][n]})`);
  const iso = (yy: number, mm: number, d: number) => `${yy}-${String(mm + 1).padStart(2, "0")}-${String(d).padStart(2, "0")}`;

  return (
    <div className="rounded-panel border border-hairline bg-surface-3 p-5 sm:p-6">
      <Titulo nota="Los días que avanzaste se pintan de verde (más oscuro = más acciones ese día); en gris, pausaste. Pasa el cursor por un día para ver el detalle.">
        Tu constancia
      </Titulo>
      <div className="flex flex-wrap gap-x-8 gap-y-6">
        {meses.map(({ y: yy, m: mm }) => {
          const primerDow = (new Date(Date.UTC(yy, mm, 1)).getUTCDay() + 6) % 7; // 0 = lunes
          const diasDelMes = new Date(Date.UTC(yy, mm + 1, 0)).getUTCDate();
          const celdas: Array<number | null> = [
            ...Array.from({ length: primerDow }, () => null),
            ...Array.from({ length: diasDelMes }, (_, i) => i + 1),
          ];
          return (
            <div key={`${yy}-${mm}`}>
              <div className="mb-2 text-[13px] font-semibold capitalize">
                {NOMBRE_MES[mm]} {yy}
              </div>
              <div className="grid grid-cols-7 gap-1">
                {DOW.map((d, i) => (
                  <span key={`h${i}`} className="text-center text-[10px] font-semibold text-dim">
                    {d}
                  </span>
                ))}
                {celdas.map((d, i) => {
                  if (d == null) return <span key={i} />;
                  const h = map.get(iso(yy, mm, d)) ?? 0;
                  const n = nivel(h);
                  return (
                    <span
                      key={i}
                      title={`${d} de ${NOMBRE_MES[mm]}: ${h} ${h === 1 ? "acción" : "acciones"}`}
                      className="grid h-8 w-8 place-items-center rounded-[7px] text-[11px] tabular-nums"
                      style={{ background: fondo(n), color: n >= 3 ? "#04240B" : n >= 1 ? "#E9F6EC" : "#6F7076" }}
                    >
                      {d}
                    </span>
                  );
                })}
              </div>
            </div>
          );
        })}
      </div>
      {/* leyenda de intensidad */}
      <div className="mt-5 flex items-center gap-2 text-[11px] text-dim">
        <span>menos</span>
        {[0, 1, 2, 3, 4].map((n) => (
          <span key={n} className="h-[13px] w-[13px] rounded-[3px]" style={{ background: fondo(n) }} />
        ))}
        <span>más</span>
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
