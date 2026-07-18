"use client";

/**
 * PotenciaTuIdea — la fila "Potencia tu idea" (canon 07-B / 08): grilla de
 * tarjetas con ícono arriba-izquierda + chip arriba-derecha (créditos /
 * "Activo · n/m" verde / "Activar · beta"), nombre y promesa, con hover que
 * eleva la tarjeta. Tus Números (2 créditos) + los mundos del catálogo. Precios
 * SIEMPRE desde precios.ts / packs_catalog.json — ninguna cifra hardcodeada.
 * Azul piensa; el verde ejecuta marca el mundo activo.
 *
 * Beta (jul 2026): el candado se retiró. El cobro de créditos duerme hasta la
 * ETAPA 2 (ledger, migraciones 020-024 sin aplicar), y mientras tanto activar
 * un mundo es GRATIS y para todos — el fundador debe poder probar los 7 por
 * igual. El precio del catálogo se muestra tachado, para que se lea como
 * cortesía de beta y no como "siempre fue gratis". El ancla del cobro futuro
 * vive en `activarMundo`.
 */
import { useState, type ReactNode } from "react";
import catalogo from "@/lib/assets/packs_catalog.json";
import type { EstadoMundo } from "@/lib/engine/previewMundos";
import { PRECIOS } from "@/lib/precios";

interface Pack {
  clave: string;
  nombre: string;
  promesa: string;
  creditos_activar: number;
}

interface Props {
  projectId: string;
  unlocks: string[];
  progresoMundos: Record<string, { hechos: number; total: number } | null>;
  /** Fase 4.2: los mundos que el usuario dio por completados. Su chip cambia de
   * "Activo · n/m" (azul) a "Completado" (verde): el mundo tuvo un final. */
  mundosCompletados?: string[];
  /** Fase 4.5: el estado de cada mundo (bloqueado / abierto / diagnostico_listo
   * / plan_comprado), calculado por el padre con estadoMundo(). */
  estadosMundo: Record<string, EstadoMundo>;
  onVerMundo: (dominio: string) => void;
  /** Fase 4.5: ABRIR un mundo es gratis (el cobro vive en la entrega de su
   * plan). El padre refresca sus unlocks y entra al mundo. */
  onActivarMundo: (dominio: string) => void;
}

/** Íconos por mundo (trazo del canon); genérico para los mundos nuevos. */
function Icono({ clave, activo }: { clave: string; activo?: boolean }) {
  const color = clave === "tus_numeros" ? "#F5F6F8" : activo ? "#4D7CFE" : "#A6A7AD";
  const p = { stroke: color, strokeWidth: 1.5, fill: "none" as const };
  const paths: Record<string, ReactNode> = {
    tus_numeros: (
      <>
        <line x1="4" y1="16" x2="4" y2="10" stroke="#F5F6F8" strokeWidth="1.6" />
        <line x1="10" y1="16" x2="10" y2="5" stroke="#F5F6F8" strokeWidth="1.6" />
        <line x1="16" y1="16" x2="16" y2="8" stroke="#F5F6F8" strokeWidth="1.6" />
      </>
    ),
    quality: (
      <>
        <path d="M10 2.5l6 2.2v4.5c0 3.6-2.5 6.6-6 8.3-3.5-1.7-6-4.7-6-8.3V4.7z" {...p} />
        <path d="M7 9.8l2.1 2.1L13.3 8" {...p} />
      </>
    ),
    health_safety: (
      <>
        <circle cx="10" cy="6.5" r="3" {...p} />
        <path d="M4 16.5c0-3 2.7-4.8 6-4.8s6 1.8 6 4.8" {...p} />
      </>
    ),
    environmental: (
      <>
        <path d="M16 4c-7 0-11 4-11 11 6.5 0 11-4 11-11z" {...p} />
        <path d="M5.5 14.5C8 11 11 8.5 14 7" {...p} strokeWidth={1.2} />
      </>
    ),
    seguridad_digital: (
      <>
        <path d="M10 2.5l6 2.2v4.5c0 3.6-2.5 6.6-6 8.3-3.5-1.7-6-4.7-6-8.3V4.7z" {...p} />
        <rect x="8" y="8.5" width="4" height="3.5" rx="0.8" {...p} strokeWidth={1.2} />
        <path d="M8.8 8.5V7.6a1.2 1.2 0 0 1 2.4 0v0.9" {...p} strokeWidth={1.2} />
      </>
    ),
    exportacion: (
      <>
        <circle cx="10" cy="10" r="7" {...p} />
        <path d="M3 10h14M10 3c2 2.2 2 11.8 0 14M10 3c-2 2.2-2 11.8 0 14" {...p} strokeWidth={1.2} />
      </>
    ),
    franquicias: (
      <>
        <rect x="3" y="3" width="6.5" height="6.5" rx="1.2" {...p} />
        <rect x="10.5" y="3" width="6.5" height="6.5" rx="1.2" {...p} />
        <rect x="3" y="10.5" width="6.5" height="6.5" rx="1.2" {...p} />
        <rect x="10.5" y="10.5" width="6.5" height="6.5" rx="1.2" {...p} />
      </>
    ),
    risk_management: (
      <>
        <path d="M10 2.5l7.5 13H2.5z" {...p} />
        <line x1="10" y1="8" x2="10" y2="11.5" {...p} />
        <circle cx="10" cy="13.5" r="0.6" fill={color} stroke="none" />
      </>
    ),
  };
  return (
    <svg width="20" height="20" viewBox="0 0 20 20" aria-hidden className="shrink-0">
      {paths[clave] ?? paths.quality}
    </svg>
  );
}

