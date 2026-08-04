"use client";

/**
 * Calendario — la cara del modo "con fechas" (diseño de Claude Design). Tres
 * vistas de una misma verdad (las tareas del plan con fecha), con selector:
 *   - Agenda (entrada): una columna hacia adelante, agrupada relativa a HOY.
 *   - Mes: la rejilla reconocible, huecos y racimos de un vistazo.
 *   - Semana: los siete días en columnas.
 *
 * Reusa el icono de estado y el cajón de Detalle (SelectorEstado /
 * DetalleActividad), el endpoint de mover fecha con cascada, el PATCH del
 * checklist, y el generador .ics (Nivel 0: el aviso lo pone el teléfono).
 *
 * Ley de color: ámbar lo vencido (sin regaño), verde hoy/hecho/ejecutar, azul
 * prevista/planear; gris lo que falta.
 */
import { useMemo, useState } from "react";
import { IconoEstado } from "./SelectorEstado";
import { DetalleActividad } from "./DetalleActividad";
import { NotaRapida } from "./NotaRapida";
import { SuscripcionCalendario } from "./SuscripcionCalendario";
import { grupoVigente, type CambioItem, type ChecklistData, type ItemChecklistUI } from "./ManosALaObra";
import { generarIcs } from "@/lib/ics";
import { fechaHumanaCorta, fechaInputLocal, isoDesdeInputLocal } from "@/lib/fechas";
import catalogo from "@/lib/assets/packs_catalog.json";

// "Todo separado" (T6, D3): el nombre de cara de un espacio para la etiqueta.
const PACKS_CAL = (catalogo as { packs: Array<{ clave: string; nombre: string }> }).packs;
const esCoreCal = (d: string | null | undefined) => !d || d === "core";
const nombreEspacioCal = (d: string) => (esCoreCal(d) ? "Tu viaje" : PACKS_CAL.find((p) => p.clave === d)?.nombre ?? d);
/** un ítem del calendario que recuerda de qué espacio es (para etiquetar). */
type ItemCal = ItemChecklistUI & { _dominio: string };

const AZUL = "#4D7CFE";
const VERDE = "#3FB950";
const AMBAR = "#E0A64A";
const DIAS = ["domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado"];
const DOW = ["LUN", "MAR", "MIÉ", "JUE", "VIE", "SÁB", "DOM"];
const MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"];

type Vista = "agenda" | "mes" | "semana";
type Estatus = "prevista" | "hecha" | "vencida";

/** ordinal del día (local) desde epoch, para comparar por DÍA sin la hora. */
function ordinal(iso: string): number {
  return Math.floor(new Date(`${fechaInputLocal(new Date(iso))}T00:00:00`).getTime() / 86_400_000);
}
function hoyOrdinal(): number {
  return Math.floor(new Date(`${fechaInputLocal(new Date())}T00:00:00`).getTime() / 86_400_000);
}
const claveDia = (iso: string) => fechaInputLocal(new Date(iso));

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
function relativo(delta: number): string {
  if (delta === 0) return "hoy";
  if (delta === 1) return "mañana";
  if (delta === -1) return "ayer";
  if (delta < 0) return `hace ${-delta} días`;
  return `en ${delta} días`;
}

