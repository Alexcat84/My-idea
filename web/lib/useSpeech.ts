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

/**
 * Lo que ya se entregó en ESTA sesión del reconocedor: cuántas frases finales
 * (por índice) y el texto final acumulado. Se reinicia en cada sesión.
 */
export interface EstadoVoz {
  finalesEmitidos: number;
  finalAcumulado: string;
}

export function estadoVozInicial(): EstadoVoz {
  return { finalesEmitidos: 0, finalAcumulado: "" };
}

const normalizar = (t: string) => t.toLocaleLowerCase().replace(/\s+/g, " ").trim();

/** Si `texto` empieza con todo lo ya dicho en la sesión (el reconocedor lo
 * acumuló), devuelve solo lo nuevo. */
function sinLoYaDicho(texto: string, yaDicho: string): string {
  if (!yaDicho) return texto;
  const t = texto.trim();
  if (normalizar(t).startsWith(normalizar(yaDicho))) return t.slice(yaDicho.trim().length);
  return texto;
}

/**
 * Lee UN evento del reconocedor y entrega cada cosa una sola vez. Chrome, sobre
 * todo en Android, no siempre sigue el estándar: (A) reenvía en cada evento las
 * frases ya cerradas (resultIndex se queda en 0 y la lista crece), o (B) manda
 * cada frase final ACUMULANDO las anteriores. Antes se volvían a pegar y el
 * texto se duplicaba solo hasta el tope. Pura.
 */
export function leerResultados(
  results: ArrayLike<{ isFinal: boolean; transcript: string }>,
  resultIndex: number,
  estado: EstadoVoz
): { nuevoFinal: string; provisional: string; estado: EstadoVoz } {
  let { finalesEmitidos, finalAcumulado } = estado;
  let nuevoFinal = "";
  let provisional = "";
  for (let i = Math.min(resultIndex, finalesEmitidos); i < results.length; i++) {
    const r = results[i];
    if (r.isFinal) {
      if (i < finalesEmitidos) continue; // (A) ya entregada
      const nuevo = sinLoYaDicho(r.transcript, finalAcumulado); // (B)
      nuevoFinal += nuevo;
      finalAcumulado = nuevo === r.transcript ? `${finalAcumulado} ${r.transcript}`.trim() : r.transcript.trim();
      finalesEmitidos = i + 1;
    } else {
      provisional += r.transcript;
    }
  }
  return { nuevoFinal, provisional: sinLoYaDicho(provisional, finalAcumulado), estado: { finalesEmitidos, finalAcumulado } };
}

/** El navegador cierra la sesión de reconocimiento tras una pausa, un corte de
 * red o al minuto, aunque sea continua. Si el usuario no la detuvo y el error no
 * es definitivo, se reanuda sola; si se corta en seguida (menos de
 * CORTE_RAPIDO_MS) MAX_CORTES_RAPIDOS veces seguidas, se para y se dice. */
export const MAX_CORTES_RAPIDOS = 5;
export const CORTE_RAPIDO_MS = 1500;

/** Sin permiso o sin micrófono: reanudar no serviría de nada. */
export function esErrorFatalVoz(codigo: string | undefined): boolean {
  return codigo === "not-allowed" || codigo === "service-not-allowed" || codigo === "audio-capture";
}

export function debeReanudar(d: { detenidoPorUsuario: boolean; errorFatal: boolean; cortesRapidosSeguidos: number }): boolean {
  return !d.detenidoPorUsuario && !d.errorFatal && d.cortesRapidosSeguidos < MAX_CORTES_RAPIDOS;
}

/** `onTexto(nuevoFinal, provisional)`: `nuevoFinal` es SOLO el trozo recién
 * cerrado (incremental, nunca el acumulado); `provisional` es lo que aún se
 * está oyendo. El llamador agrega `nuevoFinal` a lo que tenga y muestra
 * `provisional` sin comprometerlo. */
export function useSpeech(
  onTexto: (nuevoFinal: string, provisional: string) => void,
  /** Se llama justo antes de reanudar una sesión que cortó el navegador: el
   * llamador fija lo provisional (la sesión nueva empieza de cero). */
  alReanudar?: () => void
): ResultadoVoz {
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
  const alReanudarRef = useRef(alReanudar);
  useEffect(() => {
    onTextoRef.current = onTexto;
    alReanudarRef.current = alReanudar;
  });
  // El estado de la reanudación: si el usuario lo detuvo, el último error
  // definitivo y los cortes rápidos seguidos.
  const detenidoRef = useRef(false);
  const errorFatalRef = useRef<string | null>(null);
  const cortesRapidosRef = useRef(0);

  const detener = useCallback(() => {
    detenidoRef.current = true;
    recRef.current?.stop();
    recRef.current = null;
    setEscuchando(false);
  }, []);

  const arrancar = useCallback(function arrancarSesion() {
    const Ctor = obtenerConstructor();
    if (!Ctor) return;
    const inicioSesion = Date.now();
    let estadoSesion = estadoVozInicial();
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
      // Y cada frase una sola vez aunque el navegador la reenvíe o la acumule
      // (leerResultados).
      const lista = Array.from({ length: e.results.length }, (_, k) => ({
        isFinal: e.results[k].isFinal,
        transcript: e.results[k][0].transcript,
      }));
      const r = leerResultados(lista, e.resultIndex, estadoSesion);
      estadoSesion = r.estado;
      onTextoRef.current(r.nuevoFinal, r.provisional);
    };
    rec.onend = () => {
      if (recRef.current !== rec) return; // una sesión vieja o ya detenida
      cortesRapidosRef.current = Date.now() - inicioSesion < CORTE_RAPIDO_MS ? cortesRapidosRef.current + 1 : 0;
      const reanudar = debeReanudar({
        detenidoPorUsuario: detenidoRef.current,
        errorFatal: errorFatalRef.current !== null,
        cortesRapidosSeguidos: cortesRapidosRef.current,
      });
      if (reanudar) {
        alReanudarRef.current?.();
        arrancarSesion();
        return;
      }
      recRef.current = null;
      setEscuchando(false);
      if (errorFatalRef.current) setErrorVoz(mensajeErrorVoz(errorFatalRef.current));
      else if (!detenidoRef.current) setErrorVoz(mensajeErrorVoz("network"));
    };
    rec.onerror = (e) => {
      // Lo definitivo (sin permiso, sin micrófono) para; lo demás (una pausa,
      // un corte de red) lo resuelve onend reanudando.
      if (esErrorFatalVoz(e?.error)) errorFatalRef.current = e?.error ?? "not-allowed";
    };
    recRef.current = rec;
    setEscuchando(true);
    try {
      rec.start();
    } catch {
      recRef.current = null;
      setEscuchando(false);
      setErrorVoz(mensajeErrorVoz("network"));
    }
  }, []);

  const iniciar = useCallback(() => {
    if (recRef.current) return;
    detenidoRef.current = false;
    errorFatalRef.current = null;
    cortesRapidosRef.current = 0;
    setErrorVoz(null);
    arrancar();
  }, [arrancar]);

  useEffect(
    () => () => {
      detenidoRef.current = true;
      recRef.current?.stop();
    },
    []
  );

  return { soportado, escuchando, errorVoz, iniciar, detener };
}
