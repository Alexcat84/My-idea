"use client";

/**
 * El modal del consentimiento legal versionado (decisión del fundador, 7 oct 2026; equivale a auth/complete-legal y
 * LegalConsentModal de The Original I Ching, adaptado a la casa). Vive en el layout raíz y solo aparece a una CUENTA
 * REAL que no aceptó la versión vigente de los Términos y la Privacidad: tras entrar o registrarse, y otra vez
 * cuando la versión cambia (docs/legal/version.json, la única fuente).
 *
 * Lo que manda en My Idea:
 * - La web es abierta. La identidad invisible jamás lo ve, y no es un muro para usar la app sin cuenta: quien no
 *   acepta puede salir de su cuenta (vuelve a ser visitante) o ir al centro de cuenta a borrarla, donde el modal no
 *   aparece. Tampoco aparece en las páginas legales, en el login ni en los regresos de auth (lib/legal/consentimiento).
 * - Fallar ruidoso, no mentir calladito: solo se cierra cuando el servidor confirma que guardó la aceptación. Si no
 *   se pudo guardar, lo dice y sigue abierto; si no se pudo leer el estado, se pide en vez de suponerlo.
 */
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useEffect, useRef, useState } from "react";
import { elegir } from "@/lib/i18n/config";
import { useIdioma } from "@/lib/i18n/IdiomaProvider";
import { interpolar } from "@/lib/i18n/interpolar";
import { CONSENTIMIENTO } from "@/lib/i18n/mensajes/consentimiento";
import { rico } from "@/lib/i18n/rico";
import { fechaHumanaConAno } from "@/lib/fechas";
import { esInvitadoInvisible } from "@/lib/identidad";
import {
  idiomaTextoLegal,
  rutaSinConsentimiento,
  VERSION_LEGAL,
  type MotivoAceptacion,
} from "@/lib/legal/consentimiento";
import { createClient } from "@/lib/supabase/client";

type Pendiente = { userId: string; motivo: MotivoAceptacion; aviso?: string };

