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
  conPlan: boolean;
  onVerMundo: (dominio: string) => void;
  /** Beta: activar un mundo (gratis hasta la ETAPA 2). El padre refresca sus
   * unlocks y entra al mundo. */
  onActivarMundo: (dominio: string) => void;
  onTusNumeros: () => void;
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
  conPlan,
  onVerMundo,
  onActivarMundo,
  onTusNumeros,
}: Props) {
  const [avisoEn, setAvisoEn] = useState<string | null>(null);
  const [activando, setActivando] = useState<string | null>(null);
  const [errorEn, setErrorEn] = useState<string | null>(null);
  const packs = (catalogo as { packs: Pack[] }).packs;

  // Beta: el cobro de creditos duerme hasta la ETAPA 2 (ledger, migraciones
  // 020-024 sin aplicar). Mientras tanto, activar un mundo es GRATIS y para
  // todos: la web esta abierta y el fundador debe poder probar los 7 por igual.
  // El endpoint /unlock ya es un stub sin cobro; aqui va el boton que faltaba.
  //
  // ── ANCLA para la ETAPA 2: cuando el ledger despierte, esta funcion verifica
  // saldo ANTES del POST y descuenta a la activacion (los `creditos_activar` del
  // catalogo). El boton pasa de "Activar (beta)" a "Activar · N creditos". El
  // resto del flujo -- unlock -> world/start -> plan -- no cambia.
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
      <div className="grid grid-cols-1 gap-3.5 sm:grid-cols-2 lg:grid-cols-4">
        {/* Tus Números */}
        <button
          onClick={() => (conPlan ? onTusNumeros() : setAvisoEn("tus_numeros"))}
          className={claseCard + " border-accent/35 hover:border-accent/60"}
          data-transiciona
        >
          <div className="mb-3.5 flex items-center justify-between">
            <Icono clave="tus_numeros" />
            <span className="inline-flex shrink-0 items-center rounded-full border border-accent/45 px-2.5 py-[3px] text-[11px] font-bold text-accent">
              {PRECIOS.tus_numeros} créditos
            </span>
          </div>
          <p className="text-[15px] font-semibold">Tus Números</p>
          <p className="mt-1.5 text-[12.5px] leading-[1.55] text-dim [text-wrap:pretty]">
            Tus cifras reales convertidas en margen, punto de equilibrio y escenarios.
          </p>
          {avisoEn === "tus_numeros" && (
            <p className="mt-2 text-[12.5px] text-accent">Primero genera el plan de tu idea.</p>
          )}
        </button>

        {/* Los mundos del catálogo */}
        {packs.map((p) => {
          const activo = unlocks.includes(p.clave);
          const completado = mundosCompletados.includes(p.clave);
          const progreso = progresoMundos[p.clave] ?? null;
          return (
            <button
              key={p.clave}
              onClick={() => (activo ? onVerMundo(p.clave) : activarMundo(p))}
              disabled={activando !== null}
              className={claseCard + " " + (activo ? "border-accent/45" : "border-hairline") + " disabled:opacity-60"}
              data-transiciona
            >
              <div className="mb-3.5 flex items-center justify-between gap-2">
                <Icono clave={p.clave} activo={activo} />
                {completado ? (
                  /* Fase 4.2: el mundo con final. Forma (el check) además de
                     color, como el resto del canon. */
                  <span className="inline-flex shrink-0 items-center gap-1.5 rounded-full border border-done/50 bg-done-soft px-2.5 py-[3px] text-[10.5px] font-bold text-done">
                    <svg width="9" height="9" viewBox="0 0 12 12" aria-hidden>
                      <path d="M2 6.5l2.5 2.5L10 3.5" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round" />
                    </svg>
                    Completado
                  </span>
                ) : activo ? (
                  <span className="inline-flex shrink-0 items-center rounded-full border border-accent/45 bg-accent/15 px-2.5 py-[3px] text-[10.5px] font-bold text-accent">
                    Activo{progreso ? <> · <span className="text-done">{progreso.hechos}/{progreso.total}</span></> : ""}
                  </span>
                ) : (
                  /* Beta: sin candado. La tarjeta invita a ACTIVAR (gratis
                     hasta la ETAPA 2). El precio del catálogo se muestra tachado
                     al lado, para que se lea que es cortesía de beta y no que
                     siempre fue gratis. */
                  <span className="flex shrink-0 items-center gap-2">
                    <span className="text-[10.5px] font-medium text-dim/60 line-through">
                      {p.creditos_activar} créditos
                    </span>
                    <span className="inline-flex items-center rounded-full border border-accent/45 bg-accent/15 px-2.5 py-[3px] text-[10.5px] font-bold text-accent">
                      {activando === p.clave ? "Activando…" : "Activar · beta"}
                    </span>
                  </span>
                )}
              </div>
              <p className={"text-[15px] font-semibold" + (activo ? "" : " text-dim")}>{p.nombre}</p>
              <p className={"mt-1.5 text-[12.5px] leading-[1.55] [text-wrap:pretty] text-dim" + (activo ? "" : " opacity-75")}>
                {p.promesa}
              </p>
              {!activo && (
                <p className="mt-2 text-[12px] text-dim/70">
                  {errorEn === p.clave
                    ? "No pudimos activarlo; intenta de nuevo."
                    : "Gratis durante la beta · un toque lo activa"}
                </p>
              )}
            </button>
          );
        })}
      </div>
    </section>
  );
}
