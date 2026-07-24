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
import { useEffect, useMemo, useState, type ReactNode } from "react";
import { Acordeon } from "./Acordeon";
import { CampoConVoz } from "./CampoConVoz";
import { DetalleActividad } from "./DetalleActividad";
import { PlanDocumento } from "./PlanDocumento";
import { ETIQUETA_ESTADO, SelectorEstado } from "./SelectorEstado";
import { esActivo, type ChecklistEstado, type FechaBaseOrigen, type ModoCamino } from "@/lib/dbContract";
import { fechaHumana, fechaHumanaCorta, fechaInputLocal, fechaSello, isoDesdeInputLocal } from "@/lib/fechas";
import { Markdown } from "./Markdown";
import { PRECIOS } from "@/lib/precios";
import { loginConNext } from "@/lib/nextSeguro";
import { cadenciaRealSemanas, diaDominante, sugerirFechasBase } from "@/lib/fechasBase";
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
  no_aplica_motivo: string | null;
  fecha_base: string | null;
  fecha_base_origen: FechaBaseOrigen | null;
  fecha_base_original: string | null;
  created_at: string;
  updated_at: string;
}

/** Cambios que un ítem puede recibir en un toque (Fase 3.8: + completed_at;
 * Fase 4.3.2, detalle de actividad: + nota y fecha_base). La ruta PATCH ya los
 * acepta todos; el detalle solo los cablea desde la UI. */
export interface CambioItem {
  estado?: ChecklistEstado;
  completed_at?: string | null;
  no_aplica_motivo?: string | null;
  nota?: string | null;
  fecha_base?: string | null;
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

/**
 * Fase 4.1 (V3a, auditoria de paridad): un tramo del ritual de fechas. El ritual
 * cubre el proyecto ENTERO -- el viaje core y cada mundo activo -- y cada tramo
 * trae SU propio ancla: el sugeridor etapa->semana cuenta desde el created_at
 * del plan de ESE dominio, no del core (un mundo activado en abril no puede
 * fechar sus etapas desde un plan core de marzo).
 */
export interface GrupoRitual {
  dominio: string;
  nombre: string;
  planCreatedAt: string;
  titulos: Record<number, string>;
  items: ItemChecklistUI[];
}

interface MundoInfo {
  dominio: string;
  nombre: string;
  promesa: string;
  plan: { etiqueta: string; contenido_md: string; created_at: string } | null;
  /** Fase 4.2: el usuario dio este mundo por completado. null = abierto. */
  completadoAt?: string | null;
  /** Fase 4.5 (preview): el diagnóstico persistido (el escaparate) y la
   * sesión desde la que la compra genera el plan sin re-entrevistar. */
  resumenMd?: string | null;
  resumenAt?: string | null;
  previewSessionId?: string | null;
  planPagadoAt?: string | null;
}

interface Props {
  projectId: string;
  planMd: string;
  /** created_at del plan core vigente: ancla del sugeridor de fechas (§4) */
  planCreatedAt: string;
  checklist: ChecklistData;
  historial: PlanHistorial[];
  mundos: MundoInfo[];
  /** Fase 3.8: modo del camino; null hasta la primera elección. */
  modoCamino: ModoCamino | null;
  /** el PATCH /modo respondió: el padre refresca su copia del modo */
  onModoCambiado: (modo: ModoCamino) => void;
  /** tras confirmar la línea base: el padre recarga el checklist entero */
  onRecargarChecklist: () => void;
  /** abre la pantalla Análisis del proyecto (§6) */
  onVerAnalisis: () => void;
  /** Fase 4.6: abre las descargas del viaje (un documento por fase) */
  onVerDocumentos: () => void;
  /** la idea se marcó como realizada (§5): el padre abre la Celebración */
  onRealizada: () => void;
  /** Fase 4.2: un mundo se completó o se reabrió — el padre refresca su copia.
   * El cierre de un mundo NO abre la Celebración (§3: la fiesta grande es del
   * proyecto; el cierre de un mundo es un momento sobrio). */
  onMundoCerrado: (dominio: string, completadoAt: string | null) => void;
  /** true si hay una entrevista abierta para "Volver a la entrevista" */
  entrevistaAbierta: boolean;
  onVolverEntrevista: () => void;
  /** PATCH aplicado: el padre refresca su copia del checklist. Fase 4.3.2: el
   * detalle también mueve nota y fecha, así que el ítem actualizado los lleva. */
  onItemActualizado: (item: {
    id: string;
    estado?: ChecklistEstado;
    completed_at?: string | null;
    no_aplica_motivo?: string | null;
    nota?: string | null;
    fecha_base?: string | null;
    fecha_base_original?: string | null;
    fecha_base_origen?: FechaBaseOrigen | null;
  }) => void;
  /** el follow devolvió el primer turno: el padre entra a la entrevista */
  onSeguimientoIniciado: (turno: unknown) => void;
  /** POST world/start devolvió el primer turno del mundo */
  onMundoIniciado: (turno: unknown, dominio: string) => void;
  /** Fase 4.5: comprar el plan del mundo desde su escaparate (el diagnóstico).
   * El padre genera el plan DESDE la sesión del preview, sin re-entrevistar. */
  onComprarPlanMundo: (dominio: string, sessionId: string) => void;
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

/** Cuentas honestas (gestor de estados): el denominador son las ACTIVAS; las
 * retiradas (no_aplica) salen del avance y se cuentan aparte. */
function conteo(items: ItemChecklistUI[]) {
  const activas = items.filter((i) => esActivo(i.estado));
  return {
    hechos: activas.filter((i) => i.estado === "hecho").length,
    total: activas.length,
    retiradas: items.length - activas.length,
  };
}

// El vocabulario y los iconos de estado viven en SelectorEstado (fuente única
// compartida con el detalle). El ciclo por toques MURIÓ: adivinar no es
// elegir; ahora el círculo abre el menú de los 5 estados.

function FilaItem({
  item,
  ocupado,
  onCambio,
  onAbrirDetalle,
}: {
  item: ItemChecklistUI;
  ocupado: boolean;
  onCambio: (cambio: CambioItem) => void;
  /** Fase 4.3.2: tocar el texto abre "Explorar actividad" (el detalle). */
  onAbrirDetalle: () => void;
}) {
  const hecho = item.estado === "hecho";
  const retirada = item.estado === "no_aplica";
  // Marcar hecho COMPROMETE el estado en el acto, con la fecha de hoy por
  // defecto (ley vigente). La fecha se ajusta DESPUÉS con "cambiar".
  const [editandoFecha, setEditandoFecha] = useState(false);
  const hoyInput = fechaInputLocal(new Date());

  function marcarHecho(completedAt?: string | null) {
    setEditandoFecha(false);
    onCambio({ estado: "hecho", completed_at: completedAt ?? isoDesdeInputLocal(hoyInput) });
  }

  // El menú de estados manda el cambio; 'no_aplica' viaja con su motivo.
  function elegirEstado(estado: ChecklistEstado, motivo?: string | null) {
    if (estado === "hecho") return marcarHecho();
    if (estado === "no_aplica") return onCambio({ estado, no_aplica_motivo: motivo ?? null });
    onCambio({ estado });
  }

  return (
    <div
      className={
        "rounded-cinta border bg-surface px-4 py-3.5 " +
        (retirada ? "border-hairline opacity-60" : item.destacado && !hecho ? "border-done/35" : "border-hairline")
      }
    >
      <div className="flex flex-wrap items-center gap-3.5">
        {/* El círculo abre el MENÚ de los 5 estados (el ciclo por toques murió).
            A 380 el círculo es el control (frame móvil del canon 06); su área
            táctil sube a 44px con padding + margen negativo dentro del selector. */}
        <SelectorEstado
          estado={item.estado}
          ocupado={ocupado}
          onElegir={elegirEstado}
          etiquetaActual={item.no_aplica_motivo}
        />
        <span className="min-w-0 flex-1">
          {/* Fase 4.3.2: el texto abre "Explorar actividad". Es un botón (no un
              div con onClick) para que el teclado y los lectores lo alcancen.
              Hecha = tachada (trofeo); retirada = atenuada SIN tachar. */}
          <button
            onClick={onAbrirDetalle}
            className={
              "block w-full text-left text-[14.5px] hover:underline " +
              (hecho ? "text-dim line-through" : retirada ? "text-dim" : "text-ink")
            }
            title="Ver el detalle de esta actividad"
          >
            {item.texto}
          </button>
          {retirada && (
            <span className="mt-0.5 block text-[12.5px] text-dim">
              no aplica{item.no_aplica_motivo ? ` · ${item.no_aplica_motivo}` : ""}
            </span>
          )}
          {!hecho && !retirada && item.estado !== "pendiente" && (
            <span className="mt-0.5 block text-[12.5px] text-done">{ETIQUETA_ESTADO[item.estado]}</span>
          )}
          {!hecho && !retirada && item.destacado && (
            <span className="mt-0.5 block text-[12.5px] text-done">esta semana</span>
          )}
          {!hecho && !retirada && item.fecha_base && (
            <span className="mt-0.5 block text-[12.5px] text-accent">para el {fechaHumanaCorta(item.fecha_base)}</span>
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
        {/* "Marcar hecho" permanece como ATAJO (el menú es la vía completa).
            Solo en el ítem destacado a 380; en escritorio, en cada pendiente. */}
        {!hecho && !retirada && (
          <button
            onClick={() => marcarHecho()}
            disabled={ocupado}
            className={
              (item.destacado ? "basis-full py-2.5 sm:basis-auto sm:py-1.5 " : "hidden sm:block sm:py-1.5 ") +
              "shrink-0 rounded-[9px] border border-done/50 px-3.5 text-[12.5px] font-semibold text-done hover:bg-done-soft disabled:opacity-50"
            }
          >
            Marcar hecho
          </button>
        )}
      </div>

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
  onAbrirDetalle,
}: {
  grupo: NonNullable<ReturnType<typeof grupoVigente>>;
  titulos: Record<number, string>;
  ocupado: boolean;
  onCambio: (item: ItemChecklistUI, cambio: CambioItem) => void;
  /** Fase 4.3.2: abrir el detalle de un ítem, con el título de SU etapa. */
  onAbrirDetalle: (item: ItemChecklistUI, tituloEtapa: string) => void;
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
                  <FilaItem key={item.id} item={item} ocupado={ocupado} onCambio={(c) => onCambio(item, c)} onAbrirDetalle={() => onAbrirDetalle(item, titulos[etapa] ?? `Etapa ${etapa}`)} />
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
                <FilaItem key={item.id} item={item} ocupado={ocupado} onCambio={(c) => onCambio(item, c)} onAbrirDetalle={() => onAbrirDetalle(item, titulos[etapa] ?? `Etapa ${etapa}`)} />
              ))}
            </div>
          </section>
        );
      })}
    </div>
  );
}

