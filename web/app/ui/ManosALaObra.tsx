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
import { BarraAvance } from "./BarraAvance";
import { CampoConVoz } from "./CampoConVoz";
import { DetalleActividad } from "./DetalleActividad";
import { NotaRapida } from "./NotaRapida";
import { PlanDocumento } from "./PlanDocumento";
import { ETIQUETA_ESTADO, SelectorEstado } from "./SelectorEstado";
import {
  CAPACIDAD_SEMANAL,
  esActivo,
  type Banda,
  type CapacidadSemanal,
  type ChecklistEstado,
  type Dolor,
  type Probabilidad,
  type FechaBaseOrigen,
  type ModoCamino,
} from "@/lib/dbContract";
import {
  CAPACIDAD_DEFAULT,
  empaquetarFechas,
  factorPorBanda,
  hayBandas,
  type FactoresPorBanda,
  type MuestraCumplida,
} from "@/lib/empaquetado";
import { armarSnapshot } from "@/lib/engine/snapshotProyecto";
import {
  armarRegistro,
  severidadEnPalabras,
  textoProtege,
  type EntradaRegistro,
} from "@/lib/registroProteccion";
import { generarIcs } from "@/lib/ics";
import { fechaHumana, fechaHumanaCorta, fechaInputLocal, fechaSello, isoDesdeInputLocal } from "@/lib/fechas";
import { Markdown } from "./Markdown";
import { PRECIOS } from "@/lib/precios";
import { dominiosDelRitual, ESPACIO_CORE, esEspacioCore, esMundoProteccion, mundosDelEspacio } from "@/lib/espacios";
import { hitosDeEspacio } from "@/lib/hitosEspacio";
import { SelectorCara, type Cara } from "./SelectorCara";
import { LineaAvance } from "./LineaAvance";
import { loginConNext } from "@/lib/nextSeguro";
import { cadenciaRealSemanas, chapaEstaSemana, diaDominante, ordenarEnFechas, sugerirFechasBase } from "@/lib/fechasBase";
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
  /** Scheduler F1: la banda de esfuerzo estimada al nacer el plan. null = plan
   * viejo o estimación fallida: sin rango, cero invención. */
  banda: Banda | null;
  espera_externa: boolean | null;
  /** Mundos de protección (P2): el enlace con la actividad del núcleo que esta
   * respuesta protege, su detección y su severidad. null fuera de protección. */
  protege_item?: string | null;
  deteccion?: string | null;
  probabilidad?: Probabilidad | null;
  dolor?: Dolor | null;
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
  /** Scheduler F1: corrección de la banda por el usuario (evento banda_corregida). */
  banda?: Banda;
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
  /** Fase 3.8: modo del camino del CORE; null hasta la primera elección. */
  modoCamino: ModoCamino | null;
  /** "Todo separado" (T3c): el modo POR ESPACIO (mapa dominio→modo, migration
   * 032). El hub del mundo lee de aquí su propio modo; el core sigue por
   * modoCamino (dual-read en el padre). */
  modos: Record<string, ModoCamino>;
  /** Scheduler F2: las horas por semana POR ESPACIO (mapa dominio→capacidad,
   * migración 033). El ritual de cada espacio empaqueta contra la suya. */
  capacidades?: Record<string, CapacidadSemanal>;
  /** el PATCH /modo respondió: el padre refresca su copia del modo del CORE */
  onModoCambiado: (modo: ModoCamino) => void;
  /** tras confirmar la línea base: el padre recarga el checklist entero */
  onRecargarChecklist: () => void;
  /** abre la pantalla Análisis (§6). "Todo separado" (T4): con dominio, scopea el
   * análisis a ESE espacio (el mundo con su Gantt); sin dominio, el del núcleo. */
  onVerAnalisis: (dominio?: string) => void;
  /** Fase 4.6: abre las descargas del viaje. T4: con dominio, las del mundo. */
  onVerDocumentos: (dominio?: string) => void;
  /** Fase 4.8: abre la bitácora en vivo. T4: con dominio, la del mundo. */
  onVerBitacora?: (dominio?: string) => void;
  /** abre el Calendario. T4: con dominio, el del mundo (sus actividades). */
  onVerCalendario?: (dominio?: string) => void;
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
    banda?: Banda | null;
  }) => void;
  /** el follow devolvió el primer turno: el padre entra a la entrevista */
  onSeguimientoIniciado: (turno: unknown) => void;
  /** POST world/start devolvió el primer turno del mundo */
  onMundoIniciado: (turno: unknown, dominio: string) => void;
  /** Fase 4.5: comprar el plan del mundo desde su escaparate (el diagnóstico).
   * El padre genera el plan DESDE la sesión del preview, sin re-entrevistar. */
  onComprarPlanMundo: (dominio: string, sessionId: string) => void;
  /** Campaña "Espacios": esta misma vista sirve UN espacio. Sin la prop →
   * comportamiento histórico (core + mundos apilados). `"core"` → solo el core
   * (los mundos viven en su hub). Un dominio de mundo → solo la sección de ESE
   * mundo (su hub). */
  soloDominio?: string;
  /** Campaña "Espacios": la cara activa del espacio (Plan · Manos a la obra ·
   * Tu avance). Deep-linkeable: nace de ?cara= y se refleja de vuelta. La cara
   * "manos" es el comportamiento actual (aditivo). */
  caraInicial?: Cara;
  onCaraCambio?: (c: string) => void;
  /** Fechas para la cara "Tu avance" del CORE (los del mundo viajan en `mundos`). */
  proyectoCreatedAt?: string | null; // La Chispa
  organizadorAt?: string | null; // Claridad
  realizadaAt?: string | null; // Realizada
}

const ERROR_GENERICO = "algo se atoró de nuestro lado; intenta de nuevo en un momento";
/** Recuerda que el usuario ya usó el selector de estado (pista de primer uso). */
const CLAVE_PISTA_ESTADO = "mi-idea:selector-estado-usado";

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

/** BotonMini — llamada a la acción secundaria que SE VE como botón (píldora),
 * no como texto azul suelto que se confunde con el resto (cambiar fecha,
 * Recalcular pendientes, cambiar modo…). El fundador lo pidió explícito. */
function BotonMini({
  children,
  onClick,
  disabled,
  tono = "accent",
}: {
  children: React.ReactNode;
  onClick: () => void;
  disabled?: boolean;
  tono?: "accent" | "neutro";
}) {
  const estilo =
    tono === "accent"
      ? "border-accent/40 bg-accent/10 text-accent hover:bg-accent/20"
      : "border-white/15 bg-white/5 text-dim hover:border-white/30 hover:text-ink";
  return (
    <button
      onClick={onClick}
      disabled={disabled}
      className={
        "inline-flex shrink-0 items-center gap-1 rounded-full border px-2.5 py-1 text-[12px] font-semibold disabled:opacity-50 " +
        estilo
      }
    >
      {children}
    </button>
  );
}

/** Fila del panel Ritmo: icono en chip + etiqueta pequeña + valor en bold.
 * Más visual que la lista dt/dd, sin ocupar más espacio (lo pidió el fundador:
 * es un resumen importante). */
function RitmoFila({ icono, etiqueta, valor, color }: { icono: React.ReactNode; etiqueta: string; valor: string; color: "accent" | "done" | "warn" }) {
  const chip = { accent: "bg-accent/12 text-accent", done: "bg-done/12 text-done", warn: "bg-warn/12 text-warn" }[color];
  return (
    <div className="flex items-center gap-3 rounded-[10px] border border-hairline bg-surface-2/40 px-3 py-2.5">
      <span className={"grid h-7 w-7 shrink-0 place-items-center rounded-lg " + chip} aria-hidden>
        {icono}
      </span>
      <span className="flex min-w-0 flex-1 items-baseline justify-between gap-2">
        <span className="text-[11.5px] text-dim">{etiqueta}</span>
        <span className="shrink-0 text-[13.5px] font-bold tabular-nums">{valor}</span>
      </span>
    </div>
  );
}
function IconoReloj() {
  return (
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
      <circle cx="12" cy="12" r="8.5" /><path d="M12 7.5V12l3 1.8" />
    </svg>
  );
}
function IconoBandera() {
  return (
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
      <path d="M5 21V4M5 4h11l-2 3.5L16 11H5" />
    </svg>
  );
}
function IconoCiclos() {
  return (
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
      <path d="M20 11a8 8 0 1 0-.5 4M20 5v6h-6" />
    </svg>
  );
}

// El vocabulario y los iconos de estado viven en SelectorEstado (fuente única
// compartida con el detalle). El ciclo por toques MURIÓ: adivinar no es
// elegir; ahora el círculo abre el menú de los 5 estados.