export function Calendario({
  projectId,
  checklist,
  onRecargarChecklist,
  onVolver,
  onVerLoCumplido,
  dominio,
  nombreEspacio,
}: {
  projectId: string;
  /** Fuente ÚNICA de verdad: el mismo checklist que alimenta Manos a la Obra
   *  (IdeaView es el dueño). El Calendario NO guarda copia propia — lee de aquí
   *  y, tras cada acción, pide a IdeaView que lo recargue, para que la agenda y
   *  el checklist nunca digan cosas distintas. */
  checklist: ChecklistData;
  onRecargarChecklist: () => void;
  onVolver: () => void;
  onVerLoCumplido: () => void;
  /** "Todo separado" (T4): scopeado a un mundo → SUS actividades (grupoVigente de
   * su dominio). El feed personal global con etiquetas [Espacio] es la T6; esta
   * es la vista in-app del espacio. Sin dominio, el calendario del núcleo. */
  dominio?: string;
  nombreEspacio?: string;
}) {
  const [error, setError] = useState<string | null>(null);
  const [ocupado, setOcupado] = useState(false);
  const [detalle, setDetalle] = useState<{ item: ItemChecklistUI; tituloEtapa: string } | null>(null);
  const [vista, setVista] = useState<Vista>("agenda");
  const [refMs, setRefMs] = useState<number>(() => Date.parse(`${fechaInputLocal(new Date())}T00:00:00`));
  // El día abierto en la vista Mes (panel de la derecha/abajo). Por defecto, hoy.
  const [diaSel, setDiaSel] = useState<string>(() => fechaInputLocal(new Date()));

  // "Todo separado" (T4/T6): scopeado a un mundo → SUS actividades; GLOBAL (sin
  // dominio) → las de TODOS los espacios (el feed personal in-app, que crece con
  // los mundos), cada ítem recordando su espacio para etiquetar la mezcla.
  const esScoped = Boolean(dominio);
  const hayMundos = useMemo(() => checklist.planes.some((p) => !esCoreCal(p.dominio)), [checklist]);
  const itemsCore = useMemo<ItemCal[]>(() => {
    const doms = esScoped ? [dominio!] : [...new Set(checklist.planes.map((p) => p.dominio))];
    return doms.flatMap((dom) => {
      const g = grupoVigente(checklist, dom);
      return (g?.etapas.flatMap((e) => e.items) ?? []).map((i) => ({ ...i, _dominio: dom }));
    });
  }, [checklist, dominio, esScoped]);
  // La etiqueta [Espacio] SOLO donde hay MEZCLA: el global con mundos. El
  // scopeado (T4b) ya es de un espacio y no etiqueta; sin mundos, ruido cero.
  const etiquetaDe = (dom: string): string | undefined =>
    esScoped || !hayMundos ? undefined : nombreEspacioCal(dom);

  async function moverFecha(itemId: string, fecha: string, cascada: boolean) {
    setError(null);
    try {
      const res = await fetch(`/api/project/${projectId}/mover-fecha`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ item_id: itemId, fecha, cascada }),
      });
      if (!res.ok) return setError("No pudimos mover la fecha.");
      onRecargarChecklist();
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
      onRecargarChecklist();
      setDetalle(null);
    } catch {
      setError("No pudimos guardar; revisa tu internet.");
    } finally {
      setOcupado(false);
    }
  }
  const abrir = (item: ItemChecklistUI) => setDetalle({ item, tituloEtapa: `Etapa ${item.etapa}` });
  const marcarHecha = (item: ItemChecklistUI) =>
    aplicarCambio(item, { estado: "hecho", completed_at: isoDesdeInputLocal(fechaInputLocal(new Date())) });

  function descargarCalendario() {
    const tareas = itemsCore
      .filter((i) => i.fecha_base && i.estado !== "hecho" && i.estado !== "no_aplica")
      .map((i) => ({ id: i.id, texto: i.texto, etapa: i.etapa, fechaBase: i.fecha_base!, espacio: etiquetaDe(i._dominio) }));
    const ics = generarIcs({ nombreIdea: "Mi idea", tareas });
    const blob = new Blob([ics], { type: "text/calendar;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "mi-idea-calendario.ics";
    a.click();
    URL.revokeObjectURL(url);
  }

  const hoy = hoyOrdinal();
  // TODOS los ítems con fecha (incluye hechos, para mes/semana), con su estatus.
  const datados = itemsCore
    .filter((i) => i.fecha_base && i.estado !== "no_aplica")
    .map((i) => {
      const dOrd = ordinal(i.fecha_base!);
      const estatus: Estatus = i.estado === "hecho" ? "hecha" : dOrd < hoy ? "vencida" : "prevista";
      // T6: la etiqueta [Espacio] del ítem, solo en el global con mezcla.
      return { item: i, ord: dOrd, dia: claveDia(i.fecha_base!), estatus, etiqueta: etiquetaDe(i._dominio) };
    });
  const pendientes = datados
    .filter((d) => d.estatus !== "hecha")
    .map((d) => ({ item: d.item, delta: d.ord - hoy, estatus: d.estatus, etiqueta: d.etiqueta }))
    .sort((a, b) => a.delta - b.delta);
  const vencidas = pendientes.filter((p) => p.delta < 0).length;
  const sinFecha = itemsCore.filter((i) => !i.fecha_base && i.estado !== "hecho" && i.estado !== "no_aplica").length;
  const refDate = new Date(refMs);
  const hoyMs = () => Date.parse(`${fechaInputLocal(new Date())}T00:00:00`);
  // Navegación: en Mes salta de mes en mes; en Semana, de siete en siete días.
  const paso = (dir: number) =>
    setRefMs(
      vista === "mes"
        ? new Date(refDate.getFullYear(), refDate.getMonth() + dir, 1).getTime()
        : new Date(refDate.getFullYear(), refDate.getMonth(), refDate.getDate() + dir * 7).getTime()
    );
  const lunesRef = new Date(refDate.getFullYear(), refDate.getMonth(), refDate.getDate() - (((refDate.getDay() + 6) % 7)));
  const domRef = new Date(lunesRef.getFullYear(), lunesRef.getMonth(), lunesRef.getDate() + 6);
  const mesCorto = (d: Date) => MESES[d.getMonth()].slice(0, 3);
  const tituloSemana = `${lunesRef.getDate()} ${mesCorto(lunesRef)} – ${domRef.getDate()} ${mesCorto(domRef)}`;
  const titulo =
    vista === "mes"
      ? `${MESES[refDate.getMonth()]} ${refDate.getFullYear()}`.replace(/^./, (c) => c.toUpperCase())
      : vista === "semana"
        ? tituloSemana
        : "Lo que viene";
  const manejo = { ocupado, onDetalle: abrir, onMarcarHecha: marcarHecha, onNota: (item: ItemChecklistUI, nota: string | null) => aplicarCambio(item, { nota }) };

  return (
    <section className="mx-auto flex w-full max-w-[1176px] flex-col gap-6 lg:flex-row lg:items-start">
      <div className="min-w-0 flex-1">
        <button onClick={onVolver} className="mb-4 text-sm text-dim hover:text-ink">
          ← Volver
        </button>
        <p className="mb-2 flex items-center gap-2.5 text-[12px] font-semibold uppercase tracking-[1.5px]" style={{ color: AZUL }}>
          <span aria-hidden className="h-[7px] w-[7px] rounded-full" style={{ background: AZUL }} />
          {dominio ? `Calendario de ${nombreEspacio ?? "este mundo"}` : "Tu calendario"}
        </p>
        <div className="mb-5 flex flex-wrap items-center justify-between gap-3">
          <div className="flex items-center gap-3">
            <h2 className="text-[28px] font-bold leading-tight tracking-[-0.02em]">{titulo}</h2>
            {vista !== "agenda" && (
              <span className="flex items-center gap-1">
                <button aria-label={vista === "mes" ? "Mes anterior" : "Semana anterior"} onClick={() => paso(-1)} className="grid h-7 w-7 place-items-center rounded-lg border border-hairline text-dim hover:text-ink">‹</button>
                <button onClick={() => setRefMs(hoyMs())} className="rounded-lg border border-hairline px-2.5 py-1 text-[12px] text-dim hover:text-ink">Hoy</button>
                <button aria-label={vista === "mes" ? "Mes siguiente" : "Semana siguiente"} onClick={() => paso(1)} className="grid h-7 w-7 place-items-center rounded-lg border border-hairline text-dim hover:text-ink">›</button>
              </span>
            )}
          </div>
          <div className="inline-flex items-center gap-1 rounded-full border border-hairline p-1 text-[13px]">
            {(["mes", "semana", "agenda"] as Vista[]).map((v) => (
              <button
                key={v}
                onClick={() => setVista(v)}
                className={"rounded-full px-3 py-1 " + (vista === v ? "bg-accent/20 font-semibold text-accent" : "text-dim hover:text-ink")}
              >
                {v === "mes" ? "Mes" : v === "semana" ? "Semana" : "Agenda"}
              </button>
            ))}
          </div>
        </div>

        {error && <p className="mb-3 text-sm text-warn">{error}</p>}

        {/* banda de vencidas (mes/semana) */}
        {vista !== "agenda" && vencidas > 0 && (
          <div className="mb-4 flex flex-wrap items-center justify-between gap-2 rounded-[12px] border px-4 py-3 text-[13px]" style={{ borderColor: "rgba(224,166,74,0.45)", background: "rgba(224,166,74,0.10)" }}>
            <span style={{ color: AMBAR }}>
              {vencidas === 1 ? "Una fecha ya pasó y sigue abierta." : `${vencidas} fechas ya pasaron y siguen abiertas.`} Puedes moverlas al día que te sirva.
            </span>
          </div>
        )}

        {vista === "agenda" && (
          <VistaAgenda
            pendientes={pendientes}
            sinFecha={sinFecha}
            ocupado={ocupado}
            onVolver={onVolver}
            onDetalle={abrir}
            onMarcarHecha={marcarHecha}
            onNota={(item, nota) => aplicarCambio(item, { nota })}
          />
        )}
        {vista === "mes" && <VistaMes datados={datados} refDate={refDate} hoy={hoy} diaSel={diaSel} onSelDia={setDiaSel} manejo={manejo} />}
        {vista === "semana" && (
          <VistaSemana datados={datados} refDate={refDate} hoy={hoy} manejo={manejo} onMoverDia={(id, iso) => moverFecha(id, iso, false)} />
        )}
      </div>

      {/* aside compartido */}
      <aside className="flex w-full flex-col gap-4 lg:w-[348px] lg:shrink-0">
        <div className="rounded-panel border border-hairline bg-surface p-5">
          {/* Título + info (ⓘ flotante) + dos botones estándar (suscribir / .ics). */}
          <SuscripcionCalendario onDescargarIcs={descargarCalendario} puedeDescargar={pendientes.length > 0} />
        </div>
        <div className="rounded-panel border border-hairline bg-surface p-5">
          <p className="text-[14px] font-semibold">Tus estadísticas</p>
          <p className="mt-2 text-[12.5px] leading-relaxed text-dim">Tu avance, tu ritmo y tu cumplimiento, en gráficos. Aquí planeas; ahí ves cómo vas.</p>
          <button onClick={onVerLoCumplido} className="mt-3 w-full rounded-[11px] border border-accent/50 py-2.5 text-[13px] font-semibold text-accent hover:bg-accent/10">
            Ver el análisis
          </button>
        </div>
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
          // T6: la cascada de fechas es DENTRO del espacio del ítem — en el
          // calendario global, solo los del mismo espacio; en el scopeado, todos.
          itemsDominio={itemsCore.filter((i) => i._dominio === (detalle.item as ItemCal)._dominio)}
          onCerrar={() => setDetalle(null)}
        />
      )}
    </section>
  );
}

