/**
 * Consentimiento legal versionado (decisión del fundador, 7 oct 2026; corregida el mismo día: el modal se retiró).
 * Navegar es libre y nada tapa la página. La aceptación de los Términos y la Privacidad se pide en el PRIMER ENVÍO DE
 * DATOS: al escribir la idea y pulsar generar la evaluación gratuita, una línea junto al botón ("Al continuar,
 * aceptas...") y el botón "Aceptar y generar" (app/ui/LineaConsentimiento.tsx). Se pide a TODA identidad que envía
 * datos: la invisible (el usuario anónimo de proxy.ts, una fila de auth.users) también la guarda, y la adopción la
 * pasa a la cuenta al crearla (lib/cuentas.ts), sin volver a preguntar. Si la versión cambia, se vuelve a pedir en el
 * siguiente envío o al entrar con la cuenta (la línea del login), nunca al cargar una página.
 *
 * Se guarda en aceptaciones_legales (migración 050) por /api/cuenta/consentimiento, y la cumple el SERVIDOR: las rutas
 * que envían la idea rechazan sin aceptación vigente (lib/legal/aceptacionServidor.ts, exigirAceptacionVigente).
 *
 * La versión tiene UNA fuente: docs/legal/version.json, publicada en ./version.ts por scripts/sync_legal_web.py
 * (guarda: engine/test_version_legal.py, que falla si los textos cambian sin subir la versión). Este módulo es
 * seguro para el cliente: no importa los textos legales enteros ni nada del servidor.
 */
import { ACEPTACION_IDIOMA_TEXTO, type IdiomaTextoLegal, type MotivoAceptacion } from "@/lib/dbContract";
import { idiomaLegal } from "./paginas";

export { HUELLA_LEGAL, VERSION_LEGAL } from "./version";
import { VERSION_LEGAL } from "./version";

export type { IdiomaTextoLegal, MotivoAceptacion };

export interface EstadoConsentimiento {
  requiere: boolean;
  motivo: MotivoAceptacion | null;
}

/** ¿Hay que pedirle la aceptación antes de enviar sus datos? A toda identidad (invitada o con cuenta) cuya última
 * versión aceptada no es la vigente. */
export function estadoConsentimiento(ultimaVersion: string | null): EstadoConsentimiento {
  if (ultimaVersion === VERSION_LEGAL) return { requiere: false, motivo: null };
  return { requiere: true, motivo: ultimaVersion === null ? "primera_aceptacion" : "nueva_version" };
}

/** La marca del rechazo del servidor cuando falta la aceptación vigente (status 428): la pantalla pinta la línea. */
export const STATUS_SIN_ACEPTACION = 428;

/** El idioma del texto legal que lee quien usa la interfaz en `idioma` (los textos existen en es y fr). */
export function idiomaTextoLegal(idioma: string): IdiomaTextoLegal {
  return idiomaLegal(idioma);
}

export function esIdiomaTextoLegal(x: unknown): x is IdiomaTextoLegal {
  return typeof x === "string" && (ACEPTACION_IDIOMA_TEXTO as readonly string[]).includes(x);
}
