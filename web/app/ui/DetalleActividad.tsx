"use client";

/**
 * DetalleActividad — Fase 4.3.2, "Explorar actividad" (canon 13, diseñado por
 * Claude Design). Hasta ahora cada acción del checklist era una fila con
 * "marcar hecho" y nada más. El detalle abre la actividad y deja ver y ajustar
 * DENTRO: su texto completo, su cumplimiento (espejo, jamás regaño), su fecha
 * (con "mover fecha" y la original preservada — la historia no se reescribe),
 * su nota libre (escribir o dictar), su historia de replanificaciones, y
 * marcarla hecha.
 *
 * Se abre tocando la fila; se ve como CAJÓN lateral en desktop y HOJA inferior
 * en móvil; se cierra con la X o tocando el velo. La fila conserva sus acciones
 * rápidas (el círculo y "Marcar hecho"): el detalle es la vista profunda.
 */
import { useEffect, useMemo, useState } from "react";
import { CampoConVoz } from "./CampoConVoz";
import { IconoEstado, ORDEN_ESTADOS } from "./SelectorEstado";
import { fechaHumana, fechaInputLocal, isoDesdeInputLocal } from "@/lib/fechas";
import { BANDA, type Banda, type ChecklistEstado, type ModoCamino } from "@/lib/dbContract";
import { rangoDeBanda } from "@/lib/engine/estimacion";
import type { CambioItem, ItemChecklistUI } from "./ManosALaObra";
import { elegir, type Locale } from "@/lib/i18n/config";
import { useIdioma } from "@/lib/i18n/IdiomaProvider";
import { interpolar, plural } from "@/lib/i18n/interpolar";
import { rico } from "@/lib/i18n/rico";
import { DETALLE_ACTIVIDAD } from "@/lib/i18n/mensajes/detalleActividad";
import { ESTADOS_TAREA } from "@/lib/i18n/mensajes/estadosTarea";

/** Días redondeados entre dos fechas (para el chip de cumplimiento). */
function difDias(desdeIso: string, hastaIso: string): number {
  return Math.round((new Date(hastaIso).getTime() - new Date(desdeIso).getTime()) / 86_400_000);
}

/** El chip de cumplimiento del ítem, en tono ESPEJO (la tardía en ámbar, nunca
 * rojo). null si no hay fecha planificada contra la cual medir. */
function chipCumplimiento(item: ItemChecklistUI, idioma: Locale): { texto: string; clase: string } | null {
  const t = elegir(DETALLE_ACTIVIDAD, idioma).chip;
  if (!item.fecha_base) return null;
  if (item.completed_at) {
    const d = difDias(item.fecha_base, item.completed_at); // + = tarde
    if (Math.abs(d) <= 1) return { texto: t.aTiempo, clase: "border-done/50 text-done" };
    if (d > 0) return { texto: plural(idioma, d, t.tardia), clase: "border-warn/50 text-warn" };
    return { texto: plural(idioma, -d, t.adelantada), clase: "border-accent/50 text-accent" };
  }
  // Pendiente: solo se marca "tardía" si ya pasó su fecha; jamás como regaño.
  const atraso = difDias(item.fecha_base, new Date().toISOString());
  if (atraso > 0) return { texto: plural(idioma, atraso, t.tardia), clase: "border-warn/50 text-warn" };
  return null;
}

// ORDEN_ESTADOS e IconoEstado viven en SelectorEstado (fuente única), y las
// etiquetas de estado en su catálogo (estadosTarea). El detalle es la vista completa: elige cualquiera de los 5 estados
// directo, y 'no aplica' abre su motivo editable.