// ── Vista Agenda ────────────────────────────────────────────────────────────
type PendItem = { item: ItemChecklistUI; delta: number; estatus: Estatus; etiqueta?: string };
function VistaAgenda({
  pendientes,
  sinFecha,
  ocupado,
  onVolver,
  onDetalle,
  onMarcarHecha,
  onNota,
}: {
  pendientes: PendItem[];
  sinFecha: number;
  ocupado: boolean;
  onVolver: () => void;
  onDetalle: (i: ItemChecklistUI) => void;
  onMarcarHecha: (i: ItemChecklistUI) => void;
  onNota: (i: ItemChecklistUI, nota: string | null) => void;
}) {
  const porGrupo = new Map<Grupo, PendItem[]>();
  for (const p of pendientes) (porGrupo.get(grupoDe(p.delta)) ?? porGrupo.set(grupoDe(p.delta), []).get(grupoDe(p.delta))!).push(p);
  const colorGrupo = (g: Grupo) => (g === "vencidas" ? AMBAR : g === "hoy" ? VERDE : "#A6A7AD");
  const renderizados = ORDEN_GRUPOS.filter((g) => porGrupo.get(g)?.length);
  // Acordeones por periodo: lo CERCANO abierto (para que "lo que viene" se vea de
  // una); lo FUTURO colapsado, para no abrumar. Siempre queda algo abierto.
  const CERCANOS: Grupo[] = ["vencidas", "hoy", "manana", "semana"];
  const [abiertos, setAbiertos] = useState<Set<Grupo>>(() => {
    const s = new Set<Grupo>(renderizados.filter((g) => CERCANOS.includes(g)));
    if (s.size === 0 && renderizados.length) s.add(renderizados[0]);
    return s;
  });
  const toggle = (g: Grupo) =>
    setAbiertos((prev) => {
      const n = new Set(prev);
      if (n.has(g)) n.delete(g);
      else n.add(g);
      return n;
    });
  if (pendientes.length === 0)
    return (
      <p className="rounded-panel border border-hairline bg-surface p-6 text-[14px] leading-relaxed text-dim">
        No tienes tareas con fecha por delante. Cuando pongas fechas a tus tareas, aquí verás qué toca y cuándo.
      </p>
    );
  return (
    <div className="flex flex-col gap-7">
      {renderizados.map((g) => {
        const filas = porGrupo.get(g)!;
        const abierto = abiertos.has(g);
        return (
          <div key={g}>
            <button
              type="button"
              onClick={() => toggle(g)}
              aria-expanded={abierto}
              className={"flex w-full items-center gap-3 text-left " + (abierto ? "mb-3" : "")}
            >
              <span className="text-[12px] font-semibold uppercase tracking-[1.2px]" style={{ color: colorGrupo(g) }}>{ROTULO[g]}</span>
              <span className="h-px flex-1" style={{ background: g === "vencidas" ? "rgba(224,166,74,0.30)" : g === "hoy" ? "rgba(63,185,80,0.28)" : "rgba(255,255,255,0.08)" }} />
              <span className="text-[12px] tabular-nums text-dim">{filas.length}</span>
              <svg width="11" height="11" viewBox="0 0 12 12" aria-hidden className={"shrink-0 text-dim transition-transform " + (abierto ? "" : "-rotate-90")}>
                <path d="M2 4l4 4 4-4" stroke="currentColor" strokeWidth="1.5" fill="none" />
              </svg>
            </button>
            {abierto && (
              <div className="flex flex-col gap-2.5">
                {filas.map(({ item, delta, etiqueta }) => (
                  <FilaAgenda
                    key={item.id}
                    item={item}
                    delta={delta}
                    grupo={g}
                    etiqueta={etiqueta}
                    ocupado={ocupado}
                    onDetalle={() => onDetalle(item)}
                    onMarcarHecha={() => onMarcarHecha(item)}
                    onGuardarNota={(nota) => onNota(item, nota)}
                  />
                ))}
              </div>
            )}
          </div>
        );
      })}
      {sinFecha > 0 && (
        <div className="flex flex-wrap items-center justify-between gap-3 rounded-cinta border border-dashed border-hairline px-4 py-3 text-[13px] text-dim">
          <span>Después de esto, <span className="font-semibold text-ink tabular-nums">{sinFecha}</span> tarea{sinFecha === 1 ? "" : "s"} sigue{sinFecha === 1 ? "" : "n"} sin fecha.</span>
          <button onClick={onVolver} className="font-semibold text-accent hover:underline">Ponerles fecha</button>
        </div>
      )}
    </div>
  );
}

