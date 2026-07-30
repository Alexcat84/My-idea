"use client";

/**
 * Calendario — la cara del modo "con fechas" (canon nuevo, diseñado por Claude
 * Design). Fase 1: la vista AGENDA (la entrada recomendada): una sola columna
 * hacia adelante, agrupada relativa a HOY — Ya pasó y sigue abierto, Hoy,
 * Mañana, Esta semana, La próxima, Más adelante. Responde "¿qué toca ahora?".
 *
 * Reusa lo que ya existe: el icono de estado y el cajón de Detalle
 * (SelectorEstado / DetalleActividad), el endpoint de mover fecha con cascada,
 * el PATCH del checklist, y el generador .ics (Nivel 0: el aviso lo pone el
 * teléfono). Mes y Semana quedan para la fase 2 (el selector ya los anuncia).
 *
 * Ley de color: ámbar lo vencido (sin regaño), verde hoy/ejecutar, azul planear.
 */
import { useCallback, useEffect, useMemo, useState } from "react";
import { IconoEstado } from "./SelectorEstado";
import { DetalleActividad } from "./DetalleActividad";
import { grupoVigente, type CambioItem, type ChecklistData, type ItemChecklistUI } from "./ManosALaObra";
import { generarIcs } from "@/lib/ics";
import { fechaHumanaCorta, fechaInputLocal, isoDesdeInputLocal } from "@/lib/fechas";

const AZUL = "#4D7CFE";
const VERDE = "#3FB950";
const AMBAR = "#E0A64A";

/** ordinal del día (local) desde epoch, para comparar por DÍA sin la hora. */
function diaOrdinal(iso: string): number {
  const s = fechaInputLocal(new Date(iso));
  return Math.floor(new Date(`${s}T00:00:00`).getTime() / 86_400_000);
}
function hoyOrdinal(): number {
  return Math.floor(new Date(`${fechaInputLocal(new Date())}T00:00:00`).getTime() / 86_400_000);
}
const DIAS = ["domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado"];

type Grupo = "vencidas" | "hoy" | "manana" | "semana" | "proxima" | "adelante";
const ORDEN_GRUPOS: Grupo[] = ["vencidas", "hoy", "manana", "semana", "proxima", "adelante"];
const ROTULO: Record<Grupo, string> = {
  vencidas: "Ya pasó y sigue abierto",
  hoy: "Hoy",
  manana: "Mañana",
  semana: "Esta semana",
  proxima: "La próxima semana",
  adelante: "Más adelante",
};

function grupoDe(delta: number): Grupo {
  if (delta < 0) return "vencidas";
  if (delta === 0) return "hoy";
  if (delta === 1) return "manana";
  if (delta <= 7) return "semana";
  if (delta <= 14) return "proxima";
  return "adelante";
}
/** "hace 6 días" / "hoy" / "mañana" / "en 3 días" */
function relativo(delta: number): string {
  if (delta === 0) return "hoy";
  if (delta === 1) return "mañana";
  if (delta === -1) return "ayer";
  if (delta < 0) return `hace ${-delta} días`;
  return `en ${delta} días`;
}

