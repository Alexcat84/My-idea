"use client";

/**
 * El selector de idioma (i18n F3, DISENO §3.2): cada idioma activo con su
 * nombre en su propia escritura. Elegir uno vuelve a pedir la misma página con
 * ?lang=xx; proxy.ts lo negocia y escribe la cookie (D9).
 */
import { ACTIVE_LOCALES, elegir, NOMBRE_IDIOMA, type ActiveLocale } from "@/lib/i18n/config";
import { useIdioma } from "@/lib/i18n/IdiomaProvider";
import { SELECTOR_IDIOMA } from "@/lib/i18n/mensajes/selectorIdioma";
import { urlConIdioma } from "@/lib/i18n/selector";

export function SelectorIdioma({ className, style }: { className?: string; style?: React.CSSProperties }) {
  const idioma = useIdioma();
  const t = elegir(SELECTOR_IDIOMA, idioma);
  return (
    <label className={className} style={{ display: "inline-flex", alignItems: "center", gap: "8px", ...style }}>
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" aria-hidden>
        <circle cx="12" cy="12" r="9" />
        <path d="M3 12h18M12 3c2.5 2.8 3.8 5.8 3.8 9s-1.3 6.2-3.8 9c-2.5-2.8-3.8-5.8-3.8-9S9.5 5.8 12 3z" />
      </svg>
      <select
        value={idioma}
        aria-label={t.etiqueta}
        onChange={(e) => window.location.assign(urlConIdioma(window.location.href, e.target.value as ActiveLocale))}
        style={{ background: "transparent", color: "inherit", font: "inherit", border: "none", cursor: "pointer" }}
      >
        {ACTIVE_LOCALES.map((l) => (
          <option key={l} value={l} lang={l} style={{ color: "#16171A" }}>
            {NOMBRE_IDIOMA[l]}
          </option>
        ))}
      </select>
    </label>
  );
}
