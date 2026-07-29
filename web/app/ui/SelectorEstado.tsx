"use client";

/**
 * SelectorEstado — el gestor de estados por tarea (decisión del fundador, jul
 * 2026): el usuario ELIGE el estado, no lo adivina ciclando un círculo.
 *
 * El control (círculo + palabra) abre un menú de los 5 estados: hoja inferior
 * a lo ancho en móvil, popover junto al control en escritorio. Cada estado se
 * distingue por FORMA además de color (ley del canon). "Hecha" compromete al
 * acto con la fecha de hoy (ley vigente del marcado). "No aplica" ofrece un
 * motivo OPCIONAL (texto o voz) para la memoria del usuario.
 *
 * Este módulo es la fuente ÚNICA del vocabulario y los iconos de estado: lo
 * comparten la fila del checklist y el cajón de detalle, para que nunca digan
 * cosas distintas.
 */
import { useState } from "react";
import { CampoConVoz } from "./CampoConVoz";
import type { ChecklistEstado } from "@/lib/dbContract";

/** Etiqueta de cara de cada estado. 'a_medias' se renombró a "en proceso"
 * (migration 030); "no aplica" es la tarea retirada. */
export const ETIQUETA_ESTADO: Record<ChecklistEstado, string> = {
  pendiente: "sin empezar",
  empezado: "apenas empezada",
  en_proceso: "en proceso",
  hecho: "hecha",
  no_aplica: "no aplica",
};

/** Orden del DETALLE (la vista completa): progresión natural, de menos a más
 * avance, con la retirada al final. */
export const ORDEN_ESTADOS: ChecklistEstado[] = ["pendiente", "empezado", "en_proceso", "hecho", "no_aplica"];

/** Orden del MENÚ del checklist: "Hecha" PRIMERA y resaltada. Marcar hecho es
 * el ~80% de los toques; al abrir el menú, la acción común queda a un toque de
 * distancia (mitigación del fundador al quitar el atajo "Marcar hecho"). */
export const ORDEN_MENU: ChecklistEstado[] = ["hecho", "en_proceso", "empezado", "pendiente", "no_aplica"];

/** El icono de un estado, distinguible por FORMA además de color. Verde
 * ejecuta (empezada/en proceso/hecha); la retirada va en gris con una barra
 * (ni verde ni rojo: no es logro ni alarma, es "fuera de esta idea"). */
export function IconoEstado({ estado, tamano = 22 }: { estado: ChecklistEstado; tamano?: number }) {
  const px = `${tamano}px`;
  if (estado === "hecho") {
    return (
      <span
        className="anima-check-pop flex shrink-0 items-center justify-center rounded-full bg-done"
        style={{ width: px, height: px }}
      >
        <svg width={tamano * 0.5} height={tamano * 0.5} viewBox="0 0 12 12" aria-hidden>
          <path d="M2.5 6.5l2.5 2.5 4.5-5.5" stroke="#04120A" strokeWidth="2" fill="none" />
        </svg>
      </span>
    );
  }
  if (estado === "en_proceso") {
    return (
      <span
        className="box-border flex shrink-0 overflow-hidden rounded-full border-[1.5px] border-done"
        style={{ width: px, height: px }}
      >
        <span className="h-full w-1/2 bg-done" />
      </span>
    );
  }
  if (estado === "empezado") {
    return (
      <span
        className="box-border flex shrink-0 items-center justify-center rounded-full border-[1.5px] border-done"
        style={{ width: px, height: px }}
      >
        <span className="rounded-full bg-done" style={{ width: tamano * 0.32, height: tamano * 0.32 }} />
      </span>
    );
  }
  if (estado === "no_aplica") {
    return (
      <span
        className="box-border flex shrink-0 items-center justify-center rounded-full border-[1.5px] border-[#5A5B62]"
        style={{ width: px, height: px }}
      >
        <span className="block rounded-full bg-[#8A8B92]" style={{ width: tamano * 0.5, height: "1.5px" }} />
      </span>
    );
  }
  return (
    <span
      className="box-border block shrink-0 rounded-full border-[1.5px] border-white/30"
      style={{ width: px, height: px }}
    />
  );
}

/**
 * El menú de estados. Se renderiza sobre un `<span className="relative">` para
 * anclar el popover de escritorio; en móvil ignora el ancla y sale como hoja
 * inferior. `onElegir` recibe el estado y, para 'no_aplica', el motivo opcional.
 */
