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
import { ETIQUETA_ESTADO, IconoEstado, ORDEN_ESTADOS } from "./SelectorEstado";
import { fechaHumana, fechaInputLocal, isoDesdeInputLocal } from "@/lib/fechas";
import type { CambioItem, ItemChecklistUI } from "./ManosALaObra";

/** Días redondeados entre dos fechas (para el chip de cumplimiento). */
function difDias(desdeIso: string, hastaIso: string): number {
  return Math.round((new Date(hastaIso).getTime() - new Date(desdeIso).getTime()) / 86_400_000);
}

/** El chip de cumplimiento del ítem, en tono ESPEJO (la tardía en ámbar, nunca
 * rojo). null si no hay fecha planificada contra la cual medir. */
function chipCumplimiento(item: ItemChecklistUI): { texto: string; clase: string } | null {
  if (!item.fecha_base) return null;
  if (item.completed_at) {
    const d = difDias(item.fecha_base, item.completed_at); // + = tarde
    if (Math.abs(d) <= 1) return { texto: "A tiempo", clase: "border-done/50 text-done" };
    if (d > 0) return { texto: `Tardía · ${d} ${d === 1 ? "día" : "días"}`, clase: "border-warn/50 text-warn" };
    return { texto: `Adelantada · ${-d} ${-d === 1 ? "día" : "días"}`, clase: "border-accent/50 text-accent" };
  }
  // Pendiente: solo se marca "tardía" si ya pasó su fecha; jamás como regaño.
  const atraso = difDias(item.fecha_base, new Date().toISOString());
  if (atraso > 0) return { texto: `Tardía · ${atraso} ${atraso === 1 ? "día" : "días"}`, clase: "border-warn/50 text-warn" };
  return null;
}

// ETIQUETA_ESTADO, ORDEN_ESTADOS e IconoEstado viven en SelectorEstado (fuente
// única). El detalle es la vista completa: elige cualquiera de los 5 estados
// directo, y 'no aplica' abre su motivo editable.