function FilaAgenda({
  item,
  delta,
  grupo,
  etiqueta,
  ocupado,
  onDetalle,
  onMarcarHecha,
  onGuardarNota,
}: {
  item: ItemChecklistUI;
  delta: number;
  grupo: Grupo;
  /** T6: el espacio del ítem, en el calendario global con mezcla. */
  etiqueta?: string;
  ocupado: boolean;
  onDetalle: () => void;
  onMarcarHecha: () => void;
  onGuardarNota: (nota: string | null) => void;
}) {
  const borde = grupo === "vencidas" ? "border-warn/45 bg-warn/[0.07]" : grupo === "hoy" ? "border-done/30 bg-done/[0.05]" : "border-hairline bg-surface";
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
        <div className="flex flex-wrap items-center gap-1.5">
          <span className="text-[11px] font-semibold uppercase tracking-[1px] text-accent">Etapa {item.etapa}</span>
          {/* T6: la etiqueta [Espacio], solo en el calendario global con mezcla. */}
          {etiqueta && (
            <span className="rounded-full bg-accent/12 px-2 py-0.5 text-[10px] font-semibold text-[#7B9DFF]">{etiqueta}</span>
          )}
        </div>
        {/* Vista cortísima: una línea; el texto completo vive en "Detalle". */}
        <div className="line-clamp-1 text-[14.5px] leading-snug">{item.texto}</div>
      </div>
      <div className="col-span-3 flex flex-wrap items-center gap-2 sm:col-span-1 sm:justify-end">
        {grupo === "hoy" && (
          <button onClick={onMarcarHecha} className="rounded-[9px] bg-done px-3.5 py-1.5 text-[12.5px] font-bold text-[#04120A] hover:opacity-90">Marcar hecha</button>
        )}
        <button onClick={onDetalle} className="rounded-[9px] border border-accent/40 bg-accent/10 px-3.5 py-1.5 text-[12.5px] font-semibold text-accent hover:bg-accent/20">
          {grupo === "vencidas" ? "Ponerle fecha nueva" : "Mover fecha"}
        </button>
        <button onClick={onDetalle} className="rounded-[9px] border border-hairline px-3.5 py-1.5 text-[12.5px] font-semibold text-dim hover:text-ink">Detalle</button>
        <NotaRapida id={item.id} nota={item.nota} ocupado={ocupado} onGuardar={onGuardarNota} tamano={19} />
      </div>
    </div>
  );
}

