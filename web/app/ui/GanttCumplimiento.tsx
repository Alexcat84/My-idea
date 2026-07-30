"use client";

/**
 * GanttCumplimiento — el gráfico "Cómo se movió tu camino" del Análisis (canon
 * 11, capa de cumplimiento), calibrado por Claude Design. TRES vistas que
 * comparten datos, escala, leyenda numerada, línea de HOY y regla de color;
 * solo cambia la forma de dibujar:
 *   - Riel fantasma (la que abre): la línea base en gris, encima los días reales.
 *   - Escalera: guía base + trazo real + el escalón al pasar de etapa.
 *   - Dos cintas: una cinta "plan" y otra "real", con el corrimiento anotado.
 * El selector guarda la preferencia del usuario. Tardía en ámbar, jamás rojo;
 * "hoy" solo con el proyecto en marcha; nunca mecánica del motor.
 *
 * Portado fiel de la entrega de Design (medidas/tokens en su `notas.md`); los
 * números salen de analytics (cero LLM).
 */
import { useEffect, useState, type CSSProperties, type ReactNode } from "react";

export type VistaGantt = "riel" | "escalera" | "cintas";

export interface EtapaGantt {
  etapa: number;
  baseInicio: number;
  baseFin: number | null;
  realInicio: number | null;
  realFin: number | null;
}

const VERDE = "#3FB950";
const AMBAR = "#E0A64A";
const BASE_BORDE = "#5C5E66";
const BASE_FONDO = "#2C2D33";
const AZUL = "#4D7CFE";

// Nombres profesionales de las vistas (el id interno no cambia: la preferencia
// guardada sigue siendo riel/escalera/cintas).
const VISTAS: Array<{ id: VistaGantt; nombre: string }> = [
  { id: "riel", nombre: "Plan y real" },
  { id: "escalera", nombre: "Escalonado" },
  { id: "cintas", nombre: "Bandas" },
];

function Selector({ vista, onCambio }: { vista: VistaGantt; onCambio: (v: VistaGantt) => void }) {
  return (
    <div style={{ display: "flex", flexWrap: "wrap", alignItems: "center", gap: 10, marginBottom: 18 }}>
      <span style={{ fontSize: 11, fontWeight: 600, letterSpacing: "1.2px", textTransform: "uppercase", color: "#6F7076" }}>
        vista
      </span>
      <div
        style={{
          display: "inline-flex",
          alignItems: "center",
          gap: 4,
          padding: 4,
          borderRadius: 999,
          background: "rgba(77,124,254,0.08)",
          boxShadow: "inset 0 0 0 1px rgba(77,124,254,0.24)",
        }}
      >
        {VISTAS.map((v) => {
          const activa = v.id === vista;
          return (
            <button
              key={v.id}
              onClick={() => onCambio(v.id)}
              style={{
                fontSize: 12,
                fontWeight: activa ? 700 : 600,
                color: activa ? "#DCE7FF" : "#8A8C95",
                background: activa ? "rgba(77,124,254,0.28)" : "transparent",
                boxShadow: activa ? "inset 0 0 0 1px rgba(77,124,254,0.75)" : "none",
                borderRadius: 999,
                padding: "6px 13px",
                whiteSpace: "nowrap",
                border: "none",
                cursor: "pointer",
              }}
            >
              {v.nombre}
            </button>
          );
        })}
      </div>
    </div>
  );
}

