/**
 * mensajeServidor.ts: cómo lee la pantalla un rechazo del servidor (AUD-09 H03).
 *
 * El servidor ya habla en palabras de persona cuando tiene una razón: sin saldo
 * (402), doble factor (403), un muro del seguimiento (409), el límite diario
 * (429), el fusible (503) y el texto demasiado largo (400 con `limite`). La
 * pantalla lo cambiaba todo por "algo se atoró de nuestro lado", que es mentira
 * cuando la razón existe. La regla: el genérico SOLO cuando el servidor no dio
 * razón. Sin imports de servidor: lo usan los componentes del cliente.
 */
import { elegir, LOCALE_BASE, type Locale } from "./i18n/config";
import { SERVIDOR_COMUN } from "./i18n/mensajes/servidorComun";

/** El genérico en el idioma pedido (las pantallas pasan el suyo). */
export function errorGenerico(idioma: Locale = LOCALE_BASE): string {
  return elegir(SERVIDOR_COMUN, idioma).errorGenerico;
}
export const ERROR_GENERICO = errorGenerico(LOCALE_BASE);

export type Rechazo =
  | { tipo: "mensaje"; mensaje: string }
  /** 403 del doble factor: la pantalla abre el desafío en vez de solo avisar. */
  | { tipo: "segundo_factor"; mensaje: string };

const CON_RAZON = new Set([402, 403, 409, 429, 503]);

interface CuerpoRechazo {
  error?: unknown;
  segundo_factor_requerido?: unknown;
  limite?: unknown;
}

export async function leerRechazo(res: Response, idioma: Locale = LOCALE_BASE): Promise<Rechazo> {
  const generico = elegir(SERVIDOR_COMUN, idioma).errorGenerico;
  let cuerpo: CuerpoRechazo | null;
  try {
    cuerpo = (await res.json()) as CuerpoRechazo | null;
  } catch {
    cuerpo = null;
  }
  const error = typeof cuerpo?.error === "string" && cuerpo.error.trim() ? cuerpo.error : null;
  if (cuerpo?.segundo_factor_requerido === true) {
    return { tipo: "segundo_factor", mensaje: error ?? generico };
  }
  const conRazon = CON_RAZON.has(res.status) || (res.status === 400 && typeof cuerpo?.limite === "number");
  return { tipo: "mensaje", mensaje: error && conRazon ? error : generico };
}

/** Lleva al desafío del doble factor (la pantalla de login lo atiende) y, al
 * superarlo, de vuelta a `volverA`. El método sale de la cuenta. */
export async function irAlDesafio(volverA: string): Promise<void> {
  let metodo = "totp";
  try {
    const r = await fetch("/api/cuenta/seguridad");
    const d = (await r.json()) as { metodo?: string | null };
    if (d.metodo === "email") metodo = "email";
  } catch {
    // sin el método, el desafío abre en TOTP y ofrece el rescate
  }
  window.location.assign(`/login?desafio=1&metodo=${metodo}&next=${encodeURIComponent(volverA)}`);
}