export function DetalleActividad({
  item,
  tituloEtapa,
  ocupado,
  onCambio,
  onMoverFecha,
  itemsDominio = [],
  onCerrar,
}: {
  item: ItemChecklistUI;
  tituloEtapa: string;
  ocupado: boolean;
  onCambio: (cambio: CambioItem) => void;
  /** Fase 4.7: mover la fecha objetivo con cascada opcional a las posteriores.
   * Si no viene, el detalle cae al cambio simple de una sola fecha. */
  onMoverFecha?: (fecha: string, cascada: boolean) => void;
  /** Los ítems del MISMO dominio, para calcular la oferta de cascada. */
  itemsDominio?: ItemChecklistUI[];
  onCerrar: () => void;
}) {
  const hecho = item.estado === "hecho";
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
  const [editandoFechaHecho, setEditandoFechaHecho] = useState(false);
  const [editandoMotivo, setEditandoMotivo] = useState(false);
  const [motivo, setMotivo] = useState(item.no_aplica_motivo ?? "");
  const hoyInput = fechaInputLocal(new Date());
  const chip = chipCumplimiento(item);
  const notaCambiada = (item.nota ?? "") !== nota.trim();
  const retirada = item.estado === "no_aplica";

  // Cerrar con Escape: un cajón modal debe responder al teclado.
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => e.key === "Escape" && onCerrar();
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [onCerrar]);

  // Marcar hecho COMPROMETE en el acto (con la fecha de hoy por defecto). El
  // prompt anterior no comprometía si se cancelaba y dejaba el ítem atrapado
  // en "a medias" (bug del fundador, jul 2026). La fecha se ajusta después.
  function marcarHecho(completedAt?: string | null) {
    setEditandoFechaHecho(false);
    onCambio({ estado: "hecho", completed_at: completedAt ?? isoDesdeInputLocal(hoyInput) });
  }

  return (
    <div className="fixed inset-0 z-50 flex" aria-modal role="dialog" aria-label="Detalle de la actividad">
      {/* velo: tocar fuera cierra */}
      <button
        aria-label="Cerrar"
        onClick={onCerrar}
        className="absolute inset-0 bg-black/[0.55] backdrop-blur-[1px]"
      />
      {/* cajón: hoja inferior en móvil, cajón lateral de 520px en desktop, sobre
          superficie #0C0C10 (un paso más oscura, como capa flotante). */}
      <section
        className={
          "relative z-10 ml-auto flex max-h-[88vh] w-full flex-col overflow-hidden rounded-t-[20px] " +
          "border border-white/[0.12] bg-surface-3 sm:h-full sm:max-h-none sm:w-[520px] sm:rounded-none sm:rounded-l-[20px] " +
          "anima-hoja-in mt-auto sm:mt-0"
        }
        data-detalle-actividad
      >
        {/* asa de arrastre (solo estética móvil) */}
        <span className="mx-auto mt-2.5 h-1 w-9 shrink-0 rounded-full bg-white/20 sm:hidden" />

        <header className="flex items-center justify-between gap-3 border-b border-hairline px-5 py-4 sm:px-6">
          <p className="text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">Detalle de la actividad</p>
          <button
            onClick={onCerrar}
            aria-label="Cerrar el detalle"
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
            Etapa {item.etapa} · <span className="text-accent">{tituloEtapa}</span>
          </p>
          <p className={"mt-1.5 text-[17px] font-semibold leading-relaxed [text-wrap:pretty] " + (hecho ? "text-dim line-through" : "text-ink")}>
            {item.texto}
          </p>
          {chip && (
            <span className={"mt-3 inline-flex items-center rounded-full border px-3 py-1 text-[12px] font-bold " + chip.clase}>
              {chip.texto}
            </span>
          )}

          {/* estado: los 5, de un toque (el detalle es la vista completa).
              'no aplica' abre su motivo editable justo abajo. */}
          <div className="mt-6">
            <p className="mb-2 text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">Estado</p>
            <div className="flex flex-wrap gap-2">
              {ORDEN_ESTADOS.map((e) => {
                const activo = item.estado === e;
                const esRetirar = e === "no_aplica";
                return (
                  <button
                    key={e}
                    onClick={() => {
                      if (activo) {
                        if (esRetirar) setEditandoMotivo((v) => !v);
                        return;
                      }
                      if (e === "hecho") marcarHecho();
                      else if (esRetirar) {
                        setMotivo(item.no_aplica_motivo ?? "");
                        onCambio({ estado: "no_aplica", no_aplica_motivo: item.no_aplica_motivo ?? null });
                      } else onCambio({ estado: e });
                    }}
                    disabled={ocupado}
                    className={
                      // El VIGENTE se marca SIEMPRE en azul (borde 60% / fondo
                      // 14%): el azul dice "esto es lo elegido". El verde solo
                      // vive DENTRO del icono de hecha, nunca en la pastilla.
                      "inline-flex items-center gap-2 rounded-[11px] border px-[15px] py-2.5 text-[13.5px] font-semibold disabled:opacity-50 " +
                      (activo
                        ? "border-accent/60 bg-accent/[0.14] text-ink"
                        : "border-hairline text-dim hover:text-ink")
                    }
                  >
                    <IconoEstado estado={e} tamano={17} />
                    <span className="capitalize">{ETIQUETA_ESTADO[e]}</span>
                  </button>
                );
              })}
            </div>

            {/* Motivo de "no aplica": opcional, editable aquí (texto o voz). */}
            {retirada && (
              <div className="mt-3 rounded-cinta border border-hairline bg-surface-2 px-4 py-3">
                {!editandoMotivo ? (
                  <p className="text-[12.5px] text-dim">
                    {item.no_aplica_motivo ? (
                      <>
                        No aplica porque: <span className="text-ink">{item.no_aplica_motivo}</span>{" "}
                      </>
                    ) : (
                      <>Retirada, sin motivo anotado. </>
                    )}
                    <button
                      onClick={() => {
                        setMotivo(item.no_aplica_motivo ?? "");
                        setEditandoMotivo(true);
                      }}
                      disabled={ocupado}
                      className="font-semibold text-accent hover:underline disabled:opacity-50"
                    >
                      {item.no_aplica_motivo ? "cambiar" : "añadir motivo"}
                    </button>
                  </p>
                ) : (
                  <div>
                    <p className="mb-2 text-[12.5px] text-dim">¿Por qué no aplica? Para tu propia memoria.</p>
                    <CampoConVoz
                      id={`motivo-${item.id}`}
                      valor={motivo}
                      onCambio={setMotivo}
                      filas={2}
                      placeholder="No corre para esta idea porque…"
                    />
                    <div className="mt-2 flex items-center gap-2.5">
                      <button
                        onClick={() => {
                          onCambio({ no_aplica_motivo: motivo.trim() || null });
                          setEditandoMotivo(false);
                        }}
                        disabled={ocupado}
                        className="rounded-[9px] bg-accent px-3.5 py-1.5 text-[12.5px] font-semibold text-white hover:opacity-90 disabled:opacity-50"
                      >
                        Guardar
                      </button>
                      <button onClick={() => setEditandoMotivo(false)} className="text-[12.5px] text-dim hover:text-ink">
                        cancelar
                      </button>
                    </div>
                  </div>
                )}
              </div>
            )}
            {/* Fecha de realización de un ítem YA hecho: editable, sin trampa.
                El estado ya está comprometido; esto solo ajusta el "cuándo". */}
            {hecho && (
              <div className="mt-3">
                {!editandoFechaHecho ? (
                  <p className="flex flex-wrap items-center gap-x-2.5 gap-y-0.5 text-[12.5px]">
                    <span className="text-done">
                      {item.completed_at ? `Hecho el ${fechaHumana(item.completed_at)}` : "Hecho"}
                    </span>
                    <button
                      onClick={() => setEditandoFechaHecho(true)}
                      disabled={ocupado}
                      className="font-medium text-accent hover:underline disabled:opacity-50"
                    >
                      cambiar fecha
                    </button>
                  </p>
                ) : (
                  <div className="flex flex-wrap items-center gap-2.5">
                    <span className="text-[12.5px] text-dim">¿Cuándo lo hiciste?</span>
                    <input
                      type="date"
                      max={hoyInput}
                      defaultValue={item.completed_at ? fechaInputLocal(new Date(item.completed_at)) : hoyInput}
                      onChange={(ev) => ev.target.value && marcarHecho(isoDesdeInputLocal(ev.target.value))}
                      disabled={ocupado}
                      aria-label="Cambiar la fecha en que lo hiciste"
                      className="rounded-[9px] border border-hairline bg-surface-2 px-2.5 py-1.5 text-[12.5px] text-ink outline-none focus:border-done/60 disabled:opacity-50"
                    />
                    <button onClick={() => setEditandoFechaHecho(false)} className="text-[12.5px] text-dim hover:text-ink">
                      listo
                    </button>
                  </div>
                )}
              </div>
            )}
          </div>

          {/* FECHA: solo si el ítem tiene una fecha planificada (modo fechas) */}
          {item.fecha_base && (
            <div className="mt-6">
              {/* Rótulo "FECHA" y la píldora "cambiar fecha" en la MISMA fila
                  (Design): el rótulo a la izquierda, el disparador arriba-derecha
                  de la sección; debajo, el valor o el editor. */}
              <div className="mb-3 flex items-center justify-between gap-3">
                <p className="text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">Fecha</p>
                {!moviendoFecha && (
                  <button
                    onClick={() => setMoviendoFecha(true)}
                    disabled={ocupado}
                    className="shrink-0 rounded-full border border-accent/40 bg-accent/10 px-3 py-1 text-[12px] font-semibold text-accent hover:bg-accent/20 disabled:opacity-50"
                  >
                    cambiar fecha
                  </button>
                )}
              </div>
              {!moviendoFecha ? (
                <div className="rounded-cinta border border-hairline bg-surface-2 px-4 py-3 text-[14px]">
                  {fechaHumana(item.fecha_base)}
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
                  const rumbo = deltaDias >= 0 ? `${magnitud} ${magnitud === 1 ? "día" : "días"} después` : `${magnitud} ${magnitud === 1 ? "día" : "días"} antes`;
                  const mover = (cascada: boolean) => {
                    onMoverFecha?.(ofertaFecha, cascada);
                    setOfertaFecha(null);
                    setMoviendoFecha(false);
                  };
                  return (
                    <div className="rounded-[14px] border border-accent/[0.45] bg-accent/[0.06] px-5 py-4">
                      <p className="text-[13.5px] leading-relaxed [text-wrap:pretty]">
                        Nueva fecha: <span className="font-semibold text-accent">{fechaHumana(ofertaFecha)}</span>.{" "}
                        Hay <span className="font-semibold">{cuantos}</span> {cuantos === 1 ? "actividad pendiente que sigue" : "actividades pendientes que siguen"}.
                      </p>
                      <p className="mt-1 text-[12.5px] text-dim">¿Las muevo también, {rumbo} cada una?</p>
                      <div className="mt-4 flex flex-wrap gap-2.5">
                        <button
                          onClick={() => mover(true)}
                          disabled={ocupado}
                          className="rounded-[11px] bg-accent px-5 py-2.5 text-[14px] font-bold text-white hover:opacity-90 disabled:opacity-50"
                        >
                          Sí, mover todas
                        </button>
                        <button
                          onClick={() => mover(false)}
                          disabled={ocupado}
                          className="rounded-[11px] border border-white/[0.18] px-5 py-2.5 text-[14px] font-semibold text-ink hover:border-accent/60 disabled:opacity-50"
                        >
                          Solo esta
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
                    aria-label="Nueva fecha objetivo"
                    className="rounded-[9px] border border-hairline bg-surface px-2.5 py-1.5 text-[13px] text-ink outline-none focus:border-accent/60 disabled:opacity-50"
                  />
                  <button onClick={() => { setMoviendoFecha(false); setOfertaFecha(null); }} className="text-[12.5px] text-dim hover:text-ink">
                    cancelar
                  </button>
                </div>
              )}
              <p className="mt-2 text-[12px] text-dim">
                {item.fecha_base_original
                  ? `Ya la moviste: la original (${fechaHumana(item.fecha_base_original)}) se conserva en tu historia.`
                  : "Si la mueves, la fecha original se conserva en tu historia. No se reescribe nada."}
              </p>
            </div>
          )}

          {/* TU NOTA: libre, escribir o dictar. Registrar avance es gratis. */}
          <div className="mt-6">
            <p className="mb-2 text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">Tu nota</p>
            <CampoConVoz
              id={`nota-${item.id}`}
              valor={nota}
              onCambio={setNota}
              filas={3}
              placeholder="Lo que necesites recordar de esta acción…"
            />
            <p className="mt-1.5 text-[12px] text-dim">Registrar tu nota es gratis, siempre.</p>
          </div>
        </div>

        {/* pie: Guardar (la nota) + Cancelar. "Marcar hecho" se quitó por
            redundante: el estado ya se elige arriba, con "Hecha" en el selector
            (el cambio de estado se aplica al instante, no necesita el pie). */}
        <footer className="flex items-center gap-3 border-t border-hairline px-5 py-4 sm:px-6">
          <button
            onClick={() => {
              if (notaCambiada) onCambio({ nota: nota.trim() || null });
              onCerrar();
            }}
            disabled={ocupado}
            className="flex-1 rounded-[12px] bg-accent py-3 text-[14.5px] font-bold text-white hover:opacity-90 disabled:opacity-50"
          >
            Guardar
          </button>
          <button
            onClick={onCerrar}
            disabled={ocupado}
            className="rounded-[10px] border border-hairline px-5 py-2.5 text-[13.5px] font-semibold text-dim hover:text-ink disabled:opacity-40"
          >
            Cancelar
          </button>
        </footer>
      </section>
    </div>
  );
}