// ── Vista Mes ───────────────────────────────────────────────────────────────
type Datado = { item: ItemChecklistUI; ord: number; dia: string; estatus: Estatus; etiqueta?: string };
const tieneNota = (i: ItemChecklistUI) => Boolean(i.nota && i.nota.trim());

function chipMes(d: Datado, onDetalle: (i: ItemChecklistUI) => void, sel: boolean) {
  const c =
    d.estatus === "hecha"
      ? { bg: "rgba(63,185,80,0.10)", punto: VERDE, texto: "#93AE99" }
      : d.estatus === "vencida"
        ? { bg: "rgba(224,166,74,0.14)", punto: AMBAR, texto: "#F2DDB8" }
        : { bg: sel ? "rgba(77,124,254,0.16)" : "rgba(77,124,254,0.12)", punto: AZUL, texto: "#DCE7FF" };
  const con = tieneNota(d.item);
  return (
    <button
      key={d.item.id}
      onClick={(e) => {
        e.stopPropagation();
        onDetalle(d.item);
      }}
      title={(d.etiqueta ? `[${d.etiqueta}] ` : "") + d.item.texto + (con ? " (con nota)" : "")}
      className="flex w-full items-center gap-1.5 truncate rounded-[6px] px-[7px] py-1 text-left text-[11px]"
      style={{ background: c.bg, color: c.texto, boxShadow: sel ? "inset 0 0 0 1px rgba(77,124,254,0.40)" : undefined }}
    >
      {d.estatus === "hecha" ? (
        <span className="shrink-0 text-[10px] font-bold" style={{ color: VERDE }}>✓</span>
      ) : (
        <span className="h-1.5 w-1.5 shrink-0 rounded-full" style={{ background: c.punto }} />
      )}
      {/* T6: prefijo [Espacio] en la mezcla del calendario global. */}
      <span className="min-w-0 flex-1 truncate">
        {d.etiqueta ? <span className="font-semibold opacity-80">[{d.etiqueta}] </span> : ""}
        {d.item.texto}
      </span>
      {con && <span aria-hidden className="h-[5px] w-[5px] shrink-0 rounded-full" style={{ background: c.texto }} />}
    </button>
  );
}

