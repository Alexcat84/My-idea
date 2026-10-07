/**
 * Consentimiento legal versionado (decisión del fundador, 7 oct 2026; la idea viene de The Original I Ching:
 * auth/complete-legal, LegalConsentModal y user_legal_acceptances). Las cuentas REALES aceptan los Términos y la
 * Privacidad por versión, y la app vuelve a pedirlo cuando la versión cambia. Se guarda en aceptaciones_legales
 * (migración 050) por /api/cuenta/consentimiento; el modal es app/ui/ConsentimientoLegal.tsx.
 *
 * Lo que manda en My Idea: la web es ABIERTA. La identidad invisible (proxy.ts) nunca ve el modal, y el modal nunca
 * es un muro para usar la app sin cuenta: quien no acepta puede salir de su cuenta y seguir como visitante, o ir al
 * centro de cuenta a borrarla (allí el modal no aparece).
 *
 * La versión tiene UNA fuente: docs/legal/version.json, publicada en ./version.ts por scripts/sync_legal_web.py
 * (guarda: engine/test_version_legal.py, que falla si los textos cambian sin subir la versión). Este módulo es
 * seguro para el cliente: no importa los textos legales enteros.
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

/** ¿Hay que pedirle la aceptación? Solo a una cuenta real cuya última versión aceptada no es la vigente. */
export function estadoConsentimiento(esCuentaReal: boolean, ultimaVersion: string | null): EstadoConsentimiento {
  if (!esCuentaReal || ultimaVersion === VERSION_LEGAL) return { requiere: false, motivo: null };
  return { requiere: true, motivo: ultimaVersion === null ? "primera_aceptacion" : "nueva_version" };
}

/** Las rutas donde el modal no aparece nunca: las páginas legales y de ayuda (hay que poder leer lo que se acepta),
 * el login y los regresos de auth (el doble factor va antes), y el centro de cuenta, para que quien no acepta pueda
 * borrar su cuenta sin aceptar nada. */
const RUTAS_SIN_CONSENTIMIENTO = ["/terminos", "/privacidad", "/cookies", "/eliminar-cuenta", "/preguntas-frecuentes",
  "/login", "/auth", "/cuenta"];

export function rutaSinConsentimiento(pathname: string): boolean {
  return RUTAS_SIN_CONSENTIMIENTO.some((r) => pathname === r || pathname.startsWith(r + "/"));
}

/** El idioma del texto legal que lee quien usa la interfaz en `idioma` (los textos existen en es y fr). */
export function idiomaTextoLegal(idioma: string): IdiomaTextoLegal {
  return idiomaLegal(idioma);
}

export function esIdiomaTextoLegal(x: unknown): x is IdiomaTextoLegal {
  return typeof x === "string" && (ACEPTACION_IDIOMA_TEXTO as readonly string[]).includes(x);
}
