"use client";

/**
 * CampoConVoz — textarea + botón de micrófono (brief 2.3 y 2.5). El
 * micrófono solo se renderiza si el navegador soporta la Web Speech API
 * (fallback limpio: en Firefox simplemente no aparece). La transcripción
 * entra en vivo al campo y es editable antes de enviar.
 */
import { useEffect, useRef, useState } from "react";
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
  const [provisional, setProvisional] = useState("");
  // El valor VIVO: el dictado agrega sobre lo que hay AHORA, aunque el
  // usuario haya corregido a mano mientras hablaba. (Antes se guardaba una
  // "base" al arrancar el micrófono y se recomponía desde ella; si el
  // usuario editaba, esa base ya contenía lo dictado y todo se duplicaba.)
  const valorRef = useRef(valor);
  useEffect(() => {
    valorRef.current = valor;
  });

  const { soportado, escuchando, iniciar, detener } = useSpeech((nuevoFinal, prov) => {
    const trozo = nuevoFinal.trim();
    if (trozo) {
      const actual = valorRef.current;
      onCambio(actual ? `${actual} ${trozo}` : trozo);
    }
    setProvisional(prov);
  });

  function alternarMicrofono() {
    setProvisional("");
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
        value={provisional ? `${valor}${valor ? " " : ""}${provisional}` : valor}
        onChange={(e) => {
          setProvisional("");
          onCambio(e.target.value);
        }}
        className="w-full resize-y rounded-panel border border-hairline bg-surface px-4 py-3 text-base leading-relaxed text-ink placeholder:text-dim disabled:opacity-60"
      />
      {soportado && (
        <button
          type="button"
          onClick={alternarMicrofono}
          disabled={deshabilitado}
          aria-label={escuchando ? "Detener dictado" : "Dictar por voz"}
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
    </div>
  );
}
