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
import { elegir, type Locale } from "@/lib/i18n/config";
import { useIdioma } from "@/lib/i18n/IdiomaProvider";
import { interpolar } from "@/lib/i18n/interpolar";
import { CORREGIR_CIFRAS } from "@/lib/i18n/mensajes/corregirCifras";
import { pluralDe } from "@/lib/pluralUnidad";

type Valor = number | { min: number; max: number };
type TextosCorregir = (typeof CORREGIR_CIFRAS)["es"];
type ClaveCampo = keyof TextosCorregir["campos"];
/** La etiqueta y el porqué salen del catálogo por la clave del campo. */
type Campo = { clave: ClaveCampo; porque?: keyof TextosCorregir["porque"] };

const CAMPOS_CORE: Campo[] = [
  { clave: "costo_materiales_unidad" },
  { clave: "horas_por_unidad" },
  { clave: "valor_hora" },
  { clave: "precio_tentativo" },
  { clave: "capacidad_semanal" },
  { clave: "costos_fijos_mensuales" },
  { clave: "unidades_vendidas" },
];

// El ciclo de conversión de efectivo: opcional, afina la foto de caja.
const CAMPOS_CICLO: Campo[] = [
  { clave: "dias_inventario", porque: "dias_inventario" },
  { clave: "dias_cobro_clientes", porque: "dias_cobro_clientes" },
  { clave: "dias_pago_proveedores", porque: "dias_pago_proveedores" },
];

const etiquetaDe = (t: TextosCorregir, clave: ClaveCampo, u: string, idioma: Locale) =>
  interpolar(t.campos[clave], { u, unidades: pluralDe(u, idioma) });

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
  const idioma = useIdioma();
  const t = elegir(CORREGIR_CIFRAS, idioma);
  return (
    <label className="flex flex-col gap-1.5 text-[13px]">
      <span className="text-dim">{etiquetaDe(t, campo.clave, u, idioma)}</span>
      <input
        id={`corregir-${campo.clave}`}
        inputMode="decimal"
        value={valor}
        onChange={(e) => onCambio(e.target.value)}
        placeholder="—"
        className="rounded-cinta border border-hairline bg-surface-2 px-3 py-2 text-ink outline-none focus:border-accent/60"
      />
      {campo.porque && <span className="text-[12px] text-dim/80">{t.porque[campo.porque]}</span>}
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
  const idioma = useIdioma();
  const t = elegir(CORREGIR_CIFRAS, idioma);
  const u = unidad || t.unidadPorDefecto;
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
      const limpio = texto.trim();
      if (limpio === "") continue;
      const n = Number(limpio.replace(",", "."));
      if (!Number.isFinite(n) || n < 0) {
        // `valores` nace de TODOS: cada clave tiene su campo.
        const campo = TODOS.find((c) => c.clave === clave)!;
        setError(interpolar(t.errorNumero, { campo: etiquetaDe(t, campo.clave, u, idioma) }));
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
        setError(((await r.json()) as { error?: string }).error ?? t.errorGuardar);
        setGuardando(false);
        return;
      }
      onGuardado(await r.json());
    } catch {
      setError(t.errorConectar);
      setGuardando(false);
    }
  }

  return (
    <div ref={contenedor} className="rounded-panel border border-accent/40 bg-surface p-6">
      <h3 className="text-[15px] font-bold">{t.titulo}</h3>
      <p className="mt-1 text-[13px] leading-relaxed text-dim">{t.intro}</p>

      <div className="mt-4 grid gap-3.5 sm:grid-cols-2">
        {CAMPOS_CORE.map((c) => (
          <CampoInput key={c.clave} campo={c} u={u} valor={valores[c.clave]} onCambio={(v) => setValores((s) => ({ ...s, [c.clave]: v }))} />
        ))}
      </div>

      <div className="mt-6 border-t border-hairline pt-5">
        <p className="text-[13px] font-semibold">{t.cicloTitulo}</p>
        <p className="mt-1 text-[12.5px] leading-relaxed text-dim">{t.cicloIntro}</p>
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
          className="rounded-cinta border border-accent/40 bg-accent/10 px-5 py-2.5 text-sm font-medium text-accent hover:bg-accent/20 disabled:opacity-50"
        >
          {guardando ? t.calculando : t.volverACalcular}
        </button>
        <button onClick={onCancelar} disabled={guardando} className="rounded-cinta border border-accent/40 bg-accent/10 text-accent hover:bg-accent/20 px-5 py-2.5 text-sm font-medium disabled:opacity-50">
          {t.cancelar}
        </button>
      </div>
    </div>
  );
}
