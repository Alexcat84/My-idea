"use client";

/**
 * El consentimiento en el primer envío de datos, lado pantalla (corrección del fundador, 7 oct 2026). Pregunta al
 * servidor si quien está aquí (la identidad invisible o una cuenta) ya aceptó la versión vigente de los Términos y la
 * Privacidad, para pintar la línea "Al continuar, aceptas..." y el botón "Aceptar y generar"; y guarda la aceptación
 * ANTES de que la pantalla envíe nada. No decide nada por su cuenta: la guarda de verdad está en el servidor
 * (lib/legal/aceptacionServidor.ts), que rechaza el envío sin aceptación registrada.
 *
 * Fallar ruidoso: mientras no se sabe, o si no se pudo saber, se pide (nunca se supone aceptado); si guardar falla,
 * `aceptar` lo dice y la pantalla no envía nada.
 */
import { useCallback, useEffect, useState } from "react";
import { elegir, type Locale } from "@/lib/i18n/config";
import { CONSENTIMIENTO } from "@/lib/i18n/mensajes/consentimiento";
import { idiomaTextoLegal, VERSION_LEGAL, type MotivoAceptacion } from "./consentimiento";

export type ResultadoAceptar = { ok: true } | { ok: false; error: string };

/** `consultarAlMontar: false` (La Exploración): no pregunta al cargar; solo pide la aceptación si el servidor rechaza
 * un envío con 428 (`pedirDeNuevo`). */
export function useConsentimiento(idioma: Locale, { consultarAlMontar = true }: { consultarAlMontar?: boolean } = {}) {
  const [requiere, setRequiere] = useState(consultarAlMontar);
  const [motivo, setMotivo] = useState<MotivoAceptacion>("primera_aceptacion");

  useEffect(() => {
    if (!consultarAlMontar) return;
    let vivo = true;
    fetch("/api/cuenta/consentimiento", { cache: "no-store" })
      .then(async (res) => {
        const d = (await res.json().catch(() => ({}))) as { requiere?: boolean; motivo?: MotivoAceptacion };
        if (!vivo) return;
        if (res.ok && d.requiere === false) return setRequiere(false);
        if (d.motivo === "nueva_version") setMotivo("nueva_version");
      })
      .catch(() => {
        // Sin respuesta: la línea se queda y la aceptación se guarda al enviar.
      });
    return () => {
      vivo = false;
    };
  }, [consultarAlMontar]);

  /** El servidor dijo que falta la aceptación (un 428 del envío): vuelve a pedirla con su motivo. */
  const pedirDeNuevo = useCallback((m: MotivoAceptacion) => {
    setMotivo(m);
    setRequiere(true);
  }, []);

  /** Guarda la aceptación de la versión vigente. Solo devuelve ok si el servidor confirmó que la guardó. */
  const aceptar = useCallback(async (): Promise<ResultadoAceptar> => {
    const t = elegir(CONSENTIMIENTO, idioma).envio;
    try {
      const res = await fetch("/api/cuenta/consentimiento", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ version: VERSION_LEGAL, idioma_texto: idiomaTextoLegal(idioma) }),
      });
      const d = (await res.json().catch(() => ({}))) as { ok?: boolean; error?: string };
      // 409: este navegador trae una versión vieja de los textos; hay que recargar para ver la vigente.
      if (res.status === 409) return { ok: false, error: t.versionCambio };
      if (!res.ok || d.ok !== true) return { ok: false, error: d.error ?? t.errorGuardar };
      setRequiere(false);
      return { ok: true };
    } catch {
      return { ok: false, error: t.errorGuardar };
    }
  }, [idioma]);

  return { requiere, motivo, aceptar, pedirDeNuevo };
}
