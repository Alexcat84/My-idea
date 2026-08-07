"use client";

/**
 * NotaRapida — el atajo de nota (decisión del fundador, jul 2026). Un iconito en
 * la fila que es a la vez INDICADOR (relleno en azul cuando ya hay nota) y
 * ENTRADA (un clic abre un popover con el campo, con voz). Escribe el MISMO
 * campo `nota` del ítem, así la nota es idéntica desde Manos a la Obra y desde
 * el Calendario (una sola verdad). Opcional siempre: vacío = sin nota, jamás
 * obliga ni bloquea.
 *
 * Popover junto al control en escritorio, hoja inferior a lo ancho en móvil
 * (mismo patrón que SelectorEstado, para que se sienta de la casa).
 */
import { useState } from "react";
import { CampoConVoz } from "./CampoConVoz";

function IconoNota({ tiene, tamano }: { tiene: boolean; tamano: number }) {
  if (tiene) {
    return (
      <svg width={tamano} height={tamano} viewBox="0 0 20 20" aria-hidden>
        <rect x="3.5" y="3" width="13" height="14" rx="2.5" fill="currentColor" />
        <path d="M6.8 7.4h6.4M6.8 10.2h6.4M6.8 13h3.8" stroke="#0C0C10" strokeWidth="1.4" strokeLinecap="round" />
      </svg>
    );
  }
  return (
    <svg width={tamano} height={tamano} viewBox="0 0 20 20" fill="none" aria-hidden>
      <rect x="3.5" y="3" width="13" height="14" rx="2.5" stroke="currentColor" strokeWidth="1.5" />
      <path d="M6.8 7.4h6.4M6.8 10.2h6.4M6.8 13h3.8" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" />
    </svg>
  );
}

export function NotaRapida({
  id,
  nota,
  ocupado,
  onGuardar,
  tamano = 18,
}: {
  id: string;
  nota: string | null;
  ocupado: boolean;
  /** guarda la nota (o null para quitarla) en el MISMO campo `nota` del ítem */
  onGuardar: (nota: string | null) => void;
  tamano?: number;
}) {
  const [abierto, setAbierto] = useState(false);
  const [texto, setTexto] = useState(nota ?? "");
  const tiene = Boolean(nota && nota.trim());

  function abrir() {
    setTexto(nota ?? "");
    setAbierto(true);
  }
  function guardar() {
    onGuardar(texto.trim() || null);
    setAbierto(false);
  }

  return (
    <span className="relative inline-flex">
      <button
        type="button"
        onClick={() => (abierto ? setAbierto(false) : abrir())}
        disabled={ocupado}
        aria-haspopup="dialog"
        aria-expanded={abierto}
        title={tiene ? "Ver o editar tu nota" : "Añadir una nota"}
        aria-label={tiene ? "Ver o editar tu nota" : "Añadir una nota"}
        className={
          "-my-[9px] -mr-[7px] flex shrink-0 items-center justify-center p-[9px] transition-opacity hover:opacity-75 disabled:opacity-50 sm:m-0 sm:p-0 " +
          (tiene ? "text-accent" : "text-dim hover:text-ink")
        }
      >
        <IconoNota tiene={tiene} tamano={tamano} />
      </button>

      {abierto && (
        <>
          <button
            type="button"
            aria-label="Cerrar la nota"
            onClick={() => setAbierto(false)}
            className="fixed inset-0 z-40 cursor-default bg-black/40 sm:bg-transparent"
          />
          <div
            role="dialog"
            aria-label="Tu nota"
            className={
              "z-50 border border-white/[0.14] bg-surface-2 shadow-[0_18px_40px_rgba(0,0,0,0.6)] " +
              "fixed inset-x-0 bottom-0 rounded-t-[18px] p-4 pb-5 " +
              "sm:absolute sm:inset-x-auto sm:bottom-auto sm:right-0 sm:top-full sm:mt-2 sm:w-[300px] sm:rounded-[14px] sm:p-3"
            }
          >
            <span className="mx-auto mb-3 block h-1 w-9 rounded-full bg-white/20 sm:hidden" />
            <p className="mb-2 px-0.5 text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">Tu nota</p>
            <CampoConVoz
              id={`nota-rapida-${id}`}
              valor={texto}
              onCambio={setTexto}
              filas={3}
              placeholder="Lo que necesites recordar…"
            />
            <div className="mt-3 flex items-center gap-2">
              <button
                type="button"
                onClick={guardar}
                disabled={ocupado}
                className="rounded-[9px] border border-accent/40 bg-accent/10 px-4 py-1.5 text-[13px] font-semibold text-accent hover:bg-accent/20 disabled:opacity-50"
              >
                Guardar
              </button>
              <button type="button" onClick={() => setAbierto(false)} className="text-[12.5px] text-dim hover:text-ink">
                cerrar
              </button>
              {tiene && (
                <button
                  type="button"
                  onClick={() => {
                    onGuardar(null);
                    setTexto("");
                    setAbierto(false);
                  }}
                  disabled={ocupado}
                  className="ml-auto text-[12.5px] text-dim hover:text-warn disabled:opacity-50"
                >
                  quitar
                </button>
              )}
            </div>
          </div>
        </>
      )}
    </span>
  );
}