type ManejoDia = {
  ocupado: boolean;
  onDetalle: (i: ItemChecklistUI) => void;
  onMarcarHecha: (i: ItemChecklistUI) => void;
  onNota: (i: ItemChecklistUI, nota: string | null) => void;
};

/** La fila operable de una tarea dentro del panel del día (reúsa el círculo de
 * estados de Manos, marca hecha, mover fecha y la nota rápida). */
function FilaDia({ d, manejo }: { d: Datado; manejo: ManejoDia }) {
  return (
    <div className="flex items-center gap-3 rounded-[10px] border border-hairline bg-surface-2 px-3 py-2.5">
      <button onClick={() => manejo.onDetalle(d.item)} title="Ver el detalle" aria-label="Ver el detalle" className="shrink-0">
        <IconoEstado estado={d.item.estado} tamano={20} />
      </button>
      <div className="min-w-0 flex-1">
        <div className="line-clamp-2 text-[13px] leading-snug">{d.item.texto}</div>
        <div className="text-[11px] text-dim">
          Etapa {d.item.etapa}
          {d.estatus === "vencida" && <span style={{ color: AMBAR }}> · ya pasó</span>}
        </div>
      </div>
      {d.estatus !== "hecha" && (
        <button onClick={() => manejo.onMarcarHecha(d.item)} className="shrink-0 rounded-[8px] bg-done px-3 py-1 text-[12px] font-bold text-[#04120A] hover:opacity-90">
          Hecha
        </button>
      )}
      <button onClick={() => manejo.onDetalle(d.item)} className="shrink-0 rounded-[8px] border border-accent/40 bg-accent/10 px-3 py-1 text-[12px] font-semibold text-accent hover:bg-accent/20">
        Mover
      </button>
      <NotaRapida id={d.item.id} nota={d.item.nota} ocupado={manejo.ocupado} onGuardar={(nota) => manejo.onNota(d.item, nota)} />
    </div>
  );
}

/** El panel del día elegido (Design "mes opción 1a"): las tareas de ese día,
 * operables. Por defecto, hoy. */
function PanelDia({ clave, items, manejo }: { clave: string; items: Datado[]; manejo: ManejoDia }) {
  const d = new Date(`${clave}T00:00:00`);
  const label = `${DIAS[d.getDay()]} ${d.getDate()} de ${MESES[d.getMonth()]}`;
  return (
    <div className="mt-4 rounded-panel border border-hairline bg-surface p-4">
      <p className="mb-3 text-[13px] font-semibold capitalize">{label}</p>
      {items.length === 0 ? (
        <p className="text-[13px] text-dim">No hay tareas con fecha este día. Toca otro día para ver las suyas.</p>
      ) : (
        <div className="flex flex-col gap-2">
          {items.map((it) => (
            <FilaDia key={it.item.id} d={it} manejo={manejo} />
          ))}
        </div>
      )}
    </div>
  );
}

