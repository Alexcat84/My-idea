"use client";

/**
 * CuentaCliente — el centro de cuenta = SOLO opciones de cuenta (sin mezclar
 * procesos, regla del fundador): identidad, seguridad en dos pasos (TOTP con
 * QR o código por correo; rescates mostrados UNA sola vez) y borrar la cuenta
 * escribiendo ELIMINAR. Los créditos viven en /creditos y las ideas en
 * /ideas: aquí no aparecen. Estado-sin-vara: canon del encargo de Design.
 */
import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { createClient } from "@/lib/supabase/client";

type Flujo2FA =
  | { paso: "reposo" }
  | { paso: "totp_qr"; qrDataUrl: string; error?: string }
  | { paso: "email_codigo"; aviso: string; error?: string }
  | { paso: "rescate"; codigos: string[] };

interface Seguridad {
  habilitado: boolean;
  metodo: "totp" | "email" | null;
  desafioSuperado: boolean;
}

function Seccion({ titulo, children }: { titulo: string; children: React.ReactNode }) {
  return (
    <section className="mt-8 rounded-panel border border-hairline bg-surface px-5 py-5 sm:px-6">
      <h2 className="text-[11px] font-semibold uppercase tracking-[1.2px] text-dim">{titulo}</h2>
      <div className="mt-3">{children}</div>
    </section>
  );
}

