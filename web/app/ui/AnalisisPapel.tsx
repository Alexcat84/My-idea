"use client";

/**
 * AnalisisPapel — el Análisis del proyecto llevado a papel, VISUAL (Fase 4.6.1).
 * Antes el PDF de Análisis solo traía la página "Cómo te fue" (resumen) y no
 * mostraba ningún gráfico; el fundador lo quiere con TODA la estadística nueva y
 * bien visual. Aquí se dibujan, en tokens de PAPEL (tinta oscura sobre blanco),
 * las mismas piezas que la pantalla: avance, avance acumulado, cómo van las
 * acciones, ritmo, esfuerzo, proyección de cierre y, con línea base, el
 * cumplimiento. Todo determinista (de analytics), cero LLM.
 *
 * El pie va en el <tfoot> de HojaImpresion (se repite y reserva su alto).
 */
import { useState } from "react";
import { HojaImpresion, FilaPapel } from "./HojaImpresion";

const AZUL = "#3B6BE8";
const VERDE = "#1F8A34";
const AMBAR = "#96690C";
const BASE_BORDE = "#B9BDC6";
const BASE_FONDO = "#EAECF0";
const TINTA = "#16171A";
const SEC = "#4B4E55";
const TER = "#6B6E75";
const HILO = "#E4E7EC";
const CARD = "#FAFBFC";

export interface AnalisisPapelData {
  cerrada: boolean;
  avance: { hechas: number; total: number };
  cifras: { dias: number; ritmo: number; racha: number; ciclos: number; mundos: number };
  retiradas: number;
  avancePorSemana: Array<{ semana: number; hechas: number }>;
  distribucionEstados: Array<{ estado: string; n: number }>;
  accionesPorEtapa: Array<{ etapa: number; total: number; hechas: number }>;
  proyeccion: { restantes: number; semanas: number; fechaHumana: string; ritmo: number } | null;
  cumplimiento: null | {
    adelantadas: number;
    aTiempo: number;
    tardias: number;
    pctAdelantadas: number;
    pctATiempo: number;
    pctTardias: number;
    desviacionMediaDias: number;
    porDominio: Array<{ nombre: string; adelantadas: number; aTiempo: number; tardias: number; completado: boolean }>;
    /** Barras "plan vs real" por etapa para el Gantt (días desde la chispa). */
    porEtapa: Array<{ etapa: number; baseInicio: number; baseFin: number | null; realInicio: number | null; realFin: number | null }>;
  };
}

type EstadoEtapa = "adelantada" | "aTiempo" | "tarde" | null;
const COLOR_ETAPA: Record<"adelantada" | "aTiempo" | "tarde", string> = { adelantada: VERDE, aTiempo: AZUL, tarde: AMBAR };

const LABEL_ESTADO: Record<string, string> = {
  hecho: "hecha",
  en_proceso: "en proceso",
  empezado: "apenas empezada",
  pendiente: "sin empezar",
};
const COLOR_ESTADO: Record<string, string> = {
  hecho: VERDE,
  en_proceso: "rgba(31,138,52,0.60)",
  empezado: "rgba(31,138,52,0.32)",
  pendiente: "#C7CAD0",
};

function Tarjeta({ titulo, nota, children }: { titulo: string; nota?: string; children: React.ReactNode }) {
  return (
    <div style={{ border: `1px solid ${HILO}`, background: CARD, borderRadius: 12, padding: "18px 20px", breakInside: "avoid", marginTop: 14 }}>
      <div style={{ fontSize: 13, fontWeight: 700, color: TINTA }}>{titulo}</div>
      {nota && <div style={{ fontSize: 11.5, color: TER, marginTop: 3, lineHeight: 1.5 }}>{nota}</div>}
      <div style={{ marginTop: 14 }}>{children}</div>
    </div>
  );
}

function Chip({ color, texto }: { color: string; texto: string }) {
  return (
    <span style={{ display: "inline-flex", alignItems: "center", gap: 6, fontSize: 11.5, color: TER }}>
      <span style={{ width: 10, height: 10, borderRadius: 3, background: color }} />
      {texto}
    </span>
  );
}

