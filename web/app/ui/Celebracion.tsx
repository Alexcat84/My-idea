"use client";

/**
 * Celebracion — Fase 3.8 §5 (canon 09): el viaje como timeline fechado. La
 * barra azul desciende encendiendo cada hito en secuencia (duración FIJA
 * ~7s sin importar el largo), un toque la salta, prefers-reduced-motion va
 * directo al estado estático. Al llegar a REALIZADA, UNA onda verde y nace
 * el proyecto: se estampa el pill "Proyecto" y el héroe. Todo de lo
 * persistido (cero LLM). Estadísticas reales; la línea de cumplimiento solo
 * con baseline confirmada.
 */
import { useEffect, useState } from "react";
import catalogo from "@/lib/assets/packs_catalog.json";
import type { Analytics, Hito } from "@/lib/analytics";
import { fechaHumanaCorta } from "@/lib/fechas";
import { elegir } from "@/lib/i18n/config";
import { useIdioma } from "@/lib/i18n/IdiomaProvider";
import { interpolar, plural } from "@/lib/i18n/interpolar";
import { CELEBRACION } from "@/lib/i18n/mensajes/celebracion";

/** El mundo se nombra como el usuario lo conoce, jamás por su clave técnica. */
const NOMBRE_DOMINIO: Record<string, string> = Object.fromEntries(
  (catalogo as { packs: Array<{ clave: string; nombre: string }> }).packs.map((p) => [p.clave, p.nombre])
);

/** El matiz de los mundos, extraído del canon 09 (el punto de "Mundo activado:
 * Calidad y Confianza"): ni el azul que piensa ni el verde que ejecuta — los
 * mundos tienen tono propio en el timeline. */
const MATIZ_MUNDO = "#3A9B8F";

/** Fase 4.2: el hito se lee "Mundo activado: Calidad y Confianza" (canon 09).
 * La etiqueta viene sin nombre desde analytics (que es puro y no conoce el
 * catálogo); aquí se completa. */
function etiquetaHito(h: Hito): string {
  return h.dominio ? `${h.etiqueta}: ${NOMBRE_DOMINIO[h.dominio] ?? h.dominio}` : h.etiqueta;
}

interface Respuesta {
  nombre: string;
  tiene_baseline: boolean;
  /** Fase 4.0 §8: el porqué del cierre, en las palabras del usuario. */
  cierre_motivo?: string | null;
  analytics: Analytics;
  hitosCelebracion: Hito[];
}

function colorHito(h: Hito): string {
  if (h.tipo === "realizada") return "var(--done)";
  if (h.tipo === "accion") return h.cumplimiento === "tardia" ? "var(--warn)" : "var(--done)";
  if (h.tipo === "mundo" || h.tipo === "mundo_completado") return MATIZ_MUNDO;
  return "var(--accent)";
}

/** El timeline animado. Se monta con los hitos ya cargados: así useState
 * arranca con el total real (reduce → todo revelado). */
