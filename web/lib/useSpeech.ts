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
import { textoDeSesion, type ResultadoVoz as ResultadoDictado } from "./dictado";

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
  if (codigo === SILENCIO_LARGO) return "Apagué el micrófono porque dejé de oírte. Tócalo para seguir dictando.";
  return "El dictado se cortó. Puedes volver a intentarlo o escribir.";
}

/** Cada sesión del reconocedor es UNA frase (continuous = false: el modo que
 * Chrome en Android maneja bien) y al terminar se reanuda sola, salvo que el
 * usuario la detuviera, el error sea definitivo, lleve SILENCIO_MAX_MS sin oír
 * nada, o se corte en seguida sin oír nada (menos de CORTE_RAPIDO_MS)
 * MAX_CORTES_RAPIDOS veces seguidas (un bucle de errores). */
export const MAX_CORTES_RAPIDOS = 5;
export const CORTE_RAPIDO_MS = 1500;
export const SILENCIO_MAX_MS = 30_000;
/** Código propio para el apagado por silencio (no es un error del navegador). */
export const SILENCIO_LARGO = "silencio-largo";

/** Un corte rápido cuenta para el tope solo si en esa sesión no se oyó nada. */
export function esCorteRapido(duracionMs: number, oyoAlgo: boolean): boolean {
  return !oyoAlgo && duracionMs < CORTE_RAPIDO_MS;
}

/** Sin permiso o sin micrófono: reanudar no serviría de nada. */
export function esErrorFatalVoz(codigo: string | undefined): boolean {
  return codigo === "not-allowed" || codigo === "service-not-allowed" || codigo === "audio-capture";
}

export function debeReanudar(d: {
  detenidoPorUsuario: boolean;
  errorFatal: boolean;
  cortesRapidosSeguidos: number;
  silencioMs: number;
}): boolean {
  return (
    !d.detenidoPorUsuario && !d.errorFatal && d.cortesRapidosSeguidos < MAX_CORTES_RAPIDOS && d.silencioMs < SILENCIO_MAX_MS
  );
}

/** `onTexto(textoSesion)`: el texto ENTERO de la sesión en curso (lo final y lo
 * provisional, ya sin repeticiones: textoDeSesion). El llamador lo pone en el
 * campo en lugar del anterior de la misma sesión (componerDictado). */
export function useSpeech(
  onTexto: (textoSesion: string) => void,
  /** Se llama justo antes de cada sesión nueva (al iniciar y al reanudar): lo
   * de la sesión anterior queda fijo en el campo. */
  alNuevaSesion?: () => void
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
  const alNuevaSesionRef = useRef(alNuevaSesion);
  useEffect(() => {
    onTextoRef.current = onTexto;
    alNuevaSesionRef.current = alNuevaSesion;
  });
  // El estado de la reanudación: si el usuario lo detuvo, el último error
  // definitivo, los cortes rápidos seguidos y cuándo se oyó voz por última vez.
  const detenidoRef = useRef(false);
  const errorFatalRef = useRef<string | null>(null);
  const cortesRapidosRef = useRef(0);
  const ultimaVozRef = useRef(0);

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
    let oyoAlgo = false;
    alNuevaSesionRef.current?.();
    const rec = new Ctor();
    rec.lang = "es-MX";
    rec.continuous = false;
    rec.interimResults = true;
    rec.onresult = (e) => {
      // La lista ENTERA de la sesión en cada evento: textoDeSesion funde las
      // versiones repetidas que manda Android, y el campo reemplaza (no pega).
      const lista: ResultadoDictado[] = Array.from({ length: e.results.length }, (_, k) => ({
        isFinal: e.results[k].isFinal,
        transcript: e.results[k][0].transcript,
      }));
      const texto = textoDeSesion(lista);
      // Un evento vacío no borra lo que la sesión ya puso en el campo.
      if (!texto) return;
      oyoAlgo = true;
      ultimaVozRef.current = Date.now();
      onTextoRef.current(texto);
    };
    rec.onend = () => {
      if (recRef.current !== rec) return; // una sesión vieja o ya detenida
      const ahora = Date.now();
      cortesRapidosRef.current = esCorteRapido(ahora - inicioSesion, oyoAlgo) ? cortesRapidosRef.current + 1 : 0;
      const silencioMs = ahora - ultimaVozRef.current;
      const reanudar = debeReanudar({
        detenidoPorUsuario: detenidoRef.current,
        errorFatal: errorFatalRef.current !== null,
        cortesRapidosSeguidos: cortesRapidosRef.current,
        silencioMs,
      });
      if (reanudar) {
        arrancarSesion();
        return;
      }
      recRef.current = null;
      setEscuchando(false);
      if (errorFatalRef.current) setErrorVoz(mensajeErrorVoz(errorFatalRef.current));
      else if (detenidoRef.current) return;
      else if (silencioMs >= SILENCIO_MAX_MS) setErrorVoz(mensajeErrorVoz(SILENCIO_LARGO));
      else setErrorVoz(mensajeErrorVoz("network"));
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
    ultimaVozRef.current = Date.now();
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