function VistaMes({
  datados,
  refDate,
  hoy,
  diaSel,
  onSelDia,
  manejo,
}: {
  datados: Datado[];
  refDate: Date;
  hoy: number;
  diaSel: string;
  onSelDia: (clave: string) => void;
  manejo: ManejoDia;
}) {
  const y = refDate.getFullYear();
  const m = refDate.getMonth();
  const primero = new Date(y, m, 1);
  const inicio = new Date(y, m, 1 - (((primero.getDay() + 6) % 7))); // lunes de la primera semana
  const porDia = new Map<string, Datado[]>();
  for (const d of datados) (porDia.get(d.dia) ?? porDia.set(d.dia, []).get(d.dia)!).push(d);
  const celdas = Array.from({ length: 42 }, (_, i) => new Date(inicio.getFullYear(), inicio.getMonth(), inicio.getDate() + i));
  return (
    <>
      <div className="rounded-panel border border-hairline bg-surface p-3 sm:p-4">
        <div className="grid grid-cols-7">
          {DOW.map((d) => (
            <div key={d} className="pb-2 text-center text-[10.5px] font-semibold tracking-[0.8px] text-dim">{d}</div>
          ))}
          {celdas.map((cd, i) => {
            const clave = fechaInputLocal(cd);
            const ord = Math.floor(new Date(`${clave}T00:00:00`).getTime() / 86_400_000);
            const enMes = cd.getMonth() === m;
            const esHoy = ord === hoy;
            const esSel = clave === diaSel;
            const chips = porDia.get(clave) ?? [];
            return (
              <div
                key={i}
                role="button"
                tabIndex={0}
                onClick={() => onSelDia(clave)}
                onKeyDown={(e) => {
                  if (e.key === "Enter" || e.key === " ") {
                    e.preventDefault();
                    onSelDia(clave);
                  }
                }}
                aria-label={`Ver el ${cd.getDate()}`}
                className="min-h-[92px] cursor-pointer border border-white/[0.06] p-[7px] text-left align-top"
                style={{
                  background: esHoy ? "rgba(63,185,80,0.05)" : enMes ? "transparent" : "#08080B",
                  boxShadow: esSel
                    ? "inset 0 0 0 1.5px rgba(77,124,254,0.55)"
                    : esHoy
                      ? "inset 0 0 0 1px rgba(63,185,80,0.28)"
                      : undefined,
                }}
              >
                <div className="mb-1 flex justify-start">
                  {esHoy ? (
                    <span className="grid h-[22px] w-[22px] place-items-center rounded-full text-[12px] font-bold" style={{ background: VERDE, color: "#04120A" }}>{cd.getDate()}</span>
                  ) : (
                    <span className="text-[12px] tabular-nums" style={{ color: enMes ? "#F5F6F8" : "#4A4B52" }}>{cd.getDate()}</span>
                  )}
                </div>
                <div className="flex flex-col gap-1">
                  {chips.slice(0, 3).map((d) => chipMes(d, manejo.onDetalle, esSel))}
                  {chips.length > 3 && <span className="px-1 text-[10.5px] text-dim">+{chips.length - 3} más</span>}
                </div>
              </div>
            );
          })}
        </div>
        {/* leyenda */}
        <div className="mt-3 flex flex-wrap items-center gap-x-5 gap-y-2 px-1 text-[11.5px] text-dim">
          <span className="flex items-center gap-2"><span className="h-2 w-2 rounded-full" style={{ background: AZUL }} />Prevista</span>
          <span className="flex items-center gap-2"><span className="h-2 w-2 rounded-full" style={{ background: VERDE }} />Hecha</span>
          <span className="flex items-center gap-2"><span className="h-2 w-2 rounded-full" style={{ background: AMBAR }} />Ya pasó</span>
          <span className="flex items-center gap-2"><span className="grid h-4 w-4 place-items-center rounded-full text-[9px] font-bold" style={{ background: VERDE, color: "#04120A" }}>·</span>Hoy</span>
        </div>
      </div>
      <PanelDia clave={diaSel} items={porDia.get(diaSel) ?? []} manejo={manejo} />
    </>
  );
}