/** Una fila del diagrama en Riel fantasma / Escalera (una etapa por fila). */
function FilaCarril({
  n,
  base,
  real,
  tarde,
  planDias,
  realTexto,
  realColor,
  vista,
  primeraSiguienteReal,
}: {
  n: number;
  base: { l: number; w: number } | null;
  real: { l: number; w: number } | null;
  tarde: boolean;
  planDias: number | null;
  realTexto: string;
  realColor: string;
  vista: VistaGantt;
  primeraSiguienteReal: number | null; // % del arranque de la etapa siguiente (escalón)
}) {
  const colorReal = tarde ? AMBAR : VERDE;
  return (
    <div
      style={{
        display: "grid",
        gridTemplateColumns: "20px 1fr 136px",
        gap: 14,
        alignItems: "center",
        padding: "9px 0",
        borderBottom: "1px solid rgba(255,255,255,0.1)",
      }}
    >
      <span style={{ fontSize: 11.5, fontWeight: 700, color: AZUL, textAlign: "right", fontVariantNumeric: "tabular-nums" }}>
        {n}
      </span>
      <div style={{ position: "relative", height: vista === "escalera" ? 27 : 20 }}>
        {vista === "riel" ? (
          <>
            {base && (
              <div
                style={{
                  position: "absolute",
                  top: "50%",
                  transform: "translateY(-50%)",
                  left: `${base.l}%`,
                  width: `${base.w}%`,
                  height: 16,
                  borderRadius: 8,
                  border: `1px solid ${BASE_BORDE}`,
                  background: BASE_FONDO,
                }}
              />
            )}
            {real && (
              <div
                style={{ position: "absolute", top: "50%", transform: "translateY(-50%)", left: `${real.l}%`, width: `${real.w}%`, height: 6, borderRadius: 3, background: colorReal }}
              />
            )}
          </>
        ) : (
          <>
            {base && (
              <>
                <div style={{ position: "absolute", left: `${base.l}%`, width: `${base.w}%`, top: 7, height: 2, background: "#7A7C85" }} />
                <div style={{ position: "absolute", left: `${base.l}%`, top: 4, width: 1, height: 8, background: "#7A7C85" }} />
                <div style={{ position: "absolute", left: `${base.l + base.w}%`, top: 4, width: 1, height: 8, background: "#7A7C85" }} />
              </>
            )}
            {real && (
              <div style={{ position: "absolute", left: `${real.l}%`, width: `${real.w}%`, top: 16, height: 11, borderRadius: 6, background: colorReal }} />
            )}
            {primeraSiguienteReal != null && (
              <div style={{ position: "absolute", left: `${primeraSiguienteReal}%`, top: 27, width: 1, height: 10, background: "rgba(255,255,255,0.22)" }} />
            )}
          </>
        )}
      </div>
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 12, fontSize: 12, textAlign: "right", fontVariantNumeric: "tabular-nums" }}>
        <span style={{ color: "#6F7076" }}>{planDias != null ? `${planDias}d` : "—"}</span>
        <span style={{ color: realColor, fontWeight: 600 }}>{realTexto}</span>
      </div>
    </div>
  );
}