export function Calendario({
  projectId,
  onVolver,
  onVerLoCumplido,
}: {
  projectId: string;
  onVolver: () => void;
  /** puerta a "Tu constancia" (vive en el Análisis) */
  onVerLoCumplido: () => void;
}) {
  const [checklist, setChecklist] = useState<ChecklistData | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [ocupado, setOcupado] = useState(false);
  const [detalle, setDetalle] = useState<{ item: ItemChecklistUI; tituloEtapa: string } | null>(null);

  const cargar = useCallback(() => {
    fetch(`/api/project/${projectId}/checklist`)
      .then((r) => (r.ok ? r.json() : Promise.reject(new Error(String(r.status)))))
      .then((d: ChecklistData) => setChecklist(d))
      .catch(() => setError("No pudimos cargar tu calendario. Vuelve a intentarlo en un momento."));
  }, [projectId]);
  useEffect(() => cargar(), [cargar]);

  const core = checklist ? grupoVigente(checklist, "core") : null;
  const itemsCore = useMemo(() => core?.etapas.flatMap((e) => e.items) ?? [], [core]);

  async function moverFecha(itemId: string, fecha: string, cascada: boolean) {
    setError(null);
    try {
      const res = await fetch(`/api/project/${projectId}/mover-fecha`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ item_id: itemId, fecha, cascada }),
      });
      if (!res.ok) return setError("No pudimos mover la fecha.");
      cargar();
    } catch {
      setError("No pudimos mover la fecha; revisa tu internet.");
    }
  }
  async function aplicarCambio(item: ItemChecklistUI, cambio: CambioItem) {
    setOcupado(true);
    setError(null);
    try {
      const res = await fetch(`/api/project/${projectId}/checklist`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ item_id: item.id, ...cambio }),
      });
      if (!res.ok) return setError("No pudimos guardar el cambio.");
      cargar();
      setDetalle(null);
    } catch {
      setError("No pudimos guardar; revisa tu internet.");
    } finally {
      setOcupado(false);
    }
  }

  function descargarCalendario() {
    const tareas = itemsCore
      .filter((i) => i.fecha_base && i.estado !== "hecho" && i.estado !== "no_aplica")
      .map((i) => ({ id: i.id, texto: i.texto, etapa: i.etapa, fechaBase: i.fecha_base! }));
    const ics = generarIcs({ nombreIdea: "Mi idea", tareas });
    const blob = new Blob([ics], { type: "text/calendar;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "mi-idea-calendario.ics";
    a.click();
    URL.revokeObjectURL(url);
  }

  if (error && !checklist) return <p className="text-sm text-warn">{error}</p>;
  if (!checklist) return <p className="text-dim">Cargando tu calendario…</p>;

  const hoy = hoyOrdinal();
  // "Lo que viene": tareas con fecha, aún abiertas (hecha/no_aplica salen).
  const pendientes = itemsCore
    .filter((i) => i.fecha_base && i.estado !== "hecho" && i.estado !== "no_aplica")
    .map((i) => ({ item: i, delta: diaOrdinal(i.fecha_base!) - hoy }))
    .sort((a, b) => a.delta - b.delta);
  const porGrupo = new Map<Grupo, typeof pendientes>();
  for (const p of pendientes) {
    const g = grupoDe(p.delta);
    (porGrupo.get(g) ?? porGrupo.set(g, []).get(g)!).push(p);
  }
  const sinFecha = itemsCore.filter((i) => !i.fecha_base && i.estado !== "hecho" && i.estado !== "no_aplica").length;
  const conAviso = pendientes.length; // Nivel 0: todas las pendientes con fecha llevan aviso en el .ics
  const hoyLabel = `${DIAS[new Date().getDay()]} ${fechaHumanaCorta(new Date().toISOString())}`;

  const colorGrupo = (g: Grupo) => (g === "vencidas" ? AMBAR : g === "hoy" ? VERDE : "#A6A7AD");

  return (
    <section className="mx-auto flex w-full max-w-[1120px] flex-col gap-6 lg:flex-row lg:items-start">
      <div className="min-w-0 flex-1">
        <button onClick={onVolver} className="mb-4 text-sm text-dim hover:text-ink">
          ← Volver
        </button>
        <p className="mb-2 flex items-center gap-2.5 text-[12px] font-semibold uppercase tracking-[1.5px]" style={{ color: AZUL }}>
          <span aria-hidden className="h-[7px] w-[7px] rounded-full" style={{ background: AZUL }} />
          Tu calendario
        </p>
        <div className="mb-5 flex flex-wrap items-center justify-between gap-3">
          <h2 className="text-[28px] font-bold leading-tight tracking-[-0.02em]">Lo que viene</h2>
          {/* selector de vista: Agenda activa; Mes/Semana llegan en la fase 2 */}
          <div className="inline-flex items-center gap-1 rounded-full border border-hairline p-1 text-[13px]">
            <span className="cursor-not-allowed rounded-full px-3 py-1 text-dim/70" title="Próximamente">
              Mes
            </span>
            <span className="cursor-not-allowed rounded-full px-3 py-1 text-dim/70" title="Próximamente">
              Semana
            </span>
            <span className="rounded-full bg-accent/20 px-3 py-1 font-semibold text-accent">Agenda</span>
          </div>
        </div>

        {error && <p className="mb-3 text-sm text-warn">{error}</p>}

        {pendientes.length === 0 ? (
          <p className="rounded-panel border border-hairline bg-surface p-6 text-[14px] leading-relaxed text-dim">
            No tienes tareas con fecha por delante. Cuando pongas fechas a tus tareas, aquí verás qué toca y cuándo.
          </p>
        ) : (
          <div className="flex flex-col gap-7">
            {ORDEN_GRUPOS.filter((g) => porGrupo.get(g)?.length).map((g) => {
              const filas = porGrupo.get(g)!;
              return (
                <div key={g}>
                  <div className="mb-3 flex items-center gap-3">
                    <span className="text-[12px] font-semibold uppercase tracking-[1.2px]" style={{ color: colorGrupo(g) }}>
                      {ROTULO[g]}
                    </span>
                    <span className="h-px flex-1" style={{ background: g === "vencidas" ? "rgba(224,166,74,0.30)" : g === "hoy" ? "rgba(63,185,80,0.28)" : "rgba(255,255,255,0.08)" }} />
                    <span className="text-[12px] tabular-nums text-dim">{filas.length}</span>
                  </div>
                  <div className="flex flex-col gap-2.5">
                    {filas.map(({ item, delta }) => (
                      <FilaAgenda
                        key={item.id}
                        item={item}
                        delta={delta}
                        grupo={g}
                        onDetalle={() => setDetalle({ item, tituloEtapa: `Etapa ${item.etapa}` })}
                        onMarcarHecha={() => aplicarCambio(item, { estado: "hecho", completed_at: isoDesdeInputLocal(fechaInputLocal(new Date())) })}
                      />
                    ))}
                  </div>
                </div>
              );
            })}

            {sinFecha > 0 && (
              <div className="flex flex-wrap items-center justify-between gap-3 rounded-cinta border border-dashed border-hairline px-4 py-3 text-[13px] text-dim">
                <span>
                  Después de esto, <span className="font-semibold text-ink tabular-nums">{sinFecha}</span> tarea{sinFecha === 1 ? "" : "s"} sigue{sinFecha === 1 ? "" : "n"} sin fecha.
                </span>
                <button onClick={onVolver} className="font-semibold text-accent hover:underline">
                  Ponerles fecha
                </button>
              </div>
            )}
          </div>
        )}
      </div>

      {/* aside */}
      <aside className="flex w-full flex-col gap-4 lg:w-[348px] lg:shrink-0">
        <div className="rounded-panel border border-hairline bg-surface p-5">
          <div className="flex items-center justify-between gap-2">
            <p className="text-[14px] font-semibold">Tus recordatorios</p>
            <span className="rounded-full border border-done/50 px-2.5 py-0.5 text-[10.5px] font-semibold uppercase tracking-[0.6px] text-done">
              Activados
            </span>
          </div>
          <p className="mt-2 text-[12.5px] leading-relaxed text-dim">La víspera a las 20:00, en el calendario de tu teléfono.</p>
          <p className="mt-3 flex items-baseline justify-between text-[13px]">
            <span className="text-dim">Tareas con aviso</span>
            <span className="font-semibold tabular-nums">{conAviso} de {pendientes.length}</span>
          </p>
        </div>

        <div className="rounded-panel border border-hairline bg-surface p-5">
          <p className="text-[14px] font-semibold">Llévatelo al teléfono</p>
          <p className="mt-2 text-[12.5px] leading-relaxed text-dim">
            Añade tus fechas al calendario que ya usas. El aviso lo pone tu teléfono, aunque no abras la app.
          </p>
          <button
            onClick={descargarCalendario}
            disabled={pendientes.length === 0}
            className="mt-3 w-full rounded-[11px] bg-done py-2.5 text-[13.5px] font-bold text-[#04120A] hover:opacity-90 disabled:opacity-50"
          >
            Añadir a mi calendario
          </button>
          <button
            disabled
            title="Próximamente"
            className="mt-2 w-full cursor-not-allowed rounded-[11px] border border-hairline py-2.5 text-[13px] font-semibold text-dim/70"
          >
            Conectar mi cuenta de Google
          </button>
        </div>

        <div className="rounded-panel border border-hairline bg-surface p-5">
          <p className="text-[14px] font-semibold">Tu constancia</p>
          <p className="mt-2 text-[12.5px] leading-relaxed text-dim">Los días que ya avanzaste viven en el análisis, en la vista de atrás.</p>
          <button
            onClick={onVerLoCumplido}
            className="mt-3 w-full rounded-[11px] border border-accent/50 py-2.5 text-[13px] font-semibold text-accent hover:bg-accent/10"
          >
            Ver lo cumplido
          </button>
        </div>
        <p className="px-1 text-[11px] leading-relaxed text-dim/70">
          Hoy es {hoyLabel}. El aviso llega desde el archivo que añades a tu teléfono.
        </p>
      </aside>

      {detalle && (
        <DetalleActividad
          item={detalle.item}
          tituloEtapa={detalle.tituloEtapa}
          ocupado={ocupado}
          onCambio={(cambio) => aplicarCambio(detalle.item, cambio)}
          onMoverFecha={(fecha, cascada) => {
            moverFecha(detalle.item.id, fecha, cascada);
            setDetalle(null);
          }}
          itemsDominio={itemsCore}
          onCerrar={() => setDetalle(null)}
        />
      )}
    </section>
  );
}

/** Una fila de la agenda: fecha (relativa + absoluta), estado, etapa + texto y
 * las acciones según el grupo. */
function FilaAgenda({
  item,
  delta,
  grupo,
  onDetalle,
  onMarcarHecha,
}: {
  item: ItemChecklistUI;
  delta: number;
  grupo: Grupo;
  onDetalle: () => void;
  onMarcarHecha: () => void;
}) {
  const borde =
    grupo === "vencidas"
      ? "border-warn/45 bg-warn/[0.07]"
      : grupo === "hoy"
        ? "border-done/30 bg-done/[0.05]"
        : "border-hairline bg-surface";
  const colorFecha = grupo === "vencidas" ? "text-warn" : grupo === "hoy" ? "text-done" : "text-ink";
  return (
    <div className={"grid grid-cols-[88px_34px_1fr] items-center gap-3 rounded-[12px] border px-[18px] py-3.5 sm:grid-cols-[96px_34px_1fr_auto] " + borde}>
      <div className="min-w-0">
        <div className={"text-[13.5px] font-semibold capitalize " + colorFecha}>{relativo(delta)}</div>
        <div className="text-[11.5px] text-dim">{fechaHumanaCorta(item.fecha_base!)}</div>
      </div>
      <button onClick={onDetalle} className="justify-self-center" title="Ver el detalle" aria-label="Ver el detalle de la tarea">
        <IconoEstado estado={item.estado} tamano={22} />
      </button>
      <div className="min-w-0">
        <div className="text-[11px] font-semibold uppercase tracking-[1px] text-accent">Etapa {item.etapa}</div>
        <div className="text-[14.5px] leading-snug [text-wrap:pretty]">{item.texto}</div>
      </div>
      <div className="col-span-3 flex flex-wrap items-center gap-2 sm:col-span-1 sm:justify-end">
        {grupo === "hoy" && (
          <button
            onClick={onMarcarHecha}
            className="rounded-[9px] bg-done px-3.5 py-1.5 text-[12.5px] font-bold text-[#04120A] hover:opacity-90"
          >
            Marcar hecha
          </button>
        )}
        <button
          onClick={onDetalle}
          className="rounded-[9px] border border-accent/40 bg-accent/10 px-3.5 py-1.5 text-[12.5px] font-semibold text-accent hover:bg-accent/20"
        >
          {grupo === "vencidas" ? "Ponerle fecha nueva" : "Mover fecha"}
        </button>
        <button onClick={onDetalle} className="rounded-[9px] border border-hairline px-3.5 py-1.5 text-[12.5px] font-semibold text-dim hover:text-ink">
          Detalle
        </button>
      </div>
    </div>
  );
}