// ── Vista Semana ────────────────────────────────────────────────────────────
function VistaSemana({
  datados,
  refDate,
  hoy,
  manejo,
  onMoverDia,
}: {
  datados: Datado[];
  refDate: Date;
  hoy: number;
  manejo: ManejoDia;
  /** arrastrar una tarea a otro día (escritorio): mueve su fecha a ese día */
  onMoverDia: (itemId: string, nuevaIso: string) => void;
}) {
  // la semana (lunes a domingo) que contiene la fecha de referencia
  const lunes = new Date(refDate.getFullYear(), refDate.getMonth(), refDate.getDate() - (((refDate.getDay() + 6) % 7)));
  const dias = Array.from({ length: 7 }, (_, i) => new Date(lunes.getFullYear(), lunes.getMonth(), lunes.getDate() + i));
  const porDia = new Map<string, Datado[]>();
  for (const d of datados) (porDia.get(d.dia) ?? porDia.set(d.dia, []).get(d.dia)!).push(d);
  const [sobre, setSobre] = useState<string | null>(null);
  return (
    <div className="grid grid-cols-2 gap-2 sm:grid-cols-4 lg:grid-cols-7">
      {dias.map((cd, i) => {
        const clave = fechaInputLocal(cd);
        const ord = Math.floor(new Date(`${clave}T00:00:00`).getTime() / 86_400_000);
        const esHoy = ord === hoy;
        const esSobre = sobre === clave;
        const chips = porDia.get(clave) ?? [];
        return (
          <div
            key={i}
            onDragOver={(e) => {
              e.preventDefault();
              if (sobre !== clave) setSobre(clave);
            }}
            onDragLeave={() => setSobre((s) => (s === clave ? null : s))}
            onDrop={(e) => {
              e.preventDefault();
              setSobre(null);
              const dato = e.dataTransfer.getData("text/plain");
              const [id, diaOrigen] = dato.split("|");
              if (id && diaOrigen !== clave) onMoverDia(id, isoDesdeInputLocal(clave));
            }}
            className="min-h-[110px] rounded-[12px] border p-2.5"
            style={{
              background: esSobre ? "rgba(77,124,254,0.10)" : esHoy ? "rgba(63,185,80,0.05)" : "#101013",
              borderColor: esSobre ? "rgba(77,124,254,0.55)" : "var(--border)",
            }}
          >
            <div className="mb-2 flex items-baseline gap-1.5">
              <span className="text-[11px] uppercase tracking-[0.6px] text-dim">{DOW[i]}</span>
              <span className={"text-[15px] font-bold tabular-nums " + (esHoy ? "text-done" : "")}>{cd.getDate()}</span>
            </div>
            <div className="flex flex-col gap-1.5">
              {chips.map((d) => {
                const c = d.estatus === "hecha" ? { bg: "rgba(63,185,80,0.10)", tx: "#93AE99" } : d.estatus === "vencida" ? { bg: "rgba(224,166,74,0.14)", tx: "#F2DDB8" } : { bg: "rgba(77,124,254,0.12)", tx: "#DCE7FF" };
                const movible = d.estatus !== "hecha";
                return (
                  <button
                    key={d.item.id}
                    draggable={movible}
                    onDragStart={(e) => {
                      e.dataTransfer.setData("text/plain", `${d.item.id}|${d.dia}`);
                      e.dataTransfer.effectAllowed = "move";
                    }}
                    onClick={() => manejo.onDetalle(d.item)}
                    title={(d.etiqueta ? `[${d.etiqueta}] ` : "") + d.item.texto + (tieneNota(d.item) ? " (con nota)" : "") + (movible ? " · arrastra para mover" : "")}
                    className={"rounded-[8px] px-2 py-1.5 text-left text-[11.5px] leading-snug " + (movible ? "lg:cursor-grab" : "")}
                    style={{ background: c.bg, color: c.tx }}
                  >
                    <span className="flex items-start gap-1.5">
                      <span className="line-clamp-2 min-w-0 flex-1">
                        {/* T6: prefijo [Espacio] en la mezcla del calendario global. */}
                        {d.etiqueta ? <span className="font-semibold opacity-80">[{d.etiqueta}] </span> : ""}
                        {d.item.texto}
                      </span>
                      {tieneNota(d.item) && <span aria-hidden className="mt-1 h-[5px] w-[5px] shrink-0 rounded-full" style={{ background: c.tx }} />}
                    </span>
                    {d.estatus === "vencida" && <span className="mt-0.5 block text-[10px]" style={{ color: AMBAR }}>ya pasó</span>}
                    {movible && <span className="mt-0.5 hidden text-[10px] opacity-60 lg:block">arrastra para mover</span>}
                  </button>
                );
              })}
              {chips.length === 0 && <span className="text-[11px] text-dim/60">—</span>}
              {esHoy && chips.some((d) => d.estatus !== "hecha") && (
                <button onClick={() => manejo.onMarcarHecha(chips.find((d) => d.estatus !== "hecha")!.item)} className="mt-1 rounded-[8px] bg-done px-2 py-1 text-[11px] font-bold text-[#04120A]">
                  Marcar la primera hecha
                </button>
              )}
            </div>
          </div>
        );
      })}
    </div>
  );
}