/** Ritual de 3 tarjetas: checklist → detalles → enfoque (con "No estoy seguro").
 *
 * Fase 4.2: el mismo ritual sirve al viaje principal y a cada mundo activo —
 * son las MISMAS tres tarjetas. `mundo` (su nombre) es lo único que cambia: de
 * quién habla. Un solo componente, porque un mundo es un subproyecto completo y
 * su seguimiento no es una versión recortada del otro. */
function RitualContinuar({
  resumen,
  mundo,
  enviando,
  error,
  onEnviar,
  onCerrar,
}: {
  resumen: { hechos: number; total: number };
  mundo?: string;
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
          {mundo ? `Continuar ${mundo}` : "Continuar mi idea"} · {paso} de 3
        </p>
        <button onClick={onCerrar} className="text-sm text-dim hover:text-ink">
          Cerrar
        </button>
      </div>

      {/* Fase 4.0 §4: el ritual NO exige avance mínimo (la realidad cambia antes
          de ejecutar), pero SE ADAPTA. Con cero avance, "llevas 0 de 28" es
          absurdo y desmoralizante: la pregunta cambia, la puerta no. */}
      {paso === 1 && resumen.hechos === 0 && (
        <>
          <p className="text-[17px] font-medium leading-relaxed">
            {mundo
              ? `¿Aún no arrancas con ${mundo}? Cuéntame qué cambió desde que armamos su plan.`
              : "¿Aún no arrancas? Cuéntame qué cambió desde que armamos el plan."}
          </p>
          <p className="mt-2 text-sm text-dim">
            A veces la realidad se mueve antes que uno: un proveedor que falla, algo que se cayó, una
            oportunidad nueva. Si ya hiciste algo, márcalo arriba y lo tomo en cuenta.
          </p>
          <button
            onClick={() => setPaso(2)}
            className="mt-4 rounded-[10px] bg-accent px-5 py-2.5 font-medium text-white hover:opacity-90"
          >
            Te cuento
          </button>
        </>
      )}

      {paso === 1 && resumen.hechos > 0 && (
        <>
          <p className="text-[17px] font-medium leading-relaxed">
            Tu checklist es tu historia: ¿ya refleja lo que hiciste?
          </p>
          <p className="mt-2 text-sm text-dim">
            Llevas {resumen.hechos} de {resumen.total} acciones {mundo ? `de ${mundo} ` : ""}hechas. Ajusta arriba
            lo que haga falta — de eso compongo el «qué ha pasado», sin que lo redactes dos veces.
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
              {enviando ? "Pensando…" : mundo ? "Continuar este mundo" : "Continuar mi idea"}
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

/** Borde azul de elección (canon 10: rgba(77,124,254,0.5)) — el azul piensa. */
const BORDE_AZUL = { border: "1px solid rgba(77,124,254,0.5)" } as const;

/** Vista A del canon 10 (tarjeta ligera al entrar): la elección de modo, con
 * dos opciones de PESO VISUAL IGUAL. */
function TarjetaModo({
  ocupado,
  onElegir,
}: {
  ocupado: boolean;
  onElegir: (modo: ModoCamino) => void;
}) {
  // Íconos del canon 10: reloj (a mi ritmo) y calendario (con fechas), en un
  // badge redondeado arriba-izquierda. Trazo dim; azul piensa el tiempo.
  const iconoReloj = (
    <svg width="18" height="18" viewBox="0 0 20 20" fill="none" aria-hidden>
      <circle cx="10" cy="10" r="7" stroke="#A6A7AD" strokeWidth="1.5" />
      <path d="M10 6v4l2.5 2" stroke="#A6A7AD" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  );
  const iconoCalendario = (
    <svg width="18" height="18" viewBox="0 0 20 20" fill="none" aria-hidden>
      <rect x="3" y="4.5" width="14" height="12.5" rx="2" stroke="#4D7CFE" strokeWidth="1.5" />
      <path d="M3 8h14M6.5 3v3M13.5 3v3" stroke="#4D7CFE" strokeWidth="1.5" strokeLinecap="round" />
      <rect x="6" y="11" width="2.5" height="2.5" rx="0.5" fill="#4D7CFE" />
    </svg>
  );
  const opciones: Array<{ modo: ModoCamino; titulo: string; desc: string; icono: ReactNode }> = [
    {
      modo: "ritmo",
      titulo: "A mi ritmo",
      desc: "Marca tu avance cuando suceda. Sin fechas ni presiones.",
      icono: iconoReloj,
    },
    {
      modo: "fechas",
      titulo: "Con fechas y recordatorios",
      desc: "Te sugiero un calendario; tú lo ajustas. Yo te recuerdo.",
      icono: iconoCalendario,
    },
  ];
  return (
    <section className="anima-plan-in rounded-panel border border-hairline bg-black p-6 text-center sm:p-8">
      <h3 className="mx-auto max-w-md text-2xl font-bold leading-tight tracking-tight [text-wrap:balance]">
        ¿Cómo quieres llevar tu camino?
      </h3>
      <div className="mt-7 flex flex-col gap-4 text-left sm:flex-row">
        {opciones.map((o) => (
          <button
            key={o.modo}
            onClick={() => onElegir(o.modo)}
            disabled={ocupado}
            className="flex flex-1 flex-col rounded-panel border border-white/10 bg-surface p-6 text-left transition-transform hover:-translate-y-0.5 disabled:opacity-50"
          >
            <span className="mb-4 flex h-10 w-10 items-center justify-center rounded-[11px] bg-surface-2">
              {o.icono}
            </span>
            <span className="text-[17px] font-semibold">{o.titulo}</span>
            <span className="mt-2 text-[13.5px] leading-relaxed text-dim [text-wrap:pretty]">{o.desc}</span>
            <span
              className="mt-5 rounded-[10px] py-2.5 text-center text-[13.5px] font-semibold text-ink"
              style={BORDE_AZUL}
            >
              Elegir este
            </span>
          </button>
        ))}
      </div>
      <p className="mt-5 text-xs text-dim">Puedes cambiar de modo cuando quieras.</p>
    </section>
  );
}

/** El interruptor permanente "Fechas y recordatorios: activados / pausados"
 * (canon 10). Alterna 'fechas' ↔ 'ritmo'; pausar nunca borra fechas. */
/** El ritual de la línea base (canon 10, vista B). Las fechas se sugieren
 * determinísticamente (fechasBase.ts, cero LLM) y el usuario ajusta la que
 * quiera. Tema azul: fijar fechas es planear. */
function RitualFechas({
  grupos,
  cadenciaSemanas,
  soloPendientes,
  guardando,
  error,
  onAceptar,
  onPosponer,
}: {
  grupos: GrupoRitual[];
  soloPendientes: boolean;
  guardando: boolean;
  error: string | null;
  onAceptar: (fechas: Array<{ item_id: string; fecha: string; origen: FechaBaseOrigen }>) => void;
  onPosponer: () => void;
  /** Fase 4.0 §1[8]: semanas por etapa aprendidas del ciclo previo. */
  cadenciaSemanas?: number;
}) {
  // Con "recalcular", solo lo que sigue vivo. Un mundo recien activado trae
  // todos sus items pendientes: por eso aparece aqui aunque la baseline core
  // ya estuviera confirmada (V3a).
  const tramos = useMemo(
    () =>
      grupos
        .map((g) => ({ ...g, items: soloPendientes ? g.items.filter((i) => i.estado !== "hecho") : g.items }))
        .filter((g) => g.items.length > 0),
    [grupos, soloPendientes]
  );
  const items = useMemo(() => tramos.flatMap((g) => g.items), [tramos]);
  const diaPreferido = useMemo(() => diaDominante(items.map((i) => i.completed_at)), [items]);
  // Una llamada al sugeridor POR TRAMO: cada dominio cuenta desde su propio plan.
  const sugeridas = useMemo(
    () =>
      Object.fromEntries(
        tramos.flatMap((g) =>
          sugerirFechasBase({
            planCreatedAt: g.planCreatedAt,
            diaPreferido,
            cadenciaSemanas,
            items: g.items.map((i) => ({ id: i.id, etapa: i.etapa, destacado: i.destacado })),
          }).map((s) => [s.id, s.fecha])
        )
      ),
    [tramos, diaPreferido, cadenciaSemanas]
  );
  // Fecha vigente por ítem (YYYY-MM-DD) y qué ítems tocó el usuario (=ajustada).
  const [fechas, setFechas] = useState<Record<string, string>>(sugeridas);
  const [editados, setEditados] = useState<Record<string, true>>({});

  const porTramo = useMemo(
    () =>
      tramos.map((g) => {
        const m = new Map<number, ItemChecklistUI[]>();
        for (const it of g.items) {
          if (!m.has(it.etapa)) m.set(it.etapa, []);
          m.get(it.etapa)!.push(it);
        }
        return { ...g, etapas: [...m.entries()].sort((a, b) => a[0] - b[0]) };
      }),
    [tramos]
  );

  function fijar(id: string, fecha: string) {
    setFechas((f) => ({ ...f, [id]: fecha }));
    setEditados((e) => ({ ...e, [id]: true }));
  }

  function moverEtapa(dominio: string, etapa: number) {
    setFechas((f) => {
      const copia = { ...f };
      const marcados: Record<string, true> = {};
      for (const it of items) {
        if (it.etapa !== etapa || it.dominio !== dominio) continue;
        const base = copia[it.id] ?? sugeridas[it.id];
        const d = new Date(`${base}T12:00:00`);
        copia[it.id] = fechaInputLocal(new Date(d.getFullYear(), d.getMonth(), d.getDate() + 7, 12));
        marcados[it.id] = true;
      }
      setEditados((e) => ({ ...e, ...marcados }));
      return copia;
    });
  }

  function aceptar() {
    onAceptar(
      items.map((it) => ({
        item_id: it.id,
        fecha: isoDesdeInputLocal(fechas[it.id] ?? sugeridas[it.id]),
        origen: editados[it.id] ? "ajustada" : "sugerida",
      }))
    );
  }

  return (
    <section className="anima-plan-in overflow-hidden rounded-panel border border-hairline bg-surface">
      <div className="px-6 pb-4 pt-7 sm:px-8">
        <h3 className="text-2xl font-bold tracking-tight">
          {soloPendientes ? "Recalcular las fechas pendientes" : "Ponle fechas a tu camino"}
        </h3>
        <p className="mt-2 text-sm leading-relaxed text-dim">
          Te propongo estas fechas en lenguaje humano; ajusta la que quieras. La hora es opcional.
        </p>
      </div>

      <div className="flex flex-col gap-1 px-6 pb-2 sm:px-8">
        {porTramo.map((tramo) => (
          <section key={tramo.dominio}>
            {/* V3a: el mundo se anuncia por su nombre. Con un solo tramo (solo
                core) no hace falta cintillo: no se le pone nombre a lo obvio. */}
            {porTramo.length > 1 && (
              <p className="mt-5 text-[11px] font-bold uppercase tracking-[1.2px] text-dim">{tramo.nombre}</p>
            )}
            {tramo.etapas.map(([etapa, its]) => (
          <div key={etapa}>
            <div className="my-3 flex items-center gap-3">
              <span className="text-[11px] font-bold uppercase tracking-[1.2px] text-accent">
                Etapa {etapa}
                {tramo.titulos[etapa] ? ` · ${tramo.titulos[etapa]}` : ""}
              </span>
              <span className="h-px flex-1 bg-hairline" />
              <button
                onClick={() => moverEtapa(tramo.dominio, etapa)}
                disabled={guardando}
                className="rounded-[8px] border border-white/15 px-2.5 py-1 text-[12px] text-dim hover:text-ink disabled:opacity-50"
              >
                Mover esta etapa una semana
              </button>
            </div>
            <div className="flex flex-col gap-2.5">
              {its.map((it) => {
                const fecha = fechas[it.id] ?? sugeridas[it.id];
                return (
                  <div
                    key={it.id}
                    className="flex flex-wrap items-center gap-3.5 rounded-cinta border border-hairline bg-surface px-4 py-3"
                  >
                    <span
                      className="h-4 w-4 shrink-0 rounded-full border-[1.6px]"
                      style={{ borderColor: "var(--accent)" }}
                    />
                    <span className="min-w-0 flex-1 text-[14.5px]">{it.texto}</span>
                    <span className="flex items-center gap-2">
                      <span className="hidden text-[12.5px] text-dim sm:inline">{fechaHumana(isoDesdeInputLocal(fecha))}</span>
                      <input
                        type="date"
                        value={fecha}
                        onChange={(e) => e.target.value && fijar(it.id, e.target.value)}
                        disabled={guardando}
                        aria-label={`Fecha para: ${it.texto}`}
                        className="rounded-[9px] border bg-surface-2 px-2.5 py-1.5 text-[12.5px] text-ink outline-none disabled:opacity-50"
                        style={{ borderColor: "rgba(77,124,254,0.4)" }}
                      />
                    </span>
                  </div>
                );
              })}
            </div>
          </div>
            ))}
          </section>
        ))}
      </div>

      {error && <p className="px-6 pt-2 text-sm text-warn sm:px-8">{error}</p>}

      <div className="flex flex-wrap items-center gap-4 px-6 py-6 sm:px-8">
        <button
          onClick={aceptar}
          disabled={guardando}
          className="rounded-[10px] bg-accent px-6 py-3 text-sm font-semibold text-white hover:opacity-90 disabled:opacity-50"
        >
          {guardando ? "Guardando…" : "Aceptar estas fechas"}
        </button>
        <div className="flex flex-col">
          <button onClick={onPosponer} disabled={guardando} className="text-left text-[13.5px] text-dim hover:text-ink disabled:opacity-50">
            Ponerlas después
          </button>
          <span className="text-xs text-dim opacity-75">Sin fechas no podré recordarte nada.</span>
        </div>
      </div>
    </section>
  );
}

export function ManosALaObra({
  projectId,
  planMd,
  planCreatedAt,
  checklist,
  historial,
  mundos,
  modoCamino,
  onModoCambiado,
  onRecargarChecklist,
  onVerAnalisis,
  onVerDocumentos,
  onRealizada,
  onMundoCerrado,
  entrevistaAbierta,
  onVolverEntrevista,
  onItemActualizado,
  onSeguimientoIniciado,
  onMundoIniciado,
  onComprarPlanMundo,
}: Props) {
  // Fase 4.0: el ritual SOLO se abre desde aqui ("Contar que paso"): una
  // sola puerta (docs/FLUJO_TRACKING.md §2). Ya no se puede abrir desde el plan.
  const [ritual, setRitual] = useState(false);
  // Fase 4.3.2: el "Explorar actividad" abierto. Se guarda el ID (no el ítem):
  // el ítem VIVO se deriva del checklist al renderizar, así el cajón refleja
  // cada cambio (marcar hecho, mover fecha, nota) sin cerrarse ni recargar.
  const [detalleItem, setDetalleItem] = useState<{ id: string; tituloEtapa: string } | null>(null);
  const abrirDetalle = (item: ItemChecklistUI, tituloEtapa: string) =>
    setDetalleItem({ id: item.id, tituloEtapa });
  // Fase 4.2: el ritual de un mundo (su dominio) y su cierre. Van aparte del
  // core a propósito: dos subproyectos abiertos a la vez no comparten estado.
  const [ritualMundo, setRitualMundo] = useState<string | null>(null);
  const [cerrandoMundo, setCerrandoMundo] = useState<string | null>(null);
  const [motivoMundo, setMotivoMundo] = useState("");
  const [guardandoMundo, setGuardandoMundo] = useState(false);
  const [ocupado, setOcupado] = useState(false);
  const [enviandoFollow, setEnviandoFollow] = useState(false);
  const [arrancandoMundo, setArrancandoMundo] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [errorRitual, setErrorRitual] = useState<string | null>(null);
  const [guardandoModo, setGuardandoModo] = useState(false);
  // Fase 4.3.2 (Manos a la Obra a 380, canon refrescado): el modo se muestra
  // COMPACTO ("Modo: a mi ritmo · cambiar"); el selector grande solo aparece en
  // la primera entrada (modoCamino===null) o cuando el usuario toca "cambiar".
  const [mostrarSelectorModo, setMostrarSelectorModo] = useState(false);
  // Fase 3.8 §4 — ritual de la línea base
  // Fase 4.0 §1[8]: el ciclo N+1 aprende la VELOCIDAD real del N. La duración
  // real por etapa la calcula analytics.ts (§6: la única calculadora del
  // tiempo); aquí solo se deriva la cadencia. /analisis es cero-LLM, cero costo.
  const [cadenciaSemanas, setCadenciaSemanas] = useState(1);
  useEffect(() => {
    let vivo = true;
    (async () => {
      try {
        const res = await fetch(`/api/project/${projectId}/analisis`);
        if (!res.ok) return;
        const d = (await res.json()) as {
          analytics?: { universal?: { duracionPorEtapa?: Array<{ etapa: number; dias: number }> } };
        };
        if (vivo) setCadenciaSemanas(cadenciaRealSemanas(d.analytics?.universal?.duracionPorEtapa ?? []));
      } catch {
        /* sin datos: se queda la cadencia por defecto (1 semana por etapa) */
      }
    })();
    return () => {
      vivo = false;
    };
  }, [projectId]);

  const [pospuesto, setPospuesto] = useState(false);
  const [recalcularPendientes, setRecalcularPendientes] = useState(false);
  const [guardandoBaseline, setGuardandoBaseline] = useState(false);
  const [errorBaseline, setErrorBaseline] = useState<string | null>(null);
  // Fase 4.0 §8 — el porqué del cierre, en las palabras del usuario (opcional)
  const [cierreMotivo, setCierreMotivo] = useState("");
  // Fase 3.8 §5 — confirmación de "Marcar como realizada"
  const [confirmandoRealizar, setConfirmandoRealizar] = useState(false);
  const [realizando, setRealizando] = useState(false);

  const titulosCore = useMemo(() => titulosDeEtapas(planMd), [planMd]);
  const core = grupoVigente(checklist, "core");
  const itemsCore = core?.etapas.flatMap((e) => e.items) ?? [];
  const cCore = conteo(itemsCore);
  const tituloPlan = planMd.match(/^#\s+(.+)$/m)?.[1]?.trim() ?? null;
  // Fase 3.8: la baseline está confirmada si algún ítem core ya tiene fecha.
  // Fase 4.1 (V3a): el ritual cubre el proyecto ENTERO. Cada tramo lleva su
  // propio ancla (el created_at del plan de SU dominio) y sus propios titulos
  // de etapa: un mundo activado en abril no puede fechar desde un plan core de
  // marzo. Un mundo sin plan o sin checklist todavia no tiene nada que fechar.
  const gruposRitual: GrupoRitual[] = useMemo(() => {
    const out: GrupoRitual[] = [];
    if (core) {
      out.push({ dominio: "core", nombre: "Tu viaje principal", planCreatedAt, titulos: titulosCore, items: itemsCore });
    }
    for (const mundo of mundos) {
      const g = grupoVigente(checklist, mundo.dominio);
      if (!g || !mundo.plan) continue;
      out.push({
        dominio: mundo.dominio,
        nombre: mundo.nombre,
        planCreatedAt: mundo.plan.created_at,
        titulos: titulosDeEtapas(mundo.plan.contenido_md),
        items: g.etapas.flatMap((e) => e.items),
      });
    }
    return out;
  }, [core, planCreatedAt, titulosCore, itemsCore, mundos, checklist]);

  // Con fechas ya puestas en CUALQUIER dominio no se reabre el ritual inicial;
  // un mundo nuevo entra por "recalcular pendientes" (V3a).
  const hayFechas = itemsCore.some((i) => i.fecha_base);

  // Ritmo: lecturas directas de lo persistido.
  const ultimaAccion = itemsCore
    .filter((i) => i.estado !== "pendiente")
    .map((i) => i.updated_at)
    .sort()
    .at(-1);
  const desde = itemsCore.map((i) => i.created_at).sort()[0];
  const ciclosAjuste = historial.filter((h) => h.etiqueta === "seguimiento").length;

  async function elegirModo(modo: ModoCamino) {
    setGuardandoModo(true);
    setError(null);
    try {
      const res = await fetch(`/api/project/${projectId}/modo`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ modo_camino: modo }),
      });
      if (!res.ok) {
        setError(ERROR_GENERICO);
        return;
      }
      // Reactivar fechas reabre el ritual (si aún no hay ninguna puesta).
      if (modo === "fechas") setPospuesto(false);
      setMostrarSelectorModo(false);
      onModoCambiado(modo);
    } catch {
      setError("no pudimos guardar tu elección; revisa tu internet e intenta de nuevo");
    } finally {
      setGuardandoModo(false);
    }
  }

  async function confirmarBaseline(fechas: Array<{ item_id: string; fecha: string; origen: FechaBaseOrigen }>) {
    if (!core) return;
    setGuardandoBaseline(true);
    setErrorBaseline(null);
    try {
      const res = await fetch(`/api/project/${projectId}/baseline`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ plan_id: core.plan_id, fechas }),
      });
      if (!res.ok) {
        setErrorBaseline(ERROR_GENERICO);
        return;
      }
      setRecalcularPendientes(false);
      onRecargarChecklist();
    } catch {
      setErrorBaseline("no pudimos guardar tus fechas; revisa tu internet e intenta de nuevo");
    } finally {
      setGuardandoBaseline(false);
    }
  }

  async function marcarRealizada() {
    setRealizando(true);
    setError(null);
    try {
      const res = await fetch(`/api/project/${projectId}/realizar`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ accion: "realizar", motivo: cierreMotivo.trim() || null }),
      });
      if (!res.ok) {
        setError(ERROR_GENERICO);
        return;
      }
      setConfirmandoRealizar(false);
      onRealizada();
    } catch {
      setError("no pudimos guardar; revisa tu internet e intenta de nuevo");
    } finally {
      setRealizando(false);
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
      if (!res.ok) {
        setError(ERROR_GENERICO);
        return;
      }
      // La ruta devuelve el ítem persistido COMPLETO (completed_at ya resuelto;
      // fecha_base / fecha_base_original / origen tras una replanificación; la
      // nota guardada). Se propaga todo para que el detalle y la fila reflejen
      // lo persistido sin recargar.
      const data = (await res.json()) as { item?: Partial<ItemChecklistUI> };
      onItemActualizado({
        id: item.id,
        estado: data.item?.estado ?? cambio.estado,
        completed_at: data.item?.completed_at,
        no_aplica_motivo: data.item?.no_aplica_motivo ?? null,
        nota: data.item?.nota ?? cambio.nota,
        fecha_base: data.item?.fecha_base ?? cambio.fecha_base,
        fecha_base_original: data.item?.fecha_base_original,
        fecha_base_origen: data.item?.fecha_base_origen,
      });
    } catch {
      setError("no pudimos guardar el cambio; revisa tu internet e intenta de nuevo");
    } finally {
      setOcupado(false);
    }
  }

  // Fase 4.2: el mismo follow para el viaje principal y para un mundo. El
  // `dominio` viaja al servidor y allí manda sobre los ítems, el bloque de
  // realidad y la puerta; aquí solo se dice de quién es el ritual.
  async function enviarFollow(detalles: string | null, enfoque: string | null, dominio = "core") {
    setEnviandoFollow(true);
    setErrorRitual(null);
    try {
      const res = await fetch(`/api/project/${projectId}/follow`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ detalles, enfoque, dominio }),
      });
      const data = await res.json();
      if (res.status === 401 && data.login_requerido) {
        // ETAPA 2 (la frontera): cuenta real para el seguimiento. Al volver,
        // reanuda en Manos a la Obra (donde vive el ritual de seguimiento).
        window.location.assign(loginConNext(`/idea/${projectId}?vista=manos`));
        return;
      }
      if (!res.ok) {
        // 429 (limite) y 402 (saldo) hablan en palabras de persona: se muestran.
        setErrorRitual(res.status === 429 || res.status === 402 ? String(data.error) : ERROR_GENERICO);
        return;
      }
      onSeguimientoIniciado(data);
    } catch {
      setErrorRitual("no pudimos conectar; revisa tu internet e intenta de nuevo");
    } finally {
      setEnviandoFollow(false);
    }
  }

  /** Fase 4.2: el cierre de un mundo — el acta en miniatura. Mismos parámetros
   * que el del proyecto: no exige el checklist al 100%, el motivo es opcional y
   * es reversible. Reabrir no borra el motivo: la historia no se reescribe. */
  async function cerrarMundo(dominio: string, accion: "completar" | "reabrir") {
    setGuardandoMundo(true);
    setError(null);
    try {
      const res = await fetch(`/api/project/${projectId}/world/${dominio}/completar`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ accion, motivo: accion === "completar" ? motivoMundo.trim() || null : null }),
      });
      if (!res.ok) {
        setError(ERROR_GENERICO);
        return;
      }
      const data = (await res.json()) as { completado_at?: string | null };
      setCerrandoMundo(null);
      setMotivoMundo("");
      // El chip sale de lo que respondió el servidor, no de lo que pedimos.
      onMundoCerrado(dominio, data.completado_at ?? null);
    } catch {
      setError("no pudimos guardar; revisa tu internet e intenta de nuevo");
    } finally {
      setGuardandoMundo(false);
    }
  }

  async function arrancarMundo(dominio: string) {
    setArrancandoMundo(dominio);
    setError(null);
    try {
      const res = await fetch(`/api/project/${projectId}/world/${dominio}/start`, { method: "POST" });
      const data = await res.json();
      if (res.status === 401 && data.login_requerido) {
        // ETAPA 2 (la frontera): el login nace aqui; la idea se adopta al
        // volver y se reanuda en Manos (donde se activan los mundos).
        window.location.assign(loginConNext(`/idea/${projectId}?vista=manos`));
        return;
      }
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
                {cCore.retiradas > 0 && (
                  <span className="ml-2 font-normal text-dim">· {cCore.retiradas} retirada{cCore.retiradas === 1 ? "" : "s"}</span>
                )}
              </span>
            </div>
          )}
          {/* Fase 4.3.2: el modo, COMPACTO (canon refrescado). El selector grande
              ya no vive aquí salvo en la primera entrada; "cambiar" lo reabre. */}
          {modoCamino !== null && !mostrarSelectorModo && (
            <p className="mt-3 text-[13px] text-dim">
              Modo: <span className="font-semibold text-ink">{modoCamino === "ritmo" ? "a mi ritmo" : "con fechas"}</span>
              {" · "}
              <button
                onClick={() => setMostrarSelectorModo(true)}
                className="font-semibold text-accent hover:underline"
              >
                cambiar
              </button>
            </p>
          )}
        </header>

        {error && <p className="text-sm text-warn">{error}</p>}

        {/* Fase 3.8 §3 — la elección del modo: primera entrada (modoCamino null)
            o cuando el usuario toca "cambiar". */}
        {(modoCamino === null || mostrarSelectorModo) && (
          <TarjetaModo ocupado={guardandoModo} onElegir={elegirModo} />
        )}

        {/* Fase 3.8 §4 — ritual de la línea base (modo fechas) */}
        {modoCamino === "fechas" && core && (recalcularPendientes || (!hayFechas && !pospuesto)) && (
          <RitualFechas
            grupos={gruposRitual}
            cadenciaSemanas={cadenciaSemanas}
            soloPendientes={recalcularPendientes}
            guardando={guardandoBaseline}
            error={errorBaseline}
            onAceptar={confirmarBaseline}
            onPosponer={() => {
              setPospuesto(true);
              setRecalcularPendientes(false);
            }}
          />
        )}

        {/* fechas ya puestas: pospuesta (reabrir) o activas (recalcular) */}
        {modoCamino === "fechas" && core && !recalcularPendientes && !hayFechas && pospuesto && (
          <div className="flex items-center justify-between gap-3 rounded-cinta border border-hairline bg-surface px-4 py-3">
            <p className="text-[13px] text-dim">Sin fechas no podré recordarte nada.</p>
            <button
              onClick={() => setPospuesto(false)}
              className="shrink-0 text-[12.5px] font-semibold text-accent hover:underline"
            >
              Poner fechas ahora
            </button>
          </div>
        )}
        {modoCamino === "fechas" && core && !recalcularPendientes && hayFechas && (
          <div className="flex items-center justify-between gap-3 rounded-cinta border border-hairline bg-surface px-4 py-3">
            <p className="text-[13px] text-dim">
              <span className="font-semibold text-accent">Fechas activas.</span> Tu camino tiene línea base.
            </p>
            <button
              onClick={() => setRecalcularPendientes(true)}
              className="shrink-0 text-[12.5px] font-semibold text-accent hover:underline"
            >
              Recalcular pendientes
            </button>
          </div>
        )}

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

        {/* Fase 4.3.2 (Manos a la Obra a 380): "Contar qué pasó" ARRIBA en móvil.
            Antes vivía SOLO en el aside, que en móvil cae al fondo (~2.800px): la
            puerta principal al seguimiento quedaba enterrada. Esta tarjeta es
            lg:hidden (la del aside es hidden lg:block): la acción sale una vez en
            cada viewport, en su sitio. El azul dispara al motor a repensar. */}
        {core && cCore.total > 0 && !ritual && (
          <div className="rounded-panel border border-accent/40 bg-surface p-5 lg:hidden">
            <p className="mb-2 text-[11px] font-semibold uppercase tracking-[1.2px] text-accent">
              Ciclo de profundización
            </p>
            <p className="text-[15px] font-semibold leading-relaxed">
              ¿La realidad te cambió el plan? Cuéntame qué pasó y lo recalculo desde donde estás.
            </p>
            <button
              onClick={() => setRitual(true)}
              className="mt-3 block w-full rounded-[10px] bg-accent py-2.5 text-center text-[13.5px] font-semibold text-white hover:opacity-90"
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
        )}

        {/* checklist maestro: viaje core */}
        {core && mundos.length > 0 && (
          <p className="text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">
            Tu viaje core · <span className="text-done">{cCore.hechos}/{cCore.total}</span>
          </p>
        )}
        {core ? (
          <GrupoEtapas grupo={core} titulos={titulosCore} ocupado={ocupado} onCambio={aplicarCambio} onAbrirDetalle={abrirDetalle} />
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
          const completado = Boolean(mundo.completadoAt);
          return (
            <section key={mundo.dominio} className="rounded-panel border border-hairline bg-surface p-5 sm:p-6">
              <div className="flex flex-wrap items-center gap-3">
                <h3 className="text-base font-semibold">{mundo.nombre}</h3>
                {/* Fase 4.2: el chip del mundo completado. Distingue por FORMA
                    (el check) además de por color, como el resto del canon. */}
                {completado ? (
                  <span className="inline-flex items-center gap-1.5 rounded-full border border-done/50 bg-done-soft px-3 py-1 text-[11px] font-bold text-done">
                    <svg width="9" height="9" viewBox="0 0 12 12" aria-hidden>
                      <path d="M2 6.5l2.5 2.5L10 3.5" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round" />
                    </svg>
                    Completado
                  </span>
                ) : grupo ? (
                  <span className="inline-flex items-center rounded-full border border-done/45 px-3 py-1 text-[11px] font-bold text-done">
                    Mundo activo · {c.hechos}/{c.total}
                  </span>
                ) : mundo.resumenMd && !mundo.plan ? (
                  /* Fase 4.5: el estado protagonista del preview. */
                  <span className="inline-flex items-center rounded-full border border-accent/50 bg-accent/10 px-3 py-1 text-[11px] font-bold text-accent">
                    Listo para generar tu plan
                  </span>
                ) : (
                  <span className="inline-flex items-center rounded-full border border-accent/45 px-3 py-1 text-[11px] font-bold text-accent">
                    {mundo.plan ? "Mundo activo" : "Explóralo gratis"}
                  </span>
                )}
              </div>
              <p className="mt-1 text-sm text-dim">{mundo.promesa}</p>
              {completado && (
                <p className="mt-2 text-[12.5px] text-dim">
                  Lo diste por terminado {haceCuanto(mundo.completadoAt!)}
                  {c.total > c.hechos ? ". Lo que quedó pendiente sigue aquí: es parte de tu historia." : "."}
                </p>
              )}

              {/* mini viaje del mundo: Exploración → Plan → Manos a la Obra */}
              <div className="mt-3 flex items-center gap-2.5 text-[12px] text-dim">
                <span className={mundo.plan || mundo.resumenMd ? "text-accent" : ""}>Exploración</span>
                <span className="w-3 border-t-2 border-dashed border-white/20" />
                <span className={mundo.plan ? "text-accent" : ""}>Plan</span>
                <span className="w-3 border-t-2 border-dashed border-white/20" />
                <span className={grupo ? "font-semibold text-done" : ""}>
                  Manos a la Obra{grupo ? ` · ${c.hechos}/${c.total}` : ""}
                </span>
              </div>

              {grupo ? (
                <div className="mt-4">
                  <GrupoEtapas grupo={grupo} titulos={titulosMundo} ocupado={ocupado} onCambio={aplicarCambio} onAbrirDetalle={abrirDetalle} />
                </div>
              ) : mundo.resumenMd && !mundo.plan ? (
                /* Fase 4.5: EL ESCAPARATE. El diagnóstico persiste y se relee;
                   la compra genera el plan desde la sesión del preview, sin
                   re-entrevistar. Diagnóstico, jamás plan encubierto (§3). */
                <div className="mt-4">
                  <div className="rounded-panel border border-accent/30 bg-accent/[0.04] p-5">
                    <p className="mb-3 text-[11px] font-semibold uppercase tracking-[1.2px] text-accent">
                      Tu diagnóstico{mundo.resumenAt ? ` · ${fechaSello(mundo.resumenAt)}` : ""}
                    </p>
                    <Markdown>{mundo.resumenMd}</Markdown>
                  </div>
                  <div className="mt-4 flex flex-wrap items-center gap-3">
                    <button
                      onClick={() => mundo.previewSessionId && onComprarPlanMundo(mundo.dominio, mundo.previewSessionId)}
                      disabled={!mundo.previewSessionId}
                      className="rounded-[10px] bg-accent px-5 py-2.5 text-sm font-semibold text-white hover:opacity-90 disabled:opacity-50"
                    >
                      Generar mi plan de {mundo.nombre}
                    </button>
                    <span className="text-[12.5px] text-dim">{PRECIOS.mundo_activar} créditos</span>
                  </div>
                </div>
              ) : (
                <button
                  onClick={() => arrancarMundo(mundo.dominio)}
                  disabled={arrancandoMundo !== null}
                  className="mt-4 rounded-[10px] bg-accent px-5 py-2.5 text-sm font-medium text-white hover:opacity-90 disabled:opacity-50"
                >
                  {arrancandoMundo === mundo.dominio ? "Preparando tu mundo…" : "Explorar este mundo · gratis"}
                </button>
              )}

              {/* Fase 4.2 §1 — el ritual de 3 tarjetas, TAMBIÉN aquí: un mundo
                  es un subproyecto y tiene su propio ciclo de seguimiento. */}
              {grupo && !completado && ritualMundo === mundo.dominio && (
                <div className="mt-4">
                  <RitualContinuar
                    resumen={c}
                    mundo={mundo.nombre}
                    enviando={enviandoFollow}
                    error={errorRitual}
                    onEnviar={(d, e) => enviarFollow(d, e, mundo.dominio)}
                    onCerrar={() => setRitualMundo(null)}
                  />
                </div>
              )}

              {/* Fase 4.2 §2 — el cierre del mundo: el acta en miniatura. Sobrio
                  a propósito (§2: un momento, no la fiesta): la Celebración
                  grande, con su constelación y su pulso, es del PROYECTO. */}
              {grupo && (
                <div className="mt-5 flex flex-wrap items-center gap-3 border-t border-hairline pt-4">
                  {completado ? (
                    <>
                      <button
                        onClick={() => cerrarMundo(mundo.dominio, "reabrir")}
                        disabled={guardandoMundo}
                        className="text-[13px] font-semibold text-accent hover:underline disabled:opacity-50"
                      >
                        {guardandoMundo ? "Reabriendo…" : "Reabrir este mundo"}
                      </button>
                      <span className="text-[12.5px] text-dim">Si vuelves a él, tu checklist te espera igual.</span>
                    </>
                  ) : cerrandoMundo === mundo.dominio ? (
                    <div className="w-full">
                      <p className="text-[14px] font-semibold leading-relaxed">
                        ¿Diste {mundo.nombre} por terminado? Podrás reabrirlo cuando quieras.
                      </p>
                      {/* El espejo del momento: sus números reales, sin juicio. */}
                      <p className="mt-2 text-[12.5px] text-dim">
                        Llevas {c.hechos} de {c.total} acciones de este mundo
                        {c.total > 0 ? ` (${Math.round((c.hechos / c.total) * 100)}%)` : ""}. Las que queden
                        pendientes se guardan tal cual. Cerrar este mundo no cierra tu idea.
                      </p>
                      <label htmlFor={`motivo-${mundo.dominio}`} className="mt-3.5 block text-[12.5px] text-dim">
                        ¿Por qué lo cierras aquí? <span className="text-dim/70">(opcional, para tu propia memoria)</span>
                      </label>
                      <div className="mt-1.5">
                        <CampoConVoz
                          id={`motivo-${mundo.dominio}`}
                          valor={motivoMundo}
                          onCambio={setMotivoMundo}
                          filas={2}
                          placeholder="Lo cierro porque…"
                        />
                      </div>
                      <div className="mt-3 flex items-center gap-3">
                        <button
                          onClick={() => cerrarMundo(mundo.dominio, "completar")}
                          disabled={guardandoMundo}
                          className="rounded-[10px] bg-done px-4 py-2.5 text-[13px] font-semibold text-[#04120A] hover:opacity-90 disabled:opacity-50"
                        >
                          {guardandoMundo ? "Cerrando…" : "Sí, lo doy por terminado"}
                        </button>
                        <button
                          onClick={() => setCerrandoMundo(null)}
                          disabled={guardandoMundo}
                          className="text-[13px] text-dim hover:text-ink disabled:opacity-50"
                        >
                          Todavía no
                        </button>
                      </div>
                    </div>
                  ) : (
                    <>
                      <button
                        onClick={() => {
                          setRitualMundo(mundo.dominio);
                          setErrorRitual(null);
                        }}
                        className="rounded-[10px] bg-accent px-4 py-2.5 text-[13px] font-semibold text-white hover:opacity-90"
                      >
                        Contar qué pasó
                      </button>
                      <button
                        onClick={() => {
                          setCerrandoMundo(mundo.dominio);
                          setMotivoMundo("");
                        }}
                        className="rounded-[10px] border border-done/50 px-4 py-2.5 text-[13px] font-semibold text-done hover:bg-done-soft"
                      >
                        Marcar este mundo como completado
                      </button>
                    </>
                  )}
                </div>
              )}
              {mundo.plan && (
                <div className="mt-4">
                  <Acordeon titulo={`El plan de ${mundo.nombre}`}>
                    <PlanDocumento md={mundo.plan.contenido_md} nombreIdea={mundo.nombre} />
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
                  <PlanDocumento md={h.contenido_md} nombreIdea={`Plan ${h.etiqueta}`} />
                </Acordeon>
              ))}
            </div>
          </Acordeon>
        )}
      </div>

      {/* lateral: análisis + realizar + ciclo de profundización + ritmo.
          El modo ya no vive aquí (Fase 4.3.2): es el indicador compacto del
          header. En móvil este aside cae debajo del checklist (posición del
          canon para análisis/ritmo); "Contar qué pasó" ya subió arriba. */}
      <aside className="flex flex-col gap-6">
        {/* Fase 3.8 §6 — puerta al análisis del proyecto */}
        {cCore.total > 0 && (
          <button
            onClick={onVerAnalisis}
            className="rounded-cinta border border-hairline bg-surface px-4 py-3 text-left text-[13px] font-semibold hover:border-accent/60"
          >
            Ver análisis del proyecto
            <span className="mt-0.5 block text-[12px] font-normal text-dim">
              Tu ritmo, tus etapas y tu cumplimiento, calculados de lo que hiciste.
            </span>
          </button>
        )}

        {/* Fase 4.6 — llevarse el trabajo: un documento por fase del camino */}
        <button
          onClick={onVerDocumentos}
          className="rounded-cinta border border-hairline bg-surface px-4 py-3 text-left text-[13px] font-semibold hover:border-accent/60"
        >
          Tus documentos
          <span className="mt-0.5 block text-[12px] font-normal text-dim">
            Tu plan, cada seguimiento y el expediente completo, en .md o en PDF.
          </span>
        </button>

        {/* Fase 3.8 §5 — marcar la idea como realizada (nace el proyecto) */}
        {cCore.total > 0 && (
          <div className="rounded-panel border border-done/40 bg-surface p-5">
            {!confirmandoRealizar ? (
              <>
                <p className="text-[13px] font-semibold text-done">¿Tu idea ya es un proyecto?</p>
                <p className="mt-1 text-[12.5px] leading-relaxed text-dim">
                  Cuando lo sientas real, ciérrala. No hace falta terminar todo el checklist.
                </p>
                <button
                  onClick={() => setConfirmandoRealizar(true)}
                  className="mt-3 w-full rounded-[10px] border border-done/50 py-2.5 text-[13px] font-semibold text-done hover:bg-done-soft"
                >
                  Marcar como realizada
                </button>
              </>
            ) : (
              /* Fase 4.0 §8 — EL ACTA DE CIERRE: mini-ritual de dos elementos.
                 (a) el espejo del momento, con los números reales y SIN juicio;
                 (b) el porqué, OPCIONAL. Cero fricción: se cierra sin escribir
                 nada, como siempre. */
              <>
                <p className="text-[14px] font-semibold leading-relaxed">
                  Esto cierra tu idea y nace tu proyecto. Podrás reabrirla cuando quieras.
                </p>
                <p className="mt-2 text-[12.5px] text-dim">
                  Llevas {cCore.hechos} de {cCore.total} acciones
                  {cCore.total > 0 ? ` (${Math.round((cCore.hechos / cCore.total) * 100)}%)` : ""}. Las que queden
                  pendientes se guardan tal cual: son parte de tu historia.
                </p>
                <label htmlFor="cierre-motivo" className="mt-3.5 block text-[12.5px] text-dim">
                  ¿Por qué la cierras aquí? <span className="text-dim/70">(opcional, para tu propia memoria)</span>
                </label>
                <div className="mt-1.5">
                  <CampoConVoz
                    id="cierre-motivo"
                    valor={cierreMotivo}
                    onCambio={setCierreMotivo}
                    filas={2}
                    placeholder="La cierro porque…"
                  />
                </div>
                <div className="mt-3 flex items-center gap-3">
                  <button
                    onClick={marcarRealizada}
                    disabled={realizando}
                    className="rounded-[10px] bg-done px-4 py-2.5 text-[13px] font-semibold text-[#04120A] hover:opacity-90 disabled:opacity-50"
                  >
                    {realizando ? "Cerrando…" : "Sí, es un proyecto"}
                  </button>
                  <button
                    onClick={() => setConfirmandoRealizar(false)}
                    disabled={realizando}
                    className="text-[13px] text-dim hover:text-ink disabled:opacity-50"
                  >
                    Todavía no
                  </button>
                </div>
              </>
            )}
          </div>
        )}
        {/* Ciclo de profundización — SOLO desktop (hidden lg:block): en móvil
            esta acción ya subió arriba con su propia tarjeta (lg:hidden). */}
        <div className="hidden rounded-panel border border-hairline bg-surface p-5 lg:block">
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

      {/* Fase 4.3.2 — "Explorar actividad": el cajón/hoja del detalle de un ítem.
          Se deriva el ítem VIVO del checklist por su id (refleja cada cambio); si
          el ítem desapareció (recarga), se cierra solo. */}
      {(() => {
        if (!detalleItem) return null;
        const vivo = checklist.planes
          .flatMap((p) => p.etapas)
          .flatMap((e) => e.items)
          .find((i) => i.id === detalleItem.id);
        if (!vivo) return null;
        return (
          <DetalleActividad
            item={vivo}
            tituloEtapa={detalleItem.tituloEtapa}
            ocupado={ocupado}
            onCambio={(cambio) => aplicarCambio(vivo, cambio)}
            onCerrar={() => setDetalleItem(null)}
          />
        );
      })()}
    </div>
  );
}
