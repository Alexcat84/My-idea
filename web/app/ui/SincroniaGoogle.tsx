"use client";

/**
 * SincroniaGoogle — la tarjeta de conexión con Google Calendar (Nivel 1, una
 * vía). El texto se adapta a CÓMO entró el usuario: si ya usa Google, es
 * "activar sincronía" (un permiso más, no un login nuevo); si entró por correo,
 * "conectar una cuenta de Google". Conectado: sincronizar ahora / desconectar.
 *
 * El botón de conectar es un ENLACE normal a /api/calendar/google/conectar (el
 * OAuth navega la página); desconectar y sincronizar van por fetch (POST).
 */
import { useEffect, useState } from "react";

type Estado = { disponible: boolean; conectado: boolean; email: string | null; provider: string | null };

export function SincroniaGoogle() {
  const [estado, setEstado] = useState<Estado | null>(null);
  const [ocupado, setOcupado] = useState(false);
  const [aviso, setAviso] = useState<string | null>(null);

  const cargar = () =>
    fetch("/api/calendar/google/estado")
      .then((r) => r.json())
      .then(setEstado)
      .catch(() => setEstado({ disponible: false, conectado: false, email: null, provider: null }));

  useEffect(() => {
    cargar();
    // Feedback tras volver del OAuth (?gcal=ok/error/…), luego se limpia el query.
    const p = new URLSearchParams(window.location.search).get("gcal");
    if (p === "ok") setAviso("Listo: tus fechas ya están en tu calendario de Google.");
    else if (p === "sinrefresh") setAviso("Google no dejó el permiso permanente. Vuelve a intentar y acepta el acceso a tu calendario.");
    else if (p === "config") setAviso("Falta un ajuste del lado del servidor. Avísanos.");
    else if (p === "error") setAviso("No se pudo conectar. Intenta de nuevo.");
    if (p) {
      const u = new URL(window.location.href);
      u.searchParams.delete("gcal");
      window.history.replaceState({}, "", u.toString());
    }
  }, []);

  if (!estado) return null;
  if (!estado.disponible) {
    return <p className="mt-3 text-[12px] leading-relaxed text-dim/80">Crea tu cuenta para sincronizar con Google Calendar.</p>;
  }

  const next = typeof window !== "undefined" ? window.location.pathname + window.location.search : "/ideas";
  const href = `/api/calendar/google/conectar?next=${encodeURIComponent(next)}`;

  async function accion(ruta: string, msg: string) {
    setOcupado(true);
    setAviso(null);
    try {
      const r = await fetch(ruta, { method: "POST" });
      if (r.ok) {
        setAviso(msg);
        await cargar();
      } else setAviso("No se pudo. Intenta de nuevo.");
    } catch {
      setAviso("Revisa tu internet e intenta de nuevo.");
    } finally {
      setOcupado(false);
    }
  }

  if (estado.conectado) {
    return (
      <div className="mt-3">
        <p className="flex items-center gap-2 text-[12.5px] font-semibold text-done">
          <span aria-hidden className="h-1.5 w-1.5 rounded-full bg-done" />
          Conectado{estado.email ? ` · ${estado.email}` : ""}
        </p>
        <div className="mt-2.5 flex gap-2">
          <button
            onClick={() => accion("/api/calendar/google/sync", "Sincronizado.")}
            disabled={ocupado}
            className="flex-1 rounded-[11px] border border-accent/50 py-2 text-[12.5px] font-semibold text-accent hover:bg-accent/10 disabled:opacity-50"
          >
            Sincronizar ahora
          </button>
          <button
            onClick={() => accion("/api/calendar/google/desconectar", "Desconectado. Se quitó el calendario “My Idea”.")}
            disabled={ocupado}
            className="rounded-[11px] border border-hairline px-3 py-2 text-[12.5px] font-semibold text-dim hover:text-warn disabled:opacity-50"
          >
            Desconectar
          </button>
        </div>
        {aviso && <p className="mt-2 text-[11.5px] text-dim">{aviso}</p>}
      </div>
    );
  }

  const esGoogle = estado.provider === "google";
  return (
    <div className="mt-3">
      <a
        href={href}
        className="block w-full rounded-[11px] border border-accent/50 bg-accent/10 py-2.5 text-center text-[13px] font-semibold text-accent hover:bg-accent/20"
      >
        {esGoogle ? "Activar sincronía con mi calendario" : "Conectar una cuenta de Google"}
      </a>
      <p className="mt-2 text-[11.5px] leading-relaxed text-dim/80">
        {esGoogle
          ? "Ya entraste con Google; solo falta permitir el acceso a tu calendario. Crearemos un calendario “My Idea” para tus fechas."
          : "Crearemos un calendario “My Idea” en tu Google y pondremos ahí tus fechas. No tocamos el resto de tu calendario."}
      </p>
      {aviso && <p className="mt-2 text-[11.5px] text-dim">{aviso}</p>}
    </div>
  );
}
