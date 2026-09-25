"use client";

/**
 * CampoConVoz — textarea + botón de micrófono (brief 2.3 y 2.5). El
 * micrófono solo se renderiza si el navegador soporta la Web Speech API
 * (fallback limpio: en Firefox simplemente no aparece). La transcripción
 * entra en vivo al campo y es editable antes de enviar.
 */
import { useEffect, useRef } from "react";
import { alEditarAMano, componerDictado, estadoDictadoInicial } from "@/lib/dictado";
import { elegir } from "@/lib/i18n/config";
import { useIdioma } from "@/lib/i18n/IdiomaProvider";
import { VOZ } from "@/lib/i18n/mensajes/voz";
import { useSpeech } from "@/lib/useSpeech";

interface Props {
  valor: string;
  onCambio: (v: string) => void;
  placeholder?: string;
  filas?: number;
  autoFocus?: boolean;
  deshabilitado?: boolean;
  id?: string;
}

export function CampoConVoz({ valor, onCambio, placeholder, filas = 6, autoFocus, deshabilitado, id }: Props) {
  const idioma = useIdioma();
  const t = elegir(VOZ, idioma);
  // Lo dictado vive DENTRO del valor (AUD-09 B14b: enviar o detener a mitad
  // de frase no lo pierde). Cada sesión del micrófono reemplaza su propio
  // aporte con el texto entero de la sesión, así que por más que el navegador
  // reenvíe la frase, ocupa su lugar una vez (lib/dictado.ts).
  const estadoDictado = useRef(estadoDictadoInicial());
  const ultimoTextoSesion = useRef("");
  // El valor VIVO: el dictado trabaja sobre lo que hay AHORA, aunque el
  // usuario haya corregido a mano mientras hablaba.
  const valorRef = useRef(valor);
  useEffect(() => {
    valorRef.current = valor;
  });

  const { soportado, escuchando, errorVoz, iniciar, detener } = useSpeech(
    (textoSesion) => {
      ultimoTextoSesion.current = textoSesion;
      const r = componerDictado(valorRef.current, estadoDictado.current, textoSesion);
      estadoDictado.current = r.estado;
      if (r.valor === valorRef.current) return;
      valorRef.current = r.valor;
      onCambio(r.valor);
    },
    // Sesión nueva (al iniciar o al reanudarse sola): lo de la anterior queda
    // fijo en el campo.
    () => {
      estadoDictado.current = estadoDictadoInicial();
      ultimoTextoSesion.current = "";
    },
    idioma
  );

  // Detener NO descarta lo oído: ya está en el campo.
  function alternarMicrofono() {
    if (escuchando) detener();
    else iniciar();
  }

  return (
    <div className="relative">
      <textarea
        id={id}
        rows={filas}
        autoFocus={autoFocus}
        disabled={deshabilitado}
        placeholder={placeholder}
        value={valor}
        onChange={(e) => {
          const v = e.target.value;
          if (v === valorRef.current) return; // eco del teclado: nada cambió
          // lo que el usuario escribe es suyo: el dictado no lo pisa ni repite
          estadoDictado.current = alEditarAMano(v, estadoDictado.current, ultimoTextoSesion.current);
          valorRef.current = v;
          onCambio(v);
        }}
        className="w-full resize-y rounded-panel border border-hairline bg-surface px-4 py-3 text-base leading-relaxed text-ink placeholder:text-dim disabled:opacity-60"
      />
      {soportado && (
        <button
          type="button"
          onClick={alternarMicrofono}
          disabled={deshabilitado}
          aria-label={escuchando ? t.detenerDictado : t.dictarPorVoz}
          aria-pressed={escuchando}
          className={
            "absolute bottom-3 right-3 flex h-10 w-10 items-center justify-center rounded-full " +
            (escuchando ? "bg-accent text-white animate-pulse" : "border border-hairline bg-surface-2 text-dim hover:text-ink")
          }
        >
          {/* micrófono en SVG inline: sin dependencias de iconos */}
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden>
            <rect x="9" y="2" width="6" height="12" rx="3" />
            <path d="M5 10v1a7 7 0 0 0 14 0v-1" />
            <line x1="12" y1="18" x2="12" y2="22" />
          </svg>
        </button>
      )}
      {/* AUD-09 B14c: si el dictado se apaga por algo (permiso, sin micrófono),
          se dice en vez de apagarse en silencio. */}
      {errorVoz && <p className="mt-2 text-[12.5px] text-warn">{errorVoz}</p>}
    </div>
  );
}
