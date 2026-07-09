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
  onerror: (() => void) | null;
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

export function useSpeech(onTexto: (finales: string, provisional: string) => void): ResultadoVoz {
  // Hydration-safe: false en el server, la verdad del navegador en el
  // cliente, sin setState-en-effect (el soporte es estático por navegador).
  const soportado = useSyncExternalStore(
    () => () => {},
    () => obtenerConstructor() !== null,
    () => false
  );
  const [escuchando, setEscuchando] = useState(false);
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
    const rec = new Ctor();
    rec.lang = "es-MX";
    rec.continuous = true;
    rec.interimResults = true;
    rec.onresult = (e) => {
      let finales = "";
      let provisional = "";
      for (let i = 0; i < e.results.length; i++) {
        const r = e.results[i];
        if (r.isFinal) finales += r[0].transcript;
        else provisional += r[0].transcript;
      }
      onTextoRef.current(finales, provisional);
    };
    rec.onend = () => {
      recRef.current = null;
      setEscuchando(false);
    };
    rec.onerror = () => {
      recRef.current = null;
      setEscuchando(false);
    };
    recRef.current = rec;
    setEscuchando(true);
    rec.start();
  }, []);

  useEffect(() => () => recRef.current?.stop(), []);

  return { soportado, escuchando, iniciar, detener };
}
