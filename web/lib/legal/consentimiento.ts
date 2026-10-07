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

/** El idioma del texto VINCULANTE que acepta quien usa la interfaz en `idioma`: el francés para el francés y el
 * español para todos los demás. Desde el 7 oct 2026 (I18N AL DÍA) las páginas legales se leen también en las otras
 * traducciones, pero son de cortesía: en caso de discrepancia prevalece el español (y el francés en Quebec), la huella
 * de la versión solo cubre es y fr (scripts/sync_legal_web.py) y la columna aceptaciones_legales.idioma_texto solo
 * admite 'es' y 'fr' (migración 050). Guardar el idioma de la traducción leída pediría una migración nueva. */
export function idiomaTextoLegal(idioma: string): IdiomaTextoLegal {
  return idioma === "fr" ? "fr" : "es";
}

export function esIdiomaTextoLegal(x: unknown): x is IdiomaTextoLegal {
  return typeof x === "string" && (ACEPTACION_IDIOMA_TEXTO as readonly string[]).includes(x);
}
