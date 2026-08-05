"use client";

/**
 * ElegirPotenciador — el paso 2 del acceso "Potenciar mis ideas": la pantalla
 * enfocada donde se elige el potenciador para la idea ya elegida, y nada más.
 *
 * LA REGLA QUE ESTA PANTALLA HONRA (fundador, ago 2026, no discutible): no hay
 * dos versiones de lo mismo. Aquí NO vive ninguna parrilla propia: se renderiza
 * EL MISMO componente `PotenciaTuIdea` que la fila de la idea, alimentado por
 * las MISMAS APIs y los MISMOS derivadores (estadoMundo, grupoVigente). Esta
 * página solo pone la puerta y el foco.
 *
 * El final del camino (fundador): elegir el potenciador y aplicarlo. Al
 * activarse, el mundo queda agregado al menú de la idea principal y se navega
 * a su hub: a partir de ese momento, todo sigue igual que siempre.
 */
import { useEffect, useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import catalogo from "@/lib/assets/packs_catalog.json";
import { estadoMundo, type EstadoMundo } from "@/lib/engine/previewMundos";
import { PotenciaTuIdea } from "@/app/ui/PotenciaTuIdea";
import { grupoVigente, type ChecklistData } from "@/app/ui/ManosALaObra";

interface MundoDetalle {
  dominio: string;
  plan?: unknown;
  completado_at?: string | null;
  resumen_md?: string | null;
  resumen_at?: string | null;
  preview_session_id?: string | null;
  plan_pagado_at?: string | null;
}

interface DetalleLite {
  idea: { nombre: string };
  plan?: unknown;
  unlocks?: string[];
  mundos?: MundoDetalle[];
}

const ERROR = "no pudimos cargar tu idea; intenta de nuevo en un momento";

export function ElegirPotenciador({ ideaId }: { ideaId: string }) {
  const router = useRouter();
  const [detalle, setDetalle] = useState<DetalleLite | null>(null);
  const [checklist, setChecklist] = useState<ChecklistData | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let vivo = true;
    (async () => {
      try {
        const [rIdea, rChecklist] = await Promise.all([
          fetch(`/api/idea/${ideaId}`),
          fetch(`/api/project/${ideaId}/checklist`),
        ]);
        if (!rIdea.ok) throw new Error(String(rIdea.status));
        const d = (await rIdea.json()) as DetalleLite;
        const c = rChecklist.ok ? ((await rChecklist.json()) as ChecklistData) : null;
        if (!vivo) return;
        setDetalle(d);
        setChecklist(c);
      } catch {
        if (vivo) setError(ERROR);
      }
    })();
    return () => {
      vivo = false;
    };
  }, [ideaId]);

  if (error) return <p className="text-sm text-warn">{error}</p>;
  if (!detalle) return <p className="text-sm text-dim">Cargando tu idea…</p>;

  // Los MISMOS derivadores que usa la idea (fuente única de la máquina de
  // estados y del progreso): nada se recalcula con reglas propias.
  const unlocks = detalle.unlocks ?? [];
  const hayPlanCore = Boolean(detalle.plan);
  const estadosMundo: Record<string, EstadoMundo> = Object.fromEntries(
    (catalogo as { packs: Array<{ clave: string }> }).packs.map((p) => [
      p.clave,
      estadoMundo(detalle.mundos?.find((x) => x.dominio === p.clave) ?? null, hayPlanCore),
    ])
  );
  const progresoMundos: Record<string, { hechos: number; total: number } | null> = {};
  for (const u of unlocks) {
    const g = checklist ? grupoVigente(checklist, u) : null;
    const items = g?.etapas.flatMap((e) => e.items) ?? [];
    progresoMundos[u] = g ? { hechos: items.filter((i) => i.estado === "hecho").length, total: items.length } : null;
  }
  const mundosCompletados = (detalle.mundos ?? []).filter((m) => m.completado_at).map((m) => m.dominio);

  // Aplicado el potenciador (o abierto uno ya activo): a la idea, al hub de ese
  // mundo. Desde ahí, todo sigue igual que siempre.
  const irAlMundo = (dominio: string) => router.push(`/idea/${ideaId}?vista=mundo&dominio=${dominio}`);

  return (
    <section className="anima-plan-in">
      <Link href="/potenciadores" className="text-[13px] text-dim hover:text-ink">
        ← Cambiar de idea
      </Link>
      <h1 className="mt-2 text-2xl font-bold tracking-tight">¿Qué potenciador quieres usar?</h1>
      <p className="mt-2 max-w-2xl text-[15px] leading-relaxed text-dim">
        Para <span className="font-semibold text-ink">{detalle.idea.nombre}</span>. Al aplicarlo queda agregado a tu
        idea, y sigues desde ahí.
      </p>
      <div className="mt-6">
        <PotenciaTuIdea
          projectId={ideaId}
          unlocks={unlocks}
          estadosMundo={estadosMundo}
          progresoMundos={progresoMundos}
          mundosCompletados={mundosCompletados}
          onVerMundo={irAlMundo}
          onActivarMundo={irAlMundo}
        />
      </div>
    </section>
  );
}