export function SelectorEstado({
  estado,
  ocupado,
  onElegir,
  etiquetaActual,
}: {
  estado: ChecklistEstado;
  ocupado: boolean;
  onElegir: (estado: ChecklistEstado, motivo?: string | null) => void;
  /** motivo actual de no_aplica, para precargar el campo al reeditar */
  etiquetaActual?: string | null;
}) {
  const [abierto, setAbierto] = useState(false);
  const [pidiendoMotivo, setPidiendoMotivo] = useState(false);
  const [motivo, setMotivo] = useState(etiquetaActual ?? "");

  function cerrar() {
    setAbierto(false);
    setPidiendoMotivo(false);
  }

  function elegir(e: ChecklistEstado) {
    if (e === "no_aplica") {
      setMotivo(etiquetaActual ?? "");
      setPidiendoMotivo(true);
      return;
    }
    onElegir(e);
    cerrar();
  }

  return (
    <span className="relative inline-flex">
      {/* Disparador REFORZADO: el círculo + un chevron, para que se lea como un
          control (no un punto pasivo). El chevron es la señal de "abre un
          menú". Área táctil de 44px a 380 (margen negativo + padding). */}
      <button
        type="button"
        onClick={() => setAbierto((v) => !v)}
        disabled={ocupado}
        aria-haspopup="menu"
        aria-expanded={abierto}
        title={`Estado: ${ETIQUETA_ESTADO[estado]} — tocar para elegir`}
        aria-label={`${ETIQUETA_ESTADO[estado]}. Tocar para elegir el estado`}
        className="-m-[11px] flex h-11 shrink-0 items-center gap-1 p-[11px] transition-opacity hover:opacity-75 disabled:opacity-50 sm:m-0 sm:h-auto sm:p-0"
      >
        <IconoEstado estado={estado} />
        <svg
          aria-hidden
          width="9"
          height="9"
          viewBox="0 0 12 12"
          className={"shrink-0 text-dim transition-transform " + (abierto ? "rotate-180" : "")}
        >
          <path d="M2 4l4 4 4-4" stroke="currentColor" strokeWidth="1.5" fill="none" />
        </svg>
      </button>

      {abierto && (
        <>
          <button
            type="button"
            aria-label="Cerrar el menú de estado"
            onClick={cerrar}
            className="fixed inset-0 z-40 cursor-default bg-black/40 sm:bg-transparent"
          />
          <div
            role="menu"
            className={
              "z-50 border border-white/[0.14] bg-surface-2 shadow-[0_18px_40px_rgba(0,0,0,0.6)] " +
              "fixed inset-x-0 bottom-0 rounded-t-[18px] p-2 pb-4 " +
              "sm:absolute sm:inset-x-auto sm:bottom-auto sm:left-0 sm:top-full sm:mt-2 sm:w-[268px] sm:rounded-[14px] sm:p-1.5 sm:pb-1.5"
            }
          >
            <span className="mx-auto mt-1 mb-2 block h-1 w-9 rounded-full bg-white/20 sm:hidden" />
            {!pidiendoMotivo ? (
              <>
                <p className="px-3 pb-1 pt-1 text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">
                  ¿Cómo va esta tarea?
                </p>
                {ORDEN_MENU.map((e) => {
                  const actual = e === estado;
                  // "Hecha" va resaltada SIEMPRE (acción común rápida), aunque no
                  // sea el estado actual; el check marca el estado de verdad.
                  const rapida = e === "hecho";
                  return (
                    <button
                      key={e}
                      type="button"
                      role="menuitemradio"
                      aria-checked={actual}
                      onClick={() => elegir(e)}
                      disabled={ocupado}
                      className={
                        "flex min-h-[40px] w-full items-center gap-3 rounded-[10px] px-3 py-2.5 text-left text-[14px] disabled:opacity-50 " +
                        (rapida
                          ? "bg-done/[0.12] font-semibold text-done hover:bg-done/[0.12]"
                          : actual
                            ? "bg-white/[0.06] font-semibold"
                            : "hover:bg-white/[0.06]")
                      }
                    >
                      <IconoEstado estado={e} tamano={18} />
                      <span className="flex-1 capitalize">{ETIQUETA_ESTADO[e]}</span>
                      {/* El check del estado VIGENTE va SIEMPRE en azul (Design):
                          el azul dice "esto es lo elegido"; el verde vive solo
                          dentro del icono de hecha, no en la marca de selección. */}
                      {actual && (
                        <svg width="13" height="13" viewBox="0 0 12 12" aria-hidden className="text-accent">
                          <path d="M2.5 6.5l2.5 2.5 4.5-5.5" stroke="currentColor" strokeWidth="2" fill="none" />
                        </svg>
                      )}
                    </button>
                  );
                })}
              </>
            ) : (
              <div className="px-2 py-1.5">
                <p className="text-[13.5px] font-semibold">¿Por qué no aplica?</p>
                <p className="mb-2 mt-0.5 text-[12.5px] text-dim">Para tu propia memoria. Puedes dejarlo en blanco.</p>
                <CampoConVoz
                  id="motivo-no-aplica"
                  valor={motivo}
                  onCambio={setMotivo}
                  filas={2}
                  placeholder="No corre para esta idea porque…"
                />
                <div className="mt-2.5 flex items-center gap-2">
                  <button
                    type="button"
                    onClick={() => {
                      onElegir("no_aplica", motivo.trim() || null);
                      cerrar();
                    }}
                    disabled={ocupado}
                    className="rounded-[9px] bg-accent px-3.5 py-1.5 text-[12.5px] font-semibold text-white hover:opacity-90 disabled:opacity-50"
                  >
                    Retirar tarea
                  </button>
                  <button
                    type="button"
                    onClick={() => setPidiendoMotivo(false)}
                    className="text-[12.5px] text-dim hover:text-ink"
                  >
                    volver
                  </button>
                </div>
              </div>
            )}
          </div>
        </>
      )}
    </span>
  );
}
