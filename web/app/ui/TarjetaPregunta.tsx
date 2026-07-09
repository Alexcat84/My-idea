"use client";

/**
 * TarjetaPregunta — la entrevista no-chat (brief 2.5): UNA pregunta a la
 * vez como tarjeta, con el título del concepto como cintillo pequeño,
 * campo de respuesta + micrófono debajo, y enviar. Sin burbujas.
 */
import { useState } from "react";
import { CampoConVoz } from "./CampoConVoz";

interface Props {
  cintillo?: string | null;
  pregunta: string;
  enviando: boolean;
  onEnviar: (respuesta: string) => void;
  textoBoton?: string;
}

export function TarjetaPregunta({ cintillo, pregunta, enviando, onEnviar, textoBoton = "Responder" }: Props) {
  const [respuesta, setRespuesta] = useState("");

  return (
    <div className="rounded-panel border border-hairline bg-surface p-5 sm:p-6">
      {cintillo && (
        <p className="mb-2 text-[11px] font-medium uppercase tracking-wider text-dim">{cintillo}</p>
      )}
      <p className="text-[17px] font-medium leading-relaxed">{pregunta}</p>
      <div className="mt-5">
        <CampoConVoz
          valor={respuesta}
          onCambio={setRespuesta}
          filas={4}
          deshabilitado={enviando}
          placeholder="Cuéntame con tus palabras…"
        />
      </div>
      <button
        onClick={() => {
          if (!respuesta.trim() || enviando) return;
          onEnviar(respuesta);
          setRespuesta("");
        }}
        disabled={!respuesta.trim() || enviando}
        className="mt-3 rounded-cinta bg-accent px-5 py-2.5 font-medium text-white hover:opacity-90 disabled:opacity-40"
      >
        {enviando ? "Pensando…" : textoBoton}
      </button>
    </div>
  );
}
