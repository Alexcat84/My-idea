"use client";

/**
 * El selector de idioma (i18n F3, DISENO §3.2): cada idioma activo con su
 * nombre en su propia escritura. Elegir uno vuelve a pedir la misma página con
 * ?lang=xx; proxy.ts lo negocia y escribe la cookie (D9).
 *
 * Es OPCIONAL (decisión del fundador, 25 sep 2026): el idioma lo pone solo la
 * cookie o el navegador; esto es para cambiarlo a mano. `compacto` es la
 * versión de cabecera, a la derecha de toda pantalla: el globo y el código
 * ("ES"), con el menú nativo encima (al tocarlo se ven los nombres enteros).
 */
import { ACTIVE_LOCALES, elegir, NOMBRE_IDIOMA, type ActiveLocale } from "@/lib/i18n/config";
import { useIdioma } from "@/lib/i18n/IdiomaProvider";
import { SELECTOR_IDIOMA } from "@/lib/i18n/mensajes/selectorIdioma";
import { urlConIdioma } from "@/lib/i18n/selector";

function Globo() {
  return (
    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" aria-hidden>
      <circle cx="12" cy="12" r="9" />
      <path d="M3 12h18M12 3c2.5 2.8 3.8 5.8 3.8 9s-1.3 6.2-3.8 9c-2.5-2.8-3.8-5.8-3.8-9S9.5 5.8 12 3z" />
    </svg>
  );
}

export function SelectorIdioma({
  className,
  style,
  compacto = false,
}: {
  className?: string;
  style?: React.CSSProperties;
  compacto?: boolean;
}) {
  const idioma = useIdioma();
  const t = elegir(SELECTOR_IDIOMA, idioma);
  const cambiar = (e: React.ChangeEvent<HTMLSelectElement>) =>
    window.location.assign(urlConIdioma(window.location.href, e.target.value as ActiveLocale));
  const opciones = ACTIVE_LOCALES.map((l) => (
    <option key={l} value={l} lang={l} style={{ color: "#16171A" }}>
      {NOMBRE_IDIOMA[l]}
    </option>
  ));

  if (compacto) {
    return (
      <label
        title={t.etiqueta}
        className={
          "relative flex h-8 shrink-0 items-center gap-1.5 rounded-full border border-hairline px-2.5 text-[12px] font-semibold uppercase tracking-[0.6px] text-dim hover:border-white/25 hover:text-ink " +
          (className ?? "")
        }
        style={style}
      >
        <Globo />
        {/* En pantallas angostas, solo el globo: el menú dice el resto. */}
        <span aria-hidden className="hidden sm:inline">
          {idioma}
        </span>
        <select
          value={idioma}
          aria-label={t.etiqueta}
          onChange={cambiar}
          className="absolute inset-0 cursor-pointer opacity-0"
        >
          {opciones}
        </select>
      </label>
    );
  }

  return (
    <label className={className} style={{ display: "inline-flex", alignItems: "center", gap: "8px", ...style }}>
      <Globo />
      <select
        value={idioma}
        aria-label={t.etiqueta}
        onChange={cambiar}
        style={{ background: "transparent", color: "inherit", font: "inherit", border: "none", cursor: "pointer" }}
      >
        {opciones}
      </select>
    </label>
  );
}