/** Barra de avance: % + relleno + escala 25/50/75/100. */
function BarraAvance({ pct }: { pct: number }) {
  return (
    <div>
      <div style={{ display: "flex", alignItems: "baseline", gap: 8, marginBottom: 8 }}>
        <span style={{ fontSize: 30, fontWeight: 800, letterSpacing: "-1px", color: VERDE, fontVariantNumeric: "tabular-nums" }}>{pct}%</span>
        <span style={{ fontSize: 12.5, color: TER }}>de tus acciones, cerradas</span>
      </div>
      <div style={{ position: "relative", height: 12, borderRadius: 999, background: "#EDEFF3", overflow: "hidden" }}>
        <div style={{ width: `${pct}%`, height: "100%", borderRadius: 999, background: `linear-gradient(to right, ${AZUL}, ${VERDE})` }} />
      </div>
      <div style={{ display: "flex", justifyContent: "space-between", marginTop: 5, fontSize: 10, color: "#9A9DA4", fontVariantNumeric: "tabular-nums" }}>
        <span>0</span><span>25</span><span>50</span><span>75</span><span>100</span>
      </div>
    </div>
  );
}

/** Curva de avance acumulado (área). */
function AvanceAcumulado({ series, total }: { series: Array<{ semana: number; hechas: number }>; total: number }) {
  if (series.length === 0 || total === 0) return null;
  let acc = 0;
  const pts = series.map((s) => {
    acc += s.hechas;
    return { semana: s.semana, pct: Math.min(100, (acc / total) * 100) };
  });
  const W = 540, H = 180, PL = 34, PR = 10, PT = 12, PB = 24;
  const iw = W - PL - PR, ih = H - PT - PB;
  const x = (i: number) => (pts.length === 1 ? PL + iw / 2 : PL + (i / (pts.length - 1)) * iw);
  const y = (p: number) => PT + (1 - p / 100) * ih;
  const linea = pts.map((p, i) => `${i === 0 ? "M" : "L"}${x(i).toFixed(1)} ${y(p.pct).toFixed(1)}`).join(" ");
  const area = `${linea} L${x(pts.length - 1).toFixed(1)} ${y(0).toFixed(1)} L${x(0).toFixed(1)} ${y(0).toFixed(1)} Z`;
  return (
    <svg viewBox={`0 0 ${W} ${H}`} width="100%" style={{ display: "block" }}>
      <defs>
        <linearGradient id="acum-papel" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stopColor={VERDE} stopOpacity="0.24" />
          <stop offset="100%" stopColor={VERDE} stopOpacity="0.02" />
        </linearGradient>
      </defs>
      {[0, 25, 50, 75, 100].map((g) => (
        <g key={g}>
          <line x1={PL} x2={W - PR} y1={y(g)} y2={y(g)} stroke="#EAECF0" strokeWidth="1" />
          <text x={PL - 6} y={y(g) + 3.5} textAnchor="end" fontSize="10" fill="#9A9DA4">{g}%</text>
        </g>
      ))}
      <path d={area} fill="url(#acum-papel)" />
      <path d={linea} fill="none" stroke={VERDE} strokeWidth="2.4" strokeLinejoin="round" strokeLinecap="round" />
      {pts.map((p, i) => (
        <circle key={i} cx={x(i)} cy={y(p.pct)} r={i === pts.length - 1 ? 4.5 : 2.4} fill={VERDE} />
      ))}
      <text x={x(0)} y={H - 6} textAnchor="middle" fontSize="10" fill="#9A9DA4">S{pts[0].semana}</text>
      {pts.length > 1 && <text x={x(pts.length - 1)} y={H - 6} textAnchor="middle" fontSize="10" fill="#9A9DA4">S{pts[pts.length - 1].semana}</text>}
    </svg>
  );
}

