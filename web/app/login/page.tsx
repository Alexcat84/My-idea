"use client";

/**
 * Login (brief 2.1, remodelado ETAPA 2): pantalla mínima — logo, campo
 * email, frase de producto. Allowlist; el no invitado recibe un mensaje
 * amable, jamás un error técnico.
 *
 * Decisión del fundador (jul 2026): el acceso es por CÓDIGO de 6 dígitos
 * (el correo lo trae vía Resend; el usuario lo escribe aquí). El enlace
 * mágico quedó obsoleto: sin redirects frágiles ni enlaces que caducan.
 */
import { Suspense, useEffect, useRef, useState } from "react";
import { useRouter, useSearchParams } from "next/navigation";

type Estado =
  | { fase: "form"; error?: string }
  | { fase: "codigo"; email: string; error?: string }
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
  // Si Google devolvió un correo que no está invitado, el callback vuelve
  // aquí con ?google=no-invitado: se abre directo la pantalla amable. Con
  // ?desafio=1 (2FA activo), se abre directo el segundo paso.
  const [estado, setEstado] = useState<Estado>(() => {
    if (searchParams.get("google") === "no-invitado") return { fase: "no_invitado" };
    if (searchParams.get("desafio") === "1") {
      return { fase: "desafio", metodo: searchParams.get("metodo") === "email" ? "email" : "totp", rescate: false };
    }
    return { fase: "form" };
  });
  const [email, setEmail] = useState("");
  const [codigo, setCodigo] = useState("");
  const [codigoRescate, setCodigoRescate] = useState("");
  const [enviando, setEnviando] = useState(false);

  // Método email del 2FA: al entrar al desafío se envía el código UNA vez
  // (el botón "Reenviarme el código" cubre los reintentos).
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

  async function enviar(e: React.FormEvent) {
    e.preventDefault();
    if (enviando) return;
    setEnviando(true);
    try {
      const res = await fetch("/api/auth/magic-link", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email }),
      });
      const data = await res.json();
      if (!res.ok) {
        setEstado({ fase: "form", error: data.error ?? "algo se atoró; intenta de nuevo" });
      } else if (!data.invitado) {
        setEstado({ fase: "no_invitado" });
      } else {
        setCodigo("");
        setEstado({ fase: "codigo", email });
      }
    } catch {
      setEstado({ fase: "form", error: "no pudimos conectar; revisa tu internet e intenta de nuevo" });
    } finally {
      setEnviando(false);
    }
  }

  async function verificar(e: React.FormEvent) {
    e.preventDefault();
    if (enviando || estado.fase !== "codigo") return;
    setEnviando(true);
    try {
      const res = await fetch("/api/auth/verificar-codigo", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email: estado.email, codigo }),
      });
      const data = await res.json();
      if (!res.ok) {
        setEstado({ fase: "codigo", email: estado.email, error: data.error ?? "algo se atoró; intenta de nuevo" });
        return;
      }
      // Con 2FA activo, el login sigue con el desafío del segundo factor.
      if (data.requiere2FA) {
        setCodigo("");
        setEstado({ fase: "desafio", metodo: data.metodo === "email" ? "email" : "totp", rescate: false });
        return;
      }
      // Sesión creada (y la cortesía/adopción ya corrieron): a sus ideas.
      router.push("/ideas");
      router.refresh();
    } catch {
      setEstado({ fase: "codigo", email: estado.email, error: "no pudimos conectar; revisa tu internet e intenta de nuevo" });
    } finally {
      setEnviando(false);
    }
  }

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
      router.push("/ideas");
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

  if (estado.fase === "codigo") {
    return (
      <form onSubmit={verificar} className="flex w-full flex-col gap-3 text-center">
        <p className="text-lg">Te enviamos un código a</p>
        <p className="font-semibold">{estado.email}</p>
        <label htmlFor="codigo" className="sr-only">
          Código de 6 dígitos
        </label>
        <input
          id="codigo"
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
        {estado.error && <p className="text-sm text-warn">{estado.error}</p>}
        <button
          type="submit"
          disabled={enviando || codigo.length !== 6}
          className="rounded-cinta bg-accent px-4 py-3 font-medium text-white hover:opacity-90 disabled:opacity-50"
        >
          {enviando ? "Verificando…" : "Entrar"}
        </button>
        <button
          type="button"
          onClick={() => setEstado({ fase: "form" })}
          className="text-sm text-dim hover:text-ink"
        >
          Pedir otro código o cambiar de correo
        </button>
      </form>
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
    return (
      <div className="text-center">
        <p className="text-lg">My Idea está en beta privada.</p>
        <p className="mt-3 text-sm text-dim">
          Ese correo aún no está en la lista de invitados. Si crees que debería estarlo, escríbele a
          quien te compartió el enlace — guardamos tu lugar con gusto.
        </p>
        <button
          onClick={() => setEstado({ fase: "form" })}
          className="mt-6 text-sm text-accent hover:opacity-80"
        >
          Probar con otro correo
        </button>
      </div>
    );
  }

  return (
    <form onSubmit={enviar} className="flex w-full flex-col gap-3">
      {enlaceVencido && (
        <p className="rounded-cinta border border-hairline bg-surface px-4 py-3 text-sm text-warn">
          Ese enlace ya venció o ya se usó. Pide uno nuevo aquí abajo.
        </p>
      )}
      {googleFallo && (
        <p className="rounded-cinta border border-hairline bg-surface px-4 py-3 text-sm text-warn">
          No pudimos completar el acceso con Google. Intenta de nuevo, o entra con tu código.
        </p>
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
      {estado.error && <p className="text-sm text-warn">{estado.error}</p>}
      <button
        type="submit"
        disabled={enviando}
        className="rounded-cinta bg-accent px-4 py-3 font-medium text-white hover:opacity-90 disabled:opacity-50"
      >
        {enviando ? "Enviando…" : "Enviarme mi código de acceso"}
      </button>
      <div className="flex items-center gap-3 py-1 text-xs text-dim" aria-hidden>
        <span className="h-px flex-1 bg-hairline" />
        o
        <span className="h-px flex-1 bg-hairline" />
      </div>
      <a
        href="/api/auth/google"
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
