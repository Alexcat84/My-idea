/**
 * LA MONEDA SALE DE LOS DATOS QUE DIO LA PERSONA, NUNCA DE LA IA (decision del fundador, corrida final, 8 oct 2026).
 *
 * El juez de fidelidad sostuvo una invencion en un plan de Riesgos: «para ver en pesos cuánto te cuesta un mes sin ese
 * canal», cuando la persona solo dio cifras. Aqui, en codigo:
 *  - monedaDicha: la moneda tal como la dijo la persona en SUS palabras (su idea, sus respuestas, la frase literal de
 *    cada numero). El signo "$" se queda como "$": no se traduce a dolares ni a pesos.
 *  - limpiarMonedaNoDicha: antes de entregar un texto, quita la moneda que la persona no dijo (la cifra queda sola) o la
 *    cambia por la que si dijo.
 */
const PALABRAS: Array<[RegExp, string]> = [
  [/^pesos?$/, "pesos"],
  [/^d[oó]lar(es)?$/, "dólares"],
  [/^euros?$/, "euros"],
  [/^soles$/, "soles"],
  [/^bol[ií]vares$/, "bolívares"],
  [/^quetzales$/, "quetzales"],
  [/^colones$/, "colones"],
  [/^lempiras$/, "lempiras"],
  [/^c[oó]rdobas$/, "córdobas"],
  [/^guaran[ií]es$/, "guaraníes"],
];
const CODIGOS = ["USD", "MXN", "COP", "CLP", "ARS", "PEN", "EUR", "US$"];

// Una palabra de moneda en plural sola, o en singular solo detras de una cifra ("1 peso", nunca "el peso de la maceta").
const L = "\\p{L}";
const PLURALES = "pesos|d[oó]lares|euros|soles|bol[ií]vares|quetzales|colones|lempiras|c[oó]rdobas|guaran[ií]es";
const SINGULARES = "peso|d[oó]lar|euro";
const COD = "USD|MXN|COP|CLP|ARS|PEN|EUR|US\\$";

function canonica(palabra: string): string | null {
  const p = palabra.toLowerCase();
  for (const [re, nombre] of PALABRAS) if (re.test(p)) return nombre;
  const c = palabra.toUpperCase();
  return CODIGOS.includes(c) ? c : null;
}

/** La moneda que la persona nombro en sus propias palabras; "$" si solo uso el signo; null si no dijo ninguna. */
export function monedaDicha(textosDeLaPersona: Array<string | null | undefined>): string | null {
  const texto = textosDeLaPersona.filter(Boolean).join("\n");
  const palabra = new RegExp(`(?<![${L}])(${PLURALES}|${COD})(?![${L}])|\\d\\s*(${SINGULARES})(?![${L}])`, "giu").exec(texto);
  if (palabra) return canonica(palabra[1] ?? palabra[2]);
  if (/€/.test(texto)) return "euros";
  if (/\$/.test(texto)) return "$";
  return null;
}

/** El texto sin monedas que la persona no dijo. Con `moneda` = una palabra suya, la moneda distinta se cambia por la
 * suya; con null o "$", la cifra queda sola. Solo toca monedas pegadas a una cifra o tras "en". */
export function limpiarMonedaNoDicha(texto: string, moneda: string | null): { texto: string; cambios: number } {
  const suya = moneda && moneda !== "$" ? moneda : null;
  let cambios = 0;
  const distinta = (m: string) => canonica(m) !== suya;
  let out = texto.replace(new RegExp(`\\s+en\\s+(${PLURALES}|${COD})(?![${L}])`, "giu"), (todo, m: string) => {
    if (!distinta(m)) return todo;
    cambios += 1;
    return suya ? ` en ${suya}` : "";
  });
  out = out.replace(new RegExp(`(\\d[\\d.,]*)\\s+(${PLURALES}|${SINGULARES}|${COD})(?![${L}])`, "giu"), (todo, cifra: string, m: string) => {
    if (!distinta(m)) return todo;
    cambios += 1;
    return suya ? `${cifra} ${suya}` : cifra;
  });
  return { texto: out, cambios };
}
