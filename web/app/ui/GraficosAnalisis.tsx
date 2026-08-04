"use client";

/**
 * GraficosAnalisis — los gráficos estadísticos del Análisis del proyecto, todos
 * DETERMINISTAS (de datos ya guardados; cero LLM) y pensados para que un fundador
 * los lea solo, sin jerga. Idioma de color de la casa: verde adelantada/ejecución,
 * azul a tiempo, ámbar tardía; gris lo que falta. Espejo, nunca juez.
 */
import { fechaHumanaCorta } from "@/lib/fechas";

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

/** La tile de una cifra (grande, centrada) con su etiqueta. Compartida por el
 * Análisis del proyecto (global) y las Estadísticas por espacio (Fase 3): la
 * misma vara visual mide el proyecto y cada espacio. */
export function Tile({ valor, etiqueta, color }: { valor: string; etiqueta: string; color?: string }) {
  return (
    <div className="flex flex-col items-center justify-center rounded-[14px] border border-hairline bg-surface-3 px-4 py-6 text-center">
      <p className="text-[38px] font-extrabold leading-none tracking-tight tabular-nums" style={color ? { color } : undefined}>
        {valor}
      </p>
      <p className="mt-2 text-[12px] text-dim [text-wrap:balance]">{etiqueta}</p>
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
      <Titulo nota="Cómo llegaste a cada fecha que te pusiste.">Reparto de tu cumplimiento</Titulo>
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
      <Titulo nota="Acciones que cerraste cada semana.">Tu ritmo, semana a semana</Titulo>
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

/** Avance acumulado: la curva de culminación. Suma semana a semana cuántas
 * acciones llevas cerradas sobre el total activo, así se ve cuánto del plan va
 * completado y a qué ritmo se acerca al 100 %. Un área verde que sube: registro
 * y control de avance, sin una sola palabra de más. */
export function AvanceAcumulado({ series, total }: { series: Array<{ semana: number; hechas: number }>; total: number }) {
  if (series.length === 0 || total === 0) return null;
  // Suma acumulada SIN reasignar durante el render (regla react-hooks/immutability):
  // cada punto suma lo suyo y lo previo. Series cortas (semanas): el costo no importa.
  const pts = series.map((s, i) => {
    const acc = series.slice(0, i + 1).reduce((sum, x) => sum + x.hechas, 0);
    return { semana: s.semana, pct: Math.min(100, (acc / total) * 100) };
  });
  const W = 640;
  const H = 210;
  const PL = 42;
  const PR = 16;
  const PT = 16;
  const PB = 30;
  const iw = W - PL - PR;
  const ih = H - PT - PB;
  const x = (i: number) => (pts.length === 1 ? PL + iw / 2 : PL + (i / (pts.length - 1)) * iw);
  const y = (p: number) => PT + (1 - p / 100) * ih;
  const linea = pts.map((p, i) => `${i === 0 ? "M" : "L"}${x(i).toFixed(1)} ${y(p.pct).toFixed(1)}`).join(" ");
  const area = `${linea} L${x(pts.length - 1).toFixed(1)} ${y(0).toFixed(1)} L${x(0).toFixed(1)} ${y(0).toFixed(1)} Z`;
  const finalPct = Math.round(pts[pts.length - 1].pct);
  return (
    <div className="rounded-panel border border-hairline bg-surface-3 p-5 sm:p-6">
      <div className="mb-4 flex items-baseline justify-between gap-3">
        <p className="text-[13px] font-semibold">Tu avance acumulado</p>
        <p className="text-[13px] tabular-nums" style={{ color: VERDE }}>
          <span className="text-[22px] font-extrabold leading-none">{finalPct}%</span> cerrado
        </p>
      </div>
      <svg viewBox={`0 0 ${W} ${H}`} width="100%" className="block" style={{ maxHeight: 220 }}>
        <defs>
          <linearGradient id="grad-acumulado" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor={VERDE} stopOpacity="0.34" />
            <stop offset="100%" stopColor={VERDE} stopOpacity="0.02" />
          </linearGradient>
        </defs>
        {[0, 25, 50, 75, 100].map((g) => (
          <g key={g}>
            <line x1={PL} x2={W - PR} y1={y(g)} y2={y(g)} stroke="rgba(255,255,255,0.07)" strokeWidth="1" />
            <text x={PL - 8} y={y(g) + 4} textAnchor="end" fontSize="11" fill="#6F7076" style={{ fontVariantNumeric: "tabular-nums" }}>
              {g}%
            </text>
          </g>
        ))}
        <path d={area} fill="url(#grad-acumulado)" />
        <path d={linea} fill="none" stroke={VERDE} strokeWidth="2.5" strokeLinejoin="round" strokeLinecap="round" />
        {pts.map((p, i) => (
          <circle key={i} cx={x(i)} cy={y(p.pct)} r={i === pts.length - 1 ? 5 : 2.5} fill={VERDE}>
            <title>{`Semana ${p.semana}: ${Math.round(p.pct)}% cerrado`}</title>
          </circle>
        ))}
        <text x={x(0)} y={H - 8} textAnchor="middle" fontSize="11" fill="#6F7076">
          S{pts[0].semana}
        </text>
        {pts.length > 1 && (
          <text x={x(pts.length - 1)} y={H - 8} textAnchor="middle" fontSize="11" fill="#6F7076">
            S{pts[pts.length - 1].semana}
          </text>
        )}
      </svg>
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
      <Titulo nota="Cuántas acciones tiene cada etapa y cuántas cerraste.">Dónde pusiste el esfuerzo</Titulo>
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

// ═══ Candidatos (a criba del fundador): proyección, cumplimiento por mundo en
//     barras y distribución de estados. Todos deterministas, cero LLM. ═══

/** Proyección de cierre: a tu ritmo actual, cuándo cerrarías lo que falta. Una
 * estimación honesta (se nombra como tal), no una promesa. Fecha grande + barra
 * de hecho (sólido) y resto (punteado). Se oculta si el proyecto ya se cerró o
 * si aún no hay ritmo para proyectar. */
export function ProyeccionCierre({
  hechas,
  total,
  ritmoPorSemana,
  cerrada,
}: {
  hechas: number;
  total: number;
  ritmoPorSemana: number;
  cerrada: boolean;
}) {
  if (cerrada || total === 0) return null;
  const restantes = total - hechas;
  if (restantes <= 0) return null; // ya está todo cerrado; la barra de avance lo dice
  const pctHecho = Math.round((hechas / total) * 100);
  const puede = ritmoPorSemana > 0;
  const semanasRest = puede ? Math.ceil(restantes / ritmoPorSemana) : 0;
  // Proyección "a tu ritmo, cuándo cerrarías": la fecha se estima DESDE HOY, así
  // que Date.now() aquí es intencional (una estimación de display, no un valor de
  // dominio). Cualquier forma de "capturar ahora" cae en otra regla (setState en
  // efecto); se exime la de pureza SOLO en esta línea.
  // eslint-disable-next-line react-hooks/purity
  const fechaCierre = puede ? fechaHumanaCorta(new Date(Date.now() + semanasRest * 7 * 86_400_000).toISOString()) : null;
  return (
    <div className="rounded-panel border border-hairline bg-surface-3 p-5 sm:p-6">
      <Titulo nota="A tu ritmo actual, cuándo cerrarías lo que falta. Es una estimación: si aceleras, se adelanta.">Proyección de cierre</Titulo>
      {puede ? (
        <>
          <p className="text-[26px] font-extrabold leading-none tracking-tight" style={{ color: VERDE }}>
            ~{fechaCierre}
          </p>
          <p className="mt-2 text-[13px] text-dim">
            Faltan <span className="font-semibold text-ink tabular-nums">{restantes}</span> {restantes === 1 ? "acción" : "acciones"} · a{" "}
            <span className="tabular-nums text-ink">{ritmoPorSemana}</span>/semana · ~
            <span className="tabular-nums text-ink">{semanasRest}</span> {semanasRest === 1 ? "semana" : "semanas"}
          </p>
          <div className="mt-4 flex h-3 w-full overflow-hidden rounded-full bg-white/[0.06]">
            <div style={{ width: `${pctHecho}%`, background: VERDE }} />
            <div className="flex-1" style={{ backgroundImage: "repeating-linear-gradient(45deg, rgba(63,185,80,0.30) 0 6px, transparent 6px 12px)" }} />
          </div>
        </>
      ) : (
        <p className="text-[13.5px] text-dim">Cuando cierres tu primera acción podremos estimar tu fecha de cierre.</p>
      )}
    </div>
  );
}

const LABEL_ESTADO: Record<string, string> = {
  hecho: "hecha",
  en_proceso: "en proceso",
  empezado: "apenas empezada",
  pendiente: "sin empezar",
};
/** Verde pleno = hecha; verdes cada vez más tenues = en proceso / empezada
 * (progresión, como los iconos de estado); gris = sin empezar (lo que falta). */
const COLOR_ESTADO: Record<string, string> = {
  hecho: "#3FB950",
  en_proceso: "rgba(63,185,80,0.62)",
  empezado: "rgba(63,185,80,0.34)",
  pendiente: "#4A4B52",
};

/** Distribución de estados: una barra apilada del estado actual de cada acción
 * activa (hecha → en proceso → empezada → sin empezar). El "cómo van" de un
 * vistazo, sin números en prosa. */
export function DistribucionEstados({ dist }: { dist: Array<{ estado: string; n: number }> }) {
  const total = dist.reduce((s, d) => s + d.n, 0);
  if (total === 0) return null;
  return (
    <div className="rounded-panel border border-hairline bg-surface-3 p-5 sm:p-6">
      <Titulo nota="En qué estado está cada acción activa ahora mismo.">Cómo van tus acciones</Titulo>
      <div className="flex h-4 w-full gap-[2px] overflow-hidden rounded-full">
        {dist.map((d) => (
          <div
            key={d.estado}
            title={`${LABEL_ESTADO[d.estado] ?? d.estado}: ${d.n}`}
            style={{ width: `${(d.n / total) * 100}%`, background: COLOR_ESTADO[d.estado] ?? "#4A4B52", minWidth: 3 }}
          />
        ))}
      </div>
      <div className="mt-4 flex flex-wrap items-center gap-x-4 gap-y-1.5 text-[12px]">
        {dist.map((d) => (
          <span key={d.estado} className="flex items-center gap-1.5 text-dim">
            <span className="h-2.5 w-2.5 rounded-[3px]" style={{ background: COLOR_ESTADO[d.estado] ?? "#4A4B52" }} />
            {LABEL_ESTADO[d.estado] ?? d.estado}
            <span className="font-semibold tabular-nums text-ink">{d.n}</span>
          </span>
        ))}
      </div>
    </div>
  );
}
