"use client";

/**
 * ManosALaObra — la etapa 5 (canon 3.6, mockups 06 y 08): el plan
 * convertido en checklist agrupado por etapa (y por mundo cuando hay
 * unlocks), los 4 estados de un toque + "Marcar hecho", el ritual de 3
 * tarjetas de "Continuar mi idea" (checklist → detalles → enfoque), el
 * acordeón Historia y el ritmo. EL VERDE EJECUTA: todo el progreso aquí
 * es verde; el azul queda para el ciclo de profundización (pensar).
 *
 * REGLA DE ORO: cada número, barra y check viene de checklist_items
 * persistido (rutas 3.3). Los títulos de etapa se leen del markdown REAL
 * del plan ("## Etapa N: título"); si el plan no los trae, se muestra
 * solo el número. Nada se anima sin un evento real detrás.
 */
import { useMemo, useState } from "react";
import { Acordeon } from "./Acordeon";
import { Markdown } from "./Markdown";
import type { ChecklistEstado, FechaBaseOrigen } from "@/lib/dbContract";
import { fechaHumanaCorta, fechaInputLocal, isoDesdeInputLocal } from "@/lib/fechas";
import { haceCuanto } from "@/lib/ideas";

export interface ItemChecklistUI {
  id: string;
  plan_id: string;
  dominio: string;
  etapa: number;
  orden: number;
  texto: string;
  destacado: boolean;
  estado: ChecklistEstado;
  nota: string | null;
  completed_at: string | null;
  fecha_base: string | null;
  fecha_base_origen: FechaBaseOrigen | null;
  fecha_base_original: string | null;
  created_at: string;
  updated_at: string;
}

/** Cambios que un ítem puede recibir en un toque (Fase 3.8: + completed_at). */
export interface CambioItem {
  estado?: ChecklistEstado;
  completed_at?: string | null;
}

export interface ChecklistData {
  planes: Array<{
    plan_id: string;
    dominio: string;
    etapas: Array<{ etapa: number; items: ItemChecklistUI[] }>;
  }>;
  resumen: Record<string, { total: number; hechos: number }>;
}

export interface PlanHistorial {
  etiqueta: string;
  created_at: string;
  contenido_md: string;
}

interface MundoInfo {
  dominio: string;
  nombre: string;
  promesa: string;
  plan: { etiqueta: string; contenido_md: string; created_at: string } | null;
}

interface Props {
  projectId: string;
  planMd: string;
  checklist: ChecklistData;
  historial: PlanHistorial[];
  mundos: MundoInfo[];
  /** true si hay una entrevista abierta para "Volver a la entrevista" */
  entrevistaAbierta: boolean;
  onVolverEntrevista: () => void;
  /** PATCH aplicado: el padre refresca su copia del checklist */
  onItemActualizado: (item: { id: string; estado?: ChecklistEstado; completed_at?: string | null }) => void;
  /** el follow devolvió el primer turno: el padre entra a la entrevista */
  onSeguimientoIniciado: (turno: unknown) => void;
  /** POST world/start devolvió el primer turno del mundo */
  onMundoIniciado: (turno: unknown, dominio: string) => void;
  /** abrir el ritual directamente (CTA "Ajustar el plan" del plan) */
  ritualAbierto?: boolean;
}

const ERROR_GENERICO = "algo se atoró de nuestro lado; intenta de nuevo en un momento";