export function CuentaCliente({
  email,
  proveedores,
}: {
  email: string;
  proveedores: string[];
}) {
  const router = useRouter();
  const [seguridad, setSeguridad] = useState<Seguridad | null>(null);
  const [flujo, setFlujo] = useState<Flujo2FA>({ paso: "reposo" });
  const [codigo2FA, setCodigo2FA] = useState("");
  const [ocupado, setOcupado] = useState(false);
  const [avisoSeguridad, setAvisoSeguridad] = useState<string | null>(null);
  const [palabraCuenta, setPalabraCuenta] = useState("");
  const [errorCuenta, setErrorCuenta] = useState<string | null>(null);

  useEffect(() => {
    fetch("/api/cuenta/seguridad")
      .then((r) => (r.ok ? r.json() : null))
      .then((d) => {
        if (d && !d.invisible) {
          setSeguridad({ habilitado: d.habilitado, metodo: d.metodo, desafioSuperado: d.desafioSuperado });
        }
      })
      .catch(() => {});
  }, []);

  async function llamar(url: string, body?: unknown): Promise<{ ok: boolean; data: Record<string, unknown> }> {
    const res = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: body === undefined ? undefined : JSON.stringify(body),
    });
    const data = (await res.json().catch(() => ({}))) as Record<string, unknown>;
    return { ok: res.ok, data };
  }

  // ── Seguridad: alta TOTP ─────────────────────────────────────────────

  async function empezarTotp() {
    if (ocupado) return;
    setOcupado(true);
    setAvisoSeguridad(null);
    try {
      const { ok, data } = await llamar("/api/cuenta/2fa/enroll");
      if (!ok || typeof data.qrDataUrl !== "string") {
        setAvisoSeguridad(String(data.error ?? "algo se atoró; intenta de nuevo"));
        return;
      }
      setCodigo2FA("");
      setFlujo({ paso: "totp_qr", qrDataUrl: data.qrDataUrl });
    } finally {
      setOcupado(false);
    }
  }

  async function verificarTotp(e: React.FormEvent) {
    e.preventDefault();
    if (ocupado || flujo.paso !== "totp_qr") return;
    setOcupado(true);
    try {
      const { ok, data } = await llamar("/api/cuenta/2fa/verificar", { token: codigo2FA });
      if (!ok || !Array.isArray(data.recoveryCodes)) {
        setFlujo({ ...flujo, error: String(data.error ?? "algo se atoró; intenta de nuevo") });
        return;
      }
      setSeguridad({ habilitado: true, metodo: "totp", desafioSuperado: true });
      setFlujo({ paso: "rescate", codigos: data.recoveryCodes as string[] });
    } finally {
      setOcupado(false);
    }
  }

  // ── Seguridad: alta por correo ───────────────────────────────────────

  async function empezarEmail() {
    if (ocupado) return;
    setOcupado(true);
    setAvisoSeguridad(null);
    try {
      const { ok, data } = await llamar("/api/cuenta/2fa/email/enviar");
      if (!ok) {
        setAvisoSeguridad(String(data.error ?? "no pudimos enviar el código; intenta de nuevo"));
        return;
      }
      setCodigo2FA("");
      setFlujo({ paso: "email_codigo", aviso: `Te enviamos un código a ${email}.` });
    } finally {
      setOcupado(false);
    }
  }

  async function verificarEmail(e: React.FormEvent) {
    e.preventDefault();
    if (ocupado || flujo.paso !== "email_codigo") return;
    setOcupado(true);
    try {
      const { ok, data } = await llamar("/api/cuenta/2fa/email/verificar", { code: codigo2FA });
      if (!ok || !Array.isArray(data.recoveryCodes)) {
        setFlujo({ ...flujo, error: String(data.error ?? "algo se atoró; intenta de nuevo") });
        return;
      }
      setSeguridad({ habilitado: true, metodo: "email", desafioSuperado: true });
      setFlujo({ paso: "rescate", codigos: data.recoveryCodes as string[] });
    } finally {
      setOcupado(false);
    }
  }

  async function desactivar2FA() {
    if (ocupado) return;
    setOcupado(true);
    setAvisoSeguridad(null);
    try {
      const { ok, data } = await llamar("/api/cuenta/2fa/desactivar");
      if (!ok) {
        setAvisoSeguridad(
          data.segundo_factor_requerido
            ? "Para desactivarla, vuelve a entrar y supera el desafío primero."
            : String(data.error ?? "algo se atoró; intenta de nuevo")
        );
        return;
      }
      setSeguridad({ habilitado: false, metodo: null, desafioSuperado: true });
      setFlujo({ paso: "reposo" });
      setAvisoSeguridad("Verificación en dos pasos desactivada.");
    } finally {
      setOcupado(false);
    }
  }

  // ── Borrar la cuenta ─────────────────────────────────────────────────

  async function borrarCuenta(e: React.FormEvent) {
    e.preventDefault();
    if (ocupado) return;
    setOcupado(true);
    setErrorCuenta(null);
    try {
      const { ok, data } = await llamar("/api/cuenta/eliminar", { confirmacion: palabraCuenta });
      if (!ok) {
        setErrorCuenta(String(data.error ?? "algo se atoró; intenta de nuevo"));
        return;
      }
      // La cuenta ya no existe: limpiar la sesión local y a la landing.
      await createClient().auth.signOut().catch(() => {});
      router.push("/");
      router.refresh();
    } finally {
      setOcupado(false);
    }
  }

  const inputCodigo = (
    <input
      inputMode="numeric"
      pattern="[0-9]{6}"
      maxLength={6}
      required
      autoFocus
      placeholder="······"
      value={codigo2FA}
      onChange={(e) => setCodigo2FA(e.target.value.replace(/\D/g, ""))}
      className="w-44 rounded-cinta border border-hairline bg-surface-2 px-4 py-2.5 text-center text-xl font-bold tracking-[0.4em] text-ink placeholder:text-dim"
    />
  );

  return (
    <>
      <Seccion titulo="Tu identidad">
        <p className="text-[15px] font-semibold">{email}</p>
        <p className="mt-1 text-sm text-dim">
          Entras con {proveedores.length > 0 ? proveedores.join(" y ") : "correo"}.
        </p>
      </Seccion>

      <Seccion titulo="Seguridad · verificación en dos pasos">
        {seguridad === null ? (
          <p className="text-sm text-dim">Leyendo el estado de tu seguridad…</p>
        ) : flujo.paso === "rescate" ? (
          <div>
            <p className="text-[15px] font-semibold text-done">Verificación en dos pasos activada.</p>
            <p className="mt-2 text-sm text-dim">
              Guarda estos códigos de rescate en un lugar seguro. Cada uno abre tu cuenta UNA vez si pierdes tu
              método habitual, y no volverán a mostrarse.
            </p>
            <div className="mt-3 grid grid-cols-2 gap-2 sm:grid-cols-4">
              {flujo.codigos.map((c) => (
                <code key={c} className="rounded-cinta border border-hairline bg-surface-2 px-2 py-1.5 text-center font-mono text-[13px]">
                  {c}
                </code>
              ))}
            </div>
            <button
              onClick={() => setFlujo({ paso: "reposo" })}
              className="mt-4 rounded-cinta bg-accent px-4 py-2.5 text-sm font-medium text-white hover:opacity-90"
            >
              Ya los guardé
            </button>
          </div>
        ) : seguridad.habilitado ? (
          <div>
            <p className="text-[15px]">
              <span className="font-semibold text-done">Activada</span>
              <span className="text-dim">
                {" "}
                · {seguridad.metodo === "email" ? "código por correo" : "app de autenticación"}
              </span>
            </p>
            <p className="mt-1 text-sm text-dim">
              Al entrar, además de tu acceso normal te pediremos{" "}
              {seguridad.metodo === "email" ? "un código que llega a tu correo" : "el código de tu app"}.
            </p>
            {avisoSeguridad && <p className="mt-2 text-sm text-warn">{avisoSeguridad}</p>}
            <button
              onClick={desactivar2FA}
              disabled={ocupado}
              className="mt-3 text-sm text-dim underline-offset-2 hover:text-ink hover:underline disabled:opacity-50"
            >
              Desactivar la verificación en dos pasos
            </button>
          </div>
        ) : flujo.paso === "totp_qr" ? (
          <form onSubmit={verificarTotp}>
            <p className="text-sm text-dim">
              1. Escanea este código con tu app de autenticación (Google Authenticator, 1Password, Authy…).
            </p>
            {/* El QR es un data URI generado por el servidor (lib qrcode) */}
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img src={flujo.qrDataUrl} alt="Código QR para tu app de autenticación" className="mt-3 h-[210px] w-[210px] rounded-cinta border border-hairline bg-white p-2" />
            <p className="mt-3 text-sm text-dim">2. Escribe el código de 6 dígitos que te muestra la app.</p>
            <div className="mt-2 flex items-center gap-3">
              {inputCodigo}
              <button
                type="submit"
                disabled={ocupado || codigo2FA.length !== 6}
                className="rounded-cinta bg-accent px-4 py-2.5 text-sm font-medium text-white hover:opacity-90 disabled:opacity-50"
              >
                {ocupado ? "Verificando…" : "Activar"}
              </button>
              <button type="button" onClick={() => setFlujo({ paso: "reposo" })} className="text-sm text-dim hover:text-ink">
                Cancelar
              </button>
            </div>
            {flujo.error && <p className="mt-2 text-sm text-warn">{flujo.error}</p>}
          </form>
        ) : flujo.paso === "email_codigo" ? (
          <form onSubmit={verificarEmail}>
            <p className="text-sm text-dim">{flujo.aviso}</p>
            <div className="mt-2 flex items-center gap-3">
              {inputCodigo}
              <button
                type="submit"
                disabled={ocupado || codigo2FA.length !== 6}
                className="rounded-cinta bg-accent px-4 py-2.5 text-sm font-medium text-white hover:opacity-90 disabled:opacity-50"
              >
                {ocupado ? "Verificando…" : "Activar"}
              </button>
              <button type="button" onClick={() => setFlujo({ paso: "reposo" })} className="text-sm text-dim hover:text-ink">
                Cancelar
              </button>
            </div>
            {flujo.error && <p className="mt-2 text-sm text-warn">{flujo.error}</p>}
          </form>
        ) : (
          <div>
            <p className="text-sm text-dim">
              Un segundo paso al entrar protege tu cuenta. Es opcional y puedes apagarlo cuando quieras.
            </p>
            {avisoSeguridad && <p className="mt-2 text-sm text-warn">{avisoSeguridad}</p>}
            <div className="mt-3 flex flex-wrap gap-3">
              <button
                onClick={empezarTotp}
                disabled={ocupado}
                className="rounded-cinta border border-accent/40 px-4 py-2.5 text-sm font-medium text-accent hover:border-accent/70 disabled:opacity-50"
              >
                Activar con app de autenticación
              </button>
              <button
                onClick={empezarEmail}
                disabled={ocupado}
                className="rounded-cinta border border-hairline px-4 py-2.5 text-sm font-medium text-ink hover:border-white/25 disabled:opacity-50"
              >
                Activar con código por correo
              </button>
            </div>
          </div>
        )}
      </Seccion>

      <Seccion titulo="Borrar tu cuenta">
        <p className="text-sm text-dim">
          Se borra todo: tus ideas, tus planes, tu historial y tus créditos. No hay vuelta atrás. Para confirmar,
          escribe <span className="font-mono font-semibold text-warn">ELIMINAR</span>.
        </p>
        <form onSubmit={borrarCuenta} className="mt-3 flex flex-wrap items-center gap-3">
          <input
            value={palabraCuenta}
            onChange={(e) => setPalabraCuenta(e.target.value.toUpperCase())}
            placeholder="ELIMINAR"
            className="w-44 rounded-cinta border border-hairline bg-surface-2 px-4 py-2.5 text-center font-mono text-sm tracking-widest text-ink placeholder:text-dim"
          />
          <button
            type="submit"
            disabled={ocupado || palabraCuenta.trim() !== "ELIMINAR"}
            className="rounded-cinta border border-warn/50 px-4 py-2.5 text-sm font-semibold text-warn hover:border-warn disabled:opacity-40"
          >
            Borrar mi cuenta para siempre
          </button>
        </form>
        {errorCuenta && <p className="mt-2 text-sm text-warn">{errorCuenta}</p>}
      </Seccion>
    </>
  );
}