export function PotenciaTuIdea({
  projectId,
  unlocks,
  progresoMundos,
  mundosCompletados = [],
  estadosMundo,
  onVerMundo,
  onActivarMundo,
}: Props) {
  const [activando, setActivando] = useState<string | null>(null);
  const [errorEn, setErrorEn] = useState<string | null>(null);
  const [avisoBloqueado, setAvisoBloqueado] = useState<string | null>(null);
  const packs = (catalogo as { packs: Pack[] }).packs;

  // Fase 4.5 (PREVIEW_MUNDOS_PLAN): abrir un mundo es GRATIS, siempre. Lo que
  // se compra es su PLAN, a la entrega (ancla ETAPA 2 en la ruta del plan).
  // Esta funcion solo crea la fila (unlock stub) para que la seccion del mundo
  // exista en Manos a la Obra.
  async function activarMundo(pack: Pack) {
    setActivando(pack.clave);
    setErrorEn(null);
    try {
      const res = await fetch(`/api/project/${projectId}/world/${pack.clave}/unlock`, { method: "POST" });
      if (!res.ok) {
        setErrorEn(pack.clave);
        return;
      }
      onActivarMundo(pack.clave);
    } catch {
      setErrorEn(pack.clave);
    } finally {
      setActivando(null);
    }
  }

  const claseCard =
    "group flex flex-col rounded-[14px] border bg-surface p-[22px] text-left transition-[transform,background,border-color] duration-200 hover:-translate-y-[3px] hover:bg-surface-2";

  return (
    <section className="mt-2">
      <p className="mb-4 text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">Potencia tu idea</p>
      {/* Canon 05: Tus Números NO va aquí (se dedujo: ya es la fila-CTA bajo el
          plan). Este grid es solo los mundos del catálogo. */}
      <div className="grid grid-cols-1 gap-3.5 sm:grid-cols-2 lg:grid-cols-4">
        {/* Los mundos del catálogo — Fase 4.5: los CUATRO estados del preview
            (bloqueado / abierto / diagnóstico listo / plan comprado). */}
        {packs.map((p) => {
          const estado = estadosMundo[p.clave] ?? "abierto";
          const abierto = unlocks.includes(p.clave);
          const completado = mundosCompletados.includes(p.clave);
          const progreso = progresoMundos[p.clave] ?? null;
          const comprado = estado === "plan_comprado";
          const bloqueado = estado === "bloqueado";
          const destacado = comprado || estado === "diagnostico_listo";
          return (
            <button
              key={p.clave}
              onClick={() => {
                if (bloqueado) setAvisoBloqueado(p.clave);
                else if (abierto) onVerMundo(p.clave);
                else activarMundo(p);
              }}
              disabled={activando !== null}
              className={claseCard + " " + (destacado ? "border-accent/45" : "border-hairline") + " disabled:opacity-60"}
              data-transiciona
            >
              <div className="mb-3.5 flex items-center justify-between gap-2">
                <Icono clave={p.clave} activo={destacado} />
                {completado ? (
                  /* Fase 4.2: el mundo con final. Forma (el check) además de
                     color, como el resto del canon. */
                  <span className="inline-flex shrink-0 items-center gap-1.5 rounded-full border border-done/50 bg-done-soft px-2.5 py-[3px] text-[10.5px] font-bold text-done">
                    <svg width="9" height="9" viewBox="0 0 12 12" aria-hidden>
                      <path d="M2 6.5l2.5 2.5L10 3.5" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round" />
                    </svg>
                    Completado
                  </span>
                ) : comprado ? (
                  <span className="inline-flex shrink-0 items-center rounded-full border border-accent/45 bg-accent/15 px-2.5 py-[3px] text-[10.5px] font-bold text-accent">
                    Activo{progreso ? <> · <span className="text-done">{progreso.hechos}/{progreso.total}</span></> : ""}
                  </span>
                ) : estado === "diagnostico_listo" ? (
                  /* El estado protagonista: el escaparate espera. */
                  <span className="inline-flex shrink-0 items-center rounded-full border border-accent/50 bg-accent/15 px-2.5 py-[3px] text-[10.5px] font-bold text-accent">
                    Listo para tu plan
                  </span>
                ) : bloqueado ? (
                  <span className="inline-flex shrink-0 items-center rounded-full border border-hairline px-2.5 py-[3px] text-[10.5px] font-bold text-dim">
                    Se abre con tu plan
                  </span>
                ) : (
                  <span className="inline-flex shrink-0 items-center rounded-full border border-accent/45 bg-accent/15 px-2.5 py-[3px] text-[10.5px] font-bold text-accent">
                    {activando === p.clave ? "Abriendo…" : "Explóralo gratis"}
                  </span>
                )}
              </div>
              <p className={"text-[15px] font-semibold" + (destacado ? "" : " text-dim")}>{p.nombre}</p>
              <p className={"mt-1.5 text-[12.5px] leading-[1.55] [text-wrap:pretty] text-dim" + (destacado ? "" : " opacity-75")}>
                {p.promesa}
              </p>
              {!comprado && !completado && (
                <p className="mt-2 text-[12px] text-dim/70">
                  {errorEn === p.clave ? (
                    "No pudimos abrirlo; intenta de nuevo."
                  ) : avisoBloqueado === p.clave ? (
                    "Primero genera el plan de tu idea."
                  ) : estado === "diagnostico_listo" ? (
                    <>
                      Tu diagnóstico te espera · su plan: {PRECIOS.mundo_activar} créditos
                    </>
                  ) : (
                    <>
                      {/* ETAPA 2: el precio es VIVO (se paga con la cortesía);
                          el tachado de beta murió. Siempre de precios.ts. */}
                      El preview es gratis · su plan: {PRECIOS.mundo_activar} créditos
                    </>
                  )}
                </p>
              )}
            </button>
          );
        })}
      </div>
    </section>
  );
}
