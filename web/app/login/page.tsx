"use client";

/**
 * Login (modelo del I Ching, jul 2026): correo + CONTRASEÑA. El
 * código-cada-vez quedó obsoleto — chocaba con el límite de correos de
 * producción ("esperar dos horas") y con el 2FA. Aquí: pestañas Entrar /
 * Crear cuenta, botón de Google, "olvidé mi contraseña" y reenviar
 * confirmación. La allowlist gatea (el no invitado recibe un mensaje amable).
 * El desafío 2FA y el ?next= ("seguimos justo donde quedaste") se conservan.
 */
import { Suspense, useEffect, useRef, useState } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import { destinoPostLogin } from "@/lib/nextSeguro";
import { validarPassword } from "@/lib/password";

type Estado =
  | { fase: "form"; modo: "entrar" | "crear"; error?: string; sinConfirmar?: boolean; aviso?: string }
  | { fase: "revisa_correo"; email: string }
  | { fase: "reset_enviado"; email: string }
  | { fase: "desafio"; metodo: "totp" | "email"; rescate: boolean; aviso?: string; error?: string }
  | { fase: "no_invitado" };

/** El glifo oficial de Google (mismo trazado que usa el I Ching). */
function GlifoGoogle() {
  return (
    <svg viewBox="0 0 24 24" width={18} height={18} aria-hidden>
      <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" />
      <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" />
      <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" />
      <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" />
    </svg>
  );
}

