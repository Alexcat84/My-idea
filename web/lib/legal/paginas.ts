/**
 * Páginas públicas de cuenta y de ayuda (encargo del fundador del 6 oct 2026, punto 6): las instrucciones para
 * eliminar la cuenta (requisito de Google Play: accesible sin la app y sin iniciar sesión), las preguntas frecuentes y
 * el pie común. Estructura tomada de The Original I Ching (apps/web/src/app/delete-account y faqs).
 *
 * Idiomas (I18N AL DÍA, 7 oct 2026): los once. Los textos viven en el catálogo lib/i18n/mensajes/paginasAyuda.ts y
 * aquí solo se les ponen sus marcadores. Los precios salen SIEMPRE de precios.ts (regla P1) y los rótulos del centro
 * de cuenta, del catálogo de la cuenta (una sola fuente). Ningún texto nombra libros, autores ni estudios (regla D1).
 *
 * Los textos legales (Privacidad, Términos, Cookies) se leen en el idioma de la persona si su traducción está
 * publicada (scripts/sync_legal_web.py publica solo las que tienen su huella, scripts/legal_huellas.py) y, si no, en
 * español, sin aviso (se retiró el de "disponible en español y en francés").
 */
import { elegir, type ActiveLocale } from "@/lib/i18n/config";
import { interpolar } from "@/lib/i18n/interpolar";
import { CUENTA } from "@/lib/i18n/mensajes/cuenta";
import { PAGINAS_AYUDA } from "@/lib/i18n/mensajes/paginasAyuda";
import { PRECIOS } from "@/lib/precios";
import { TEXTOS_LEGALES, type DocumentoLegal } from "./textos";

export const CORREO_CONTACTO = "support@myideaproject.com";
export const CORREO_PRIVACIDAD = "privacy@myideaproject.com";

/** El idioma en que se lee un texto legal: el de la persona si su traducción está publicada; si no, el español. */
export function idiomaLegal(idioma: string, documento: DocumentoLegal): string {
  return TEXTOS_LEGALES[documento][idioma] !== undefined ? idioma : "es";
}

/** Pone los marcadores en todas las cadenas de un objeto del catálogo (listas incluidas). */
function conMarcadores<T>(x: T, valores: Record<string, string | number>): T {
  if (typeof x === "string") return interpolar(x, valores) as T;
  if (Array.isArray(x)) return x.map((y) => conMarcadores(y, valores)) as T;
  if (x && typeof x === "object")
    return Object.fromEntries(Object.entries(x).map(([k, v]) => [k, conMarcadores(v, valores)])) as T;
  return x;
}

function valores(idioma: ActiveLocale): Record<string, string | number> {
  const peligro = elegir(CUENTA, idioma).peligro;
  return {
    plan: PRECIOS.plan_completo,
    seguimiento: PRECIOS.seguimiento,
    mundo: PRECIOS.mundo_activar,
    contacto: CORREO_CONTACTO,
    privacidad: CORREO_PRIVACIDAD,
    zona: peligro.titulo,
    borrarTuCuenta: peligro.borrarTuCuenta,
    borrarParaSiempre: peligro.borrarParaSiempre,
    paginaEliminar: elegir(PAGINAS_AYUDA, idioma).nav.eliminar,
  };
}

type Ayuda = (typeof PAGINAS_AYUDA)["es"];

/** El pie común de las páginas públicas, en el idioma de la persona. */
export function navPublica(idioma: ActiveLocale): Ayuda["nav"] {
  return elegir(PAGINAS_AYUDA, idioma).nav;
}

/** /eliminar-cuenta, en el idioma de la persona y con sus marcadores puestos. */
export function eliminarCuenta(idioma: ActiveLocale): Ayuda["eliminarCuenta"] {
  return conMarcadores(elegir(PAGINAS_AYUDA, idioma).eliminarCuenta, valores(idioma));
}

/** /preguntas-frecuentes, en el idioma de la persona y con los precios de precios.ts. */
export function preguntasFrecuentes(idioma: ActiveLocale): Ayuda["preguntas"] {
  return conMarcadores(elegir(PAGINAS_AYUDA, idioma).preguntas, valores(idioma));
}
