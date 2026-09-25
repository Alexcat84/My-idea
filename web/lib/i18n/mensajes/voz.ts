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

export const VOZ: PorIdioma<typeof es> = { es };
