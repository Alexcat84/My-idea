"use client";

/**
 * PotenciaTuIdea — la fila de potenciadores (canon 3.6, mockup 07 B):
 * Tus Números (2 créditos) + los tres mundos (3 créditos, candado).
 * Precios SIEMPRE desde precios.ts / packs_catalog.json — ninguna cifra
 * hardcodeada. Mundo con candado: tarjeta no-modal "Disponible
 * próximamente" + telemetría pack_clicks. Mundo con fila en
 * project_unlocks: chip verde "Activo · n/m" (el verde ejecuta) y va a
 * su sección en Manos a la Obra.
 */
import { useState } from "react";
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
  /** progreso del checklist por dominio (null si el mundo no arrancó) */
  progresoMundos: Record<string, { hechos: number; total: number } | null>;
  /** hay plan core: Tus Números disponible */
  conPlan: boolean;
  /** ver el mundo activo (lleva a Manos a la Obra) */
  onVerMundo: (dominio: string) => void;
  /** ir a la tarjeta Tus Números bajo el plan */
  onTusNumeros: () => void;
}

function Candado() {
  return (
    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden className="shrink-0 text-dim">
      <rect x="3" y="11" width="18" height="11" rx="2" />
      <path d="M7 11V7a5 5 0 0 1 10 0v4" />
    </svg>
  );
}

function ChipCreditos({ n }: { n: number }) {
  return (
    <span className="inline-flex shrink-0 items-center rounded-full border border-accent/45 px-2.5 py-1 text-[11px] font-bold text-accent">
      {n} créditos
    </span>
  );
}

export function PotenciaTuIdea({ projectId, unlocks, progresoMundos, conPlan, onVerMundo, onTusNumeros }: Props) {
  const [avisoEn, setAvisoEn] = useState<string | null>(null);
  const packs = (catalogo as { packs: Pack[] }).packs;

  function clickBloqueado(pack: Pack) {
    setAvisoEn(pack.clave);
    // fire-and-forget: la telemetría pack_clicks no bloquea nada
    fetch("/api/packs/interes", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ pack: pack.clave, project_id: projectId }),
    }).catch(() => {});
  }

  return (
    <section className="mt-2">
      <h3 className="text-base font-semibold">Potencia tu idea</h3>
      <p className="mt-1 text-sm text-dim">Conocimiento especializado que se suma a tu plan.</p>
      <div className="mt-3 flex flex-col gap-3">
        {/* Tus Números */}
        <button
          onClick={() => (conPlan ? onTusNumeros() : setAvisoEn("tus_numeros"))}
          className="rounded-cinta border border-hairline bg-surface px-5 py-4 text-left hover:border-accent/55"
          data-transiciona
        >
          <div className="flex items-center justify-between gap-3">
            <p className="font-medium">Tus Números</p>
            <ChipCreditos n={PRECIOS.tus_numeros} />
          </div>
          <p className="mt-1 text-sm text-dim">
            Tus cifras reales convertidas en margen, punto de equilibrio y escenarios.
          </p>
          {avisoEn === "tus_numeros" && (
            <p className="mt-2 text-sm text-accent">Disponible con tu plan: primero genera el plan de tu idea.</p>
          )}
        </button>

        {/* Los tres mundos */}
        {packs.map((p) => {
          const activo = unlocks.includes(p.clave);
          const progreso = progresoMundos[p.clave] ?? null;
          return (
            <button
              key={p.clave}
              onClick={() => (activo ? onVerMundo(p.clave) : clickBloqueado(p))}
              className={
                "rounded-cinta border bg-surface px-5 py-4 text-left " +
                (activo ? "border-done/30 hover:border-done/60" : "border-hairline hover:bg-surface-2")
              }
              data-transiciona
            >
              <div className="flex items-center justify-between gap-3">
                <p className="font-medium">{p.nombre}</p>
                {activo ? (
                  <span className="inline-flex shrink-0 items-center rounded-full border border-done/45 px-2.5 py-1 text-[11px] font-bold text-done">
                    {progreso ? `Activo · ${progreso.hechos}/${progreso.total}` : "Activo"}
                  </span>
                ) : (
                  <span className="flex shrink-0 items-center gap-2">
                    <ChipCreditos n={p.creditos_activar} />
                    <Candado />
                  </span>
                )}
              </div>
              <p className="mt-1 text-sm text-dim">{p.promesa}</p>
              {avisoEn === p.clave && !activo && (
                <p className="mt-2 text-sm text-accent">Disponible próximamente. Te avisaremos aquí mismo.</p>
              )}
            </button>
          );
        })}
      </div>
    </section>
  );
}