export function DetalleActividad({
  item,
  tituloEtapa,
  ocupado,
  onCambio,
  onMoverFecha,
  itemsDominio = [],
  protegidaPor = [],
  protege = null,
  onCerrar,
  modo = null,
}: {
  item: ItemChecklistUI;
  /** AUD-09 M38: el modo del espacio de la tarea. A mi ritmo no hay plazos:
   * sin chip de cumplimiento ni sección de fecha. */
  modo?: ModoCamino | null;
  tituloEtapa: string;
  ocupado: boolean;
  onCambio: (cambio: CambioItem) => void;
  /** Fase 4.7: mover la fecha objetivo con cascada opcional a las posteriores.
   * Si no viene, el detalle cae al cambio simple de una sola fecha. */
  onMoverFecha?: (fecha: string, cascada: boolean) => void;
  /** Los ítems del MISMO dominio, para calcular la oferta de cascada. */
  itemsDominio?: ItemChecklistUI[];
  /** Mundos de protección (P4): las respuestas que cuidan a ESTE ítem del
   * núcleo. Vacío/ausente = sin chip (ruido cero). */
  protegidaPor?: Array<{ respuesta: string; mundo: string }>;
  /** P4: si ESTE ítem es una respuesta de protección, a qué protege. La
   * detección se muestra SIEMPRE que exista (regla anti-silencio); si lo
   * protegido se retiró, se dice. */
  protege?: { titulo: string | null; deteccion: string | null; retirada: boolean; sistemica: boolean } | null;
  onCerrar: () => void;
}) {
  const idioma = useIdioma();
  const t = elegir(DETALLE_ACTIVIDAD, idioma);
  const etiquetaEstado = elegir(ESTADOS_TAREA, idioma).etiquetas;
  const [nota, setNota] = useState(item.nota ?? "");
  const [moviendoFecha, setMoviendoFecha] = useState(false);
  // La nueva fecha elegida, en espera de decidir la cascada (null = sin oferta).
  const [ofertaFecha, setOfertaFecha] = useState<string | null>(null);
  // Pendientes POSTERIORES del mismo dominio (misma etapa o posteriores, por
  // fecha vigente; excluye hechas y retiradas): las candidatas a la cascada.
  const posteriores = useMemo(
    () =>
      item.fecha_base
        ? itemsDominio.filter(
            (i) =>
              i.id !== item.id &&
              i.estado !== "hecho" &&
              i.estado !== "no_aplica" &&
              i.etapa >= item.etapa &&
              i.fecha_base !== null &&
              Date.parse(i.fecha_base) > Date.parse(item.fecha_base!)
          )
        : [],
    [itemsDominio, item.id, item.etapa, item.fecha_base]
  );
  const hoyInput = fechaInputLocal(new Date());
  const conFechas = modo !== "ritmo";
  const chip = conFechas ? chipCumplimiento(item, idioma) : null;
  const notaCambiada = (item.nota ?? "") !== nota.trim();

  // BORRADOR (jul 2026, pedido del fundador): en el CAJÓN el estado NO se guarda
  // al elegirlo; queda pendiente hasta "Guardar". (En la FILA del checklist el
  // cambio sigue siendo inmediato: allí está bien.) Se acumulan estado, motivo
  // de "no aplica" y la fecha de realización de "hecha" como borrador.
  const [bEstado, setBEstado] = useState<ChecklistEstado>(item.estado);
  const [bMotivo, setBMotivo] = useState(item.no_aplica_motivo ?? "");
  const [bCompletado, setBCompletado] = useState<string | null>(item.completed_at ?? null);
  const [menuAbierto, setMenuAbierto] = useState(false);
  // Scheduler F1: la banda también es borrador (se corrige y se guarda con el
  // resto). null = sin estimar; entonces no se muestra la sección de esfuerzo.
  const [bBanda, setBBanda] = useState<Banda | null>(item.banda ?? null);
  const [corrigiendoBanda, setCorrigiendoBanda] = useState(false);
  const hecho = bEstado === "hecho";
  const retirada = bEstado === "no_aplica";

  function elegirEstado(e: ChecklistEstado) {
    setBEstado(e);
    setMenuAbierto(false);
    if (e === "hecho" && !bCompletado) setBCompletado(isoDesdeInputLocal(hoyInput));
  }

  // Guardar el borrador (estado + motivo + fecha de realización + nota) en UN
  // solo cambio. Cancelar descarta todo.
  function guardar() {
    const cambio: CambioItem = {};
    if (bEstado !== item.estado) cambio.estado = bEstado;
    if (bEstado === "hecho") {
      const c = bCompletado ?? isoDesdeInputLocal(hoyInput);
      if (bEstado !== item.estado || c !== (item.completed_at ?? null)) cambio.completed_at = c;
    }
    if (bEstado === "no_aplica" && (bMotivo.trim() || null) !== (item.no_aplica_motivo ?? null)) {
      cambio.no_aplica_motivo = bMotivo.trim() || null;
    }
    if (notaCambiada) cambio.nota = nota.trim() || null;
    if (bBanda && bBanda !== (item.banda ?? null)) cambio.banda = bBanda;
    if (Object.keys(cambio).length > 0) onCambio(cambio);
    onCerrar();
  }

  // Cerrar con Escape: un cajón modal debe responder al teclado (descarta).
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => e.key === "Escape" && onCerrar();
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [onCerrar]);

  return (
    <div className="fixed inset-0 z-50 flex" aria-modal role="dialog" aria-label={t.dialogo}>
      {/* velo: tocar fuera cierra */}
      <button
        aria-label={t.cerrar}
        onClick={onCerrar}
        className="absolute inset-0 bg-black/[0.55] backdrop-blur-[1px]"
      />
      {/* cajón: hoja inferior en móvil, cajón lateral de 520px en desktop, sobre
          superficie #0C0C10 (un paso más oscura, como capa flotante). */}
      <section
        className={
          "relative z-10 ms-auto flex max-h-[88vh] w-full flex-col overflow-hidden rounded-t-[20px] " +
          "border border-white/[0.12] bg-surface-3 sm:h-full sm:max-h-none sm:w-[520px] sm:rounded-none sm:rounded-s-[20px] " +
          "anima-hoja-in mt-auto sm:mt-0"
        }
        data-detalle-actividad
      >
        {/* asa de arrastre (solo estética móvil) */}
        <span className="mx-auto mt-2.5 h-1 w-9 shrink-0 rounded-full bg-white/20 sm:hidden" />

        <header className="flex items-center justify-between gap-3 border-b border-hairline px-5 py-4 sm:px-6">
          <p className="text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">{t.dialogo}</p>
          <button
            onClick={onCerrar}
            aria-label={t.cerrarDetalle}
            className="flex h-8 w-8 shrink-0 items-center justify-center rounded-[9px] border border-hairline text-dim hover:text-ink"
          >
            <svg width="12" height="12" viewBox="0 0 12 12" aria-hidden>
              <path d="M2 2l8 8M10 2l-8 8" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" />
            </svg>
          </button>
        </header>

        <div className="flex-1 overflow-y-auto px-5 py-5 sm:px-6" style={{ scrollbarWidth: "thin" }}>
          {/* etapa (azul: navegación/estructura) + texto completo del ítem */}
          <p className="text-[12.5px] text-dim">
            {interpolar(t.etapa, { n: item.etapa })} · <span className="text-accent">{tituloEtapa}</span>
          </p>
          <p className={"mt-1.5 text-[17px] font-semibold leading-relaxed [text-wrap:pretty] " + (hecho ? "text-dim line-through" : "text-ink")}>
            {item.texto}
          </p>
          {chip && (
            <span className={"mt-3 inline-flex items-center rounded-full border px-3 py-1 text-[12px] font-bold " + chip.clase}>
              {chip.texto}
            </span>
          )}

          {/* P4 — el enlace de protección, en las dos direcciones. Solo-lectura:
              nace del plan del mundo y no se edita aquí. */}
          {protegidaPor.length > 0 && (
            <div className="mt-3 flex flex-col gap-1.5" data-chip-proteccion>
              {protegidaPor.map((pr, i) => (
                <p key={i} className="text-[12.5px] leading-relaxed text-dim [text-wrap:pretty]">
                  <span className="me-1.5 inline-flex items-center rounded-full border border-accent/40 bg-accent/10 px-2 py-0.5 text-[10.5px] font-bold uppercase tracking-[0.6px] text-accent">
                    {t.protegida}
                  </span>
                  {pr.respuesta} <span className="text-dim/70">· {pr.mundo}</span>
                </p>
              ))}
            </div>
          )}
          {protege && (
            <div className="mt-3 rounded-cinta border border-hairline bg-surface-2 px-4 py-3" data-chip-proteccion>
              {protege.deteccion && (
                <p className="text-[13px] font-semibold [text-wrap:pretty]">{protege.deteccion}</p>
              )}
              <p className={"text-[12.5px] text-dim [text-wrap:pretty]" + (protege.deteccion ? " mt-1" : "")}>
                {t.protege}{" "}
                <span className="text-ink">
                  {protege.retirada
                    ? t.protegeRetirada
                    : protege.sistemica
                      ? t.protegeSistemica
                      : protege.titulo ?? t.protegeFueraDelPlan}
                </span>
              </p>
            </div>
          )}

          {/* estado: LISTA DESPLEGABLE (no cintas) — más fácil de escoger y
              visual (la forma de cada estado). En el CAJÓN es BORRADOR: elegir
              NO guarda; se compromete con "Guardar". 'no aplica' y 'hecha' abren
              su editor (motivo / fecha) justo abajo, también en borrador. */}
          <div className="mt-6">
            <p className="mb-2 text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">{t.estado}</p>
            <div className="relative">
              <button
                type="button"
                onClick={() => setMenuAbierto((v) => !v)}
                disabled={ocupado}
                aria-haspopup="listbox"
                aria-expanded={menuAbierto}
                className="flex w-full items-center gap-3 rounded-[12px] border border-hairline bg-surface-2 px-4 py-3 text-start transition-colors hover:border-white/25 disabled:opacity-50"
              >
                <IconoEstado estado={bEstado} tamano={20} />
                <span className="flex-1 text-[14.5px] font-semibold capitalize">{etiquetaEstado[bEstado]}</span>
                <svg width="12" height="12" viewBox="0 0 12 12" aria-hidden className={"shrink-0 text-dim transition-transform " + (menuAbierto ? "rotate-180" : "")}>
                  <path d="M2 4l4 4 4-4" stroke="currentColor" strokeWidth="1.5" fill="none" />
                </svg>
              </button>
              {menuAbierto && (
                <div role="listbox" aria-label={t.elegirEstado} className="mt-2 overflow-hidden rounded-[12px] border border-white/[0.14] bg-surface-2">
                  {ORDEN_ESTADOS.map((e) => {
                    const activo = e === bEstado;
                    return (
                      <button
                        key={e}
                        type="button"
                        role="option"
                        aria-selected={activo}
                        onClick={() => elegirEstado(e)}
                        disabled={ocupado}
                        className={
                          "flex min-h-[44px] w-full items-center gap-3 px-4 py-2.5 text-start text-[14px] hover:bg-white/[0.05] disabled:opacity-50 " +
                          (activo ? "bg-white/[0.06] font-semibold" : "")
                        }
                      >
                        <IconoEstado estado={e} tamano={18} />
                        <span className="flex-1 capitalize">{etiquetaEstado[e]}</span>
                        {activo && (
                          <svg width="13" height="13" viewBox="0 0 12 12" aria-hidden className="text-accent">
                            <path d="M2.5 6.5l2.5 2.5 4.5-5.5" stroke="currentColor" strokeWidth="2" fill="none" />
                          </svg>
                        )}
                      </button>
                    );
                  })}
                </div>
              )}
            </div>

            {/* Motivo de "no aplica" (borrador): opcional, texto o voz. */}
            {retirada && (
              <div className="mt-3 rounded-cinta border border-hairline bg-surface-2 px-4 py-3">
                <p className="mb-2 text-[12.5px] text-dim">{t.porQueNoAplica}</p>
                <CampoConVoz
                  id={`motivo-${item.id}`}
                  valor={bMotivo}
                  onCambio={setBMotivo}
                  filas={2}
                  placeholder={t.placeholderMotivo}
                />
              </div>
            )}
            {/* Fecha de realización (borrador) al marcar hecha. */}
            {hecho && (
              <div className="mt-3 flex flex-wrap items-center gap-2.5">
                <span className="text-[12.5px] text-dim">{t.cuandoLoHiciste}</span>
                <input
                  type="date"
                  max={hoyInput}
                  value={bCompletado ? fechaInputLocal(new Date(bCompletado)) : hoyInput}
                  onChange={(ev) => ev.target.value && setBCompletado(isoDesdeInputLocal(ev.target.value))}
                  disabled={ocupado}
                  aria-label={t.cuandoLoHicisteAria}
                  className="rounded-[9px] border border-hairline bg-surface px-2.5 py-1.5 text-[12.5px] text-ink outline-none focus:border-done/60 disabled:opacity-50"
                />
              </div>
            )}
          </div>

          {/* ESFUERZO (Scheduler F1): el rango HONESTO de la banda estimada, con
              corrección del usuario. Si el ítem no tiene banda (plan viejo o la
              estimación falló) la sección NO aparece: sin rango, cero invención. */}
          {bBanda && (
            <div className="mt-6">
              <div className="mb-3 flex items-center justify-between gap-3">
                <p className="text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">{t.esfuerzo}</p>
                {!corrigiendoBanda && (
                  <button
                    onClick={() => setCorrigiendoBanda(true)}
                    disabled={ocupado}
                    className="shrink-0 rounded-full border border-accent/40 bg-accent/10 px-3 py-1 text-[12px] font-semibold text-accent hover:bg-accent/20 disabled:opacity-50"
                  >
                    {t.corregir}
                  </button>
                )}
              </div>
              {!corrigiendoBanda ? (
                <div className="rounded-cinta border border-hairline bg-surface-2 px-4 py-3">
                  <p className="text-[14px]">
                    <span className="font-semibold">{rangoDeBanda(bBanda, idioma)}</span>
                    {item.espera_externa ? <span className="text-dim"> {t.dependeDeTerceros}</span> : null}
                  </p>
                  <p className="mt-1 text-[12px] leading-relaxed text-dim">
                    {item.espera_externa
                      ? t.estimadoConEspera
                      : t.estimado}
                  </p>
                </div>
              ) : (
                <div className="rounded-cinta border border-accent/40 bg-surface-2 px-4 py-3">
                  <p className="mb-2.5 text-[12.5px] text-dim">{t.cuantoTeToma}</p>
                  <div className="flex flex-wrap gap-2">
                    {BANDA.map((b) => {
                      const activa = b === bBanda;
                      return (
                        <button
                          key={b}
                          type="button"
                          onClick={() => {
                            setBBanda(b);
                            setCorrigiendoBanda(false);
                          }}
                          disabled={ocupado}
                          aria-pressed={activa}
                          className={
                            "min-h-[40px] rounded-[10px] border px-3.5 py-2 text-[13px] font-semibold disabled:opacity-50 " +
                            (activa
                              ? "border-accent bg-accent/15 text-accent"
                              : "border-hairline text-ink hover:border-accent/60")
                          }
                        >
                          {rangoDeBanda(b, idioma)}
                        </button>
                      );
                    })}
                  </div>
                  <button
                    onClick={() => {
                      setBBanda(item.banda ?? null);
                      setCorrigiendoBanda(false);
                    }}
                    className="mt-3 text-[12.5px] text-dim hover:text-ink"
                  >
                    {t.cancelarEdicion}
                  </button>
                </div>
              )}
            </div>
          )}

          {/* FECHA: solo si el ítem tiene una fecha planificada (modo fechas) */}
          {conFechas && item.fecha_base && (
            <div className="mt-6">
              {/* Rótulo "FECHA" y la píldora "cambiar fecha" en la MISMA fila
                  (Design): el rótulo a la izquierda, el disparador arriba-derecha
                  de la sección; debajo, el valor o el editor. */}
              <div className="mb-3 flex items-center justify-between gap-3">
                <p className="text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">{t.fecha}</p>
                {!moviendoFecha && (
                  <button
                    onClick={() => setMoviendoFecha(true)}
                    disabled={ocupado}
                    className="shrink-0 rounded-full border border-accent/40 bg-accent/10 px-3 py-1 text-[12px] font-semibold text-accent hover:bg-accent/20 disabled:opacity-50"
                  >
                    {t.cambiarFecha}
                  </button>
                )}
              </div>
              {!moviendoFecha ? (
                <div className="rounded-cinta border border-hairline bg-surface-2 px-4 py-3 text-[14px]">
                  {fechaHumana(item.fecha_base, idioma)}
                </div>
              ) : ofertaFecha ? (
                // Oferta de CASCADA: al elegir la nueva fecha, si hay pendientes
                // posteriores se ofrece moverlas el mismo delta. Nada se mueve
                // sin el sí; "Solo esta" mueve únicamente esta. Simétrico
                // (adelantar también ofrece). Fase 4.7.
                (() => {
                  const deltaDias = Math.round(
                    (Date.parse(ofertaFecha) - Date.parse(item.fecha_base!)) / 86_400_000
                  );
                  const cuantos = posteriores.length;
                  const magnitud = Math.abs(deltaDias);
                  const rumbo = plural(idioma, magnitud, deltaDias >= 0 ? t.diasDespues : t.diasAntes);
                  const mover = (cascada: boolean) => {
                    onMoverFecha?.(ofertaFecha, cascada);
                    setOfertaFecha(null);
                    setMoviendoFecha(false);
                  };
                  return (
                    <div className="rounded-[14px] border border-accent/[0.45] bg-accent/[0.06] px-5 py-4">
                      <p className="text-[13.5px] leading-relaxed [text-wrap:pretty]">
                        {rico(interpolar(t.nuevaFecha, { fecha: fechaHumana(ofertaFecha, idioma) }), { b: (c) => <span className="font-semibold text-accent">{c}</span> })}{" "}
                        {rico(plural(idioma, cuantos, t.hayPosteriores), { b: (c) => <span className="font-semibold">{c}</span> })}
                      </p>
                      <p className="mt-1 text-[12.5px] text-dim">{interpolar(t.lasMuevo, { rumbo })}</p>
                      <div className="mt-4 flex flex-wrap gap-2.5">
                        <button
                          onClick={() => mover(true)}
                          disabled={ocupado}
                          className="rounded-[11px] border border-accent/40 bg-accent/10 px-5 py-2.5 text-[14px] font-bold text-accent hover:bg-accent/20 disabled:opacity-50"
                        >
                          {t.moverTodas}
                        </button>
                        <button
                          onClick={() => mover(false)}
                          disabled={ocupado}
                          className="rounded-[11px] border border-white/[0.18] px-5 py-2.5 text-[14px] font-semibold text-ink hover:border-accent/60 disabled:opacity-50"
                        >
                          {t.soloEsta}
                        </button>
                      </div>
                    </div>
                  );
                })()
              ) : (
                <div className="flex flex-wrap items-center gap-2.5 rounded-cinta border border-accent/40 bg-surface-2 px-4 py-3">
                  <input
                    type="date"
                    defaultValue={fechaInputLocal(new Date(item.fecha_base))}
                    onChange={(ev) => {
                      if (!ev.target.value) return;
                      const nueva = isoDesdeInputLocal(ev.target.value);
                      // Con hermanos posteriores y soporte de cascada: ofrecer.
                      // Si no, mover directo (comportamiento simple de siempre).
                      if (onMoverFecha && posteriores.length > 0) {
                        setOfertaFecha(nueva);
                      } else if (onMoverFecha) {
                        onMoverFecha(nueva, false);
                        setMoviendoFecha(false);
                      } else {
                        onCambio({ fecha_base: nueva });
                        setMoviendoFecha(false);
                      }
                    }}
                    disabled={ocupado}
                    aria-label={t.nuevaFechaObjetivo}
                    className="rounded-[9px] border border-hairline bg-surface px-2.5 py-1.5 text-[13px] text-ink outline-none focus:border-accent/60 disabled:opacity-50"
                  />
                  <button onClick={() => { setMoviendoFecha(false); setOfertaFecha(null); }} className="text-[12.5px] text-dim hover:text-ink">
                    {t.cancelarEdicion}
                  </button>
                </div>
              )}
              <p className="mt-2 text-[12px] text-dim">
                {item.fecha_base_original
                  ? interpolar(t.yaLaMoviste, { fecha: fechaHumana(item.fecha_base_original, idioma) })
                  : t.siLaMueves}
              </p>
            </div>
          )}

          {/* TU NOTA: libre, escribir o dictar. Registrar avance es gratis. */}
          <div className="mt-6">
            <p className="mb-2 text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">{t.tuNota}</p>
            <CampoConVoz
              id={`nota-${item.id}`}
              valor={nota}
              onCambio={setNota}
              filas={3}
              placeholder={t.placeholderNota}
            />
            <p className="mt-1.5 text-[12px] text-dim">{t.notaGratis}</p>
          </div>
        </div>

        {/* pie: Guardar (la nota) + Cancelar. "Marcar hecho" se quitó por
            redundante: el estado ya se elige arriba, con "Hecha" en el selector
            (el cambio de estado se aplica al instante, no necesita el pie). */}
        <footer className="flex items-center gap-3 border-t border-hairline px-5 py-4 sm:px-6">
          <button
            onClick={guardar}
            disabled={ocupado}
            className="flex-1 rounded-[12px] border border-accent/40 bg-accent/10 py-3 text-[14.5px] font-bold text-accent hover:bg-accent/20 disabled:opacity-50"
          >
            {t.guardar}
          </button>
          <button
            onClick={onCerrar}
            disabled={ocupado}
            className="rounded-[10px] border border-accent/40 bg-accent/10 text-accent hover:bg-accent/20 px-5 py-2.5 text-[13.5px] font-semibold disabled:opacity-40"
          >
            {t.botonCancelar}
          </button>
        </footer>
      </section>
    </div>
  );
}