/** "## Etapa N: título" del markdown real del plan → {N: título}. */
export function titulosDeEtapas(planMd: string): Record<number, string> {
  const titulos: Record<number, string> = {};
  for (const m of planMd.matchAll(/^##\s+Etapa\s+(\d+)\s*:\s*(.+)$/gm)) {
    titulos[parseInt(m[1], 10)] = m[2].trim();
  }
  return titulos;
}

/** El grupo VIGENTE de un dominio: el último plan (el GET viene cronológico). */
export function grupoVigente(checklist: ChecklistData, dominio: string) {
  const grupos = checklist.planes.filter((p) => p.dominio === dominio);
  return grupos.at(-1) ?? null;
}

function conteo(items: ItemChecklistUI[]) {
  return { hechos: items.filter((i) => i.estado === "hecho").length, total: items.length };
}

const ETIQUETA_ESTADO: Record<ChecklistEstado, string> = {
  pendiente: "sin empezar",
  empezado: "apenas empezado",
  a_medias: "a medias",
  hecho: "hecho",
};

const SIGUIENTE_ESTADO: Record<ChecklistEstado, ChecklistEstado> = {
  pendiente: "empezado",
  empezado: "a_medias",
  a_medias: "hecho",
  hecho: "pendiente",
};

/** El icono de estado distingue por FORMA, nunca solo por color. */
function IconoEstado({ estado }: { estado: ChecklistEstado }) {
  if (estado === "hecho") {
    return (
      <span className="anima-check-pop flex h-[22px] w-[22px] shrink-0 items-center justify-center rounded-full bg-done">
        <svg width="11" height="11" viewBox="0 0 12 12" aria-hidden>
          <path d="M2.5 6.5l2.5 2.5 4.5-5.5" stroke="#04120A" strokeWidth="2" fill="none" />
        </svg>
      </span>
    );
  }
  if (estado === "a_medias") {
    return (
      <span className="box-border flex h-[22px] w-[22px] shrink-0 overflow-hidden rounded-full border-[1.5px] border-done/70">
        <span className="h-full w-1/2 bg-done/70" />
      </span>
    );
  }
  if (estado === "empezado") {
    return (
      <span className="box-border flex h-[22px] w-[22px] shrink-0 items-center justify-center rounded-full border-[1.5px] border-done/70">
        <span className="h-1.5 w-1.5 rounded-full bg-done/70" />
      </span>
    );
  }
  return <span className="box-border block h-[22px] w-[22px] shrink-0 rounded-full border-[1.5px] border-white/20" />;
}

function FilaItem({
  item,
  ocupado,
  onCambio,
}: {
  item: ItemChecklistUI;
  ocupado: boolean;
  onCambio: (cambio: CambioItem) => void;
}) {
  const hecho = item.estado === "hecho";
  // Fase 3.8 §2 — timeline real: al marcar hecho, "¿Cuándo lo hiciste?
  // HOY / elegir fecha". HOY es el default de un toque; la fecha puede ser
  // pasada, nunca futura; editable después desde el ítem ya hecho.
  const [preguntando, setPreguntando] = useState(false);
  const [editandoFecha, setEditandoFecha] = useState(false);
  const hoyInput = fechaInputLocal(new Date());

  function marcarHecho(completedAt?: string | null) {
    setPreguntando(false);
    setEditandoFecha(false);
    onCambio({ estado: "hecho", completed_at: completedAt });
  }

  function pasoDeCirculo() {
    const siguiente = SIGUIENTE_ESTADO[item.estado];
    if (siguiente === "hecho") setPreguntando(true);
    else onCambio({ estado: siguiente }); // hecho→pendiente limpia completed_at en la ruta
  }

  return (
    <div
      className={
        "rounded-cinta border bg-surface px-4 py-3.5 " +
        (item.destacado && !hecho ? "border-done/35" : "border-hairline")
      }
    >
      <div className="flex items-center gap-3.5">
        {/* un toque: pendiente → empezado → a medias → hecho → pendiente */}
        <button
          onClick={pasoDeCirculo}
          disabled={ocupado}
          title={`Estado: ${ETIQUETA_ESTADO[item.estado]} — tocar para cambiar`}
          aria-label={`${item.texto}: ${ETIQUETA_ESTADO[item.estado]}, tocar para cambiar`}
          className="shrink-0 disabled:opacity-50"
        >
          <IconoEstado estado={item.estado} />
        </button>
        <span className="min-w-0 flex-1">
          <span className={"block text-[14.5px] " + (hecho ? "text-dim line-through" : "text-ink")}>
            {item.texto}
          </span>
          {!hecho && item.estado !== "pendiente" && (
            <span className="mt-0.5 block text-[12.5px] text-done">{ETIQUETA_ESTADO[item.estado]}</span>
          )}
          {!hecho && item.destacado && (
            <span className="mt-0.5 block text-[12.5px] text-done">esta semana</span>
          )}
          {hecho && item.completed_at && !editandoFecha && (
            <button
              onClick={() => setEditandoFecha(true)}
              disabled={ocupado}
              className="mt-0.5 block text-[12.5px] text-done hover:underline disabled:opacity-50"
            >
              hecho el {fechaHumanaCorta(item.completed_at)} · cambiar
            </button>
          )}
        </span>
        {!hecho && !preguntando && (
          <button
            onClick={() => setPreguntando(true)}
            disabled={ocupado}
            className="shrink-0 rounded-[9px] border border-done/50 px-3.5 py-1.5 text-[12.5px] font-semibold text-done hover:bg-done-soft disabled:opacity-50"
          >
            Marcar hecho
          </button>
        )}
      </div>

      {/* mini-prompt "¿Cuándo lo hiciste?" al marcar hecho */}
      {preguntando && (
        <div className="mt-3 flex flex-wrap items-center gap-2.5 border-t border-hairline pt-3">
          <span className="text-[12.5px] text-dim">¿Cuándo lo hiciste?</span>
          <button
            onClick={() => marcarHecho()}
            disabled={ocupado}
            className="rounded-[9px] bg-done px-3.5 py-1.5 text-[12.5px] font-semibold text-[#04120A] hover:opacity-90 disabled:opacity-50"
          >
            Hoy
          </button>
          <input
            type="date"
            max={hoyInput}
            onChange={(e) => e.target.value && marcarHecho(isoDesdeInputLocal(e.target.value))}
            disabled={ocupado}
            aria-label="Elegir la fecha en que lo hiciste"
            className="rounded-[9px] border border-hairline bg-surface-2 px-2.5 py-1.5 text-[12.5px] text-ink outline-none focus:border-done/60 disabled:opacity-50"
          />
          <button onClick={() => setPreguntando(false)} className="text-[12.5px] text-dim hover:text-ink">
            cancelar
          </button>
        </div>
      )}

      {/* editar la fecha de un ítem ya hecho */}
      {hecho && editandoFecha && (
        <div className="mt-3 flex flex-wrap items-center gap-2.5 border-t border-hairline pt-3">
          <span className="text-[12.5px] text-dim">Cambiar la fecha:</span>
          <input
            type="date"
            max={hoyInput}
            defaultValue={item.completed_at ? fechaInputLocal(new Date(item.completed_at)) : hoyInput}
            onChange={(e) => e.target.value && onCambio({ completed_at: isoDesdeInputLocal(e.target.value) })}
            disabled={ocupado}
            aria-label="Cambiar la fecha en que lo hiciste"
            className="rounded-[9px] border border-hairline bg-surface-2 px-2.5 py-1.5 text-[12.5px] text-ink outline-none focus:border-done/60 disabled:opacity-50"
          />
          <button onClick={() => setEditandoFecha(false)} className="text-[12.5px] text-dim hover:text-ink">
            listo
          </button>
        </div>
      )}
    </div>
  );
}

function GrupoEtapas({
  grupo,
  titulos,
  ocupado,
  onCambio,
}: {
  grupo: NonNullable<ReturnType<typeof grupoVigente>>;
  titulos: Record<number, string>;
  ocupado: boolean;
  onCambio: (item: ItemChecklistUI, cambio: CambioItem) => void;
}) {
  // La primera etapa con pendientes queda abierta; las demás, plegadas.
  const primeraActiva = grupo.etapas.find((e) => e.items.some((i) => i.estado !== "hecho"))?.etapa;
  return (
    <div className="flex flex-col gap-5">
      {grupo.etapas.map(({ etapa, items }) => {
        const c = conteo(items);
        // Abiertas hasta la primera etapa con pendientes; las siguientes, plegadas.
        const abierta = primeraActiva === undefined || etapa <= primeraActiva;
        const encabezado = (
          <span className="flex items-center gap-3">
            <span className="text-[13px] font-bold text-accent">{String(etapa).padStart(2, "0")}</span>
            <span className="text-[15px] font-semibold">{titulos[etapa] ?? `Etapa ${etapa}`}</span>
            <span className="text-xs font-semibold text-done">
              {c.hechos}/{c.total}
            </span>
          </span>
        );
        if (!abierta) {
          return (
            <Acordeon key={etapa} titulo={encabezado}>
              <div className="flex flex-col gap-2.5">
                {items.map((item) => (
                  <FilaItem key={item.id} item={item} ocupado={ocupado} onCambio={(c) => onCambio(item, c)} />
                ))}
              </div>
            </Acordeon>
          );
        }
        return (
          <section key={etapa}>
            <div className="mb-3">{encabezado}</div>
            <div className="flex flex-col gap-2.5">
              {items.map((item) => (
                <FilaItem key={item.id} item={item} ocupado={ocupado} onCambio={(c) => onCambio(item, c)} />
              ))}
            </div>
          </section>
        );
      })}
    </div>
  );
}

/** Ritual de 3 tarjetas: checklist → detalles → enfoque (con "No estoy seguro"). */
function RitualContinuar({
  resumen,
  enviando,
  error,
  onEnviar,
  onCerrar,
}: {
  resumen: { hechos: number; total: number };
  enviando: boolean;
  error: string | null;
  onEnviar: (detalles: string | null, enfoque: string | null) => void;
  onCerrar: () => void;
}) {
  const [paso, setPaso] = useState<1 | 2 | 3>(1);
  const [detalles, setDetalles] = useState("");
  const [enfoque, setEnfoque] = useState("");

  return (
    <div className="rounded-panel border border-accent/40 bg-surface p-5 sm:p-6">
      <div className="mb-3 flex items-center justify-between">
        <p className="text-[11px] font-semibold uppercase tracking-[1.2px] text-accent">
          Continuar mi idea · {paso} de 3
        </p>
        <button onClick={onCerrar} className="text-sm text-dim hover:text-ink">
          Cerrar
        </button>
      </div>

      {paso === 1 && (
        <>
          <p className="text-[17px] font-medium leading-relaxed">
            Tu checklist es tu historia: ¿ya refleja lo que hiciste?
          </p>
          <p className="mt-2 text-sm text-dim">
            Llevas {resumen.hechos} de {resumen.total} acciones hechas. Ajusta arriba lo que haga falta —
            de eso compongo el "qué ha pasado", sin que lo redactes dos veces.
          </p>
          <button
            onClick={() => setPaso(2)}
            className="mt-4 rounded-[10px] bg-accent px-5 py-2.5 font-medium text-white hover:opacity-90"
          >
            Así va, sigamos
          </button>
        </>
      )}

      {paso === 2 && (
        <>
          <p className="text-[17px] font-medium leading-relaxed">¿Algo más que deba saber?</p>
          <p className="mt-2 text-sm text-dim">
            Lo que pasó fuera del checklist: una sorpresa, un cambio, algo que descubriste. Opcional.
          </p>
          <textarea
            value={detalles}
            onChange={(e) => setDetalles(e.target.value)}
            rows={3}
            className="mt-3 w-full resize-y rounded-cinta border border-hairline bg-surface-2 p-3 text-[15px] outline-none focus:border-accent/60"
            placeholder="Cuéntame en tus palabras…"
          />
          <div className="mt-3 flex items-center gap-3">
            <button
              onClick={() => setPaso(3)}
              className="rounded-[10px] bg-accent px-5 py-2.5 font-medium text-white hover:opacity-90"
            >
              Seguir
            </button>
            <button onClick={() => setPaso(1)} className="text-sm text-dim hover:text-ink">
              Atrás
            </button>
          </div>
        </>
      )}

      {paso === 3 && (
        <>
          <p className="text-[17px] font-medium leading-relaxed">¿Hacia dónde profundizamos?</p>
          <p className="mt-2 text-sm text-dim">
            Si algo te quita el sueño o te urge resolver, dilo aquí. Si no, yo te guío según tu avance.
          </p>
          <textarea
            value={enfoque}
            onChange={(e) => setEnfoque(e.target.value)}
            rows={2}
            className="mt-3 w-full resize-y rounded-cinta border border-hairline bg-surface-2 p-3 text-[15px] outline-none focus:border-accent/60"
            placeholder="Lo que más me interesa ahora es…"
          />
          <div className="mt-3 flex flex-wrap items-center gap-3">
            <button
              onClick={() => onEnviar(detalles.trim() || null, enfoque.trim() || null)}
              disabled={enviando}
              className="rounded-[10px] bg-accent px-5 py-2.5 font-medium text-white hover:opacity-90 disabled:opacity-50"
            >
              {enviando ? "Pensando…" : "Continuar mi idea"}
            </button>
            <button
              onClick={() => onEnviar(detalles.trim() || null, null)}
              disabled={enviando}
              className="rounded-[10px] border border-white/15 px-4 py-2.5 text-sm text-dim hover:border-accent/60 hover:text-ink disabled:opacity-50"
            >
              No estoy seguro
            </button>
            <button onClick={() => setPaso(2)} className="text-sm text-dim hover:text-ink">
              Atrás
            </button>
          </div>
        </>
      )}
      {error && <p className="mt-3 text-sm text-warn">{error}</p>}
    </div>
  );
}

export function ManosALaObra({
  projectId,
  planMd,
  checklist,
  historial,
  mundos,
  entrevistaAbierta,
  onVolverEntrevista,
  onItemActualizado,
  onSeguimientoIniciado,
  onMundoIniciado,
  ritualAbierto = false,
}: Props) {
  const [ritual, setRitual] = useState(ritualAbierto);
  const [ocupado, setOcupado] = useState(false);
  const [enviandoFollow, setEnviandoFollow] = useState(false);
  const [arrancandoMundo, setArrancandoMundo] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [errorRitual, setErrorRitual] = useState<string | null>(null);

  const titulosCore = useMemo(() => titulosDeEtapas(planMd), [planMd]);
  const core = grupoVigente(checklist, "core");
  const itemsCore = core?.etapas.flatMap((e) => e.items) ?? [];
  const cCore = conteo(itemsCore);
  const tituloPlan = planMd.match(/^#\s+(.+)$/m)?.[1]?.trim() ?? null;

  // Ritmo: lecturas directas de lo persistido.
  const ultimaAccion = itemsCore
    .filter((i) => i.estado !== "pendiente")
    .map((i) => i.updated_at)
    .sort()
    .at(-1);
  const desde = itemsCore.map((i) => i.created_at).sort()[0];
  const ciclosAjuste = historial.filter((h) => h.etiqueta === "seguimiento").length;

  async function aplicarCambio(item: ItemChecklistUI, cambio: CambioItem) {
    setOcupado(true);
    setError(null);
    try {
      const res = await fetch(`/api/project/${projectId}/checklist`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ item_id: item.id, ...cambio }),
      });
      if (!res.ok) {
        setError(ERROR_GENERICO);
        return;
      }
      // La ruta devuelve el ítem persistido (incluye completed_at ya
      // resuelto: default now() al marcar hecho, null al desmarcar).
      const data = (await res.json()) as { item?: { estado?: ChecklistEstado; completed_at?: string | null } };
      onItemActualizado({
        id: item.id,
        estado: data.item?.estado ?? cambio.estado,
        completed_at: data.item?.completed_at,
      });
    } catch {
      setError("no pudimos guardar el cambio; revisa tu internet e intenta de nuevo");
    } finally {
      setOcupado(false);
    }
  }

  async function enviarFollow(detalles: string | null, enfoque: string | null) {
    setEnviandoFollow(true);
    setErrorRitual(null);
    try {
      const res = await fetch(`/api/project/${projectId}/follow`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ detalles, enfoque }),
      });
      const data = await res.json();
      if (!res.ok) {
        setErrorRitual(res.status === 429 ? String(data.error) : ERROR_GENERICO);
        return;
      }
      onSeguimientoIniciado(data);
    } catch {
      setErrorRitual("no pudimos conectar; revisa tu internet e intenta de nuevo");
    } finally {
      setEnviandoFollow(false);
    }
  }

  async function arrancarMundo(dominio: string) {
    setArrancandoMundo(dominio);
    setError(null);
    try {
      const res = await fetch(`/api/project/${projectId}/world/${dominio}/start`, { method: "POST" });
      const data = await res.json();
      if (!res.ok) {
        setError(typeof data.error === "string" ? data.error : ERROR_GENERICO);
        return;
      }
      onMundoIniciado(data, dominio);
    } catch {
      setError("no pudimos conectar; revisa tu internet e intenta de nuevo");
    } finally {
      setArrancandoMundo(null);
    }
  }

  const barraPct = cCore.total > 0 ? Math.round((cCore.hechos / cCore.total) * 100) : 0;

  return (
    <div className="flex flex-col gap-6 lg:grid lg:grid-cols-[1fr_300px] lg:items-start lg:gap-8">
      <div className="flex min-w-0 flex-col gap-7">
        {/* encabezado: verde ejecuta */}
        <header className="anima-plan-in">
          <p className="mb-3 flex items-center gap-2 text-[11px] font-bold uppercase tracking-[1.2px] text-done">
            <span className="anima-green-pulse h-2 w-2 rounded-full bg-done" />
            Tu idea avanza en el mundo real
          </p>
          {tituloPlan && (
            <h2 className="text-2xl font-bold leading-tight tracking-tight sm:text-[28px]">{tituloPlan}</h2>
          )}
          {cCore.total > 0 && (
            <div className="mt-4 flex max-w-xl items-center gap-4">
              <div className="h-2 flex-1 overflow-hidden rounded bg-white/10">
                <div
                  className="h-2 rounded bg-gradient-to-r from-done/50 to-done"
                  style={{ width: `${barraPct}%`, animation: "barGrow 1.2s ease-out both" }}
                />
              </div>
              <span className="shrink-0 text-sm font-bold text-done">
                {cCore.hechos} de {cCore.total}
              </span>
            </div>
          )}
        </header>

        {error && <p className="text-sm text-warn">{error}</p>}

        {/* ritual de continuación (3 tarjetas) */}
        {ritual && (
          <RitualContinuar
            resumen={cCore}
            enviando={enviandoFollow}
            error={errorRitual}
            onEnviar={enviarFollow}
            onCerrar={() => setRitual(false)}
          />
        )}

        {/* checklist maestro: viaje core */}
        {core && mundos.length > 0 && (
          <p className="text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">
            Tu viaje core · <span className="text-done">{cCore.hechos}/{cCore.total}</span>
          </p>
        )}
        {core ? (
          <GrupoEtapas grupo={core} titulos={titulosCore} ocupado={ocupado} onCambio={aplicarCambio} />
        ) : (
          <p className="text-sm text-dim">
            Tu checklist nace del plan: genera tu plan y aquí aparecerán sus acciones.
          </p>
        )}

        {/* mundos activos: checklist agrupado por mundo (canon 08) */}
        {mundos.map((mundo) => {
          const grupo = grupoVigente(checklist, mundo.dominio);
          const items = grupo?.etapas.flatMap((e) => e.items) ?? [];
          const c = conteo(items);
          const titulosMundo = mundo.plan ? titulosDeEtapas(mundo.plan.contenido_md) : {};
          return (
            <section key={mundo.dominio} className="rounded-panel border border-hairline bg-surface p-5 sm:p-6">
              <div className="flex flex-wrap items-center gap-3">
                <h3 className="text-base font-semibold">{mundo.nombre}</h3>
                <span className="inline-flex items-center rounded-full border border-done/45 px-3 py-1 text-[11px] font-bold text-done">
                  {grupo ? `Mundo activo · ${c.hechos}/${c.total}` : "Mundo activo"}
                </span>
              </div>
              <p className="mt-1 text-sm text-dim">{mundo.promesa}</p>

              {/* mini viaje del mundo: Exploración → Plan → Manos a la Obra */}
              <div className="mt-3 flex items-center gap-2.5 text-[12px] text-dim">
                <span className={mundo.plan ? "text-accent" : ""}>Exploración</span>
                <span className="w-3 border-t-2 border-dashed border-white/20" />
                <span className={mundo.plan ? "text-accent" : ""}>Plan</span>
                <span className="w-3 border-t-2 border-dashed border-white/20" />
                <span className={grupo ? "font-semibold text-done" : ""}>
                  Manos a la Obra{grupo ? ` · ${c.hechos}/${c.total}` : ""}
                </span>
              </div>

              {grupo ? (
                <div className="mt-4">
                  <GrupoEtapas grupo={grupo} titulos={titulosMundo} ocupado={ocupado} onCambio={aplicarCambio} />
                </div>
              ) : (
                <button
                  onClick={() => arrancarMundo(mundo.dominio)}
                  disabled={arrancandoMundo !== null}
                  className="mt-4 rounded-[10px] bg-accent px-5 py-2.5 text-sm font-medium text-white hover:opacity-90 disabled:opacity-50"
                >
                  {arrancandoMundo === mundo.dominio ? "Preparando tu mundo…" : "Explorar este mundo"}
                </button>
              )}
              {mundo.plan && (
                <div className="mt-4">
                  <Acordeon titulo={`El plan de ${mundo.nombre}`}>
                    <Markdown>{mundo.plan.contenido_md}</Markdown>
                  </Acordeon>
                </div>
              )}
            </section>
          );
        })}

        {/* Historia: los planes anteriores, releíbles */}
        {historial.length > 0 && (
          <Acordeon titulo={`Historia (${historial.length})`}>
            <div className="flex flex-col gap-3">
              {historial.map((h, i) => (
                <Acordeon
                  key={i}
                  titulo={`Plan ${h.etiqueta} · ${haceCuanto(h.created_at)}`}
                >
                  <Markdown>{h.contenido_md}</Markdown>
                </Acordeon>
              ))}
            </div>
          </Acordeon>
        )}
      </div>

      {/* lateral: ciclo de profundización + ritmo */}
      <aside className="flex flex-col gap-6">
        <div className="rounded-panel border border-hairline bg-surface p-5">
          <p className="mb-3 text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">
            Ciclo de profundización
          </p>
          <p className="text-[15px] font-semibold leading-relaxed">
            ¿La realidad te cambió el plan? Cuéntame qué pasó y lo recalculo desde donde estás.
          </p>
          <button
            onClick={() => setRitual(true)}
            className="mt-4 block w-full rounded-[10px] bg-accent py-2.5 text-center text-[13.5px] font-semibold text-white hover:opacity-90"
          >
            Contar qué pasó
          </button>
          {entrevistaAbierta && (
            <button
              onClick={onVolverEntrevista}
              className="mt-2.5 block w-full rounded-[10px] border border-white/15 py-2.5 text-center text-[13px] text-dim hover:border-accent/60 hover:text-ink"
            >
              Volver a la entrevista
            </button>
          )}
        </div>
        {cCore.total > 0 && (
          <div className="border-t border-hairline pt-5">
            <p className="mb-3 text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">Ritmo</p>
            <dl className="flex flex-col gap-3">
              <div className="flex items-baseline justify-between">
                <dt className="text-[13px] text-dim">Última acción</dt>
                <dd className="text-[13px] font-semibold">
                  {ultimaAccion ? haceCuanto(ultimaAccion) : "aún ninguna"}
                </dd>
              </div>
              {desde && (
                <div className="flex items-baseline justify-between">
                  <dt className="text-[13px] text-dim">Manos a la Obra desde</dt>
                  <dd className="text-[13px] font-semibold">{haceCuanto(desde)}</dd>
                </div>
              )}
              <div className="flex items-baseline justify-between">
                <dt className="text-[13px] text-dim">Ciclos de ajuste</dt>
                <dd className="text-[13px] font-semibold">{ciclosAjuste}</dd>
              </div>
            </dl>
            <p className="mt-5 text-[13px] leading-relaxed text-dim">
              Pausa cuando lo necesites. Cuando vuelvas, el checklist te espera exactamente donde quedaste.
            </p>
          </div>
        )}
      </aside>
    </div>
  );
}