/** Distribución de estados: barra apilada + leyenda. */
function Distribucion({ dist }: { dist: Array<{ estado: string; n: number }> }) {
  const total = dist.reduce((s, d) => s + d.n, 0);
  if (total === 0) return null;
  return (
    <div>
      <div style={{ display: "flex", gap: 2, height: 16, borderRadius: 999, overflow: "hidden" }}>
        {dist.map((d) => (
          <div key={d.estado} style={{ width: `${(d.n / total) * 100}%`, minWidth: 3, background: COLOR_ESTADO[d.estado] ?? "#C7CAD0" }} />
        ))}
      </div>
      <div style={{ display: "flex", flexWrap: "wrap", gap: "6px 16px", marginTop: 14 }}>
        {dist.map((d) => (
          <span key={d.estado} style={{ display: "inline-flex", alignItems: "center", gap: 6, fontSize: 12, color: TER }}>
            <span style={{ width: 10, height: 10, borderRadius: 3, background: COLOR_ESTADO[d.estado] ?? "#C7CAD0" }} />
            {LABEL_ESTADO[d.estado] ?? d.estado} <b style={{ color: TINTA, fontVariantNumeric: "tabular-nums" }}>{d.n}</b>
          </span>
        ))}
      </div>
    </div>
  );
}

/** Barras de una serie (ritmo semanal). */
function RitmoSemanal({ series }: { series: Array<{ semana: number; hechas: number }> }) {
  const max = Math.max(1, ...series.map((s) => s.hechas));
  if (series.length === 0) return null;
  return (
    <div style={{ display: "flex", alignItems: "flex-end", gap: 6, height: 110 }}>
      {series.map((s) => (
        <div key={s.semana} style={{ flex: 1, minWidth: 14, display: "flex", flexDirection: "column", alignItems: "center", gap: 5 }}>
          <span style={{ fontSize: 10, color: TER, fontVariantNumeric: "tabular-nums" }}>{s.hechas > 0 ? s.hechas : ""}</span>
          <div style={{ width: "100%", height: 72, display: "flex", alignItems: "flex-end" }}>
            <div style={{ width: "100%", height: `${(s.hechas / max) * 100}%`, minHeight: s.hechas > 0 ? 3 : 0, borderRadius: 3, background: s.hechas > 0 ? VERDE : "#EDEFF3" }} />
          </div>
          <span style={{ fontSize: 10, color: TER, fontVariantNumeric: "tabular-nums" }}>S{s.semana}</span>
        </div>
      ))}
    </div>
  );
}

/** Esfuerzo por etapa: barras hechas/total. */
function Esfuerzo({ series }: { series: Array<{ etapa: number; total: number; hechas: number }> }) {
  const maxTotal = Math.max(1, ...series.map((s) => s.total));
  if (series.length === 0) return null;
  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
      {series.map((s) => (
        <div key={s.etapa}>
          <div style={{ display: "flex", justifyContent: "space-between", fontSize: 12.5, marginBottom: 5 }}>
            <span><b style={{ color: AZUL }}>{s.etapa}</b> <span style={{ color: TINTA }}>Etapa {s.etapa}</span></span>
            <span style={{ color: TER, fontVariantNumeric: "tabular-nums" }}><b style={{ color: TINTA }}>{s.hechas}</b> de {s.total}</span>
          </div>
          <div style={{ height: 9, borderRadius: 999, background: "#EDEFF3", width: `${(s.total / maxTotal) * 100}%`, minWidth: 40, overflow: "hidden" }}>
            <div style={{ height: "100%", borderRadius: 999, width: `${s.total > 0 ? (s.hechas / s.total) * 100 : 0}%`, background: VERDE }} />
          </div>
        </div>
      ))}
    </div>
  );
}

/** Barra apilada de cumplimiento por mundo. */
function PorMundo({ filas }: { filas: AnalisisPapelData["cumplimiento"] extends null ? never : NonNullable<AnalisisPapelData["cumplimiento"]>["porDominio"] }) {
  if (filas.length === 0) return null;
  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
      {filas.map((f) => {
        const total = f.adelantadas + f.aTiempo + f.tardias;
        if (total === 0) return null;
        const seg = [
          { n: f.adelantadas, c: VERDE },
          { n: f.aTiempo, c: AZUL },
          { n: f.tardias, c: AMBAR },
        ].filter((s) => s.n > 0);
        return (
          <div key={f.nombre}>
            <div style={{ display: "flex", justifyContent: "space-between", fontSize: 12.5, marginBottom: 5 }}>
              <span style={{ color: TINTA }}>
                {f.nombre}
                {f.completado && <span style={{ color: VERDE, fontWeight: 600, fontSize: 11, marginLeft: 8 }}>Completado</span>}
              </span>
              <span style={{ color: TER, fontVariantNumeric: "tabular-nums" }}>{total}</span>
            </div>
            <div style={{ display: "flex", gap: 2, height: 12, borderRadius: 999, background: "#EDEFF3", overflow: "hidden" }}>
              {seg.map((s, i) => (
                <div key={i} style={{ width: `${(s.n / total) * 100}%`, minWidth: 3, background: s.c }} />
              ))}
            </div>
          </div>
        );
      })}
    </div>
  );
}

