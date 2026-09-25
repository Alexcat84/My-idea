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
import { elegir } from "@/lib/i18n/config";
import { useIdioma } from "@/lib/i18n/IdiomaProvider";
import { interpolar } from "@/lib/i18n/interpolar";
import { CUENTA } from "@/lib/i18n/mensajes/cuenta";
import { rico } from "@/lib/i18n/rico";
import { palabraEliminar } from "@/lib/i18n/palabraEliminar";
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

/** Zona de peligro: lo irreversible se ve distinto desde lejos. Ámbar (la
 * casa no usa rojo), borde y encabezado marcados, con su ícono de aviso. */
function ZonaDePeligro({ children }: { children: React.ReactNode }) {
  const t = elegir(CUENTA, useIdioma());
  return (
    <section className="mt-10 rounded-panel border border-warn/40 bg-warn/[0.04] px-5 py-5 sm:px-6">
      <h2 className="flex items-center gap-2 text-[11px] font-semibold uppercase tracking-[1.2px] text-warn">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round" aria-hidden>
          <path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z" />
          <path d="M12 9v4" />
          <path d="M12 17h.01" />
        </svg>
        {t.peligro.titulo}
      </h2>
      <div className="mt-3">{children}</div>
    </section>
  );
}

export function CuentaCliente({ email }: { email: string }) {
  const idioma = useIdioma();
  const t = elegir(CUENTA, idioma);
  // La palabra que confirma el borrado: un DATO que /api/cuenta/eliminar
  // compara, en el idioma de la interfaz (lib/i18n/palabraEliminar).
  const PALABRA_CONFIRMAR = palabraEliminar(idioma);
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
        setAvisoSeguridad(String(data.error ?? t.errores.atoro));
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
        setFlujo({ ...flujo, error: String(data.error ?? t.errores.atoro) });
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
        setAvisoSeguridad(String(data.error ?? t.errores.enviarCodigo));
        return;
      }
      setCodigo2FA("");
      setFlujo({ paso: "email_codigo", aviso: interpolar(t.codigoEnviadoA, { email }) });
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
        setFlujo({ ...flujo, error: String(data.error ?? t.errores.atoro) });
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
            ? t.errores.desactivarSinDesafio
            : String(data.error ?? t.errores.atoro)
        );
        return;
      }
      setSeguridad({ habilitado: false, metodo: null, desafioSuperado: true });
      setFlujo({ paso: "reposo" });
      setAvisoSeguridad(t.desactivada);
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
        setErrorCuenta(String(data.error ?? t.errores.atoro));
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
      <Seccion titulo={t.tuIdentidad}>
        <p className="text-[15px] font-semibold">{email}</p>
      </Seccion>

      <Seccion titulo={t.seguridad.titulo}>
        {seguridad === null ? (
          <p className="text-sm text-dim">{t.seguridad.leyendo}</p>
        ) : flujo.paso === "rescate" ? (
          <div>
            <p className="text-[15px] font-semibold text-done">{t.seguridad.activadaCompleta}</p>
            <p className="mt-2 text-sm text-dim">{t.seguridad.guardaRescate}</p>
            <div className="mt-3 grid grid-cols-2 gap-2 sm:grid-cols-4">
              {flujo.codigos.map((c) => (
                <code key={c} className="rounded-cinta border border-hairline bg-surface-2 px-2 py-1.5 text-center font-mono text-[13px]">
                  {c}
                </code>
              ))}
            </div>
            <button
              onClick={() => setFlujo({ paso: "reposo" })}
              className="mt-4 rounded-cinta border border-accent/40 bg-accent/10 px-4 py-2.5 text-sm font-medium text-accent hover:bg-accent/20"
            >
              {t.seguridad.yaGuarde}
            </button>
          </div>
        ) : seguridad.habilitado ? (
          <div>
            <p className="text-[15px]">
              <span className="font-semibold text-done">{t.seguridad.activada}</span>
              <span className="text-dim">
                {" "}
                · {seguridad.metodo === "email" ? t.seguridad.codigoPorCorreo : t.seguridad.appAutenticacion}
              </span>
            </p>
            <p className="mt-1 text-sm text-dim">
              {interpolar(t.seguridad.alEntrar, {
                que: seguridad.metodo === "email" ? t.seguridad.unCodigoCorreo : t.seguridad.elCodigoApp,
              })}
            </p>
            {avisoSeguridad && <p className="mt-2 text-sm text-warn">{avisoSeguridad}</p>}
            <button
              onClick={desactivar2FA}
              disabled={ocupado}
              className="mt-3 text-sm text-dim underline-offset-2 hover:text-ink hover:underline disabled:opacity-50"
            >
              {t.seguridad.desactivar}
            </button>
          </div>
        ) : flujo.paso === "totp_qr" ? (
          <form onSubmit={verificarTotp}>
            <p className="text-sm text-dim">
              {t.seguridad.pasoEscanear}
            </p>
            {/* El QR es un data URI generado por el servidor (lib qrcode) */}
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img src={flujo.qrDataUrl} alt={t.seguridad.altQr} className="mt-3 h-[210px] w-[210px] rounded-cinta border border-hairline bg-white p-2" />
            <p className="mt-3 text-sm text-dim">{t.seguridad.pasoEscribir}</p>
            <div className="mt-2 flex items-center gap-3">
              {inputCodigo}
              <button
                type="submit"
                disabled={ocupado || codigo2FA.length !== 6}
                className="rounded-cinta border border-accent/40 bg-accent/10 px-4 py-2.5 text-sm font-medium text-accent hover:bg-accent/20 disabled:opacity-50"
              >
                {ocupado ? t.seguridad.verificando : t.seguridad.activar}
              </button>
              <button type="button" onClick={() => setFlujo({ paso: "reposo" })} className="rounded-cinta border border-accent/40 bg-accent/10 text-accent hover:bg-accent/20 px-4 py-2.5 text-sm font-medium">
                {t.seguridad.cancelar}
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
                className="rounded-cinta border border-accent/40 bg-accent/10 px-4 py-2.5 text-sm font-medium text-accent hover:bg-accent/20 disabled:opacity-50"
              >
                {ocupado ? t.seguridad.verificando : t.seguridad.activar}
              </button>
              <button type="button" onClick={() => setFlujo({ paso: "reposo" })} className="rounded-cinta border border-accent/40 bg-accent/10 text-accent hover:bg-accent/20 px-4 py-2.5 text-sm font-medium">
                {t.seguridad.cancelar}
              </button>
            </div>
            {flujo.error && <p className="mt-2 text-sm text-warn">{flujo.error}</p>}
          </form>
        ) : (
          <div>
            <p className="text-sm text-dim">
              {t.seguridad.queHace}
            </p>
            {avisoSeguridad && <p className="mt-2 text-sm text-warn">{avisoSeguridad}</p>}
            <div className="mt-3 flex flex-wrap gap-3">
              <button
                onClick={empezarTotp}
                disabled={ocupado}
                className="rounded-cinta border border-accent/40 px-4 py-2.5 text-sm font-medium text-accent hover:border-accent/70 disabled:opacity-50"
              >
                {t.seguridad.activarApp}
              </button>
              <button
                onClick={empezarEmail}
                disabled={ocupado}
                className="rounded-cinta border border-hairline px-4 py-2.5 text-sm font-medium text-ink hover:border-white/25 disabled:opacity-50"
              >
                {t.seguridad.activarCorreo}
              </button>
            </div>
          </div>
        )}
      </Seccion>

      <ZonaDePeligro>
        <p className="text-[15px] font-semibold text-ink">{t.peligro.borrarTuCuenta}</p>
        <p className="mt-1.5 text-sm text-dim">
          {rico(t.peligro.borrarTexto, {
            palabra: () => <span className="font-mono font-semibold text-warn">{PALABRA_CONFIRMAR}</span>,
          })}
        </p>
        {/* Un solo botón accionable: el campo es campo (etiqueta arriba,
            texto a la izquierda) y el botón es el único que se pulsa. */}
        <form onSubmit={borrarCuenta} className="mt-4 flex flex-col items-start gap-2">
          <label htmlFor="confirmar-eliminar" className="text-xs text-dim">
            {t.peligro.etiquetaPalabra}
          </label>
          <input
            id="confirmar-eliminar"
            value={palabraCuenta}
            onChange={(e) => setPalabraCuenta(e.target.value.toUpperCase())}
            placeholder={PALABRA_CONFIRMAR}
            autoComplete="off"
            className="w-full max-w-[260px] rounded-cinta border border-hairline bg-surface-2 px-4 py-2.5 text-left font-mono text-sm tracking-widest text-ink placeholder:text-dim/40"
          />
          <button
            type="submit"
            disabled={ocupado || palabraCuenta.trim() !== PALABRA_CONFIRMAR}
            className="mt-2 rounded-cinta border border-warn/50 px-4 py-2.5 text-sm font-semibold text-warn hover:border-warn disabled:opacity-40"
          >
            {t.peligro.borrarParaSiempre}
          </button>
        </form>
        {errorCuenta && <p className="mt-2 text-sm text-warn">{errorCuenta}</p>}
      </ZonaDePeligro>
    </>
  );
}
