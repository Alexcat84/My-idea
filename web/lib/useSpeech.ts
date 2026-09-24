"use client";

/**
 * useSpeech — Fase 3.2 (brief 2.3): dictado por voz con la Web Speech
 * API (SpeechRecognition) donde el navegador la tenga (Chrome/Edge/
 * Android). Transcripción en vivo (interim results) que el llamador
 * inserta en su campo, editable antes de enviar. Donde no exista
 * (Firefox), `soportado` es false y el micrófono simplemente no se
 * renderiza: fallback limpio a solo-texto, sin errores.
 * (Whisper/API de transcripción = backlog 3.4, no beta.)
 */
import { useCallback, useEffect, useRef, useState, useSyncExternalStore } from "react";

interface ResultadoVoz {
  soportado: boolean;
  escuchando: boolean;
  /** AUD-09 B14c: por qué se apagó el dictado, en palabras de persona (null =
   * nada que decir). Antes se apagaba en silencio. */
  errorVoz: string | null;
  iniciar: () => void;
  detener: () => void;
}

// La Web Speech API no está en lib.dom de TS: tipado mínimo local.
interface RecognitionResult {
  isFinal: boolean;
  0: { transcript: string };
}
interface RecognitionEvent {
  resultIndex: number;
  results: { length: number; [i: number]: RecognitionResult };
}
interface Recognition {
  lang: string;
  continuous: boolean;
  interimResults: boolean;
  onresult: ((e: RecognitionEvent) => void) | null;
  onend: (() => void) | null;
  onerror: ((e: { error?: string }) => void) | null;
  start: () => void;
  stop: () => void;
}

function obtenerConstructor(): (new () => Recognition) | null {
  if (typeof window === "undefined") return null;
  const w = window as unknown as {
    SpeechRecognition?: new () => Recognition;
    webkitSpeechRecognition?: new () => Recognition;
  };
  return w.SpeechRecognition ?? w.webkitSpeechRecognition ?? null;
}

/** AUD-09 B14c: el motivo de un fallo del dictado, en palabras de persona.
 * null cuando no hay nada que anunciar (no hablar, o detenerlo a propósito). */
export function mensajeErrorVoz(codigo: string | undefined): string | null {
  if (codigo === "no-speech" || codigo === "aborted") return null;
  if (codigo === "not-allowed" || codigo === "service-not-allowed")
    return "Tu navegador no me dio permiso para usar el micrófono. Puedes escribir, o darle permiso en la configuración del navegador.";
  if (codigo === "audio-capture") return "No encontré un micrófono. Puedes escribir tu respuesta.";
  return "El dictado se cortó. Puedes volver a intentarlo o escribir.";
}

/** `onTexto(nuevoFinal, provisional)`: `nuevoFinal` es SOLO el trozo recién
 * cerrado (incremental, nunca el acumulado); `provisional` es lo que aún se
 * está oyendo. El llamador agrega `nuevoFinal` a lo que tenga y muestra
 * `provisional` sin comprometerlo. */
export function useSpeech(onTexto: (nuevoFinal: string, provisional: string) => void): ResultadoVoz {
  // Hydration-safe: false en el server, la verdad del navegador en el
  // cliente, sin setState-en-effect (el soporte es estático por navegador).
  const soportado = useSyncExternalStore(
    () => () => {},
    () => obtenerConstructor() !== null,
    () => false
  );
  const [escuchando, setEscuchando] = useState(false);
  const [errorVoz, setErrorVoz] = useState<string | null>(null);
  const recRef = useRef<Recognition | null>(null);
  const onTextoRef = useRef(onTexto);
  useEffect(() => {
    onTextoRef.current = onTexto;
  });

  const detener = useCallback(() => {
    recRef.current?.stop();
    recRef.current = null;
    setEscuchando(false);
  }, []);

  const iniciar = useCallback(() => {
    const Ctor = obtenerConstructor();
    if (!Ctor || recRef.current) return;
    setErrorVoz(null);
    const rec = new Ctor();
    rec.lang = "es-MX";
    rec.continuous = true;
    rec.interimResults = true;
    rec.onresult = (e) => {
      // SOLO lo nuevo de ESTE evento (desde e.resultIndex). Con
      // continuous=true, e.results acumula TODA la sesión: releerlo desde 0
      // reenviaba el transcript entero en cada evento, y el llamador lo
      // volvía a pegar (texto duplicado al editar, y la respuesta anterior
      // reapareciendo en la pregunta siguiente). Incremental = una sola vez.
      let nuevoFinal = "";
      let provisional = "";
      for (let i = e.resultIndex; i < e.results.length; i++) {
        const r = e.results[i];
        if (r.isFinal) nuevoFinal += r[0].transcript;
        else provisional += r[0].transcript;
      }
      onTextoRef.current(nuevoFinal, provisional);
    };
    rec.onend = () => {
      recRef.current = null;
      setEscuchando(false);
    };
    rec.onerror = (e) => {
      recRef.current = null;
      setEscuchando(false);
      setErrorVoz(mensajeErrorVoz(e?.error));
    };
    recRef.current = rec;
    setEscuchando(true);
    rec.start();
  }, []);

  useEffect(() => () => recRef.current?.stop(), []);

  return { soportado, escuchando, errorVoz, iniciar, detener };
}
