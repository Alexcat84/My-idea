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
import { elegir } from "@/lib/i18n/config";
import { useIdioma } from "@/lib/i18n/IdiomaProvider";
import { CLAVE_NUEVA } from "@/lib/i18n/mensajes/acceso";
import { createClient } from "@/lib/supabase/client";
import { LARGO_MINIMO, validarPassword } from "@/lib/password";
import { interpolar } from "@/lib/i18n/interpolar";

export default function UpdatePassword() {
  const idioma = useIdioma();
  const t = elegir(CLAVE_NUEVA, idioma);
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
    const problema = validarPassword(password, idioma);
    if (problema) return setError(problema);
    if (password !== confirmar) return setError(t.noCoinciden);
    setEnviando(true);
    try {
      const { error } = await createClient().auth.updateUser({ password });
      if (error) {
        const msg = error.message.toLowerCase();
        setError(
          msg.includes("session") || msg.includes("token")
            ? t.enlaceVencido
            : t.noActualizo
        );
        return;
      }
      setOk(true);
      setTimeout(() => {
        router.push("/ideas");
        router.refresh();
      }, 1200);
    } catch {
      setError(t.conectarInternet);
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
          <p className="mt-2 text-dim">{t.lema}</p>
        </div>
        {ok ? (
          <p className="text-center text-done">{t.actualizada}</p>
        ) : (
          <form onSubmit={guardar} className="flex w-full flex-col gap-3">
            <label htmlFor="pass" className="sr-only">
              {t.etiquetaNueva}
            </label>
            <input
              id="pass"
              type="password"
              required
              autoFocus
              autoComplete="new-password"
              placeholder={t.placeholderNueva}
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full rounded-cinta border border-hairline bg-surface px-4 py-3 text-ink placeholder:text-dim"
            />
            <label htmlFor="pass2" className="sr-only">
              {t.etiquetaRepetir}
            </label>
            <input
              id="pass2"
              type="password"
              required
              autoComplete="new-password"
              placeholder={t.placeholderRepetir}
              value={confirmar}
              onChange={(e) => setConfirmar(e.target.value)}
              className="w-full rounded-cinta border border-hairline bg-surface px-4 py-3 text-ink placeholder:text-dim"
            />
            <p className="text-xs text-dim">{interpolar(t.reglas, { n: LARGO_MINIMO })}</p>
            {error && <p className="text-sm text-warn">{error}</p>}
            <button
              type="submit"
              disabled={enviando}
              className="rounded-cinta border border-accent/40 bg-accent/10 px-4 py-3 font-medium text-accent hover:bg-accent/20 disabled:opacity-50"
            >
              {enviando ? t.guardando : t.guardar}
            </button>
          </form>
        )}
      </div>
    </main>
  );
}
