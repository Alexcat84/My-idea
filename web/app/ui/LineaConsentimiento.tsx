"use client";

/**
 * La línea del consentimiento junto al botón del primer envío de datos (corrección del fundador, 7 oct 2026): "Al
 * continuar, aceptas los Términos y la Política de Privacidad", con sus enlaces. No es un diálogo ni tapa nada: es una
 * línea en el flujo de la página. Los enlaces abren en otra pestaña para que la idea escrita no se pierda. Si los
 * textos cambiaron desde la última aceptación, la línea lo dice (`motivo` = nueva_version).
 */
import { elegir } from "@/lib/i18n/config";
import { useIdioma } from "@/lib/i18n/IdiomaProvider";
import { CONSENTIMIENTO } from "@/lib/i18n/mensajes/consentimiento";
import { rico } from "@/lib/i18n/rico";
import type { MotivoAceptacion } from "@/lib/legal/consentimiento";

export function LineaConsentimiento({ motivo, className = "" }: { motivo: MotivoAceptacion; className?: string }) {
  const t = elegir(CONSENTIMIENTO, useIdioma()).envio;
  return (
    <p className={`text-xs leading-[1.6] text-dim ${className}`}>
      {rico(motivo === "nueva_version" ? t.lineaNueva : t.linea, {
        terminos: (c) => (
          <a href="/terminos" target="_blank" rel="noopener" className="text-accent underline underline-offset-2">
            {c}
          </a>
        ),
        privacidad: (c) => (
          <a href="/privacidad" target="_blank" rel="noopener" className="text-accent underline underline-offset-2">
            {c}
          </a>
        ),
      })}
    </p>
  );
}
