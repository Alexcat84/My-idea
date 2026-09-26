/**
 * El idioma de los DOCUMENTOS de un proyecto (i18n F6, D2).
 *
 * D2: la interfaz sigue la preferencia del usuario; el plan y los documentos
 * siguen el idioma del proyecto. Un documento lo arma el código sin IA
 * (plantillas de los catálogos), así que su idioma es el de la idea si es de
 * los once, y si no (una idea en ruso) el de la interfaz: `idiomaDePlantilla`
 * de F5. Una idea de antes de F5 (sin idioma guardado) es español.
 *
 * La regla de todo documento (markdown y papel):
 *   - el CUERPO, con sus títulos, rótulos, fechas, el nombre de archivo y los
 *     rótulos del plan que va dentro (pintarRotulos): idioma del proyecto;
 *   - lo que lo RODEA en la pantalla (el panel que lista los documentos, los
 *     botones "Descargar"/.md/PDF, los rechazos del servidor): la interfaz.
 */
import type { ActiveLocale } from "./config";
import { idiomaDePlantilla, idiomaDelProyecto } from "./detectarIdioma";

export function idiomaDeDocumentos(proyecto: { idioma?: string | null }, interfaz: ActiveLocale): ActiveLocale {
  return idiomaDePlantilla(idiomaDelProyecto(proyecto), interfaz);
}