export function GanttCumplimiento({
  porEtapa,
  maxBarra,
  nombreEtapa,
  hoyDias,
}: {
  porEtapa: EtapaGantt[];
  maxBarra: number;
  nombreEtapa: (n: number) => string;
  /** días desde la chispa hasta HOY; null si el proyecto ya se cerró */
  hoyDias: number | null;
}) {
  const [vista, setVista] = useState<VistaGantt>("riel");
  useEffect(() => {
    const v = localStorage.getItem("mi-idea:gantt-vista");
    if (v === "riel" || v === "escalera" || v === "cintas") setVista(v);
  }, []);
  const cambiar = (v: VistaGantt) => {
    setVista(v);
    try {
      localStorage.setItem("mi-idea:gantt-vista", v);
    } catch {
      /* preferencia perdida, no pasa nada */
    }
  };

  const escala = Math.max(1, maxBarra);
  const pct = (d: number) => (d / escala) * 100;
  const filas = porEtapa.map((e, i) => {
    const tieneReal = e.realFin != null && e.realInicio != null;
    const realDias = tieneReal ? Math.round(e.realFin! - e.realInicio!) : null;
    const tarde = e.realFin != null && e.baseFin != null && e.realFin > e.baseFin + 1;
    // "en curso": la etapa actual (tiene inicio real, aún no cerró el proyecto y
    // es la última con avance) muestra "en curso" en vez de los días.
    return {
      n: i + 1,
      nombre: nombreEtapa(e.etapa),
      base: e.baseFin != null ? { l: pct(e.baseInicio), w: pct(Math.max(0, e.baseFin - e.baseInicio)) } : null,
      real: tieneReal ? { l: pct(e.realInicio!), w: pct(Math.max(0, e.realFin! - e.realInicio!)) } : null,
      planDias: e.baseFin != null ? Math.round(e.baseFin - e.baseInicio) : null,
      realDias,
      tarde,
      realInicioPct: tieneReal ? pct(e.realInicio!) : null,
    };
  });
  const hoyPct = hoyDias != null ? Math.min(100, Math.max(0, pct(hoyDias))) : null;
  const ticks = [0, 0.25, 0.5, 0.75, 1].map((f) => Math.round(f * escala));

  return (
    <div className="mt-6">
      <Selector vista={vista} onCambio={cambiar} />
      <div style={{ border: "1px solid rgba(255,255,255,0.08)", borderRadius: 16, padding: "26px 28px 22px" }}>
        {/* encabezado + leyenda de colores */}
        <div style={{ display: "flex", alignItems: "flex-start", justifyContent: "space-between", gap: 24, marginBottom: 6, flexWrap: "wrap" }}>
          <div>
            <div style={{ fontSize: 15, fontWeight: 700, color: "#F5F6F8" }}>Cómo se movió tu camino</div>
            <div style={{ fontSize: 13, color: "#6F7076", marginTop: 5 }}>
              En gris, la línea base que sellaste. Encima, los días que ocupaste de verdad.
            </div>
          </div>
          <div style={{ display: "flex", gap: 16, fontSize: 12, color: "#A6A7AD", paddingTop: 3, flexWrap: "wrap" }}>
            <span style={{ display: "flex", alignItems: "center", gap: 7 }}>
              <span style={{ width: 18, height: 12, borderRadius: 6, border: `1px solid ${BASE_BORDE}`, background: BASE_FONDO }} />
              tu línea base, ya no se mueve
            </span>
            <span style={{ display: "flex", alignItems: "center", gap: 7 }}>
              <span style={{ width: 18, height: 6, borderRadius: 3, background: VERDE }} />
              lo que pasó
            </span>
            <span style={{ display: "flex", alignItems: "center", gap: 7 }}>
              <span style={{ width: 18, height: 6, borderRadius: 3, background: AMBAR }} />
              tomó bastante más
            </span>
          </div>
        </div>

        {/* leyenda numerada (nombres una vez) */}
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "4px 28px", margin: "18px 0 20px" }}>
          {filas.map((f) => (
            <div key={f.n} style={{ display: "flex", alignItems: "baseline", gap: 10, padding: "5px 0" }}>
              <span
                style={{
                  flex: "none",
                  width: 20,
                  height: 20,
                  borderRadius: "50%",
                  border: "1px solid rgba(77,124,254,0.4)",
                  color: AZUL,
                  fontSize: 11,
                  fontWeight: 700,
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  fontVariantNumeric: "tabular-nums",
                }}
              >
                {f.n}
              </span>
              <span style={{ fontSize: 13.5, color: "#F5F6F8" }}>{f.nombre}</span>
            </div>
          ))}
        </div>

        {/* diagrama */}
        <div style={{ display: "flex", alignItems: "center", gap: 14, margin: "4px 0 6px" }}>
          <span style={{ flex: "none", fontSize: 11, fontWeight: 600, letterSpacing: "1.3px", textTransform: "uppercase", color: "#6F7076" }}>
            tu camino en el tiempo
          </span>
          <span style={{ flex: 1, height: 1, background: "rgba(255,255,255,0.12)" }} />
        </div>

        <div style={{ position: "relative", paddingTop: 16 }}>
          {/* cuadrícula + EJES del área de dibujo: rejilla vertical fina cada
              12.5% para leer el tiempo, y los dos ejes principales (izquierdo y
              inferior) BIEN marcados en su borde. Deja libre la columna
              plan/real. */}
          <div
            style={{
              position: "absolute",
              left: 34,
              right: vista === "cintas" ? 0 : 150,
              top: 0,
              bottom: 34,
              background: "repeating-linear-gradient(to right, rgba(255,255,255,0.11) 0 1px, transparent 1px 12.5%)",
              borderLeft: "1.5px solid rgba(255,255,255,0.42)",
              borderBottom: "1.5px solid rgba(255,255,255,0.42)",
            }}
          />
          {hoyPct != null && (
            <div style={{ position: "absolute", left: 34, right: vista === "cintas" ? 0 : 150, top: 0, bottom: 34 }}>
              <div style={{ position: "absolute", left: `${hoyPct}%`, top: 0, bottom: 0, width: 1, background: "repeating-linear-gradient(to bottom, rgba(245,246,248,0.34) 0 4px, transparent 4px 8px)" }} />
              <div style={{ position: "absolute", left: `${hoyPct}%`, top: -4, transform: "translateX(-50%)", fontSize: 10.5, fontWeight: 600, letterSpacing: "0.6px", textTransform: "uppercase", color: "#A6A7AD", background: "#000", padding: "0 6px" }}>
                hoy
              </div>
            </div>
          )}

          {vista === "cintas" ? (
            <DosCintas filas={filas} />
          ) : (
            <div style={{ position: "relative", display: "flex", flexDirection: "column" }}>
              <div style={{ display: "grid", gridTemplateColumns: "20px 1fr 136px", gap: 14, padding: "0 0 9px" }}>
                <span />
                <span />
                <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 12, textAlign: "right", fontSize: 10, fontWeight: 600, letterSpacing: "1.1px", textTransform: "uppercase", color: "#6F7076" }}>
                  <span>plan</span>
                  <span>real</span>
                </div>
              </div>
              {filas.map((f, i) => (
                <FilaCarril
                  key={f.n}
                  n={f.n}
                  base={f.base}
                  real={f.real}
                  tarde={f.tarde}
                  planDias={f.planDias}
                  realTexto={f.realDias != null ? `${f.realDias}d` : "en curso"}
                  realColor={f.realDias != null ? (f.tarde ? AMBAR : VERDE) : VERDE}
                  vista={vista}
                  primeraSiguienteReal={vista === "escalera" ? filas[i + 1]?.realInicioPct ?? null : null}
                />
              ))}
            </div>
          )}

          {/* eje de tiempo */}
          <div style={{ display: "grid", gridTemplateColumns: vista === "cintas" ? "1fr" : "20px 1fr 136px", gap: 14, paddingTop: 12 }}>
            {vista !== "cintas" && <span />}
            <div style={{ display: "flex", justifyContent: "space-between", fontSize: 11, color: "#A6A7AD", fontVariantNumeric: "tabular-nums", marginLeft: vista === "cintas" ? 0 : 0 }}>
              {ticks.map((t, i) => (
                <span key={i}>{i === 0 ? `día ${t}` : t}</span>
              ))}
            </div>
            {vista !== "cintas" && <span />}
          </div>
        </div>
      </div>
    </div>
  );
}

