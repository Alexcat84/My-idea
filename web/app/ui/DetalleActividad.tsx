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
import { useEffect, useState } from "react";
import { CampoConVoz } from "./CampoConVoz";
import type { ChecklistEstado } from "@/lib/dbContract";
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

const ETIQUETA_ESTADO: Record<ChecklistEstado, string> = {
  pendiente: "sin empezar",
  empezado: "apenas empezado",
  a_medias: "a medias",
  hecho: "hecho",
};

const ORDEN_ESTADOS: ChecklistEstado[] = ["pendiente", "empezado", "a_medias", "hecho"];

export function DetalleActividad({
  item,
  tituloEtapa,
  ocupado,
  onCambio,
  onCerrar,
}: {
  item: ItemChecklistUI;
  tituloEtapa: string;
  ocupado: boolean;
  onCambio: (cambio: CambioItem) => void;
  onCerrar: () => void;
}) {
  const hecho = item.estado === "hecho";
  const [nota, setNota] = useState(item.nota ?? "");
  const [moviendoFecha, setMoviendoFecha] = useState(false);
  const [editandoFechaHecho, setEditandoFechaHecho] = useState(false);
  const hoyInput = fechaInputLocal(new Date());
  const chip = chipCumplimiento(item);
  const notaCambiada = (item.nota ?? "") !== nota.trim();

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
        className="absolute inset-0 bg-black/60 backdrop-blur-[1px]"
      />
      {/* cajón: hoja inferior en móvil, cajón lateral en desktop */}
      <section
        className={
          "relative z-10 ml-auto flex max-h-[88vh] w-full flex-col overflow-hidden rounded-t-[20px] " +
          "border border-hairline bg-surface sm:h-full sm:max-h-none sm:w-[440px] sm:rounded-none sm:rounded-l-[20px] " +
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

          {/* estado: los 4, de un toque (el detalle es la vista completa) */}
          <div className="mt-6">
            <p className="mb-2 text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">Estado</p>
            <div className="flex flex-wrap gap-2">
              {ORDEN_ESTADOS.map((e) => {
                const activo = item.estado === e;
                return (
                  <button
                    key={e}
                    onClick={() => {
                      if (activo) return;
                      if (e === "hecho") marcarHecho();
                      else onCambio({ estado: e });
                    }}
                    disabled={ocupado}
                    className={
                      "rounded-[9px] border px-3 py-1.5 text-[12.5px] font-semibold disabled:opacity-50 " +
                      (activo
                        ? e === "hecho"
                          ? "border-done/60 bg-done-soft text-done"
                          : "border-accent/60 bg-accent/15 text-accent"
                        : "border-hairline text-dim hover:text-ink")
                    }
                  >
                    {ETIQUETA_ESTADO[e]}
                  </button>
                );
              })}
            </div>
            {/* Fecha de realización de un ítem YA hecho: editable, sin trampa.
                El estado ya está comprometido; esto solo ajusta el "cuándo". */}
            {hecho && (
              <div className="mt-3">
                {!editandoFechaHecho ? (
                  <p className="text-[12.5px] text-done">
                    {item.completed_at ? `Hecho el ${fechaHumana(item.completed_at)}.` : "Hecho."}{" "}
                    <button
                      onClick={() => setEditandoFechaHecho(true)}
                      disabled={ocupado}
                      className="font-semibold hover:underline disabled:opacity-50"
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
              <p className="mb-2 text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">Fecha</p>
              {!moviendoFecha ? (
                <div className="flex items-center justify-between gap-3 rounded-cinta border border-hairline bg-surface-2 px-4 py-3">
                  <span className="text-[14px]">{fechaHumana(item.fecha_base)}</span>
                  <button
                    onClick={() => setMoviendoFecha(true)}
                    disabled={ocupado}
                    className="shrink-0 text-[12.5px] font-semibold text-accent hover:underline disabled:opacity-50"
                  >
                    Mover fecha
                  </button>
                </div>
              ) : (
                <div className="flex flex-wrap items-center gap-2.5 rounded-cinta border border-accent/40 bg-surface-2 px-4 py-3">
                  <input
                    type="date"
                    defaultValue={fechaInputLocal(new Date(item.fecha_base))}
                    onChange={(ev) => {
                      if (ev.target.value) {
                        onCambio({ fecha_base: isoDesdeInputLocal(ev.target.value) });
                        setMoviendoFecha(false);
                      }
                    }}
                    disabled={ocupado}
                    aria-label="Nueva fecha objetivo"
                    className="rounded-[9px] border border-hairline bg-surface px-2.5 py-1.5 text-[13px] text-ink outline-none focus:border-accent/60 disabled:opacity-50"
                  />
                  <button onClick={() => setMoviendoFecha(false)} className="text-[12.5px] text-dim hover:text-ink">
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

        {/* pie: guardar la nota (si cambió) + marcar hecho */}
        <footer className="flex items-center gap-3 border-t border-hairline px-5 py-4 sm:px-6">
          {!hecho ? (
            <button
              onClick={() => marcarHecho()}
              disabled={ocupado}
              className="flex-1 rounded-[10px] bg-done py-2.5 text-[13.5px] font-semibold text-[#04120A] hover:opacity-90 disabled:opacity-50"
            >
              Marcar hecho
            </button>
          ) : (
            <button
              onClick={() => onCambio({ estado: "pendiente" })}
              disabled={ocupado}
              className="flex-1 rounded-[10px] border border-hairline py-2.5 text-[13.5px] font-semibold text-dim hover:text-ink disabled:opacity-50"
            >
              Desmarcar
            </button>
          )}
          <button
            onClick={() => onCambio({ nota: nota.trim() || null })}
            disabled={ocupado || !notaCambiada}
            className="rounded-[10px] border border-hairline px-5 py-2.5 text-[13.5px] font-semibold text-ink hover:border-accent/60 disabled:opacity-40"
          >
            Guardar
          </button>
        </footer>
      </section>
    </div>
  );
}