export function ConsentimientoLegal() {
  const idioma = useIdioma();
  const t = elegir(CONSENTIMIENTO, idioma);
  const pathname = usePathname() ?? "/";
  const [pendiente, setPendiente] = useState<Pendiente | null>(null);
  const [marcado, setMarcado] = useState(false);
  const [enviando, setEnviando] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [desactualizado, setDesactualizado] = useState(false);
  const [revision, setRevision] = useState(0);
  // La cuenta que ya confirmó estar al día en esta carga: no se vuelve a preguntar en cada navegación.
  const alDiaPara = useRef<string | null>(null);

  // Entrar, salir o cambiar de cuenta sin recargar la página vuelve a mirar.
  useEffect(() => {
    const { data } = createClient().auth.onAuthStateChange((evento) => {
      if (evento === "SIGNED_IN" || evento === "SIGNED_OUT" || evento === "USER_UPDATED") setRevision((r) => r + 1);
    });
    return () => data.subscription.unsubscribe();
  }, []);

  useEffect(() => {
    if (rutaSinConsentimiento(pathname)) {
      setPendiente(null);
      return;
    }
    let vivo = true;
    void (async () => {
      const {
        data: { session },
      } = await createClient().auth.getSession();
      const user = session?.user;
      // Sin cuenta real (el visitante invisible o sin sesión): nada que pedir, sin llamar al servidor.
      if (!user || esInvitadoInvisible(user)) {
        if (vivo) setPendiente(null);
        return;
      }
      if (alDiaPara.current === user.id) return;
      try {
        const res = await fetch("/api/cuenta/consentimiento", { cache: "no-store" });
        const d = (await res.json().catch(() => ({}))) as { cuenta?: boolean; requiere?: boolean; motivo?: MotivoAceptacion };
        if (!vivo) return;
        if (res.ok && d.cuenta === false) return setPendiente(null);
        if (res.ok && d.requiere === false) {
          alDiaPara.current = user.id;
          return setPendiente(null);
        }
        if (res.ok && d.requiere === true) return setPendiente({ userId: user.id, motivo: d.motivo ?? "primera_aceptacion" });
        // No se pudo saber: se pide, jamás se da por aceptado en silencio.
        setPendiente({ userId: user.id, motivo: "primera_aceptacion", aviso: t.errorEstado });
      } catch {
        if (vivo) setPendiente({ userId: user.id, motivo: "primera_aceptacion", aviso: t.errorEstado });
      }
    })();
    return () => {
      vivo = false;
    };
    // `t` cambia con el idioma; el texto del aviso no justifica volver a preguntar.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [pathname, revision]);

  if (!pendiente) return null;

  async function aceptar() {
    if (!pendiente || enviando) return;
    if (desactualizado) {
      // El navegador tiene una versión vieja de los textos: se recarga para traer la vigente.
      window.location.reload();
      return;
    }
    setEnviando(true);
    setError(null);
    try {
      const res = await fetch("/api/cuenta/consentimiento", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ version: VERSION_LEGAL, idioma_texto: idiomaTextoLegal(idioma) }),
      });
      const d = (await res.json().catch(() => ({}))) as { ok?: boolean; error?: string };
      if (res.status === 409) {
        setDesactualizado(true);
        setMarcado(false);
        setError(t.versionCambio);
        return;
      }
      if (!res.ok || d.ok !== true) {
        setError(d.error ?? t.errorGuardar);
        return;
      }
      alDiaPara.current = pendiente.userId;
      setPendiente(null);
      setMarcado(false);
    } catch {
      setError(t.errorGuardar);
    } finally {
      setEnviando(false);
    }
  }

  async function salir() {
    setEnviando(true);
    try {
      await createClient().auth.signOut();
    } finally {
      // A la landing: sin cuenta, la web sigue abierta (vuelve la identidad invisible).
      window.location.assign("/");
    }
  }

  const enlaces = {
    terminos: (c: React.ReactNode) => (
      <a href="/terminos" target="_blank" rel="noopener" className="text-accent underline underline-offset-2">
        {c}
      </a>
    ),
    privacidad: (c: React.ReactNode) => (
      <a href="/privacidad" target="_blank" rel="noopener" className="text-accent underline underline-offset-2">
        {c}
      </a>
    ),
  };
  const nueva = pendiente.motivo === "nueva_version";
  const fechaVersion = /^\d{4}-\d{2}-\d{2}$/.test(VERSION_LEGAL)
    ? fechaHumanaConAno(`${VERSION_LEGAL}T12:00:00`, idioma)
    : VERSION_LEGAL;

  return (
    <div className="fixed inset-0 z-[60] flex items-center justify-center bg-black/75 px-4" role="presentation">
      <section
        role="dialog"
        aria-modal="true"
        aria-labelledby="consentimiento-titulo"
        aria-describedby="consentimiento-intro"
        className="w-full max-w-md rounded-cinta border border-hairline bg-surface p-6 text-ink shadow-2xl"
      >
        <h2 id="consentimiento-titulo" className="text-lg font-semibold">
          {nueva ? t.tituloNueva : t.tituloPrimera}
        </h2>
        <p id="consentimiento-intro" className="mt-3 text-sm text-dim">
          {rico(nueva ? t.introNueva : t.introPrimera, enlaces)}
        </p>
        <p className="mt-2 text-xs text-dim">
          {interpolar(t.version, { version: fechaVersion })}
          {idioma !== idiomaTextoLegal(idioma) && <> · {t.soloEsFr}</>}
        </p>
        {pendiente.aviso && !error && <p className="mt-3 text-sm text-warn">{pendiente.aviso}</p>}

        <label className="mt-5 flex cursor-pointer items-start gap-3 text-sm">
          <input
            type="checkbox"
            autoFocus
            checked={marcado}
            disabled={enviando || desactualizado}
            onChange={(e) => setMarcado(e.target.checked)}
            className="mt-0.5 h-4 w-4"
          />
          <span>{t.casilla}</span>
        </label>

        {error && (
          <p className="mt-3 text-sm text-warn" role="alert">
            {error}
          </p>
        )}

        <button
          type="button"
          onClick={aceptar}
          disabled={enviando || (!marcado && !desactualizado)}
          className="mt-5 w-full rounded-cinta border border-accent/40 bg-accent/10 px-4 py-3 font-medium text-accent hover:bg-accent/20 disabled:opacity-50"
        >
          {enviando ? t.guardando : t.aceptar}
        </button>

        <div className="mt-4 flex flex-wrap items-center justify-between gap-2 text-sm">
          <button type="button" onClick={salir} disabled={enviando} className="text-dim hover:text-ink disabled:opacity-50">
            {t.salir}
          </button>
          <Link href="/cuenta" className="text-dim hover:text-ink">
            {t.borrar}
          </Link>
        </div>
      </section>
    </div>
  );
}
