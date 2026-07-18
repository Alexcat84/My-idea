"use client";

/**
 * CorregirCifras.tsx - FASE B (canon 14): el recolector. Las cifras de Tus
 * Números son EDITABLES siempre. Se PRE-LLENA con lo último que declaró el
 * usuario (nunca en blanco); al guardar, POST /numeros recalcula gratis,
 * inserta una versión nueva (la vieja queda archivada) y devuelve el tablero
 * ya con el guardián GIGO cruzado sobre las cifras nuevas.
 *
 * La puerta de los faltantes: cada ítem faltante del tablero abre este
 * recolector DIRECTO en su campo (`campoInicial`). Los datos del ciclo de caja
 * (cobro/inventario/pago) van al final como OPCIONALES: si los tienes, afinan
 * tu foto de caja; si no, sigues sin ellos.
 */
import { useEffect, useRef, useState } from "react";

type Valor = number | { min: number; max: number };
type Campo = { clave: string; etiqueta: (u: string) => string; porque?: string };

const CAMPOS_CORE: Campo[] = [
  { clave: "costo_materiales_unidad", etiqueta: (u) => `Costo de materiales por ${u}` },
  { clave: "horas_por_unidad", etiqueta: (u) => `Horas de trabajo por ${u}` },
  { clave: "valor_hora", etiqueta: () => "Cuánto vale tu hora" },
  { clave: "precio_tentativo", etiqueta: (u) => `Precio al que vendes cada ${u}` },
  { clave: "capacidad_semanal", etiqueta: (u) => `Cuántas ${u}s haces por semana` },
  { clave: "costos_fijos_mensuales", etiqueta: () => "Tu gasto fijo mensual" },
  { clave: "unidades_vendidas", etiqueta: (u) => `Cuántas ${u}s vendes al mes (o tu meta)` },
];

// El ciclo de conversión de efectivo: opcional, afina la foto de caja.
const CAMPOS_CICLO: Campo[] = [
  { clave: "dias_inventario", etiqueta: () => "Días que tu dinero pasa en inventario", porque: "afecta cuándo vuelve la plata a tu bolsillo" },
  { clave: "dias_cobro_clientes", etiqueta: () => "Días que tardas en cobrar", porque: "cobrar tarde aprieta tu caja" },
  { clave: "dias_pago_proveedores", etiqueta: () => "Días que tardas en pagar a proveedores", porque: "pagar más tarde alivia tu caja" },
];

const TODOS = [...CAMPOS_CORE, ...CAMPOS_CICLO];

function aTexto(v: Valor | undefined): string {
  if (v === undefined) return "";
  if (typeof v === "object") return String((v.min + v.max) / 2);
  return String(v);
}

function CampoInput({
  campo,
  u,
  valor,
  onCambio,
}: {
  campo: Campo;
  u: string;
  valor: string;
  onCambio: (v: string) => void;
}) {
  return (
    <label className="flex flex-col gap-1.5 text-[13px]">
      <span className="text-dim">{campo.etiqueta(u)}</span>
      <input
        id={`corregir-${campo.clave}`}
        inputMode="decimal"
        value={valor}
        onChange={(e) => onCambio(e.target.value)}
        placeholder="—"
        className="rounded-cinta border border-hairline bg-surface-2 px-3 py-2 text-ink outline-none focus:border-accent/60"
      />
      {campo.porque && <span className="text-[12px] text-dim/80">{campo.porque}</span>}
    </label>
  );
}

export function CorregirCifras({
  projectId,
  unidad,
  declaradas,
  campoInicial,
  onGuardado,
  onCancelar,
}: {
  projectId: string;
  unidad: string;
  declaradas: Record<string, Valor>;
  /** Si viene, el recolector abre con foco en ese campo (la puerta de un faltante). */
  campoInicial?: string | null;
  onGuardado: (payload: unknown) => void;
  onCancelar: () => void;
}) {
  const u = unidad || "unidad";
  const [valores, setValores] = useState<Record<string, string>>(() =>
    Object.fromEntries(TODOS.map((c) => [c.clave, aTexto(declaradas[c.clave])]))
  );
  const [guardando, setGuardando] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const contenedor = useRef<HTMLDivElement>(null);

  // La puerta: al abrir desde un faltante, enfoca su campo (y lo trae a la vista).
  useEffect(() => {
    if (!campoInicial) return;
    const el = contenedor.current?.querySelector<HTMLInputElement>(`#corregir-${campoInicial}`);
    if (el) {
      el.focus({ preventScroll: true });
      el.scrollIntoView({ behavior: "smooth", block: "center" });
    }
  }, [campoInicial]);

  async function guardar() {
    setGuardando(true);
    setError(null);
    const numeros: Record<string, number> = {};
    for (const [clave, texto] of Object.entries(valores)) {
      const t = texto.trim();
      if (t === "") continue;
      const n = Number(t.replace(",", "."));
      if (!Number.isFinite(n) || n < 0) {
        setError(`Revisa "${TODOS.find((c) => c.clave === clave)?.etiqueta(u)}": debe ser un número de 0 en adelante.`);
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
    <div ref={contenedor} className="rounded-panel border border-accent/40 bg-surface p-6">
      <h3 className="text-[15px] font-bold">Corrige tus cifras</h3>
      <p className="mt-1 text-[13px] leading-relaxed text-dim">
        Ajusta lo que cambió y vuelve a calcular. El recálculo es gratis e ilimitado; tus versiones anteriores quedan
        guardadas con su fecha.
      </p>

      <div className="mt-4 grid gap-3.5 sm:grid-cols-2">
        {CAMPOS_CORE.map((c) => (
          <CampoInput key={c.clave} campo={c} u={u} valor={valores[c.clave]} onCambio={(v) => setValores((s) => ({ ...s, [c.clave]: v }))} />
        ))}
      </div>

      <div className="mt-6 border-t border-hairline pt-5">
        <p className="text-[13px] font-semibold">Tu ciclo de caja (opcional)</p>
        <p className="mt-1 text-[12.5px] leading-relaxed text-dim">
          Si los tienes, afinan tu foto de caja; si no, sigue sin ellos.
        </p>
        <div className="mt-3.5 grid gap-3.5 sm:grid-cols-3">
          {CAMPOS_CICLO.map((c) => (
            <CampoInput key={c.clave} campo={c} u={u} valor={valores[c.clave]} onCambio={(v) => setValores((s) => ({ ...s, [c.clave]: v }))} />
          ))}
        </div>
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
