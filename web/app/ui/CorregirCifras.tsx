"use client";

/**
 * CorregirCifras.tsx - FASE B (canon 14): el recolector. Las cifras de Tus
 * Numeros son EDITABLES siempre. Se PRE-LLENA con lo ultimo que declaro el
 * usuario (nunca en blanco); al guardar, POST /numeros recalcula gratis,
 * inserta una version nueva (la vieja queda archivada) y devuelve el tablero
 * ya con el guardian GIGO cruzado sobre las cifras nuevas.
 */
import { useState } from "react";

type Valor = number | { min: number; max: number };

const CAMPOS: Array<{ clave: string; etiqueta: (u: string) => string }> = [
  { clave: "costo_materiales_unidad", etiqueta: (u) => `Costo de materiales por ${u}` },
  { clave: "horas_por_unidad", etiqueta: (u) => `Horas de trabajo por ${u}` },
  { clave: "valor_hora", etiqueta: () => "Cuanto vale tu hora" },
  { clave: "precio_tentativo", etiqueta: (u) => `Precio al que vendes cada ${u}` },
  { clave: "capacidad_semanal", etiqueta: (u) => `Cuantas ${u}s haces por semana` },
  { clave: "costos_fijos_mensuales", etiqueta: () => "Tu gasto fijo mensual" },
  { clave: "unidades_vendidas", etiqueta: (u) => `Cuantas ${u}s vendes al mes (o tu meta)` },
];

function aTexto(v: Valor | undefined): string {
  if (v === undefined) return "";
  if (typeof v === "object") return String((v.min + v.max) / 2);
  return String(v);
}

export function CorregirCifras({
  projectId,
  unidad,
  declaradas,
  onGuardado,
  onCancelar,
}: {
  projectId: string;
  unidad: string;
  declaradas: Record<string, Valor>;
  onGuardado: (payload: unknown) => void;
  onCancelar: () => void;
}) {
  const u = unidad || "unidad";
  const [valores, setValores] = useState<Record<string, string>>(() =>
    Object.fromEntries(CAMPOS.map((c) => [c.clave, aTexto(declaradas[c.clave])]))
  );
  const [guardando, setGuardando] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function guardar() {
    setGuardando(true);
    setError(null);
    const numeros: Record<string, number> = {};
    for (const [clave, texto] of Object.entries(valores)) {
      const t = texto.trim();
      if (t === "") continue;
      const n = Number(t.replace(",", "."));
      if (!Number.isFinite(n) || n < 0) {
        setError(`Revisa "${CAMPOS.find((c) => c.clave === clave)?.etiqueta(u)}": debe ser un numero de 0 en adelante.`);
        setGuardando(false);
        return;
      }
      numeros[clave] = n;
    }
    try {
      const r = await fetch(`/api/project/${projectId}/numeros`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ numeros }),
      });
      if (!r.ok) {
        setError(((await r.json()) as { error?: string }).error ?? "no pudimos guardar tus cifras");
        setGuardando(false);
        return;
      }
      onGuardado(await r.json());
    } catch {
      setError("no pudimos conectar; revisa tu internet e intenta de nuevo");
      setGuardando(false);
    }
  }

  return (
    <div className="rounded-panel border border-accent/40 bg-surface p-6">
      <h3 className="text-[15px] font-bold">Corrige tus cifras</h3>
      <p className="mt-1 text-[13px] leading-relaxed text-dim">
        Ajusta lo que cambio y vuelve a calcular. El recalculo es gratis e ilimitado; tus versiones anteriores quedan guardadas
        con su fecha.
      </p>
      <div className="mt-4 grid gap-3.5 sm:grid-cols-2">
        {CAMPOS.map((c) => (
          <label key={c.clave} className="flex flex-col gap-1.5 text-[13px]">
            <span className="text-dim">{c.etiqueta(u)}</span>
            <input
              inputMode="decimal"
              value={valores[c.clave]}
              onChange={(e) => setValores((v) => ({ ...v, [c.clave]: e.target.value }))}
              placeholder="—"
              className="rounded-cinta border border-hairline bg-surface-2 px-3 py-2 text-ink outline-none focus:border-accent/60"
            />
          </label>
        ))}
      </div>
      {error && <p className="mt-3 text-[13px] text-warn">{error}</p>}
      <div className="mt-5 flex items-center gap-3">
        <button
          onClick={guardar}
          disabled={guardando}
          className="rounded-cinta bg-accent px-5 py-2.5 text-sm font-medium text-white hover:opacity-90 disabled:opacity-50"
        >
          {guardando ? "Calculando…" : "Volver a calcular"}
        </button>
        <button onClick={onCancelar} disabled={guardando} className="text-sm text-dim hover:text-ink disabled:opacity-50">
          Cancelar
        </button>
      </div>
    </div>
  );
}