function CifraTile({ valor, etiqueta, color }: { valor: string; etiqueta: string; color?: string }) {
  return (
    <div style={{ flex: 1, textAlign: "center", padding: "16px 6px", border: `1px solid ${HILO}`, borderRadius: 10, background: "#fff" }}>
      <div style={{ fontSize: 26, fontWeight: 800, letterSpacing: "-0.6px", color: color ?? TINTA, fontVariantNumeric: "tabular-nums" }}>{valor}</div>
      <div style={{ fontSize: 11, color: TER, marginTop: 4, lineHeight: 1.3 }}>{etiqueta}</div>
    </div>
  );
}

/** Reparto de cumplimiento: gráfico CIRCULAR (dona) con los tres estados. */
function RepartoDonut({ adelantadas, aTiempo, tardias }: { adelantadas: number; aTiempo: number; tardias: number }) {
  const total = adelantadas + aTiempo + tardias;
  if (total === 0) return null;
  const seg = [
    { n: adelantadas, c: VERDE, l: "adelantadas" },
    { n: aTiempo, c: AZUL, l: "a tiempo" },
    { n: tardias, c: AMBAR, l: "tardías" },
  ];
  const R = 46;
  const CIRC = 2 * Math.PI * R;
  const conValor = seg.filter((s) => s.n > 0);
  const gap = conValor.length > 1 ? 3 : 0;
  let offset = 0;
  return (
    <div style={{ display: "flex", flexWrap: "wrap", alignItems: "center", gap: "18px 30px" }}>
      <svg width="116" height="116" viewBox="0 0 128 128" style={{ flexShrink: 0 }}>
        <g transform="rotate(-90 64 64)">
          {conValor.map((s, i) => {
            const largo = (s.n / total) * CIRC;
            const visible = Math.max(0, largo - gap);
            const el = (
              <circle key={i} cx="64" cy="64" r={R} fill="none" stroke={s.c} strokeWidth="16" strokeDasharray={`${visible} ${CIRC - visible}`} strokeDashoffset={-offset} strokeLinecap={conValor.length === 1 ? "butt" : "round"} />
            );
            offset += largo;
            return el;
          })}
        </g>
        <text x="64" y="60" textAnchor="middle" fontSize="26" fontWeight="800" fill={TINTA} style={{ fontVariantNumeric: "tabular-nums" }}>{total}</text>
        <text x="64" y="79" textAnchor="middle" fontSize="10.5" fill={TER}>con fecha</text>
      </svg>
      <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
        {seg.map((s, i) => (
          <div key={i} style={{ display: "flex", alignItems: "center", gap: 9, fontSize: 13 }}>
            <span style={{ width: 12, height: 12, borderRadius: 3, background: s.c }} />
            <span style={{ color: TER }}>{s.l}</span>
            <b style={{ color: TINTA, fontVariantNumeric: "tabular-nums" }}>{s.n}</b>
            <span style={{ color: TER, fontVariantNumeric: "tabular-nums" }}>· {Math.round((s.n / total) * 100)}%</span>
          </div>
        ))}
      </div>
    </div>
  );
}

/** Gantt "Cómo se movió tu camino" en papel. Respeta la vista que el usuario
 * dejó elegida en pantalla (localStorage `mi-idea:gantt-vista`): "Bandas" =
 * dos cintas apiladas; el resto (Plan y real / Escalonado) = carriles. La lee
 * de forma SÍNCRONA en el primer render (window.print dispara enseguida). */