function LoginForm() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const enlaceVencido = searchParams.get("enlace") === "vencido";
  const googleFallo = searchParams.get("google") === "fallo";
  // "Seguimos justo donde quedaste": la frontera manda aquí con ?next=<ruta>.
  const destino = destinoPostLogin(searchParams.get("next"));
  const [estado, setEstado] = useState<Estado>(() => {
    if (searchParams.get("google") === "no-invitado") return { fase: "no_invitado" };
    if (searchParams.get("desafio") === "1") {
      return { fase: "desafio", metodo: searchParams.get("metodo") === "email" ? "email" : "totp", rescate: false };
    }
    return { fase: "form", modo: "entrar" };
  });
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [codigo, setCodigo] = useState("");
  const [codigoRescate, setCodigoRescate] = useState("");
  const [enviando, setEnviando] = useState(false);

  // Método email del 2FA: al entrar al desafío se envía el código UNA vez.
  const emailDesafioEnviado = useRef(false);
  useEffect(() => {
    if (estado.fase !== "desafio" || estado.metodo !== "email" || estado.rescate) return;
    if (emailDesafioEnviado.current) return;
    emailDesafioEnviado.current = true;
    fetch("/api/cuenta/2fa/email/enviar", { method: "POST" })
      .then(async (r) => {
        const d = await r.json().catch(() => ({}));
        setEstado((e) =>
          e.fase === "desafio"
            ? r.ok
              ? { ...e, aviso: "Te enviamos un código a tu correo." }
              : { ...e, error: d.error ?? "no pudimos enviar el código; intenta de nuevo" }
            : e
        );
      })
      .catch(() => {
        setEstado((e) => (e.fase === "desafio" ? { ...e, error: "no pudimos conectar; intenta de nuevo" } : e));
      });
  }, [estado]);

  // ── Entrar (correo + contraseña) ─────────────────────────────────────
  async function entrar(e: React.FormEvent) {
    e.preventDefault();
    if (enviando) return;
    setEnviando(true);
    try {
      const res = await fetch("/api/auth/entrar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });
      const data = await res.json();
      if (data.invitado === false) {
        setEstado({ fase: "no_invitado" });
        return;
      }
      if (res.status === 403 && data.sinConfirmar) {
        setEstado({ fase: "form", modo: "entrar", error: data.error, sinConfirmar: true });
        return;
      }
      if (!res.ok) {
        setEstado({ fase: "form", modo: "entrar", error: data.error ?? "algo se atoró; intenta de nuevo" });
        return;
      }
      if (data.requiere2FA) {
        setCodigo("");
        setEstado({ fase: "desafio", metodo: data.metodo === "email" ? "email" : "totp", rescate: false });
        return;
      }
      router.push(destino);
      router.refresh();
    } catch {
      setEstado({ fase: "form", modo: "entrar", error: "no pudimos conectar; revisa tu internet e intenta de nuevo" });
    } finally {
      setEnviando(false);
    }
  }

  // ── Crear cuenta (correo + contraseña) ───────────────────────────────
  async function crear(e: React.FormEvent) {
    e.preventDefault();
    if (enviando) return;
    const problema = validarPassword(password);
    if (problema) {
      setEstado({ fase: "form", modo: "crear", error: problema });
      return;
    }
    setEnviando(true);
    try {
      const res = await fetch("/api/auth/registrar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        // El destino viaja para reanudar tras confirmar el correo (si vino
        // de la frontera de una idea); destino es /ideas si no hay next.
        body: JSON.stringify({ email, password, next: destino }),
      });
      const data = await res.json();
      if (data.invitado === false) {
        setEstado({ fase: "no_invitado" });
        return;
      }
      if (!res.ok) {
        setEstado({ fase: "form", modo: "crear", error: data.error ?? "algo se atoró; intenta de nuevo" });
        return;
      }
      if (data.yaExistia) {
        setPassword("");
        setEstado({ fase: "form", modo: "entrar", error: "Ese correo ya tiene cuenta. Inicia sesión." });
        return;
      }
      setEstado({ fase: "revisa_correo", email });
    } catch {
      setEstado({ fase: "form", modo: "crear", error: "no pudimos conectar; revisa tu internet e intenta de nuevo" });
    } finally {
      setEnviando(false);
    }
  }

  // ── Olvidé mi contraseña ─────────────────────────────────────────────
  async function olvide() {
    if (enviando) return;
    if (!email || !email.includes("@")) {
      setEstado({ fase: "form", modo: "entrar", error: "Escribe tu correo arriba y toca de nuevo." });
      return;
    }
    setEnviando(true);
    try {
      await fetch("/api/auth/reset", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email }),
      });
      setEstado({ fase: "reset_enviado", email });
    } catch {
      setEstado({ fase: "form", modo: "entrar", error: "no pudimos conectar; intenta de nuevo" });
    } finally {
      setEnviando(false);
    }
  }

  // ── Reenviar confirmación ────────────────────────────────────────────
  async function reenviarConfirmacion() {
    if (enviando) return;
    setEnviando(true);
    try {
      await fetch("/api/auth/reenviar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email }),
      });
      setEstado({ fase: "form", modo: "entrar", aviso: "Te reenviamos el correo de confirmación. Revisa tu bandeja." });
    } catch {
      setEstado({ fase: "form", modo: "entrar", error: "no pudimos conectar; intenta de nuevo" });
    } finally {
      setEnviando(false);
    }
  }

  // ── 2FA (desafío tras el login) ──────────────────────────────────────
  async function resolverDesafio(e: React.FormEvent) {
    e.preventDefault();
    if (enviando || estado.fase !== "desafio") return;
    setEnviando(true);
    try {
      const body = estado.rescate
        ? { recoveryCode: codigoRescate.trim() }
        : estado.metodo === "email"
          ? { emailCode: codigo }
          : { token: codigo };
      const res = await fetch("/api/cuenta/2fa/desafio", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body),
      });
      const data = await res.json();
      if (!res.ok) {
        setEstado({ ...estado, error: data.error ?? "algo se atoró; intenta de nuevo" });
        return;
      }
      router.push(destino);
      router.refresh();
    } catch {
      setEstado({ ...estado, error: "no pudimos conectar; revisa tu internet e intenta de nuevo" });
    } finally {
      setEnviando(false);
    }
  }

  async function reenviarCodigoDesafio() {
    if (enviando || estado.fase !== "desafio") return;
    setEnviando(true);
    try {
      const res = await fetch("/api/cuenta/2fa/email/enviar", { method: "POST" });
      const data = await res.json().catch(() => ({}));
      setEstado(
        res.ok
          ? { ...estado, aviso: "Código nuevo enviado a tu correo.", error: undefined }
          : { ...estado, error: data.error ?? "no pudimos enviar el código; intenta de nuevo" }
      );
    } catch {
      setEstado({ ...estado, error: "no pudimos conectar; intenta de nuevo" });
    } finally {
      setEnviando(false);
    }
  }

  // ── Pantallas de mensaje ─────────────────────────────────────────────
  if (estado.fase === "revisa_correo") {
    return (
      <div className="text-center">
        <p className="text-lg">Revisa tu correo</p>
        <p className="mt-3 text-sm text-dim">
          Te enviamos un enlace a <span className="font-semibold text-ink">{estado.email}</span> para confirmar
          tu cuenta. Ábrelo y quedas dentro. (Si no lo ves, revisa el spam.)
        </p>
        <button onClick={() => setEstado({ fase: "form", modo: "entrar" })} className="mt-6 text-sm text-accent hover:opacity-80">
          Volver
        </button>
      </div>
    );
  }

  if (estado.fase === "reset_enviado") {
    return (
      <div className="text-center">
        <p className="text-lg">Enlace enviado</p>
        <p className="mt-3 text-sm text-dim">
          Si <span className="font-semibold text-ink">{estado.email}</span> tiene cuenta, le llegó un enlace para
          elegir una contraseña nueva. Revisa tu bandeja (y el spam).
        </p>
        <button onClick={() => setEstado({ fase: "form", modo: "entrar" })} className="mt-6 text-sm text-accent hover:opacity-80">
          Volver
        </button>
      </div>
    );
  }

  if (estado.fase === "desafio") {
    const listo = estado.rescate ? codigoRescate.trim().length >= 6 : codigo.length === 6;
    return (
      <form onSubmit={resolverDesafio} className="flex w-full flex-col gap-3 text-center">
        <p className="text-lg">Un paso más: tu verificación en dos pasos</p>
        {estado.rescate ? (
          <>
            <p className="text-sm text-dim">Escribe uno de tus códigos de rescate.</p>
            <label htmlFor="rescate" className="sr-only">
              Código de rescate
            </label>
            <input
              id="rescate"
              autoFocus
              required
              maxLength={12}
              placeholder="XXXXXXXXXXXX"
              value={codigoRescate}
              onChange={(e) => setCodigoRescate(e.target.value.toUpperCase().replace(/[^0-9A-F]/g, ""))}
              className="w-full rounded-cinta border border-hairline bg-surface px-4 py-3 text-center font-mono text-xl tracking-[0.3em] text-ink placeholder:text-dim"
            />
          </>
        ) : (
          <>
            <p className="text-sm text-dim">
              {estado.metodo === "totp"
                ? "Escribe el código de tu app de autenticación."
                : (estado.aviso ?? "Te enviamos un código a tu correo.")}
            </p>
            <label htmlFor="desafio" className="sr-only">
              Código de 6 dígitos
            </label>
            <input
              id="desafio"
              inputMode="numeric"
              pattern="[0-9]{6}"
              maxLength={6}
              required
              autoFocus
              placeholder="······"
              value={codigo}
              onChange={(e) => setCodigo(e.target.value.replace(/\D/g, ""))}
              className="w-full rounded-cinta border border-hairline bg-surface px-4 py-3 text-center text-2xl font-bold tracking-[0.5em] text-ink placeholder:text-dim"
            />
          </>
        )}
        {estado.error && <p className="text-sm text-warn">{estado.error}</p>}
        <button
          type="submit"
          disabled={enviando || !listo}
          className="rounded-cinta bg-accent px-4 py-3 font-medium text-white hover:opacity-90 disabled:opacity-50"
        >
          {enviando ? "Verificando…" : "Verificar"}
        </button>
        {estado.metodo === "email" && !estado.rescate && (
          <button type="button" onClick={reenviarCodigoDesafio} disabled={enviando} className="text-sm text-dim hover:text-ink">
            Reenviarme el código
          </button>
        )}
        <button
          type="button"
          onClick={() => {
            setCodigo("");
            setCodigoRescate("");
            setEstado({ ...estado, rescate: !estado.rescate, error: undefined });
          }}
          className="text-sm text-dim hover:text-ink"
        >
          {estado.rescate ? "Volver al código normal" : "No tengo mi código: usar uno de rescate"}
        </button>
      </form>
    );
  }

  if (estado.fase === "no_invitado") {
    const correoIntentado = email || searchParams.get("correo") || "";
    return (
      <div className="text-center">
        <p className="text-lg">My Idea está en beta privada.</p>
        {correoIntentado && <p className="mt-3 font-semibold">{correoIntentado}</p>}
        <p className="mt-3 text-sm text-dim">
          Ese correo aún no está en la lista de invitados, entres con tu contraseña o con Google: la lista
          es la misma. Si alguien te invitó, pídele que confirme el correo que registró.
        </p>
        <button
          onClick={() => setEstado({ fase: "form", modo: "entrar" })}
          className="mt-6 text-sm text-accent hover:opacity-80"
        >
          Probar con otro correo
        </button>
      </div>
    );
  }

  // ── La pantalla principal: pestañas Entrar / Crear cuenta ────────────
  const modo = estado.modo;
  const cambiarModo = (m: "entrar" | "crear") => setEstado({ fase: "form", modo: m });
  return (
    <form onSubmit={modo === "entrar" ? entrar : crear} className="flex w-full flex-col gap-3">
      <div className="mb-1 flex rounded-cinta border border-hairline p-1 text-sm">
        <button
          type="button"
          onClick={() => cambiarModo("entrar")}
          className={`flex-1 rounded-[10px] py-2 font-medium ${modo === "entrar" ? "bg-surface text-ink" : "text-dim hover:text-ink"}`}
        >
          Entrar
        </button>
        <button
          type="button"
          onClick={() => cambiarModo("crear")}
          className={`flex-1 rounded-[10px] py-2 font-medium ${modo === "crear" ? "bg-surface text-ink" : "text-dim hover:text-ink"}`}
        >
          Crear cuenta
        </button>
      </div>

      {enlaceVencido && (
        <p className="rounded-cinta border border-hairline bg-surface px-4 py-3 text-sm text-warn">
          Ese enlace ya venció o ya se usó. Pide uno nuevo aquí abajo.
        </p>
      )}
      {googleFallo && (
        <p className="rounded-cinta border border-hairline bg-surface px-4 py-3 text-sm text-warn">
          No pudimos completar el acceso con Google. Intenta de nuevo, o entra con tu contraseña.
        </p>
      )}
      {estado.aviso && (
        <p className="rounded-cinta border border-hairline bg-surface px-4 py-3 text-sm text-dim">{estado.aviso}</p>
      )}

      <label htmlFor="email" className="sr-only">
        Correo electrónico
      </label>
      <input
        id="email"
        type="email"
        required
        autoComplete="email"
        placeholder="tu@correo.com"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        className="w-full rounded-cinta border border-hairline bg-surface px-4 py-3 text-ink placeholder:text-dim"
      />
      <label htmlFor="password" className="sr-only">
        Contraseña
      </label>
      <input
        id="password"
        type="password"
        required
        autoComplete={modo === "entrar" ? "current-password" : "new-password"}
        placeholder="Tu contraseña"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        className="w-full rounded-cinta border border-hairline bg-surface px-4 py-3 text-ink placeholder:text-dim"
      />
      {modo === "crear" && (
        <p className="text-xs text-dim">Al menos 8 caracteres, una mayúscula y un número.</p>
      )}
      {estado.error && <p className="text-sm text-warn">{estado.error}</p>}
      {estado.sinConfirmar && (
        <button type="button" onClick={reenviarConfirmacion} disabled={enviando} className="text-left text-sm text-accent hover:opacity-80">
          Reenviarme el correo de confirmación
        </button>
      )}

      <button
        type="submit"
        disabled={enviando}
        className="rounded-cinta bg-accent px-4 py-3 font-medium text-white hover:opacity-90 disabled:opacity-50"
      >
        {enviando ? "Un momento…" : modo === "entrar" ? "Entrar" : "Crear mi cuenta"}
      </button>

      {modo === "entrar" && (
        <button type="button" onClick={olvide} disabled={enviando} className="text-sm text-dim hover:text-ink">
          Olvidé mi contraseña
        </button>
      )}

      <div className="flex items-center gap-3 py-1 text-xs text-dim" aria-hidden>
        <span className="h-px flex-1 bg-hairline" />
        o
        <span className="h-px flex-1 bg-hairline" />
      </div>
      <a
        href={destino !== "/ideas" ? `/api/auth/google?next=${encodeURIComponent(destino)}` : "/api/auth/google"}
        className="flex items-center justify-center gap-2.5 rounded-cinta border border-hairline bg-surface px-4 py-3 font-medium text-ink hover:border-white/25"
      >
        <GlifoGoogle />
        Continuar con Google
      </a>
    </form>
  );
}

export default function LoginPage() {
  return (
    <main className="flex flex-1 items-center justify-center px-6">
      <div className="flex w-full max-w-sm flex-col items-center gap-8 py-16">
        <div className="text-center">
          <h1 className="text-3xl font-semibold tracking-tight">My <span className="text-accent">Idea</span></h1>
          <p className="mt-2 text-dim">El espacio donde tus ideas se trabajan.</p>
        </div>
        <Suspense>
          <LoginForm />
        </Suspense>
      </div>
    </main>
  );
}
