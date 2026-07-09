"use client";

/**
 * Login (brief 2.1): pantalla mínima — logo, campo email, frase de
 * producto. Magic link con allowlist; el no invitado recibe un mensaje
 * amable, jamás un error técnico.
 */
import { Suspense, useState } from "react";
import { useSearchParams } from "next/navigation";

type Estado =
  | { fase: "form"; error?: string }
  | { fase: "enviado"; email: string }
  | { fase: "no_invitado" };

function LoginForm() {
  const searchParams = useSearchParams();
  const enlaceVencido = searchParams.get("enlace") === "vencido";
  const [estado, setEstado] = useState<Estado>({ fase: "form" });
  const [email, setEmail] = useState("");
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
        setEstado({ fase: "enviado", email });
      }
    } catch {
      setEstado({ fase: "form", error: "no pudimos conectar; revisa tu internet e intenta de nuevo" });
    } finally {
      setEnviando(false);
    }
  }

  if (estado.fase === "enviado") {
    return (
      <div className="text-center">
        <p className="text-lg">Te enviamos un enlace a</p>
        <p className="mt-1 font-semibold">{estado.email}</p>
        <p className="mt-4 text-sm text-dim">
          Ábrelo desde este dispositivo para entrar. Puede tardar un minuto en llegar.
        </p>
      </div>
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
        {enviando ? "Enviando…" : "Enviarme el enlace de acceso"}
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