function GanttPapel({
  porEtapa,
  dias,
  cerrada,
}: {
  porEtapa: NonNullable<AnalisisPapelData["cumplimiento"]>["porEtapa"];
  dias: number;
  cerrada: boolean;
}) {
  const [vista] = useState<"riel" | "escalera" | "cintas">(() => {
    try {
      const v = typeof localStorage !== "undefined" ? localStorage.getItem("mi-idea:gantt-vista") : null;
      return v === "cintas" || v === "escalera" || v === "riel" ? v : "riel";
    } catch {
      return "riel";
    }
  });
  if (porEtapa.length === 0) return null;
  const escala = Math.max(1, ...porEtapa.flatMap((e) => [e.baseFin ?? 0, e.realFin ?? 0]));
  const pct = (d: number) => (d / escala) * 100;
  const filas = porEtapa.map((e, i) => {
    const tieneReal = e.realFin != null && e.realInicio != null;
    const estado: EstadoEtapa =
      !tieneReal || e.baseFin == null ? null : e.realFin! > e.baseFin + 1 ? "tarde" : e.realFin! < e.baseFin - 1 ? "adelantada" : "aTiempo";
    return {
      n: i + 1,
      base: e.baseFin != null ? { l: pct(e.baseInicio), w: pct(Math.max(0, e.baseFin - e.baseInicio)) } : null,
      real: tieneReal ? { l: pct(e.realInicio!), w: pct(Math.max(0, e.realFin! - e.realInicio!)) } : null,
      planDias: e.baseFin != null ? Math.round(e.baseFin - e.baseInicio) : null,
      realDias: tieneReal ? Math.round(e.realFin! - e.realInicio!) : null,
      estado,
    };
  });
  const ticks = [0, 0.25, 0.5, 0.75, 1].map((f) => Math.round(f * escala));
  const cReal = (est: EstadoEtapa) => (est ? COLOR_ETAPA[est] : VERDE);
  const esCintas = vista === "cintas";
  return (
    <Tarjeta titulo="Cómo se movió tu camino" nota="En gris claro, la línea base que sellaste. Encima, los días que ocupaste de verdad.">
      <div style={{ display: "flex", flexWrap: "wrap", gap: "6px 16px", marginBottom: 14, fontSize: 11.5, color: TER, alignItems: "center" }}>
        <span style={{ display: "inline-flex", alignItems: "center", gap: 6 }}>
          <span style={{ width: 18, height: 11, borderRadius: 5, border: `1px solid ${BASE_BORDE}`, background: BASE_FONDO }} />
          línea base
        </span>
        <Chip color={VERDE} texto="adelantada" />
        <Chip color={AZUL} texto="a tiempo" />
        <Chip color={AMBAR} texto="tardía" />
      </div>
      {esCintas ? (
        <div>
          <div style={{ position: "relative", height: 30, marginBottom: 16 }}>
            {filas.map((f) =>
              f.base ? (
                <div key={f.n} style={{ position: "absolute", left: `${f.base.l}%`, width: `${f.base.w}%`, top: 0, height: 30, borderRadius: 7, border: `1px solid ${BASE_BORDE}`, background: BASE_FONDO, color: "#5C5E66", display: "flex", alignItems: "center", justifyContent: "center", fontSize: 11.5, fontWeight: 700 }}>{f.n}</div>
              ) : null
            )}
          </div>
          <div style={{ position: "relative", height: 30 }}>
            {filas.map((f) =>
              f.real ? (
                <div key={f.n} style={{ position: "absolute", left: `${f.real.l}%`, width: `${f.real.w}%`, top: 0, height: 30, borderRadius: 7, background: cReal(f.estado), color: "#fff", display: "flex", alignItems: "center", justifyContent: "center", fontSize: 11.5, fontWeight: 700 }}>{f.n}</div>
              ) : null
            )}
          </div>
        </div>
      ) : (
        <div style={{ display: "flex", flexDirection: "column" }}>
          {filas.map((f) => (
            <div key={f.n} style={{ display: "grid", gridTemplateColumns: "18px 1fr 84px", gap: 12, alignItems: "center", padding: "8px 0", borderBottom: `1px solid ${HILO}` }}>
              <span style={{ fontSize: 11.5, fontWeight: 700, color: AZUL, textAlign: "right", fontVariantNumeric: "tabular-nums" }}>{f.n}</span>
              <div style={{ position: "relative", height: 20 }}>
                <div style={{ position: "absolute", top: "50%", left: 0, right: 0, height: 1, transform: "translateY(-50%)", background: HILO }} />
                {f.base && <div style={{ position: "absolute", top: "50%", transform: "translateY(-50%)", left: `${f.base.l}%`, width: `${f.base.w}%`, height: 15, borderRadius: 7, border: `1px solid ${BASE_BORDE}`, background: BASE_FONDO }} />}
                {f.real && <div style={{ position: "absolute", top: "50%", transform: "translateY(-50%)", left: `${f.real.l}%`, width: `${f.real.w}%`, height: 6, borderRadius: 3, background: cReal(f.estado) }} />}
              </div>
              <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 8, fontSize: 11.5, textAlign: "right", fontVariantNumeric: "tabular-nums" }}>
                <span style={{ color: TER }}>{f.planDias != null ? `${f.planDias}d` : "—"}</span>
                <span style={{ color: cReal(f.estado), fontWeight: 600 }}>{f.realDias != null ? `${f.realDias}d` : "en curso"}</span>
              </div>
            </div>
          ))}
        </div>
      )}
      <div style={{ display: "flex", justifyContent: "space-between", fontSize: 10.5, color: TER, fontVariantNumeric: "tabular-nums", marginTop: 10, paddingLeft: esCintas ? 0 : 30, paddingRight: esCintas ? 0 : 96 }}>
        {ticks.map((t, i) => (
          <span key={i}>{i === 0 ? `día ${t}` : t}</span>
        ))}
      </div>
    </Tarjeta>
  );
}