function Timeline({ hitos, onFin }: { hitos: Hito[]; onFin: () => void }) {
  const idioma = useIdioma();
  const total = hitos.length;
  const reduce =
    typeof window !== "undefined" && window.matchMedia?.("(prefers-reduced-motion: reduce)").matches === true;
  const [revelados, setRevelados] = useState(reduce ? total : 0);

  useEffect(() => {
    if (reduce || total === 0) {
      onFin();
      return;
    }
    const paso = Math.min(900, Math.max(280, Math.round(7000 / total))); // 6-8s repartidos
    let i = 0;
    const id = setInterval(() => {
      i += 1;
      setRevelados(i);
      if (i >= total) {
        clearInterval(id);
        onFin();
      }
    }, paso);
    return () => clearInterval(id);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [total]);

  const pct = total > 0 ? Math.round((Math.min(revelados, total) / total) * 100) : 100;

  // Eje SIEMPRE centrado en desktop y a la izquierda en móvil; el punto y la
  // barra azul viajan sobre él. left-[7px] (móvil) / left-1/2 (desktop).
  const ejePos = "left-[7px] -translate-x-1/2 sm:left-1/2";

  return (
    <div className="relative py-2" onClick={() => setRevelados(total)}>
      {/* eje: pista hairline + barra azul→verde que desciende */}
      <span className={"absolute top-2 bottom-2 w-px bg-hairline " + ejePos} />
      <span
        className={"absolute top-2 w-px bg-gradient-to-b from-accent to-done transition-[height] duration-500 ease-out " + ejePos}
        style={{ height: `calc(${pct}% - 16px)` }}
      />
      <ol className="flex flex-col gap-6">
        {hitos.map((h, i) => {
          const visible = i < revelados;
          const izq = i % 2 === 0; // alternancia de lado en desktop
          const realizada = h.tipo === "realizada";
          const color = colorHito(h);
          return (
            <li
              key={i}
              className={"relative grid sm:grid-cols-2 sm:gap-x-10 " + (visible ? "anima-hito-reveal" : "")}
              style={{ opacity: visible ? 1 : 0, transition: "opacity 0.4s ease-out" }}
            >
              {/* el punto sobre el eje (anillo verde mayor para REALIZADA) */}
              <span
                className={
                  "absolute z-10 rounded-full " +
                  ejePos +
                  (realizada
                    ? " mt-0 flex h-6 w-6 items-center justify-center border-2 bg-black"
                    : " mt-1.5 h-2.5 w-2.5")
                }
                style={realizada ? { borderColor: color } : { background: color }}
              >
                {realizada && <span className="h-2 w-2 rounded-full" style={{ background: color }} />}
              </span>

              {/* contenido: móvil a la derecha del eje; desktop alterna lados */}
              <div
                className={
                  "pl-7 sm:pl-0 " +
                  (realizada
                    ? "sm:col-span-2 sm:pt-9 sm:text-center"
                    : izq
                      ? "sm:pr-10 sm:text-right"
                      : "sm:col-start-2 sm:pl-10 sm:text-left")
                }
              >
                <p className="text-[12px] text-dim">{fechaHumanaCorta(h.fecha, idioma)}</p>
                <p
                  className={
                    "mt-0.5 " +
                    (realizada
                      ? "text-[15px] font-bold uppercase tracking-wide text-done"
                      : "text-[14.5px] font-medium")
                  }
                >
                  {etiquetaHito(h)}
                </p>
                {h.subtitulo && (
                  <p className={"mt-0.5 text-[12.5px] " + (h.cumplimiento === "tardia" ? "text-warn" : "text-dim")}>
                    {h.subtitulo}
                  </p>
                )}
              </div>
            </li>
          );
        })}
      </ol>
    </div>
  );
}

export function Celebracion({
  projectId,
  onVerAnalisis,
  onVerDocumentos,
  onReabierto,
  onVolverIdeas,
}: {
  projectId: string;
  onVerAnalisis: () => void;
  /** Fase 4.6: llevarse el expediente completo del proyecto ya cerrado */
  onVerDocumentos: () => void;
  onReabierto: () => void;
  onVolverIdeas: () => void;
}) {
  const idioma = useIdioma();
  const t = elegir(CELEBRACION, idioma);
  const [datos, setDatos] = useState<Respuesta | null>(null);
  // La clave del error (no el texto): se pinta en el idioma de la pantalla.
  const [error, setError] = useState<"error" | "errorCargar" | "errorReabrir" | null>(null);
  const [terminado, setTerminado] = useState(false);
  const [reabriendo, setReabriendo] = useState(false);

  useEffect(() => {
    let vivo = true;
    (async () => {
      try {
        const res = await fetch(`/api/project/${projectId}/analisis`);
        if (!res.ok) {
          if (vivo) setError("error");
          return;
        }
        if (vivo) setDatos((await res.json()) as Respuesta);
      } catch {
        if (vivo) setError("errorCargar");
      }
    })();
    return () => {
      vivo = false;
    };
  }, [projectId]);

  async function reabrir() {
    setReabriendo(true);
    try {
      const res = await fetch(`/api/project/${projectId}/realizar`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ accion: "reabrir" }),
      });
      if (res.ok) onReabierto();
      else setError("error");
    } catch {
      setError("errorReabrir");
    } finally {
      setReabriendo(false);
    }
  }

  if (error) return <p className="text-sm text-warn">{t[error]}</p>;
  if (!datos) return <p className="text-dim">{t.preparando}</p>;

  const u = datos.analytics.universal;
  const c = datos.analytics.cumplimiento;

  return (
    <div className="mx-auto flex max-w-2xl flex-col gap-8">
      {/* héroe: nace el proyecto (el pill + pulso al terminar) */}
      <header className="relative overflow-visible text-center">
        <p className="text-[11px] font-semibold uppercase tracking-[1.6px] text-done">{t.realizada}</p>
        <h2 className="mt-3 text-2xl font-bold leading-tight tracking-tight sm:text-[30px] [text-wrap:balance]">
          {t.heroe}
        </h2>
        <p className="mt-2 text-[15px] text-dim">{datos.nombre}</p>
        <div className="relative mt-4 inline-flex items-center justify-center">
          {terminado && (
            <span
              className="anima-green-wave pointer-events-none absolute left-1/2 top-1/2 h-3 w-3 rounded-full"
              style={{ background: "rgba(63,185,80,0.5)" }}
            />
          )}
          <span
            className={
              "relative inline-flex items-center gap-1.5 rounded-full border border-done/50 bg-done-soft px-3.5 py-1.5 text-[12px] font-bold text-done " +
              (terminado ? "anima-green-pulse" : "")
            }
          >
            <svg width="11" height="11" viewBox="0 0 12 12" aria-hidden>
              <path d="M2.5 6.5l2.5 2.5 4.5-5.5" stroke="var(--done)" strokeWidth="2" fill="none" />
            </svg>
            {t.proyecto}
          </span>
        </div>
      </header>

      {/* timeline fechado */}
      <section className="rounded-panel border border-hairline bg-surface p-6 sm:p-7">
        <Timeline hitos={datos.hitosCelebracion} onFin={() => setTerminado(true)} />
        {/* Fase 4.0 §8: el acta, bajo el hito REALIZADA — discreta y en la
            voz del usuario. Solo aparece cuando la animación terminó, para
            no adelantarse al momento. */}
        {terminado && datos.cierre_motivo && (
          <figure className="anima-plan-in mx-auto mt-6 max-w-md border-t border-hairline pt-5 text-center">
            <figcaption className="mb-2 text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">
              {t.porQueCerraste}
            </figcaption>
            <blockquote className="text-[14px] leading-[1.7] text-ink [text-wrap:pretty]">
              «{datos.cierre_motivo}»
            </blockquote>
          </figure>
        )}
      </section>

      {/* estadísticas reales */}
      <section>
        <p className="mb-4 text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">
          {interpolar(t.estadisticasDe, { nombre: datos.nombre })}
        </p>
        <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
          <div className="rounded-panel border border-hairline bg-surface p-5">
            <p className="text-3xl font-bold">{u.duracionTotalDias}</p>
            <p className="mt-1 text-[12px] text-dim">{t.diasDesdeLaChispa}</p>
          </div>
          <div className="rounded-panel border border-hairline bg-surface p-5">
            <p className="text-3xl font-bold">{u.ciclosDePlan}</p>
            <p className="mt-1 text-[12px] text-dim">{t.ciclosDePlan}</p>
          </div>
          <div className="rounded-panel border border-hairline bg-surface p-5">
            <p className="text-3xl font-bold">
              {u.accionesVigente.hechas} <span className="text-lg font-semibold text-dim">{interpolar(t.deTotal, { total: u.accionesVigente.total })}</span>
            </p>
            <p className="mt-1 text-[12px] text-dim">{t.acciones}</p>
          </div>
          <div className="rounded-panel border border-hairline bg-surface p-5">
            <p className="text-3xl font-bold">{u.mundos}</p>
            <p className="mt-1 text-[12px] text-dim">{plural(idioma, u.mundos, t.mundosActivados)}</p>
          </div>
        </div>
        {/* línea de cumplimiento: SOLO con baseline confirmada */}
        {datos.tiene_baseline && c && (
          <p className="mt-4 flex flex-wrap gap-x-5 gap-y-1 text-[13.5px]">
            <span className="font-semibold text-done">{interpolar(t.aTiempo, { n: c.aTiempo })}</span>
            <span className="font-semibold text-accent">{interpolar(t.adelantadas, { n: c.adelantadas })}</span>
            <span className="font-semibold text-warn">{interpolar(t.tardias, { n: c.tardias })}</span>
          </p>
        )}
      </section>

      {/* acciones */}
      <div className="flex flex-wrap items-center gap-x-6 gap-y-3">
        <button onClick={onVerAnalisis} className="text-[14px] font-semibold text-accent hover:underline">
          {t.verAnalisis}
        </button>
        {/* Fase 4.6: al cerrar es cuando más se quiere el expediente entero. */}
        <button onClick={onVerDocumentos} className="text-[14px] font-semibold text-accent hover:underline">
          {t.descargarExpediente}
        </button>
        <button onClick={onVolverIdeas} className="text-[14px] text-dim hover:text-ink">
          {t.volverAMisIdeas}
        </button>
        <button onClick={reabrir} disabled={reabriendo} className="text-[14px] text-dim hover:text-ink disabled:opacity-50">
          {reabriendo ? t.reabriendo : t.reabrir}
        </button>
      </div>
    </div>
  );
}
