"use client";

/**
 * /auth/update-password — fijar una contraseña nueva tras "olvidé mi
 * contraseña" (modelo I Ching). Se llega desde el enlace de recuperación,
 * que /auth/callback ya convirtió en una sesión de recuperación en cookies;
 * updateUser({ password }) usa esa sesión. Sin sesión válida, no hay nada
 * que actualizar: se avisa y se manda al login.
 */
import { useState } from "react";
import { useRouter } from "next/navigation";
import { createClient } from "@/lib/supabase/client";
import { validarPassword } from "@/lib/password";

export default function UpdatePassword() {
  const router = useRouter();
  const [password, setPassword] = useState("");
  const [confirmar, setConfirmar] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [ok, setOk] = useState(false);
  const [enviando, setEnviando] = useState(false);

  async function guardar(e: React.FormEvent) {
    e.preventDefault();
    if (enviando) return;
    setError(null);
    const problema = validarPassword(password);
    if (problema) return setError(problema);
    if (password !== confirmar) return setError("Las dos contraseñas no coinciden.");
    setEnviando(true);
    try {
      const { error } = await createClient().auth.updateUser({ password });
      if (error) {
        const msg = error.message.toLowerCase();
        setError(
          msg.includes("session") || msg.includes("token")
            ? "Ese enlace ya venció o se usó. Pide uno nuevo desde 'Olvidé mi contraseña'."
            : "No pudimos actualizar tu contraseña; intenta de nuevo."
        );
        return;
      }
      setOk(true);
      setTimeout(() => {
        router.push("/ideas");
        router.refresh();
      }, 1200);
    } catch {
      setError("no pudimos conectar; revisa tu internet e intenta de nuevo");
    } finally {
      setEnviando(false);
    }
  }

  return (
    <main className="flex flex-1 items-center justify-center px-6">
      <div className="flex w-full max-w-sm flex-col items-center gap-8 py-16">
        <div className="text-center">
          <h1 className="text-3xl font-semibold tracking-tight">
            My <span className="text-accent">Idea</span>
          </h1>
          <p className="mt-2 text-dim">Elige tu nueva contraseña.</p>
        </div>
        {ok ? (
          <p className="text-center text-done">Contraseña actualizada. Entrando…</p>
        ) : (
          <form onSubmit={guardar} className="flex w-full flex-col gap-3">
            <label htmlFor="pass" className="sr-only">
              Nueva contraseña
            </label>
            <input
              id="pass"
              type="password"
              required
              autoFocus
              autoComplete="new-password"
              placeholder="Nueva contraseña"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full rounded-cinta border border-hairline bg-surface px-4 py-3 text-ink placeholder:text-dim"
            />
            <label htmlFor="pass2" className="sr-only">
              Repetir contraseña
            </label>
            <input
              id="pass2"
              type="password"
              required
              autoComplete="new-password"
              placeholder="Repite tu contraseña"
              value={confirmar}
              onChange={(e) => setConfirmar(e.target.value)}
              className="w-full rounded-cinta border border-hairline bg-surface px-4 py-3 text-ink placeholder:text-dim"
            />
            <p className="text-xs text-dim">Al menos 8 caracteres, una mayúscula y un número.</p>
            {error && <p className="text-sm text-warn">{error}</p>}
            <button
              type="submit"
              disabled={enviando}
              className="rounded-cinta bg-accent px-4 py-3 font-medium text-white hover:opacity-90 disabled:opacity-50"
            >
              {enviando ? "Guardando…" : "Guardar contraseña"}
            </button>
          </form>
        )}
      </div>
    </main>
  );
}
