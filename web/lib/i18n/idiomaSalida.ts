/**
 * La regla de IDIOMA DE SALIDA de los prompts (i18n F5, DISENO §5).
 *
 * Los prompts viven en español en `engine/` y se sincronizan byte a byte: de
 * que su prefijo no cambie depende el caché de Anthropic. Por eso el idioma de
 * la idea NO se escribe dentro del prompt: viaja en un SEGUNDO bloque de
 * sistema, después del cacheado. En español no se agrega nada.
 *
 * `rotulosFijos`: los rótulos de estructura que el código LEE de la salida
 * (los "marcadores neutros": "## Etapa N:", "**Primera acción:**"...). La IA los
 * escribe tal cual, en español, en cualquier idioma; la pantalla y los
 * documentos los pintan en el idioma de quien lee.
 */
import { nombreIdiomaParaIA } from "./detectarIdioma";
import { REGLA_SIN_FUENTES } from "../reglaSinFuentes";
import { REGLA_CONTEXTO_USUARIO } from "../reglaContextoUsuario";

export type BloqueSistema = { type: "text"; text: string; cache_control?: { type: "ephemeral"; ttl?: "5m" | "1h" } };

export function reglaIdiomaSalida(codigo: string | null | undefined, rotulosFijos: readonly string[] = []): string | null {
  if (!codigo || codigo === "es") return null;
  const nombre = nombreIdiomaParaIA(codigo);
  const partes = [
    `IDIOMA DE SALIDA: ${nombre}.`,
    `Todo el texto que la persona va a leer lo escribes solo en ${nombre}, con su ortografía y su puntuación correctas, aunque estas instrucciones estén en español; los nodos que recibes están en español: úsalos como fuente y exprésalos en ${nombre}.`,
    "Donde las instrucciones digan 'español', entiende el idioma de salida. Los ejemplos en español muestran la forma, no el idioma.",
    "Las claves de un JSON y sus valores fijos (los que las instrucciones enumeran entre comillas) se escriben tal cual.",
  ];
  if (rotulosFijos.length > 0) {
    partes.push(
      `Estos rótulos de estructura se escriben tal cual, en español, sin traducirlos, porque el sistema los lee y los muestra en el idioma de la persona: ${rotulosFijos
        .map((r) => `«${r}»`)
        .join(", ")}. Lo que va después de cada rótulo, en ${nombre}.`
    );
  }
  return partes.join(" ");
}

/** El `system` de una llamada, ordenado para el caché (contexto de la entrevista,
 * principio 3, 28 sep 2026): primero lo FIJO, idéntico para todos los usuarios y
 * cacheado 1 hora: el prompt, la regla SIN FUENTES (REGLA ESTRICTA del fundador, 26
 * sep 2026) y la REGLA ÚNICA del contexto del usuario (28 sep 2026). La marca va en
 * el último bloque fijo, así el caché cubre los tres. Después, sin marca, lo que
 * varía por idioma: fuera del español, la regla del idioma de salida. */
export function bloquesDeSistema(
  system: string,
  idiomaSalida?: string | null,
  rotulosFijos: readonly string[] = []
): BloqueSistema[] {
  const bloques: BloqueSistema[] = [
    { type: "text", text: system },
    { type: "text", text: REGLA_SIN_FUENTES },
    { type: "text", text: REGLA_CONTEXTO_USUARIO, cache_control: { type: "ephemeral", ttl: "1h" } },
  ];
  const regla = reglaIdiomaSalida(idiomaSalida, rotulosFijos);
  if (regla) bloques.push({ type: "text", text: regla });
  return bloques;
}
