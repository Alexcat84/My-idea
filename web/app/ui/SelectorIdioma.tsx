"use client";

/**
 * El selector de idioma (i18n F3, DISENO §3.2): cada idioma activo con su
 * nombre en su propia escritura. Elegir uno vuelve a pedir la misma página con
 * ?lang=xx; proxy.ts lo negocia y escribe la cookie (D9).
 *
 * Es OPCIONAL (decisión del fundador, 25 sep 2026): el idioma lo pone solo la
 * cookie o el navegador; esto es para cambiarlo a mano. `compacto` es la
 * versión de cabecera, a la derecha de toda pantalla: el globo y el código
 * ("ES"), sin recuadro.
 *
 * La lista es PROPIA, no el <select> del sistema (pedido del fundador, 25 sep
 * 2026): el menú nativo se abría como un rectángulo blanco que ignoraba el tema
 * oscuro. Botón + listbox con teclado (flechas, Enter, Escape) y cierre al
 * tocar fuera.
 */
import { useEffect, useId, useRef, useState } from "react";
import { ACTIVE_LOCALES, elegir, NOMBRE_IDIOMA, type ActiveLocale } from "@/lib/i18n/config";
import { useIdioma } from "@/lib/i18n/IdiomaProvider";
import { SELECTOR_IDIOMA } from "@/lib/i18n/mensajes/selectorIdioma";
import { moverIndice, urlConIdioma } from "@/lib/i18n/selector";

function Globo() {
  return (
    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" aria-hidden>
      <circle cx="12" cy="12" r="9" />
      <path d="M3 12h18M12 3c2.5 2.8 3.8 5.8 3.8 9s-1.3 6.2-3.8 9c-2.5-2.8-3.8-5.8-3.8-9S9.5 5.8 12 3z" />
    </svg>
  );
}

function Marca() {
  return (
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round" aria-hidden>
      <path d="M5 12.5l4.5 4.5L19 7.5" />
    </svg>
  );
}

export function SelectorIdioma({
  className,
  style,
  compacto = false,
  haciaArriba = false,
}: {
  className?: string;
  style?: React.CSSProperties;
  compacto?: boolean;
  /** La lista se abre hacia arriba (en el pie de página). */
  haciaArriba?: boolean;
}) {
  const idioma = useIdioma();
  const t = elegir(SELECTOR_IDIOMA, idioma);
  const idLista = useId();
  const raiz = useRef<HTMLDivElement>(null);
  const boton = useRef<HTMLButtonElement>(null);
  const lista = useRef<HTMLUListElement>(null);
  const [abierto, setAbierto] = useState(false);
  const [activo, setActivo] = useState(() => Math.max(0, ACTIVE_LOCALES.indexOf(idioma)));

  useEffect(() => {
    if (!abierto) return;
    lista.current?.focus();
    const fuera = (e: MouseEvent) => {
      if (raiz.current && !raiz.current.contains(e.target as Node)) setAbierto(false);
    };
    document.addEventListener("mousedown", fuera);
    return () => document.removeEventListener("mousedown", fuera);
  }, [abierto]);

  const abrir = () => {
    setActivo(Math.max(0, ACTIVE_LOCALES.indexOf(idioma)));
    setAbierto(true);
  };
  const cerrar = () => {
    setAbierto(false);
    boton.current?.focus();
  };
  const escoger = (l: ActiveLocale) => {
    if (l === idioma) return cerrar();
    window.location.assign(urlConIdioma(window.location.href, l));
  };
  const teclaLista = (e: React.KeyboardEvent) => {
    if (e.key === "ArrowDown" || e.key === "ArrowUp") {
      e.preventDefault();
      setActivo((a) => moverIndice(a, e.key === "ArrowDown" ? 1 : -1, ACTIVE_LOCALES.length));
    } else if (e.key === "Home" || e.key === "End") {
      e.preventDefault();
      setActivo(e.key === "Home" ? 0 : ACTIVE_LOCALES.length - 1);
    } else if (e.key === "Enter" || e.key === " ") {
      e.preventDefault();
      escoger(ACTIVE_LOCALES[activo]);
    } else if (e.key === "Escape") {
      e.preventDefault();
      cerrar();
    } else if (e.key === "Tab") {
      setAbierto(false);
    }
  };

  return (
    <div ref={raiz} className={"relative inline-flex " + (compacto ? "shrink-0" : "")}>
      <button
        ref={boton}
        type="button"
        title={t.etiqueta}
        aria-label={`${t.etiqueta}: ${NOMBRE_IDIOMA[idioma]}`}
        aria-haspopup="listbox"
        aria-expanded={abierto}
        aria-controls={idLista}
        onClick={() => (abierto ? setAbierto(false) : abrir())}
        onKeyDown={(e) => {
          if (e.key === "ArrowDown" || e.key === "ArrowUp") {
            e.preventDefault();
            abrir();
          }
        }}
        className={
          compacto
            ? "flex h-8 items-center gap-1.5 rounded-full px-2 text-[12px] font-semibold uppercase tracking-[0.6px] text-dim transition-colors hover:bg-white/[0.06] hover:text-ink focus-visible:bg-white/[0.06] focus-visible:text-ink " +
              (abierto ? "bg-white/[0.06] text-ink " : "") +
              (className ?? "")
            : "inline-flex items-center gap-2 transition-colors hover:text-ink " + (className ?? "")
        }
        style={style}
      >
        <Globo />
        {compacto ? (
          // En pantallas angostas, solo el globo: la lista dice el resto.
          <span aria-hidden className="hidden sm:inline">
            {idioma}
          </span>
        ) : (
          <span>{NOMBRE_IDIOMA[idioma]}</span>
        )}
      </button>
      {abierto && (
        <ul
          ref={lista}
          id={idLista}
          role="listbox"
          tabIndex={-1}
          aria-label={t.etiqueta}
          aria-activedescendant={`${idLista}-${ACTIVE_LOCALES[activo]}`}
          onKeyDown={teclaLista}
          className={
            "absolute end-0 z-50 max-h-[70vh] min-w-[176px] overflow-y-auto rounded-[12px] border border-hairline bg-surface-2 p-1 text-start normal-case tracking-normal shadow-[0_16px_40px_rgba(0,0,0,0.55)] outline-none " +
            (haciaArriba ? "bottom-full mb-2" : "top-full mt-2")
          }
        >
          {ACTIVE_LOCALES.map((l, i) => {
            const elegido = l === idioma;
            return (
              <li
                key={l}
                id={`${idLista}-${l}`}
                role="option"
                lang={l}
                aria-selected={elegido}
                onMouseEnter={() => setActivo(i)}
                onClick={() => escoger(l)}
                className={
                  "flex cursor-pointer items-center justify-between gap-3 rounded-[8px] px-3 py-2 text-[13.5px] font-medium " +
                  (i === activo ? "bg-white/[0.07] " : "") +
                  (elegido ? "text-accent" : "text-ink")
                }
              >
                <span>{NOMBRE_IDIOMA[l]}</span>
                {elegido && <Marca />}
              </li>
            );
          })}
        </ul>
      )}
    </div>
  );
}
