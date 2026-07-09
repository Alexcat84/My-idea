"use client";

/**
 * MundosAddOn — las tres tarjetas con candado (brief sección 4): nombres
 * de valor y línea de promesa desde el catálogo ESTÁTICO (nunca leyendo
 * nodos). Click → "Disponible próximamente" + registro de telemetría.
 */
import { useState } from "react";
import catalogo from "@/lib/assets/packs_catalog.json";

interface Pack {
  clave: string;
  nombre: string;
  promesa: string;
}

export function MundosAddOn({ projectId }: { projectId: string }) {
  const [avisoEn, setAvisoEn] = useState<string | null>(null);
  const packs = (catalogo as { packs: Pack[] }).packs;

  function click(pack: Pack) {
    setAvisoEn(pack.clave);
    // fire-and-forget: la telemetría no bloquea nada
    fetch("/api/packs/interes", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ pack: pack.clave, project_id: projectId }),
    }).catch(() => {});
  }

  return (
    <section className="mt-2">
      <h3 className="text-base font-semibold">Mundos para tu idea</h3>
      <p className="mt-1 text-sm text-dim">Conocimiento especializado que se suma a tu plan.</p>
      <div className="mt-3 flex flex-col gap-3">
        {packs.map((p) => (
          <button
            key={p.clave}
            onClick={() => click(p)}
            className="rounded-cinta border border-hairline bg-surface px-5 py-4 text-left hover:bg-surface-2"
          >
            <div className="flex items-center justify-between gap-3">
              <p className="font-medium">{p.nombre}</p>
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden className="shrink-0 text-dim">
                <rect x="3" y="11" width="18" height="11" rx="2" />
                <path d="M7 11V7a5 5 0 0 1 10 0v4" />
              </svg>
            </div>
            <p className="mt-1 text-sm text-dim">{p.promesa}</p>
            {avisoEn === p.clave && (
              <p className="mt-2 text-sm text-accent">Disponible próximamente — anotamos tu interés.</p>
            )}
          </button>
        ))}
      </div>
    </section>
  );
}
