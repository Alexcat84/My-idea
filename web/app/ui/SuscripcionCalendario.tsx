"use client";

/**
 * SuscripcionCalendario — "Sincronizar con mi calendario" (opción B, universal).
 * Dos botones de acción: SUSCRIBIR (abre `webcal://`, el teléfono se mantiene al
 * día solo) y DESCARGAR el .ics (una sola vez). Visual estándar de la casa (sin
 * jugar con colores); las explicaciones viven en un ⓘ flotante, no en un muro de
 * texto en la UI.
 */
import { useEffect, useState } from "react";

type FeedUrl = { disponible: boolean; url: string | null; webcal: string | null };

function IconoInfo() {
  return (
    <svg width="15" height="15" viewBox="0 0 20 20" fill="none" aria-hidden>
      <circle cx="10" cy="10" r="7.5" stroke="currentColor" strokeWidth="1.4" />
      <path d="M10 9v4.5" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" />
      <circle cx="10" cy="6.4" r="0.5" fill="currentColor" stroke="currentColor" strokeWidth="0.6" />
    </svg>
  );
}

export function SuscripcionCalendario({
  onDescargarIcs,
  puedeDescargar,
}: {
  onDescargarIcs: () => void;
  puedeDescargar: boolean;
}) {
  const [feed, setFeed] = useState<FeedUrl | null>(null);
  const [info, setInfo] = useState(false);

  useEffect(() => {
    let vivo = true;
    fetch("/api/calendar/feed-url")
      .then((r) => r.json())
      .then((d: FeedUrl) => vivo && setFeed(d))
      .catch(() => vivo && setFeed({ disponible: false, url: null, webcal: null }));
    return () => {
      vivo = false;
    };
  }, []);

  return (
    <div>
      <div className="flex items-center gap-2">
        <p className="text-[14px] font-semibold">Sincronizar con mi calendario</p>
        <span className="relative inline-flex">
          <button
            type="button"
            onClick={() => setInfo((v) => !v)}
            aria-label="Cómo funciona la sincronía"
            aria-expanded={info}
            className="text-dim hover:text-ink"
          >
            <IconoInfo />
          </button>
          {info && (
            <>
              <button type="button" aria-label="Cerrar" onClick={() => setInfo(false)} className="fixed inset-0 z-40 cursor-default" />
              <div className="absolute left-0 top-full z-50 mt-2 w-[248px] rounded-[12px] border border-white/[0.14] bg-surface-2 p-3 text-[12px] leading-relaxed text-dim shadow-[0_18px_40px_rgba(0,0,0,0.6)]">
                Te suscribes una vez y tus fechas se mantienen al día solas, en cualquier calendario (Google, Apple,
                Outlook…). El aviso lo pone tu teléfono la víspera a las 20:00.
                <span className="mt-2 block text-dim/80">
                  Cada cuánto se actualiza lo decide tu app de calendario (de minutos a unas horas). Para verlo al
                  instante, descarga el archivo.
                </span>
              </div>
            </>
          )}
        </span>
      </div>
      <p className="mt-1.5 text-[12.5px] leading-relaxed text-dim">Ten tus fechas en el calendario que ya usas.</p>

      {feed?.disponible && feed.webcal ? (
        <a
          href={feed.webcal}
          className="mt-3 block w-full rounded-[11px] border border-accent/50 bg-accent/10 py-2.5 text-center text-[13px] font-semibold text-accent hover:bg-accent/20"
        >
          Suscribir mi calendario
        </a>
      ) : (
        <p className="mt-3 text-[12px] leading-relaxed text-dim/80">Crea tu cuenta para suscribir tu calendario.</p>
      )}

      <button
        onClick={onDescargarIcs}
        disabled={!puedeDescargar}
        className="mt-2 w-full rounded-[11px] border border-hairline py-2.5 text-[13px] font-semibold text-dim hover:text-ink disabled:opacity-40"
      >
        Descargar el archivo (.ics)
      </button>
    </div>
  );
}
