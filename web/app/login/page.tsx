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
import { Suspense, useState } from "react";
import { useRouter, useSearchParams } from "next/navigation";

type Estado =
  | { fase: "form"; error?: string }
  | { fase: "codigo"; email: string; error?: string }
  | { fase: "no_invitado" };

function LoginForm() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const enlaceVencido = searchParams.get("enlace") === "vencido";
  const [estado, setEstado] = useState<Estado>({ fase: "form" });
  const [email, setEmail] = useState("");
  const [codigo, setCodigo] = useState("");
  const [enviando, setEnviando] = useState(false);

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
      // Sesión creada (y la cortesía/adopción ya corrieron): a sus ideas.
      router.push("/ideas");
      router.refresh();
    } catch {
      setEstado({ fase: "codigo", email: estado.email, error: "no pudimos conectar; revisa tu internet e intenta de nuevo" });
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
    </form>
  );
}

export default function LoginPage() {
  return (
    <main className="flex flex-1 items-center justify-center px-6">
      <div className="flex w-full max-w-sm flex-col items-center gap-8 py-16">
        <div className="text-center">
          <h1 className="text-3xl font-semibold tracking-tight">My Idea</h1>
          <p className="mt-2 text-dim">El espacio donde tus ideas se trabajan.</p>
        </div>
        <Suspense>
          <LoginForm />
        </Suspense>
      </div>
    </main>
  );
}
