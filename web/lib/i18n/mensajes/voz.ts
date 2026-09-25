/** El dictado por voz: el botón del micrófono (CampoConVoz) y los motivos por los
 * que el dictado se apaga (lib/useSpeech.ts, mensajeErrorVoz). */
import type { PorIdioma } from "../config";

const es = {
  detenerDictado: "Detener dictado",
  dictarPorVoz: "Dictar por voz",
  errores: {
    sinPermiso:
      "Tu navegador no me dio permiso para usar el micrófono. Puedes escribir, o darle permiso en la configuración del navegador.",
    sinMicrofono: "No encontré un micrófono. Puedes escribir tu respuesta.",
    silencioLargo: "Apagué el micrófono porque dejé de oírte. Tócalo para seguir dictando.",
    cortado: "El dictado se cortó. Puedes volver a intentarlo o escribir.",
  },
};

const en: typeof es = {
  detenerDictado: "Stop dictating",
  dictarPorVoz: "Dictate with your voice",
  errores: {
    sinPermiso:
      "Your browser didn't give me permission to use the microphone. You can type instead, or allow it in your browser settings.",
    sinMicrofono: "I couldn't find a microphone. You can type your answer.",
    silencioLargo: "I turned off the microphone because I stopped hearing you. Tap it to keep dictating.",
    cortado: "Dictation cut out. You can try again or type instead.",
  },
};

export const VOZ: PorIdioma<typeof es> = { es, en };