function FilaItem({
  item,
  ocupado,
  modo,
  onCambio,
  onAbrirDetalle,
}: {
  item: ItemChecklistUI;
  ocupado: boolean;
  /** el modo del espacio: decide si la chapa "esta semana" es de fecha o de bit. */
  modo: ModoCamino | null;
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
        "rounded-cinta border px-4 py-3.5 " +
        // No aplica: superficie un paso MÁS OSCURA (#0C0C10), no una opacidad
        // sobre la superficie normal — así lo retirado "se apaga" sin volverse
        // ilegible. El color nunca va solo: la forma del aro ya lo dice.
        (retirada
          ? "border-hairline bg-surface-3"
          : item.destacado && !hecho
            ? "border-done/35 bg-surface"
            : "border-hairline bg-surface")
      }
    >
      <div className="flex items-start gap-3.5">
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
              (hecho ? "text-dim line-through" : retirada ? "text-[#8A8B92]" : "text-ink")
            }
            title="Ver el detalle de esta actividad"
          >
            {item.texto}
          </button>
          {retirada && (
            <span className="mt-0.5 block text-[12.5px] text-[#8A8B92]">
              no aplica{item.no_aplica_motivo ? ` · ${item.no_aplica_motivo}` : ""}
            </span>
          )}
          {!hecho && !retirada && item.estado !== "pendiente" && (
            <span className="mt-0.5 block text-[12.5px] text-done">{ETIQUETA_ESTADO[item.estado]}</span>
          )}
          {!hecho && !retirada && chapaEstaSemana(modo, item) && (
            // "esta semana": chapa HONESTA (adjudicación ago 2026). En modo fechas
            // solo si la fecha vigente cae en la semana actual; en a-mi-ritmo,
            // atada a `destacado`. Borde verde (no fondo lleno), como fija Design.
            <span className="mt-1 inline-block rounded-full border border-done/30 px-2.5 py-0.5 text-[11.5px] font-semibold text-done">
              esta semana
            </span>
          )}
          {!hecho && !retirada && item.fecha_base && (
            <span className="mt-0.5 block text-[12.5px] text-accent">para el {fechaHumanaCorta(item.fecha_base)}</span>
          )}
          {hecho && item.completed_at && !editandoFecha && (
            // La fecha es un DATO (verde, informativo).
            <span className="mt-1 block text-[12.5px] text-done">hecho el {fechaHumanaCorta(item.completed_at)}</span>
          )}
          {/* "cambiar fecha" ABAJO A LA DERECHA, debajo del texto: no le roba
              espacio a la actividad (el texto es el protagonista). El botón
              "Marcar hecho" se retiró; el menú del círculo es la vía única. */}
          {hecho && !editandoFecha && (
            <span className="mt-2 flex justify-end">
              <BotonMini onClick={() => setEditandoFecha(true)} disabled={ocupado} tono="accent">
                cambiar fecha
              </BotonMini>
            </span>
          )}
        </span>
        {/* Nota rápida: indicador + entrada de un clic (mismo campo que el
            detalle y que el Calendario; opcional siempre). */}
        <NotaRapida id={item.id} nota={item.nota} ocupado={ocupado} onGuardar={(nota) => onCambio({ nota })} />
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
  modo,
  onCambio,
  onAbrirDetalle,
}: {
  grupo: NonNullable<ReturnType<typeof grupoVigente>>;
  titulos: Record<number, string>;
  ocupado: boolean;
  /** el modo del ESPACIO: en 'fechas' la fila lee por fecha vigente y la chapa
   * "esta semana" es honesta; en 'ritmo'/null, orden del plan + chapa=destacado. */
  modo: ModoCamino | null;
  onCambio: (item: ItemChecklistUI, cambio: CambioItem) => void;
  /** Fase 4.3.2: abrir el detalle de un ítem, con el título de SU etapa. */
  onAbrirDetalle: (item: ItemChecklistUI, tituloEtapa: string) => void;
}) {
  return (
    <div className="flex flex-col gap-5">
      {grupo.etapas.map(({ etapa, items }) => {
        const c = conteo(items);
        // El nombre puede envolver; el conteo va en `extra` (columna derecha,
        // junto al chevron) para que TODOS queden alineados, no empujados por el
        // largo del título. tabular-nums para que las cifras no bailen.
        const encabezado = (
          <span className="flex min-w-0 items-baseline gap-3">
            <span className="shrink-0 text-[13px] font-bold text-accent">{String(etapa).padStart(2, "0")}</span>
            <span className="text-[15px] font-semibold [text-wrap:pretty]">{titulos[etapa] ?? `Etapa ${etapa}`}</span>
          </span>
        );
        const conteoEtapa = (
          <span className="shrink-0 text-xs font-semibold tabular-nums text-done">
            {c.hechos}/{c.total}
          </span>
        );
        // HOMOGÉNEO: toda etapa es un acordeón (con su chevron). Decisión del
        // fundador: la primera vista SIEMPRE colapsada — ninguna etapa abre
        // sola; el lector despliega la que quiere trabajar.
        return (
          <Acordeon key={etapa} titulo={encabezado} abierto={false} extra={conteoEtapa} variante="etapa">
            <div className="flex flex-col gap-2.5">
              {/* Orden (adjudicación ago 2026): en modo FECHAS, por fecha vigente
                  asc (la destacada del lunes sube al frente); en a-mi-ritmo, el
                  orden del plan intacto. La fecha (el viernes compartido) NO se
                  toca: solo el orden de lectura. */}
              {(modo === "fechas" ? ordenarEnFechas(items) : items).map((item) => (
                <FilaItem key={item.id} item={item} ocupado={ocupado} modo={modo} onCambio={(c) => onCambio(item, c)} onAbrirDetalle={() => onAbrirDetalle(item, titulos[etapa] ?? `Etapa ${etapa}`)} />
              ))}
            </div>
          </Acordeon>
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
            lo que haga falta. De eso compongo el «qué ha pasado», sin que lo redactes dos veces.
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
/** Los chips de capacidad en palabras de persona (el valor que viaja a la base
 * es el literal de CAPACIDAD_SEMANAL; esto es solo cómo se lee en pantalla). */
const ETIQUETA_CAPACIDAD: Record<CapacidadSemanal, string> = {
  "2-5": "2 a 5 horas",
  "5-10": "5 a 10 horas",
  "10-20": "10 a 20 horas",
  "20+": "Más de 20 horas",
};

/**
 * Las fechas propuestas del ritual, por tramo (cada dominio cuenta desde su
 * propio plan). Scheduler F2: con TODAS las tareas estimadas se EMPAQUETA contra
 * la capacidad declarada (lib/empaquetado.ts); si falta una sola banda, el tramo
 * entero cae al sugeridor viejo (lib/fechasBase.ts), que sigue vivo y jamás
 * muere. La decisión es por tramo y `empaquetable` la toma el llamador mirando
 * todos: media planificación por capacidad y media por etapa sería un calendario
 * mentiroso.
 */
export function calcularFechasRitual(
  tramos: GrupoRitual[],
  opts: {
    diaPreferido: number | null;
    cadenciaSemanas?: number;
    capacidad: CapacidadSemanal;
    empaquetable: boolean;
    /** F4: el multiplicador personal de cada espacio. Solo llega en los
     * RECÁLCULOS; vacío o ausente = factor 1 (el reparto de siempre). */
    factoresPorDominio?: Record<string, FactoresPorBanda>;
  }
): Record<string, string> {
  return Object.fromEntries(
    tramos.flatMap((g) => {
      const propuestas = opts.empaquetable
        ? empaquetarFechas({
            ancla: g.planCreatedAt,
            capacidad: opts.capacidad,
            diaPreferido: opts.diaPreferido,
            factores: opts.factoresPorDominio?.[g.dominio],
            items: g.items.map((i) => ({
              id: i.id,
              etapa: i.etapa,
              destacado: i.destacado,
              banda: i.banda,
              espera_externa: i.espera_externa,
            })),
          }).fechas
        : sugerirFechasBase({
            planCreatedAt: g.planCreatedAt,
            diaPreferido: opts.diaPreferido,
            cadenciaSemanas: opts.cadenciaSemanas,
            items: g.items.map((i) => ({ id: i.id, etapa: i.etapa, destacado: i.destacado })),
          });
      return propuestas.map((s) => [s.id, s.fecha] as const);
    })
  );
}

/** El ritual de la línea base (canon 10, vista B). Las fechas se reparten
 * determinísticamente (empaquetado.ts contra la capacidad, o fechasBase.ts de
 * fallback; cero LLM en los dos) y el usuario ajusta la que quiera. Tema azul:
 * fijar fechas es planear. */
function RitualFechas({
  grupos,
  cadenciaSemanas,
  soloPendientes,
  guardando,
  error,
  capacidad,
  cumplidasPorDominio = {},
  onCapacidad,
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
  /** Scheduler F2: horas por semana declaradas para ESTE espacio (null = sin
   * declarar; el ritual arranca en el chip por defecto). */
  capacidad?: CapacidadSemanal | null;
  /** Scheduler F4: las tareas cumplidas de cada espacio (todos sus ciclos), la
   * materia prima del multiplicador personal. Solo se usan en el recálculo. */
  cumplidasPorDominio?: Record<string, MuestraCumplida[]>;
  /** Persiste la capacidad elegida. Sin este manejador la pregunta no aparece. */
  onCapacidad?: (c: CapacidadSemanal) => void;
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
  // Scheduler F2: la capacidad SOLO manda si todas las tareas traen banda. Con
  // una sin estimar, el plan entero cae al sugeridor viejo (fallback declarado)
  // y la pregunta de capacidad no se hace: preguntar algo que no mueve nada
  // sería teatro.
  const empaquetable = useMemo(() => tramos.every((g) => hayBandas(g.items)), [tramos]);
  const [capacidadLocal, setCapacidadLocal] = useState<CapacidadSemanal>(capacidad ?? CAPACIDAD_DEFAULT);
  const preguntarCapacidad = empaquetable && Boolean(onCapacidad);

  // Scheduler F4: el multiplicador personal manda SOLO en los recálculos. La
  // primera línea base se pone con el modelo limpio: todavía no hay ritmo real
  // que aprender, y estrenar un plan ya corregido por la historia de otro ciclo
  // sería adivinar. La vara del factor es la capacidad VIGENTE, así que subirla
  // deja el recálculo momentáneamente conservador hasta que entren muestras
  // nuevas: se prefiere ese error al de prometer de más.
  const factoresPorDominio = useMemo(() => {
    if (!soloPendientes || !empaquetable) return {};
    const out: Record<string, FactoresPorBanda> = {};
    for (const g of tramos) {
      out[g.dominio] = factorPorBanda({ hechas: cumplidasPorDominio[g.dominio] ?? [], capacidad: capacidadLocal });
    }
    return out;
  }, [tramos, soloPendientes, empaquetable, capacidadLocal, cumplidasPorDominio]);

  // Una llamada al repartidor POR TRAMO: cada dominio cuenta desde su propio plan.
  const sugeridas = useMemo(
    () =>
      calcularFechasRitual(tramos, {
        diaPreferido,
        cadenciaSemanas,
        capacidad: capacidadLocal,
        empaquetable,
        factoresPorDominio,
      }),
    [tramos, diaPreferido, cadenciaSemanas, capacidadLocal, empaquetable, factoresPorDominio]
  );
  // Fecha vigente por ítem (YYYY-MM-DD) y qué ítems tocó el usuario (=ajustada).
  const [fechas, setFechas] = useState<Record<string, string>>(sugeridas);
  const [editados, setEditados] = useState<Record<string, true>>({});

  // Cambiar la capacidad es cambiar la premisa: se replanifica TODO el ritual y
  // los ajustes manuales previos se descartan (quedarían mezclados con dos
  // repartos distintos). Se persiste para que el espacio lo recuerde.
  function elegirCapacidad(c: CapacidadSemanal) {
    if (c === capacidadLocal) return;
    setCapacidadLocal(c);
    // Los factores se rebasan con la capacidad nueva (la vara del "prometido"
    // cambia con ella), así que se recalculan aquí y no se arrastran.
    const factores: Record<string, FactoresPorBanda> = {};
    if (soloPendientes && empaquetable) {
      for (const g of tramos) {
        factores[g.dominio] = factorPorBanda({ hechas: cumplidasPorDominio[g.dominio] ?? [], capacidad: c });
      }
    }
    setFechas(
      calcularFechasRitual(tramos, {
        diaPreferido,
        cadenciaSemanas,
        capacidad: c,
        empaquetable,
        factoresPorDominio: factores,
      })
    );
    setEditados({});
    onCapacidad?.(c);
  }

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

      {/* Scheduler F2: la pregunta de capacidad. Es la premisa del reparto, así
          que va ARRIBA de las fechas y cambiarla las recalcula a la vista. */}
      {preguntarCapacidad && (
        <div className="mx-6 mb-2 rounded-cinta border border-hairline bg-surface-2 px-5 py-4 sm:mx-8">
          <p className="text-[14px] font-semibold">¿Cuántas horas por semana puedes darle a este espacio?</p>
          <div className="mt-3 flex flex-wrap gap-2">
            {CAPACIDAD_SEMANAL.map((c) => {
              const activa = c === capacidadLocal;
              return (
                <button
                  key={c}
                  type="button"
                  onClick={() => elegirCapacidad(c)}
                  disabled={guardando}
                  aria-pressed={activa}
                  className={
                    "min-h-[40px] rounded-[10px] border px-4 py-2 text-[13.5px] font-semibold disabled:opacity-50 " +
                    (activa ? "border-accent bg-accent/15 text-accent" : "border-hairline text-ink hover:border-accent/60")
                  }
                >
                  {ETIQUETA_CAPACIDAD[c]}
                </button>
              );
            })}
          </div>
          <p className="mt-3 text-[12.5px] leading-relaxed text-dim">
            Reparto las semanas según el trabajo que lleva cada tarea, y planeo con el piso de lo que me des: si te
            sobra tiempo, vas adelantado. Puedes cambiarlo cuando quieras.
          </p>
        </div>
      )}

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

/** Los iconos de las tres caras del espacio (para el selector segmentado). */
function IconoCara({ cara }: { cara: Cara }) {
  const p = { stroke: "currentColor", strokeWidth: 1.6, fill: "none" as const, strokeLinecap: "round" as const, strokeLinejoin: "round" as const };
  return (
    <svg width="15" height="15" viewBox="0 0 20 20" aria-hidden>
      {cara === "plan" ? (
        <>
          <rect x="4" y="3" width="12" height="14" rx="1.5" {...p} />
          <line x1="7" y1="7" x2="13" y2="7" {...p} />
          <line x1="7" y1="10" x2="13" y2="10" {...p} />
          <line x1="7" y1="13" x2="11" y2="13" {...p} />
        </>
      ) : cara === "manos" ? (
        <path d="M4 10.5l3 3 9-9" {...p} strokeWidth={2} />
      ) : (
        <>
          <line x1="3" y1="10" x2="17" y2="10" {...p} />
          <circle cx="5" cy="10" r="1.7" fill="currentColor" stroke="none" />
          <circle cx="10" cy="10" r="1.7" fill="currentColor" stroke="none" />
          <circle cx="15" cy="10" r="1.5" {...p} strokeWidth={1.4} />
        </>
      )}
    </svg>
  );
}

/**
 * Mundos de protección (P3): EL REGISTRO VISIBLE. La herramienta canónica del
 * mundo (el registro de riesgos, el de peligros, el inventario de activos)
 * instanciada sobre las actividades reales de la persona.
 *
 * Ruido cero: solo aparece en los mundos de PROTECCIÓN, y si todavía no hay
 * enlaces dice honesto que se llenará con su plan, en vez de pintar una tabla
 * vacía que parezca rota.
 */
function RegistroProteccion({ nombreMundo, entradas }: { nombreMundo: string; entradas: EntradaRegistro[] }) {
  return (
    <section className="rounded-panel border border-hairline bg-surface p-5 sm:p-6">
      <p className="text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">Registro de {nombreMundo}</p>
      {entradas.length === 0 ? (
        <p className="mt-2.5 text-[13.5px] leading-relaxed text-dim [text-wrap:pretty]">
          Este registro se llenará con el plan de este mundo: cada cosa que detecte quedará aquí junto a la
          respuesta que la atiende.
        </p>
      ) : (
        <ul className="mt-3 flex flex-col gap-2.5">
          {entradas.map((e) => {
            const sev = severidadEnPalabras(e);
            return (
              <li key={e.id} className="rounded-cinta border border-hairline bg-surface-2 px-4 py-3">
                <p className="text-[14px] font-semibold [text-wrap:pretty]">{e.deteccion ?? e.respuesta}</p>
                {sev && <p className="mt-1 text-[12.5px] text-warn">{sev}</p>}
                <p className="mt-1.5 text-[12.5px] text-dim [text-wrap:pretty]">
                  Protege: <span className="text-ink">{textoProtege(e)}</span>
                </p>
                {e.deteccion && (
                  <p className="mt-1 text-[12.5px] text-dim [text-wrap:pretty]">
                    Tu respuesta: <span className="text-ink">{e.respuesta}</span>
                  </p>
                )}
              </li>
            );
          })}
        </ul>
      )}
    </section>
  );
}

/** Scheduler F2: las horas por semana de un espacio, ya declaradas, con su
 * corrección. Vive en la cinta de "fechas activas" porque es donde el usuario
 * viene cuando su semana cambió. */
function CapacidadDelEspacio({
  dominio,
  capacidad,
  onCapacidad,
}: {
  dominio: string;
  capacidad: CapacidadSemanal;
  onCapacidad: (dominio: string, c: CapacidadSemanal) => void;
}) {
  const [editando, setEditando] = useState(false);
  if (!editando) {
    return (
      <p className="mt-2.5 border-t border-hairline pt-2.5 text-[12.5px] text-dim">
        Le das <span className="font-semibold text-ink">{ETIQUETA_CAPACIDAD[capacidad].toLowerCase()}</span> por semana.{" "}
        <button onClick={() => setEditando(true)} className="text-accent hover:underline">
          cambiar
        </button>
      </p>
    );
  }
  return (
    <div className="mt-2.5 border-t border-hairline pt-2.5">
      <p className="text-[12.5px] text-dim">¿Cuántas horas por semana puedes darle ahora?</p>
      <div className="mt-2 flex flex-wrap gap-2">
        {CAPACIDAD_SEMANAL.map((c) => (
          <button
            key={c}
            type="button"
            onClick={() => {
              if (c !== capacidad) onCapacidad(dominio, c);
              setEditando(false);
            }}
            aria-pressed={c === capacidad}
            className={
              "min-h-[36px] rounded-[9px] border px-3 py-1.5 text-[12.5px] font-semibold " +
              (c === capacidad ? "border-accent bg-accent/15 text-accent" : "border-hairline text-ink hover:border-accent/60")
            }
          >
            {ETIQUETA_CAPACIDAD[c]}
          </button>
        ))}
      </div>
      <p className="mt-2 text-[12px] text-dim">Las nuevas horas entran cuando toques Recalcular pendientes.</p>
    </div>
  );
}

/**
 * "Todo separado" (T3c): el modo del camino + ritual de fechas de UN espacio
 * (el core o un mundo). Misma experiencia scopeada: el selector, el ritual de
 * línea base, y el estado "fechas activas / pospuesta" — todo del `dominio`
 * que se le pase. Antes vivía embebido en el bloque del core; extraído para
 * que el hub del mundo lo renderice idéntico con SU contexto (grupos, plan,
 * modo). El estado (mostrarSelector/recalcular/pospuesto) es del espacio en
 * pantalla — ManosALaObra scopea una sola vista, así que uno basta.
 */
function PanelModoFechas({
  dominio,
  modo,
  planId,
  hayFechas,
  grupos,
  cadenciaSemanas,
  tieneTareasConFecha,
  mostrarSelector,
  guardandoModo,
  guardandoBaseline,
  errorBaseline,
  recalcularPendientes,
  pospuesto,
  capacidad,
  cumplidasPorDominio,
  onCapacidad,
  onElegir,
  onConfirmar,
  onPosponer,
  onPonerFechas,
  onRecalcular,
  onDescargarIcs,
}: {
  dominio: string;
  modo: ModoCamino | null;
  planId: string | null;
  hayFechas: boolean;
  grupos: GrupoRitual[];
  cadenciaSemanas: number;
  tieneTareasConFecha: boolean;
  mostrarSelector: boolean;
  guardandoModo: boolean;
  guardandoBaseline: boolean;
  errorBaseline: string | null;
  recalcularPendientes: boolean;
  pospuesto: boolean;
  /** Scheduler F2: las horas por semana de ESTE espacio (null = sin declarar). */
  capacidad?: CapacidadSemanal | null;
  /** Scheduler F4: las cumplidas por espacio, para el multiplicador personal. */
  cumplidasPorDominio?: Record<string, MuestraCumplida[]>;
  onCapacidad?: (dominio: string, c: CapacidadSemanal) => void;
  onElegir: (dominio: string, modo: ModoCamino) => void;
  onConfirmar: (planId: string, fechas: Array<{ item_id: string; fecha: string; origen: FechaBaseOrigen }>) => void;
  onPosponer: () => void;
  onPonerFechas: () => void;
  onRecalcular: () => void;
  onDescargarIcs: () => void;
}) {
  return (
    <>
      {/* la elección del modo: primera entrada (modo null) o al tocar "cambiar" */}
      {(modo === null || mostrarSelector) && (
        <TarjetaModo ocupado={guardandoModo} onElegir={(m) => onElegir(dominio, m)} />
      )}

      {/* ritual de la línea base (modo fechas) — SOLO de este espacio (B5) */}
      {modo === "fechas" && planId && (recalcularPendientes || (!hayFechas && !pospuesto)) && (
        <RitualFechas
          grupos={grupos}
          cadenciaSemanas={cadenciaSemanas}
          soloPendientes={recalcularPendientes}
          guardando={guardandoBaseline}
          error={errorBaseline}
          capacidad={capacidad}
          cumplidasPorDominio={cumplidasPorDominio}
          onCapacidad={onCapacidad ? (c) => onCapacidad(dominio, c) : undefined}
          onAceptar={(fechas) => onConfirmar(planId, fechas)}
          onPosponer={onPosponer}
        />
      )}

      {/* fechas ya puestas: pospuesta (reabrir) o activas (recalcular) */}
      {modo === "fechas" && planId && !recalcularPendientes && !hayFechas && pospuesto && (
        <div className="flex items-center justify-between gap-3 rounded-cinta border border-hairline bg-surface px-4 py-3">
          <p className="text-[13px] text-dim">Sin fechas no podré recordarte nada.</p>
          <BotonMini onClick={onPonerFechas}>Poner fechas ahora</BotonMini>
        </div>
      )}
      {modo === "fechas" && planId && !recalcularPendientes && hayFechas && (
        <div className="rounded-cinta border border-hairline bg-surface px-4 py-3">
          <div className="flex flex-wrap items-center justify-between gap-3">
            <p className="text-[13px] text-dim">
              <span className="font-semibold text-accent">Fechas activas.</span> Tu camino tiene línea base.
            </p>
            <div className="flex flex-wrap items-center gap-2">
              {/* Calendario Nivel 0: las fechas pendientes de ESTE espacio al .ics */}
              {tieneTareasConFecha && (
                <BotonMini onClick={onDescargarIcs} tono="accent">
                  Añadir a mi calendario
                </BotonMini>
              )}
              <BotonMini onClick={onRecalcular}>Recalcular pendientes</BotonMini>
            </div>
          </div>
          {/* Scheduler F2: las horas por semana de este espacio, editables aquí.
              Cambiarlas NO reescribe el calendario a tus espaldas: se usan en el
              siguiente "Recalcular pendientes", y se dice. */}
          {capacidad && onCapacidad && (
            <CapacidadDelEspacio dominio={dominio} capacidad={capacidad} onCapacidad={onCapacidad} />
          )}
        </div>
      )}
    </>
  );
}

// "Todo separado" (T5, D6): las SEIS tarjetas hermanas de un espacio — sus
// cuatro accesos (bitácora · calendario · análisis · documentos) y sus dos
// acciones (realizar/cerrar · ciclo de profundización) — comparten UNA sola
// forma: icono + título + descripción, y la TARJETA ENTERA es el botón. En las
// de acción, pulsar abre el flujo de confirmación/ritual: cambia la forma,
// jamás la función. Ninguna tarjeta de aside vive fuera de este componente
// (lo prueba un test de contrato). El `tono` 'done' viste la de realizar/cierre.
const ICONO_ACCESO = {
  bitacora: (
    <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round" aria-hidden>
      <path d="M12 5v14" /><circle cx="12" cy="6.5" r="1.6" /><circle cx="12" cy="12" r="1.6" /><circle cx="12" cy="17.5" r="1.6" />
      <path d="M14 6.5h4M14 12h4M14 17.5h3" />
    </svg>
  ),
  calendario: (
    <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round" aria-hidden>
      <rect x="3.5" y="5" width="17" height="15" rx="2.5" /><path d="M3.5 9.5h17M8 3.5v3M16 3.5v3" />
    </svg>
  ),
  analisis: (
    <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round" aria-hidden>
      <path d="M4 20V4" /><path d="M4 20h16" /><rect x="7.5" y="12" width="3" height="5" rx="0.8" /><rect x="13.5" y="8" width="3" height="9" rx="0.8" />
    </svg>
  ),
  documentos: (
    <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round" aria-hidden>
      <path d="M8 4h6l4 4v10a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z" /><path d="M13.5 4v4.5H18M9.5 13h5M9.5 16.5h5" />
    </svg>
  ),
  realizar: (
    <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round" aria-hidden>
      <path d="M5 21V4h11l-2 3.5L16 11H5" /><path d="M5 4v17" />
    </svg>
  ),
  ciclo: (
    <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round" aria-hidden>
      <path d="M4.5 12a7.5 7.5 0 0 1 12.9-5.2l1.6 1.6" /><path d="M19.5 12a7.5 7.5 0 0 1-12.9 5.2l-1.6-1.6" />
      <path d="M18.5 3.5v4.9h-4.9M5.5 20.5v-4.9h4.9" />
    </svg>
  ),
} as const;

function TarjetaAcceso({
  icono,
  titulo,
  descripcion,
  onClick,
  tono = "accent",
}: {
  icono: keyof typeof ICONO_ACCESO;
  titulo: string;
  descripcion: string;
  onClick: () => void;
  tono?: "accent" | "done";
}) {
  const chip = tono === "done" ? "bg-done/12 text-done" : "bg-accent/12 text-[#7B9DFF]";
  const borde = tono === "done" ? "hover:border-done/45" : "hover:border-accent/45";
  return (
    <button
      onClick={onClick}
      className={`w-full rounded-panel border border-hairline bg-surface p-5 text-left transition-colors hover:bg-[#141419] ${borde}`}
    >
      <div className="flex items-start gap-3.5">
        <span aria-hidden className={`grid h-[42px] w-[42px] shrink-0 place-items-center rounded-[11px] ${chip}`}>
          {ICONO_ACCESO[icono]}
        </span>
        <div className="min-w-0">
          <p className={`text-[14px] font-semibold ${tono === "done" ? "text-done" : "text-ink"}`}>{titulo}</p>
          <p className="mt-1 text-[12.5px] leading-relaxed text-dim [text-wrap:pretty]">{descripcion}</p>
        </div>
      </div>
    </button>
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
  modos,
  capacidades = {},
  onModoCambiado,
  onRecargarChecklist,
  onVerAnalisis,
  onVerDocumentos,
  onVerBitacora,
  onVerCalendario,
  onRealizada,
  onMundoCerrado,
  entrevistaAbierta,
  onVolverEntrevista,
  onItemActualizado,
  onSeguimientoIniciado,
  onMundoIniciado,
  onComprarPlanMundo,
  soloDominio,
  caraInicial,
  onCaraCambio,
  proyectoCreatedAt,
  organizadorAt,
  realizadaAt,
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
  // "Todo separado" (T3c): copia local del modo POR ESPACIO para reflejar al
  // instante el modo que un MUNDO acaba de elegir en su hub (el core sigue por
  // modoCamino, refrescado por el padre vía onModoCambiado). Se resincroniza si
  // el padre recarga y trae otro mapa — AJUSTE DURANTE EL RENDER (no en efecto),
  // el patrón de React de "guardar info de renders previos": evita el setState
  // en efecto y el render en cascada (react-hooks/set-state-in-effect).
  const [modosLocal, setModosLocal] = useState<Record<string, ModoCamino>>(modos);
  const [modosPrevios, setModosPrevios] = useState(modos);
  if (modos !== modosPrevios) {
    setModosPrevios(modos);
    setModosLocal(modos);
  }
  const modoDeMundo = (dominio: string): ModoCamino | null => modosLocal[dominio] ?? null;
  // Scheduler F2: misma mecánica para las horas por semana de cada espacio.
  const [capacidadesLocal, setCapacidadesLocal] = useState<Record<string, CapacidadSemanal>>(capacidades);
  const [capacidadesPrevias, setCapacidadesPrevias] = useState(capacidades);
  if (capacidades !== capacidadesPrevias) {
    setCapacidadesPrevias(capacidades);
    setCapacidadesLocal(capacidades);
  }
  const capacidadDe = (dominio: string): CapacidadSemanal | null => capacidadesLocal[dominio] ?? null;
  // Scheduler F4: las tareas YA cumplidas de cada espacio, de TODOS sus ciclos.
  // Son la materia prima del multiplicador personal. Se toman del checklist
  // completo y no del grupo vigente a propósito: un plan de seguimiento nace sin
  // ninguna hecha, y tirar la historia del ciclo anterior sería empezar a
  // aprender de cero cada vez que el usuario avanza.
  const cumplidasPorDominio = useMemo(() => {
    const out: Record<string, MuestraCumplida[]> = {};
    for (const p of checklist?.planes ?? []) {
      for (const e of p.etapas) {
        for (const i of e.items) {
          if (i.estado === "hecho" && i.completed_at && i.banda) {
            (out[i.dominio] ??= []).push({
              banda: i.banda,
              completed_at: i.completed_at,
              espera_externa: i.espera_externa,
            });
          }
        }
      }
    }
    return out;
  }, [checklist]);
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
  // Pista de primer uso del selector de estado (solo hasta el primer cambio,
  // recordado en localStorage). SSR-safe: nace false y se enciende al montar.
  const [mostrarPista, setMostrarPista] = useState(false);
  useEffect(() => {
    let yaUsado = true;
    try {
      yaUsado = Boolean(localStorage.getItem(CLAVE_PISTA_ESTADO));
    } catch {
      /* sin localStorage (modo privado): la pista simplemente no molesta */
    }
    if (yaUsado) return;
    // setTimeout(0) difiere el setState fuera del cuerpo del efecto (patrón
    // aceptado en este repo para set-state-in-effect; ver Landing).
    const t = setTimeout(() => setMostrarPista(true), 0);
    return () => clearTimeout(t);
  }, []);
  function pistaVista() {
    setMostrarPista(false);
    try {
      localStorage.setItem(CLAVE_PISTA_ESTADO, "1");
    } catch {
      /* no bloquea nada */
    }
  }

  const titulosCore = useMemo(() => titulosDeEtapas(planMd), [planMd]);
  const core = grupoVigente(checklist, "core");
  // useMemo: estabiliza la referencia para que las deps de los useMemo que lo
  // usan (gruposRitual) no cambien en cada render (react-hooks/exhaustive-deps).
  const itemsCore = useMemo(() => core?.etapas.flatMap((e) => e.items) ?? [], [core]);
  // Mundos de protección (P3): las actividades vigentes del núcleo con su #N,
  // del MISMO armador que usó el enlazador. El enlace se resuelve por id, así
  // que el número es solo cómo se nombra hoy: si el plan cambió, el registro
  // muestra la posición actual y no una congelada que ya no existe.
  const actividadesNucleo = useMemo(
    () =>
      armarSnapshot(
        itemsCore.map((i) => ({ id: i.id, texto: i.texto, etapa: i.etapa, orden: i.orden, estado: i.estado }))
      ).actividades.map((a) => ({ id: a.id, indice: a.indice, titulo: a.titulo })),
    [itemsCore]
  );
  const cCore = conteo(itemsCore);
  const tituloPlan = planMd.match(/^#\s+(.+)$/m)?.[1]?.trim() ?? null;

  // Campaña "Espacios": esta vista sirve UN espacio. `soloMundo` = el dominio
  // del mundo cuando estamos en su hub (si no, null). `mostrarCore` gatea todo
  // lo del core (header, rituales, checklist, historia, aside). `mundosVisibles`
  // filtra la sección de mundos: en el hub, solo ese mundo; en el core, ninguno
  // (viven en su hub); sin la prop, todos (comportamiento histórico intacto).
  const soloMundo = soloDominio && soloDominio !== ESPACIO_CORE ? soloDominio : null;
  const mostrarCore = !soloMundo;
  const mundosVisibles = mundosDelEspacio(mundos, soloDominio);

  // Campaña "Espacios": la cara activa (Plan · Manos a la obra · Tu avance). La
  // cara "manos" es el comportamiento actual (aditivo). El core la muestra en su
  // espacio; un mundo, solo cuando ya tiene plan (grupo). La URL la persiste.
  const [cara, setCara] = useState<Cara>(caraInicial ?? "manos");
  const cambiarCara = (c: Cara) => {
    setCara(c);
    onCaraCambio?.(c);
  };
  const coreEnEspacio = mostrarCore && soloDominio === ESPACIO_CORE;
  const opcionesCara: { id: Cara; nombre: string; icono: ReactNode }[] = [
    { id: "plan", nombre: "Plan", icono: <IconoCara cara="plan" /> },
    { id: "manos", nombre: "Manos a la obra", icono: <IconoCara cara="manos" /> },
    { id: "avance", nombre: "Tu avance", icono: <IconoCara cara="avance" /> },
  ];
  const hitosCore = hitosDeEspacio({
    espacio: "core",
    chispaAt: proyectoCreatedAt,
    claridadAt: organizadorAt,
    planAt: planCreatedAt,
    realizadaAt,
  });
  // Fase 3.8: la baseline está confirmada si algún ítem core ya tiene fecha.
  // Fase 4.1 (V3a): el ritual cubre el proyecto ENTERO. Cada tramo lleva su
  // propio ancla (el created_at del plan de SU dominio) y sus propios titulos
  // de etapa: un mundo activado en abril no puede fechar desde un plan core de
  // marzo. Un mundo sin plan o sin checklist todavia no tiene nada que fechar.
  // "Todo separado" (T3c, B5): el ritual del CORE es SOLO del core — ya NO
  // arrastra los tramos de los mundos (dominiosDelRitual). Cada mundo sella su
  // baseline en SU hub (T3c-2). Antes cubría el proyecto entero, mezclando medidas.
  const gruposRitual: GrupoRitual[] = useMemo(() => {
    const out: GrupoRitual[] = [];
    for (const dom of dominiosDelRitual(ESPACIO_CORE)) {
      if (esEspacioCore(dom) && core) {
        out.push({ dominio: "core", nombre: "Tu viaje principal", planCreatedAt, titulos: titulosCore, items: itemsCore });
      }
    }
    return out;
  }, [core, planCreatedAt, titulosCore, itemsCore]);

  // Con fechas ya puestas en CUALQUIER dominio no se reabre el ritual inicial;
  // un mundo nuevo entra por "recalcular pendientes" (V3a).
  const hayFechas = itemsCore.some((i) => i.fecha_base);

  // Calendario Nivel 0 (.ics, sin backend): las tareas PENDIENTES con fecha se
  // pueden llevar al calendario del teléfono, que pone el recordatorio nativo.
  const tareasConFecha = itemsCore
    .filter((i) => i.fecha_base && i.estado !== "hecho" && i.estado !== "no_aplica")
    .map((i) => ({ id: i.id, texto: i.texto, etapa: i.etapa, fechaBase: i.fecha_base! }));
  // Calendario .ics de UN espacio (T3c: cada espacio se lleva SUS fechas). T6:
  // cada evento lleva el prefijo [Espacio] en el título (mismo UID) para leerse
  // en el calendario del teléfono; `espacio` undefined = sin prefijo (ruido cero).
  function descargarIcsDe(
    tareas: Array<{ id: string; texto: string; etapa: number; fechaBase: string }>,
    nombre: string,
    espacio?: string
  ) {
    const ics = generarIcs({ nombreIdea: nombre, tareas: tareas.map((t) => ({ ...t, espacio })) });
    const blob = new Blob([ics], { type: "text/calendar;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `${nombre.replace(/[^\p{L}\p{N}]+/gu, "-").slice(0, 40) || "mi-idea"}-calendario.ics`;
    a.click();
    URL.revokeObjectURL(url);
  }

  // Ritmo: lecturas directas de lo persistido.
  const ultimaAccion = itemsCore
    .filter((i) => i.estado !== "pendiente")
    .map((i) => i.updated_at)
    .sort()
    .at(-1);
  const desde = itemsCore.map((i) => i.created_at).sort()[0];
  const ciclosAjuste = historial.filter((h) => h.etiqueta === "seguimiento").length;

  async function elegirModo(dominio: string, modo: ModoCamino) {
    setGuardandoModo(true);
    setError(null);
    try {
      const res = await fetch(`/api/project/${projectId}/modo`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ modo_camino: modo, dominio }),
      });
      if (!res.ok) {
        setError(ERROR_GENERICO);
        return;
      }
      // Reactivar fechas reabre el ritual (si aún no hay ninguna puesta).
      if (modo === "fechas") setPospuesto(false);
      setMostrarSelectorModo(false);
      // El core lo refresca el padre (dual-read); el mundo, la copia local.
      if (dominio === ESPACIO_CORE) onModoCambiado(modo);
      else setModosLocal((prev) => ({ ...prev, [dominio]: modo }));
    } catch {
      setError("no pudimos guardar tu elección; revisa tu internet e intenta de nuevo");
    } finally {
      setGuardandoModo(false);
    }
  }

  // Scheduler F2: las horas por semana que el usuario le da a ESTE espacio. Se
  // guardan en su fila de project_modos; el estado local manda mientras dure la
  // pantalla para que el ritual replanifique sin esperar al servidor. Si la
  // llamada falla, se avisa: la elección no se pierde en silencio.
  async function elegirCapacidad(dominio: string, capacidad: CapacidadSemanal) {
    setCapacidadesLocal((prev) => ({ ...prev, [dominio]: capacidad }));
    try {
      const res = await fetch(`/api/project/${projectId}/modo`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ capacidad_semanal: capacidad, dominio }),
      });
      if (!res.ok) setError(ERROR_GENERICO);
    } catch {
      setError("no pudimos guardar tus horas por semana; revisa tu internet e intenta de nuevo");
    }
  }

  // "Todo separado" (T3c): sella la baseline del plan del ESPACIO indicado (el
  // core o un mundo), no siempre el del core. Cada espacio sella lo suyo.
  async function confirmarBaseline(planId: string, fechas: Array<{ item_id: string; fecha: string; origen: FechaBaseOrigen }>) {
    setGuardandoBaseline(true);
    setErrorBaseline(null);
    try {
      const res = await fetch(`/api/project/${projectId}/baseline`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ plan_id: planId, fechas }),
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

  // Fase 4.7: mover la fecha objetivo de una pendiente, con cascada opcional a
  // las posteriores. El endpoint corre el mismo delta, congela originales y deja
  // UNA entrada de bitácora. Al terminar, recargamos para reflejar todas.
  async function moverFecha(itemId: string, fecha: string, cascada: boolean) {
    setError(null);
    try {
      const res = await fetch(`/api/project/${projectId}/mover-fecha`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ item_id: itemId, fecha, cascada }),
      });
      if (!res.ok) {
        setError(ERROR_GENERICO);
        return;
      }
      onRecargarChecklist();
    } catch {
      setError("no pudimos mover la fecha; revisa tu internet e intenta de nuevo");
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
    // Cambiar el estado cuenta como "ya descubrió el selector": la pista se va.
    if (cambio.estado !== undefined) pistaVista();
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
        // Scheduler F1: la banda corregida vuelve persistida (la ruta solo la
        // devuelve cuando se corrigió; si no, se conserva la del estado).
        banda: data.item?.banda ?? cambio.banda,
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
    <div className={"flex flex-col gap-6" + (soloMundo ? "" : " lg:grid lg:grid-cols-[1fr_300px] lg:items-start lg:gap-8")}>
      <div className="flex min-w-0 flex-col gap-7">
        {/* encabezado del core: verde ejecuta. En el hub de un mundo no va (su
            sección trae su propio encabezado). */}
        {mostrarCore && (
        <header className="anima-plan-in">
          <p className="mb-3 flex items-center gap-2 text-[11px] font-bold uppercase tracking-[1.2px] text-done">
            <span className="anima-green-pulse h-2 w-2 rounded-full bg-done" />
            Tu idea avanza en el mundo real
          </p>
          {tituloPlan && (
            <h2 className="text-2xl font-bold leading-tight tracking-tight sm:text-[28px]">{tituloPlan}</h2>
          )}
          {cCore.total > 0 && (
            // Avance en un RECUADRO propio: el porcentaje y la barra lado a lado.
            // La barra lleva ESCALA (25/50/75/100) para leer hasta dónde llega, y
            // su relleno es un DEGRADADO que arranca en azul (la iniciación) y se
            // torna verde puro al completar: el color cuenta el avance.
            <div className="mt-5 max-w-2xl rounded-[16px] border border-hairline bg-surface px-5 py-[18px]">
              <BarraAvance pct={barraPct} />
            </div>
          )}
          {/* Fase 4.3.2: el modo, COMPACTO (canon refrescado). El selector grande
              ya no vive aquí salvo en la primera entrada; "cambiar" lo reabre. */}
          {modoCamino !== null && !mostrarSelectorModo && (
            <p className="mt-3 flex flex-wrap items-center gap-2 text-[13px] text-dim">
              <span>
                Modo: <span className="font-semibold text-ink">{modoCamino === "ritmo" ? "a mi ritmo" : "con fechas"}</span>
              </span>
              <BotonMini onClick={() => setMostrarSelectorModo(true)} tono="accent">
                cambiar
              </BotonMini>
            </p>
          )}
        </header>
        )}

        {error && <p className="text-sm text-warn">{error}</p>}

        {mostrarCore && (
          <>
        {/* Campaña "Espacios": el selector segmentado de las tres caras del core.
            La cara "manos" (default) es el comportamiento actual (aditivo). */}
        {coreEnEspacio && <SelectorCara valor={cara} onCambio={cambiarCara} opciones={opcionesCara} />}
        {coreEnEspacio && cara === "plan" && planMd && (
          <PlanDocumento md={planMd} nombreIdea={tituloPlan ?? "Tu plan"} />
        )}
        {/* "Todo separado" (T2): "Tu avance" = SOLO la línea de hitos del espacio.
            Las estadísticas y la bitácora salieron de aquí; viven en sus propios
            accesos por espacio (Análisis / Mi bitácora). */}
        {coreEnEspacio && cara === "avance" && <LineaAvance hitos={hitosCore} />}
        {(!coreEnEspacio || cara === "manos") && (
          <>
        {/* "Todo separado" (T3c): el modo + ritual del CORE, con el panel común
            scopeado a su espacio (mismo componente que usa el hub del mundo). */}
        <PanelModoFechas
          dominio={ESPACIO_CORE}
          modo={modoCamino}
          planId={core?.plan_id ?? null}
          hayFechas={hayFechas}
          grupos={gruposRitual}
          cadenciaSemanas={cadenciaSemanas}
          tieneTareasConFecha={tareasConFecha.length > 0}
          mostrarSelector={mostrarSelectorModo}
          guardandoModo={guardandoModo}
          guardandoBaseline={guardandoBaseline}
          errorBaseline={errorBaseline}
          recalcularPendientes={recalcularPendientes}
          pospuesto={pospuesto}
          capacidad={capacidadDe(ESPACIO_CORE)}
          cumplidasPorDominio={cumplidasPorDominio}
          onCapacidad={elegirCapacidad}
          onElegir={elegirModo}
          onConfirmar={confirmarBaseline}
          onPosponer={() => {
            setPospuesto(true);
            setRecalcularPendientes(false);
          }}
          onPonerFechas={() => setPospuesto(false)}
          onRecalcular={() => setRecalcularPendientes(true)}
          onDescargarIcs={() => descargarIcsDe(tareasConFecha, tituloPlan ?? "Mi idea", mundos.length > 0 ? "Tu viaje" : undefined)}
        />

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
          <div className="lg:hidden">
            <TarjetaAcceso
              icono="ciclo"
              titulo="Ciclo de profundización"
              descripcion="¿La realidad te cambió el plan? Cuéntame qué pasó y lo recalculo desde donde estás."
              onClick={() => setRitual(true)}
            />
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

        {/* checklist maestro: viaje core. El rótulo solo desambigua cuando hay
            mundos VISIBLES apilados debajo (comportamiento histórico); en el
            core-solo de su hub no hay mundos abajo, así que no aparece. */}
        {core && mundosVisibles.length > 0 && (
          <p className="text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">
            Tu viaje core · <span className="text-done">{cCore.hechos}/{cCore.total}</span>
          </p>
        )}
        {/* Pista de PRIMER USO (se desvanece tras el primer cambio de estado):
            al quitar "Marcar hecho", el círculo es el único control, y hay que
            decir de una vez que ahí se toca. */}
        {core && cCore.total > 0 && mostrarPista && (
          <p className="flex items-center gap-2 rounded-cinta border border-dashed border-accent/[0.34] bg-accent/5 px-3.5 py-2 text-[12.5px] text-accent">
            <span aria-hidden className="flex h-[18px] w-[18px] shrink-0 overflow-hidden rounded-full border-[1.5px] border-accent">
              <span className="h-full w-1/2 bg-accent/60" />
            </span>
            Toca el círculo de una tarea para elegir su estado (hecha, en proceso, no aplica…).
          </p>
        )}
        {core ? (
          <GrupoEtapas grupo={core} titulos={titulosCore} ocupado={ocupado} modo={modoCamino} onCambio={aplicarCambio} onAbrirDetalle={abrirDetalle} />
        ) : (
          <p className="text-sm text-dim">
            Tu checklist nace del plan: genera tu plan y aquí aparecerán sus acciones.
          </p>
        )}
          </>
        )}
          </>
        )}

        {/* mundos activos: cada uno su sección/hub (canon 08). En el core-solo
            no se apila ninguno; en el hub, solo el suyo; sin la prop, todos. */}
        {mundosVisibles.map((mundo) => {
          const grupo = grupoVigente(checklist, mundo.dominio);
          const items = grupo?.etapas.flatMap((e) => e.items) ?? [];
          const c = conteo(items);
          const titulosMundo = mundo.plan ? titulosDeEtapas(mundo.plan.contenido_md) : {};
          // "Todo separado" (T3c): el contexto de modo/fechas de ESTE mundo (su
          // plan, su modo, sus fechas) para su propio ritual — idéntico al del
          // core, scopeado. El ancla del sugeridor es el created_at de SU plan.
          const modoMundo = modoDeMundo(mundo.dominio);
          const hayFechasMundo = items.some((i) => i.fecha_base);
          const gruposMundo: GrupoRitual[] =
            grupo && mundo.plan
              ? [{ dominio: mundo.dominio, nombre: mundo.nombre, planCreatedAt: mundo.plan.created_at, titulos: titulosMundo, items }]
              : [];
          const tareasMundo = items
            .filter((i) => i.fecha_base && i.estado !== "hecho" && i.estado !== "no_aplica")
            .map((i) => ({ id: i.id, texto: i.texto, etapa: i.etapa, fechaBase: i.fecha_base! }));
          const completado = Boolean(mundo.completadoAt);
          // En SU hub (soloMundo === este dominio) la sección es la PANTALLA
          // entera: sin marco de tarjeta y con el nombre como título grande.
          // Apilada bajo el core, conserva su tarjeta para separarse del resto.
          const esHub = soloMundo === mundo.dominio;
          return (
            <section
              key={mundo.dominio}
              className={esHub ? "anima-plan-in" : "rounded-panel border border-hairline bg-surface p-5 sm:p-6"}
            >
              <div className="flex flex-wrap items-center gap-3">
                <h3 className={esHub ? "text-2xl font-bold tracking-tight sm:text-[26px]" : "text-base font-semibold"}>
                  {mundo.nombre}
                </h3>
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
                    {mundo.plan ? "Mundo activo" : "Por explorar"}
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
                esHub ? (
                  /* Campaña "Espacios": en su hub, el mundo tiene las TRES caras
                     (selector segmentado). La cara "manos" es su checklist. */
                  <div className="mt-4">
                    <SelectorCara valor={cara} onCambio={cambiarCara} opciones={opcionesCara} />
                    {cara === "plan" && (
                      <div className="mt-4 flex flex-col gap-4">
                        {mundo.resumenMd && (
                          <div className="rounded-panel border border-accent/30 bg-accent/[0.04] p-5">
                            <p className="mb-2 text-[11px] font-semibold uppercase tracking-[1.2px] text-accent">Tu diagnóstico</p>
                            <Markdown>{mundo.resumenMd}</Markdown>
                          </div>
                        )}
                        {mundo.plan && <PlanDocumento md={mundo.plan.contenido_md} nombreIdea={mundo.nombre} />}
                      </div>
                    )}
                    {cara === "avance" && (
                      <div className="mt-4">
                        {/* "Todo separado" (T2): "Tu avance" del mundo = SOLO su línea
                            de hitos. Estadísticas y bitácora del mundo viven en sus
                            accesos por espacio (Análisis / Mi bitácora), no aquí. */}
                        <LineaAvance
                          hitos={hitosDeEspacio({
                            espacio: "mundo",
                            nombre: mundo.nombre,
                            diagnosticoAt: mundo.resumenAt,
                            planAt: mundo.plan?.created_at,
                            cerradoAt: mundo.completadoAt,
                          })}
                        />
                      </div>
                    )}
                    {cara === "manos" && (
                      <div className="mt-4 flex flex-col gap-4">
                        {/* "Todo separado" (T3c): el mundo invita a SU propio
                            modo/fechas como el core — misma experiencia scopeada,
                            no la arrastra el ritual del core (B5). */}
                        {modoMundo !== null && !mostrarSelectorModo && (
                          <p className="flex flex-wrap items-center gap-2 text-[13px] text-dim">
                            <span>
                              Modo: <span className="font-semibold text-ink">{modoMundo === "ritmo" ? "a mi ritmo" : "con fechas"}</span>
                            </span>
                            <BotonMini onClick={() => setMostrarSelectorModo(true)} tono="accent">
                              cambiar
                            </BotonMini>
                          </p>
                        )}
                        <PanelModoFechas
                          dominio={mundo.dominio}
                          modo={modoMundo}
                          planId={grupo?.plan_id ?? null}
                          hayFechas={hayFechasMundo}
                          grupos={gruposMundo}
                          cadenciaSemanas={cadenciaSemanas}
                          tieneTareasConFecha={tareasMundo.length > 0}
                          mostrarSelector={mostrarSelectorModo}
                          guardandoModo={guardandoModo}
                          guardandoBaseline={guardandoBaseline}
                          errorBaseline={errorBaseline}
                          recalcularPendientes={recalcularPendientes}
                          pospuesto={pospuesto}
                          capacidad={capacidadDe(mundo.dominio)}
                          cumplidasPorDominio={cumplidasPorDominio}
                          onCapacidad={elegirCapacidad}
                          onElegir={elegirModo}
                          onConfirmar={confirmarBaseline}
                          onPosponer={() => {
                            setPospuesto(true);
                            setRecalcularPendientes(false);
                          }}
                          onPonerFechas={() => setPospuesto(false)}
                          onRecalcular={() => setRecalcularPendientes(true)}
                          onDescargarIcs={() => descargarIcsDe(tareasMundo, mundo.nombre, mundo.nombre)}
                        />
                        <GrupoEtapas grupo={grupo} titulos={titulosMundo} ocupado={ocupado} modo={modoMundo} onCambio={aplicarCambio} onAbrirDetalle={abrirDetalle} />
                        {/* P3: la herramienta canónica del mundo, instanciada
                            sobre las actividades reales. Ruido cero: solo en
                            los mundos de PROTECCIÓN, y solo en su hub. */}
                        {esMundoProteccion(mundo.dominio) && (
                          <RegistroProteccion
                            nombreMundo={mundo.nombre}
                            entradas={armarRegistro(
                              grupo.etapas.flatMap((e) => e.items),
                              actividadesNucleo
                            )}
                          />
                        )}
                        {/* "Todo separado" (T5, D6): los CUATRO accesos scopeados
                            del espacio, en el orden del aside del núcleo, como
                            TARJETAS HERMANAS (misma forma, tarjeta entera). Sus dos
                            acciones (cerrar · contar qué pasó) también son hermanas,
                            más abajo en el hub. */}
                        {c.total > 0 && (
                          <div className="flex flex-col gap-3">
                            {onVerBitacora && (
                              <TarjetaAcceso
                                icono="bitacora"
                                titulo={`Bitácora de ${mundo.nombre}`}
                                descripcion="La historia de este mundo, paso a paso: cada decisión que has tomado aquí."
                                onClick={() => onVerBitacora(mundo.dominio)}
                              />
                            )}
                            {onVerCalendario && modoMundo === "fechas" && hayFechasMundo && (
                              <TarjetaAcceso
                                icono="calendario"
                                titulo={`Calendario de ${mundo.nombre}`}
                                descripcion="Lo que viene en este mundo, día por día. Sus fechas, hacia adelante."
                                onClick={() => onVerCalendario(mundo.dominio)}
                              />
                            )}
                            <TarjetaAcceso
                              icono="analisis"
                              titulo={`Análisis de ${mundo.nombre}`}
                              descripcion="El ritmo, las etapas y el cumplimiento de este mundo, calculados de lo que hiciste."
                              onClick={() => onVerAnalisis(mundo.dominio)}
                            />
                            <TarjetaAcceso
                              icono="documentos"
                              titulo={`Documentos de ${mundo.nombre}`}
                              descripcion="El reporte de este mundo y lo que deje cada fase de su camino, en .md o PDF."
                              onClick={() => onVerDocumentos(mundo.dominio)}
                            />
                          </div>
                        )}
                      </div>
                    )}
                  </div>
                ) : (
                  /* Modo apilado histórico (sin caras): diagnóstico + plan
                     colapsados + checklist. */
                  <div className="mt-4 flex flex-col gap-3">
                    {mundo.resumenMd && (
                      <Acordeon titulo="Tu diagnóstico">
                        <Markdown>{mundo.resumenMd}</Markdown>
                      </Acordeon>
                    )}
                    {mundo.plan && (
                      <Acordeon titulo={`El plan de ${mundo.nombre}`}>
                        <PlanDocumento md={mundo.plan.contenido_md} nombreIdea={mundo.nombre} />
                      </Acordeon>
                    )}
                    <GrupoEtapas grupo={grupo} titulos={titulosMundo} ocupado={ocupado} modo={modoMundo} onCambio={aplicarCambio} onAbrirDetalle={abrirDetalle} />
                  </div>
                )
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
                  {/* Compuerta clara (campaña "Espacios" §1.3): el costo se dice
                      ANTES de generar; el usuario sabe que se descuenta. */}
                  <p className="mt-4 text-[12.5px] text-dim">
                    Esto usará <span className="font-semibold text-ink">{PRECIOS.mundo_activar} créditos</span> de tu saldo.
                  </p>
                  <div className="mt-2 flex flex-wrap items-center gap-3">
                    <button
                      onClick={() => mundo.previewSessionId && onComprarPlanMundo(mundo.dominio, mundo.previewSessionId)}
                      disabled={!mundo.previewSessionId}
                      className="rounded-[10px] bg-accent px-5 py-2.5 text-sm font-semibold text-white hover:opacity-90 disabled:opacity-50"
                    >
                      Generar mi plan de {mundo.nombre} · {PRECIOS.mundo_activar} créditos
                    </button>
                  </div>
                </div>
              ) : (
                <div className="mt-4">
                  {/* "Por explorar": solo la puerta al diagnóstico. El precio del
                      plan se dice cuando SE VA A GENERAR (la compuerta "Esto usará
                      N créditos"), no en la invitación a explorar (decisión del
                      fundador): el texto de precio/gratis salió de aquí. */}
                  <button
                    onClick={() => arrancarMundo(mundo.dominio)}
                    disabled={arrancandoMundo !== null}
                    className="rounded-[10px] bg-accent px-5 py-2.5 text-sm font-medium text-white hover:opacity-90 disabled:opacity-50"
                  >
                    {arrancandoMundo === mundo.dominio ? "Preparando tu mundo…" : "Explorar este mundo"}
                  </button>
                </div>
              )}

              {/* Fase 4.2 §1 — el ritual de 3 tarjetas, TAMBIÉN aquí: un mundo
                  es un subproyecto y tiene su propio ciclo de seguimiento. En su
                  hub vive en la cara "manos" (la ejecución). */}
              {grupo && (!esHub || cara === "manos") && !completado && ritualMundo === mundo.dominio && (
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
                  grande, con su constelación y su pulso, es del PROYECTO. En su
                  hub vive en la cara "manos". */}
              {grupo && (!esHub || cara === "manos") && (
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
                    /* "Todo separado" (T5, D6): las DOS acciones del mundo como
                       TARJETAS HERMANAS (copy scopeado), la tarjeta entera abre su
                       flujo (ritual / acta de cierre). Misma forma que las del
                       núcleo; cambia la forma, jamás la función. */
                    <div className="flex w-full flex-col gap-3">
                      <TarjetaAcceso
                        icono="ciclo"
                        titulo="Ciclo de profundización"
                        descripcion={`¿La realidad te cambió el plan de ${mundo.nombre}? Cuéntame qué pasó y lo recalculo desde donde estás.`}
                        onClick={() => {
                          setRitualMundo(mundo.dominio);
                          setErrorRitual(null);
                        }}
                      />
                      <TarjetaAcceso
                        icono="realizar"
                        titulo={`¿Diste ${mundo.nombre} por terminado?`}
                        descripcion="Márcalo como completado cuando lo sientas cerrado. Lo que quede pendiente se guarda; podrás reabrirlo cuando quieras."
                        onClick={() => {
                          setCerrandoMundo(mundo.dominio);
                          setMotivoMundo("");
                        }}
                        tono="done"
                      />
                    </div>
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

        {/* Historia: los planes anteriores del core, releíbles. Vive en la cara
            "manos" (o en el modo apilado histórico, sin caras). */}
        {mostrarCore && (!coreEnEspacio || cara === "manos") && historial.length > 0 && (
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

      {/* lateral (solo core): análisis + realizar + documentos + bitácora. En el
          hub de un mundo no va — su documentación/estadística/bitácora propias
          llegan en la Fase 3. */}
      {mostrarCore && (
      <aside className="flex flex-col gap-6">
        {/* "Todo separado" (T5, D6): los cuatro accesos del núcleo como TARJETAS
            HERMANAS (bitácora · calendario · análisis · documentos), la misma
            forma que sus dos acciones (realizar · ciclo) más abajo. */}
        {onVerBitacora && cCore.total > 0 && (
          <TarjetaAcceso
            icono="bitacora"
            titulo="Mi bitácora"
            descripcion="La historia de tu viaje, paso a paso: cada decisión que has tomado."
            onClick={() => onVerBitacora?.()}
          />
        )}
        {onVerCalendario && modoCamino === "fechas" && hayFechas && (
          <TarjetaAcceso
            icono="calendario"
            titulo="Tu calendario"
            descripcion="Lo que viene, día por día. Llévate tus fechas al calendario del teléfono."
            onClick={() => onVerCalendario?.()}
          />
        )}
        {cCore.total > 0 && (
          <TarjetaAcceso
            icono="analisis"
            titulo="Análisis del proyecto"
            descripcion="Tu ritmo, tus etapas y tu cumplimiento, calculados de lo que hiciste."
            onClick={() => onVerAnalisis()}
          />
        )}
        <TarjetaAcceso
          icono="documentos"
          titulo="Tus documentos"
          descripcion="Tu plan, cada seguimiento y el expediente completo, en .md o en PDF."
          onClick={() => onVerDocumentos()}
        />

        {/* "Ciclo de profundización" como TARJETA HERMANA — SOLO desktop (en móvil
            ya subió arriba con su propia). La tarjeta entera abre el ritual
            (setRitual); "volver a la entrevista" queda como enlace aparte. Orden
            (recorrido del fundador): sube sobre "realizar", que cierra el aside. */}
        <div className="hidden lg:block">
          <TarjetaAcceso
            icono="ciclo"
            titulo="Ciclo de profundización"
            descripcion="¿La realidad te cambió el plan? Cuéntame qué pasó y lo recalculo desde donde estás."
            onClick={() => setRitual(true)}
          />
          {entrevistaAbierta && (
            <button
              onClick={onVolverEntrevista}
              className="mt-2.5 block w-full rounded-[10px] border border-white/15 py-2.5 text-center text-[13px] text-dim hover:border-accent/60 hover:text-ink"
            >
              Volver a la entrevista
            </button>
          )}
        </div>
        {/* La acción "realizar" como TARJETA HERMANA — la tarjeta ENTERA abre el
            acta de cierre (el mismo mini-ritual). Va AL FINAL del aside (recorrido
            del fundador): cerrar la idea es el último paso, no uno del medio. */}
        {cCore.total > 0 &&
          (!confirmandoRealizar ? (
            <TarjetaAcceso
              icono="realizar"
              titulo="¿Tu idea ya es un proyecto?"
              descripcion="Cuando lo sientas real, ciérrala. No hace falta terminar todo el checklist."
              onClick={() => setConfirmandoRealizar(true)}
              tono="done"
            />
          ) : (
            /* Fase 4.0 §8 — EL ACTA DE CIERRE: mini-ritual de dos elementos.
               (a) el espejo del momento, con los números reales y SIN juicio;
               (b) el porqué, OPCIONAL. Cero fricción: se cierra sin escribir nada. */
            <div className="rounded-panel border border-done/40 bg-surface p-5">
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
            </div>
          ))}
        {cCore.total > 0 && (
          <div className="border-t border-hairline pt-5">
            <p className="mb-3 text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">Ritmo</p>
            <div className="flex flex-col gap-2">
              <RitmoFila icono={<IconoReloj />} etiqueta="Última acción" valor={ultimaAccion ? haceCuanto(ultimaAccion) : "aún ninguna"} color="accent" />
              {desde && <RitmoFila icono={<IconoBandera />} etiqueta="Manos a la Obra desde" valor={haceCuanto(desde)} color="done" />}
              <RitmoFila icono={<IconoCiclos />} etiqueta="Ciclos de ajuste" valor={String(ciclosAjuste)} color="warn" />
            </div>
            <p className="mt-5 text-[13px] leading-relaxed text-dim">
              Pausa cuando lo necesites. Cuando vuelvas, el checklist te espera exactamente donde quedaste.
            </p>
          </div>
        )}
      </aside>
      )}

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
        const itemsDominio = checklist.planes
          .flatMap((p) => p.etapas)
          .flatMap((e) => e.items)
          .filter((i) => i.dominio === vivo.dominio);
        return (
          <DetalleActividad
            item={vivo}
            tituloEtapa={detalleItem.tituloEtapa}
            ocupado={ocupado}
            onCambio={(cambio) => aplicarCambio(vivo, cambio)}
            onMoverFecha={(fecha, cascada) => moverFecha(vivo.id, fecha, cascada)}
            itemsDominio={itemsDominio}
            onCerrar={() => setDetalleItem(null)}
          />
        );
      })()}
    </div>
  );
}