/** El CONTENIDO del análisis (sin andamio). */
export function ContenidoAnalisis({ nombre, datos }: { nombre: string; datos: AnalisisPapelData }) {
  const { avance, cifras, cumplimiento: c } = datos;
  const pct = avance.total > 0 ? Math.round((avance.hechas / avance.total) * 100) : 0;
  return (
    <div data-cuerpo-papel>
      <div style={{ fontSize: 11, fontWeight: 700, letterSpacing: "1.6px", textTransform: "uppercase", color: AZUL }}>Análisis del proyecto</div>
      <h3 style={{ margin: "18px 0 0", fontFamily: "Georgia, 'Times New Roman', serif", fontSize: 28, fontWeight: 700, letterSpacing: "-0.4px", color: TINTA }}>
        Análisis de {nombre}
      </h3>
      <p style={{ margin: "10px 0 0", fontSize: 14, lineHeight: 1.6, color: SEC }}>
        Tus registros y controles, en gráficos. Todo sale de lo que fuiste marcando; nada inventado.
      </p>

      {avance.total > 0 && <Tarjeta titulo="Tu avance"><BarraAvance pct={pct} /></Tarjeta>}

      <div style={{ display: "flex", gap: 8, marginTop: 14 }}>
        <CifraTile valor={String(cifras.dias)} etiqueta="días de camino" color={AZUL} />
        <CifraTile valor={cifras.ritmo.toFixed(1)} etiqueta="acciones/semana" color={AZUL} />
        <CifraTile valor={String(cifras.racha)} etiqueta="días de racha" color={AZUL} />
        <CifraTile valor={`${cifras.ciclos} · ${cifras.mundos}`} etiqueta="ciclos · mundos" color={AZUL} />
      </div>

      {datos.avancePorSemana.length > 0 && avance.total > 0 && (
        <Tarjeta titulo="Tu avance acumulado" nota="Cuánto del plan llevas cerrado, semana a semana.">
          <AvanceAcumulado series={datos.avancePorSemana} total={avance.total} />
        </Tarjeta>
      )}

      {datos.proyeccion && (
        <Tarjeta titulo="Proyección de cierre" nota="A tu ritmo actual, cuándo cerrarías lo que falta. Es una estimación.">
          <div style={{ fontSize: 24, fontWeight: 800, color: VERDE, letterSpacing: "-0.5px" }}>~{datos.proyeccion.fechaHumana}</div>
          <div style={{ fontSize: 12.5, color: TER, marginTop: 5 }}>
            Faltan <b style={{ color: TINTA }}>{datos.proyeccion.restantes}</b> {datos.proyeccion.restantes === 1 ? "acción" : "acciones"} · a{" "}
            <b style={{ color: TINTA }}>{datos.proyeccion.ritmo}</b>/semana · ~<b style={{ color: TINTA }}>{datos.proyeccion.semanas}</b> {datos.proyeccion.semanas === 1 ? "semana" : "semanas"}
          </div>
        </Tarjeta>
      )}

      {datos.distribucionEstados.length > 0 && (
        <Tarjeta titulo="Cómo van tus acciones" nota="En qué estado está cada acción activa ahora mismo.">
          <Distribucion dist={datos.distribucionEstados} />
        </Tarjeta>
      )}

      {datos.avancePorSemana.some((s) => s.hechas > 0) && (
        <Tarjeta titulo="Tu ritmo, semana a semana" nota="Acciones que cerraste cada semana.">
          <RitmoSemanal series={datos.avancePorSemana} />
        </Tarjeta>
      )}

      {datos.accionesPorEtapa.length > 0 && (
        <Tarjeta titulo="Dónde pusiste el esfuerzo" nota="Cuántas acciones tiene cada etapa y cuántas cerraste.">
          <Esfuerzo series={datos.accionesPorEtapa} />
        </Tarjeta>
      )}

      {c && (
        <div style={{ breakInside: "avoid", marginTop: 22 }}>
          <div style={{ fontSize: 11, fontWeight: 700, letterSpacing: "1.5px", textTransform: "uppercase", color: AMBAR, borderTop: `1px solid ${HILO}`, paddingTop: 18 }}>
            Cómo cumpliste tus fechas
          </div>
          <div style={{ display: "flex", gap: 8, marginTop: 14 }}>
            <CifraTile valor={String(c.adelantadas)} etiqueta={`adelantadas · ${c.pctAdelantadas}%`} color={VERDE} />
            <CifraTile valor={String(c.aTiempo)} etiqueta={`a tiempo · ${c.pctATiempo}%`} color={AZUL} />
            <CifraTile valor={String(c.tardias)} etiqueta={`tardías · ${c.pctTardias}%`} color={AMBAR} />
            <CifraTile valor={`${c.desviacionMediaDias > 0 ? "+" : ""}${c.desviacionMediaDias.toFixed(1)}`} etiqueta="desviación media (días)" color={AZUL} />
          </div>
          <Tarjeta titulo="Reparto de tu cumplimiento" nota="Cómo llegaste a cada fecha que te pusiste.">
            <RepartoDonut adelantadas={c.adelantadas} aTiempo={c.aTiempo} tardias={c.tardias} />
          </Tarjeta>
          <GanttPapel porEtapa={c.porEtapa} dias={datos.cifras.dias} cerrada={datos.cerrada} />
          {c.porDominio.length > 1 && (
            <Tarjeta titulo="Cumplimiento por mundo" nota="Verde adelantadas, azul a tiempo, ámbar tardías.">
              <PorMundo filas={c.porDominio} />
              <div style={{ display: "flex", flexWrap: "wrap", gap: "6px 16px", marginTop: 14 }}>
                <Chip color={VERDE} texto="adelantadas" />
                <Chip color={AZUL} texto="a tiempo" />
                <Chip color={AMBAR} texto="tardías" />
              </div>
            </Tarjeta>
          )}
        </div>
      )}
    </div>
  );
}

export function AnalisisPapel({
  nombre,
  nombreIdea,
  datos,
  oculto,
}: {
  nombre: string;
  nombreIdea: string;
  datos: AnalisisPapelData;
  oculto?: boolean;
}) {
  return (
    <HojaImpresion nombreIdea={nombreIdea} pieTitulo="Análisis del proyecto" oculto={oculto}>
      <FilaPapel>
        <ContenidoAnalisis nombre={nombre} datos={datos} />
      </FilaPapel>
    </HojaImpresion>
  );
}