/** Vista "Dos cintas": una cinta plan (gris) y una cinta real (verde/ámbar),
 * cada etapa como bloque numerado en su ventana. */
function DosCintas({ filas }: { filas: Array<{ n: number; base: { l: number; w: number } | null; real: { l: number; w: number } | null; tarde: boolean }> }) {
  const bloque = (l: number, w: number, contenido: ReactNode, estilo: CSSProperties): ReactNode => (
    <div
      style={{
        position: "absolute",
        left: `${l}%`,
        width: `${w}%`,
        top: 0,
        height: 36,
        borderRadius: 8,
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        fontSize: 12,
        fontWeight: 700,
        fontVariantNumeric: "tabular-nums",
        ...estilo,
      }}
    >
      {contenido}
    </div>
  );
  return (
    <div style={{ position: "relative" }}>
      {/* cinta plan */}
      <div style={{ position: "relative", height: 36, marginBottom: 22 }}>
        {filas.map((f) => f.base && bloque(f.base.l, f.base.w, f.n, { border: `1px solid ${BASE_BORDE}`, background: BASE_FONDO, color: "#C6C8CE" }))}
      </div>
      {/* cinta real */}
      <div style={{ position: "relative", height: 36 }}>
        {filas.map(
          (f) =>
            f.real &&
            bloque(
              f.real.l,
              f.real.w,
              f.n,
              f.tarde ? { background: AMBAR, color: "#2A1C05" } : { background: "rgba(63,185,80,0.9)", color: "#04240B" }
            )
        )}
      </div>
    </div>
  );
}
