"use client";

/**
 * SuscripcionCalendario — "Sincronizar con mi calendario" (opción B, universal).
 * En vez de conectar una cuenta de Google, el usuario se SUSCRIBE una sola vez a
 * una URL de calendario en vivo; su teléfono (Google/Apple/Outlook/cualquiera)
 * la re-lee solo y se mantiene al día. El botón abre `webcal://` (diálogo de
 * suscripción del sistema); "Copiar enlace" da la URL https para pegarla a mano.
 */
import { useEffect, useState } from "react";

type FeedUrl = { disponible: boolean; url: string | null; webcal: string | null };

export function SuscripcionCalendario() {
  const [feed, setFeed] = useState<FeedUrl | null>(null);
  const [copiado, setCopiado] = useState(false);

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

  if (!feed) return null;
  if (!feed.disponible || !feed.url || !feed.webcal) {
    return <p className="mt-3 text-[12px] leading-relaxed text-dim/80">Crea tu cuenta para suscribir tu calendario.</p>;
  }

  async function copiar() {
    try {
      await navigator.clipboard.writeText(feed!.url!);
      setCopiado(true);
      setTimeout(() => setCopiado(false), 2000);
    } catch {
      /* sin portapapeles: el usuario puede usar el botón de suscribir */
    }
  }

  return (
    <div className="mt-3">
      <a
        href={feed.webcal}
        className="block w-full rounded-[11px] bg-done py-2.5 text-center text-[13.5px] font-bold text-[#04120A] hover:opacity-90"
      >
        Suscribir mi calendario
      </a>
      <button
        onClick={copiar}
        className="mt-2 w-full rounded-[11px] border border-hairline py-2 text-[12.5px] font-semibold text-dim hover:text-ink"
      >
        {copiado ? "Enlace copiado ✓" : "Copiar el enlace"}
      </button>
      <p className="mt-2 text-[11.5px] leading-relaxed text-dim/80">
        Se suscribe una vez y se mantiene al día solo, en cualquier calendario (Google, Apple, Outlook…). El aviso lo
        pone tu teléfono la víspera.
      </p>
      <p className="mt-1.5 text-[11px] leading-relaxed text-dim/70">
        Cada cuánto se actualiza lo decide tu app de calendario, no nosotros: puede tardar desde minutos hasta unas
        horas (Google y Apple suelen refrescar cada cierto tiempo). Si quieres verlo al instante, usa la descarga (.ics).
      </p>
    </div>
  );
}
