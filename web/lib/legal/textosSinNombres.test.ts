// Decisiones del fundador (8 oct 2026) sobre los textos legales, en los ONCE
// idiomas y sobre el texto tal como se publica (TEXTOS_LEGALES, que genera
// scripts/sync_legal_web.py):
//  1. Privacidad, sección 6: los proveedores por CATEGORÍAS (función y país),
//     sin nombres de empresas. Los nombres quedan solo en el inventario interno
//     (docs/legal/INVENTARIO_DATOS.md, que no se publica).
//  2. Sin símbolos: nada de "§6"; se dice "la sección 6".
//  3. Sección 7 (transferencias fuera de Quebec): describe la práctica y NO
//     anuncia trámites pendientes ni revisiones en curso.
//  4. Cookies: sin nombres técnicos ni proveedores; cada fila dice el tipo, para
//     qué sirve y cuánto dura; la de idioma ya no dice que llegará con varios
//     idiomas (la app YA está en once).
import { describe, expect, it } from "vitest";
import { ACTIVE_LOCALES } from "@/lib/i18n/config";
import { TEXTOS_LEGALES, type DocumentoLegal } from "./textos";

const DOCUMENTOS: DocumentoLegal[] = ["privacidad", "terminos", "cookies"];
const EMPRESAS = /\b(Anthropic|Claude|Voyage|Supabase|Vercel|Resend|Upstash|Google)\b/;
const TECNICOS = /sb-\*|PKCE|post_login_next|myidea_idioma|mi-idea:/;

/** El texto publicado de un documento en un idioma (falla si no está publicado). */
function texto(doc: DocumentoLegal, idioma: string): string {
  const t = TEXTOS_LEGALES[doc][idioma];
  expect(t, `${doc}/${idioma} no está publicado`).toBeTruthy();
  return t!;
}

/** El cuerpo de una sección "## N. ..." hasta la siguiente. */
function seccion(md: string, n: number): string {
  const inicio = md.search(new RegExp(`^## ${n}\\.`, "m"));
  expect(inicio, `falta la sección ${n}`).toBeGreaterThanOrEqual(0);
  const resto = md.slice(inicio + 3);
  const fin = resto.search(/^## \d+\./m);
  return fin < 0 ? resto : resto.slice(0, fin);
}

describe("los textos legales, en los once idiomas", () => {
  it.each([...ACTIVE_LOCALES])("%s: los tres documentos están publicados y sin el símbolo §", (idioma) => {
    for (const doc of DOCUMENTOS) expect(texto(doc, idioma), `${doc}/${idioma}`).not.toContain("§");
  });

  it.each([...ACTIVE_LOCALES])("%s: la privacidad y las cookies no nombran empresas", (idioma) => {
    expect(texto("privacidad", idioma)).not.toMatch(EMPRESAS);
    expect(texto("cookies", idioma)).not.toMatch(EMPRESAS);
  });

  it.each([...ACTIVE_LOCALES])("%s: la sección 6 es una tabla de categorías sin enlaces a políticas ajenas", (idioma) => {
    const s6 = seccion(texto("privacidad", idioma), 6);
    expect(s6).not.toMatch(/https?:\/\//);
    // siete categorías: IA, búsqueda semántica, base de datos y autenticación,
    // alojamiento, correos, control de uso, inicio de sesión externo
    const filas = s6.split("\n").filter((l) => l.startsWith("|") && !/^\|\s*-/.test(l));
    expect(filas.length, idioma).toBe(1 + 7);
  });

  it.each([...ACTIVE_LOCALES])("%s: las cookies sin nombres técnicos; seis filas de tipo, uso y duración", (idioma) => {
    const c = texto("cookies", idioma);
    expect(c).not.toMatch(TECNICOS);
    const filas = c.split("\n").filter((l) => l.startsWith("|") && !/^\|\s*-/.test(l));
    expect(filas.length, idioma).toBe(1 + 6);
    for (const f of filas) expect(f.split("|").filter((x) => x.trim()).length, f).toBe(3);
  });
});

describe("en español (la versión que prevalece junto al francés)", () => {
  const priv = TEXTOS_LEGALES.privacidad.es;
  const cookies = TEXTOS_LEGALES.cookies.es;

  it("la sección 6 nombra cada categoría con su país", () => {
    const s6 = seccion(priv, 6);
    for (const cat of [
      "proveedor de inteligencia artificial",
      "búsqueda semántica",
      "base de datos y autenticación",
      "alojamiento de la app",
      "envío de correos",
      "control de uso",
      "inicio de sesión con un proveedor externo",
    ]) expect(s6.toLowerCase(), cat).toContain(cat);
    expect(s6).toContain("Estados Unidos");
  });

  it("las referencias dicen 'la sección N'", () => {
    expect(priv).toMatch(/la sección 6/);
    expect(priv).toMatch(/la sección 8/);
  });

  it("la sección 7 describe la práctica, sin trámites ni revisiones pendientes", () => {
    const s7 = seccion(priv, 7);
    expect(s7).toMatch(/protecciones contractuales y de seguridad\s+adecuadas/);
    expect(s7).not.toMatch(/revisión|pendiente|evaluaci|en curso/i);
  });

  it("la sección 10 no repite la frase de la identidad invisible", () => {
    const s10 = seccion(priv, 10);
    expect(s10.split("Sin cuenta, queda con tu identidad invisible").length - 1).toBe(1);
  });

  it("cada fila de cookies dice su tipo; la de idioma dice que la app ya está en once idiomas", () => {
    const filas = cookies.split("\n").filter((l) => l.startsWith("|") && !/^\|\s*-/.test(l)).slice(1);
    for (const f of filas) expect(f, f).toMatch(/^\|\s*(necesaria|preferencia|almacenamiento local)\s*\|/);
    const idioma = filas.find((f) => /idioma/.test(f))!;
    expect(idioma).toMatch(/once idiomas/);
    expect(idioma).not.toMatch(/se activa|varios idiomas/);
  });
});

describe("en francés (vinculante)", () => {
  it("la sección 7 tampoco anuncia trámites", () => {
    const s7 = seccion(TEXTOS_LEGALES.privacidad.fr!, 7);
    expect(s7).not.toMatch(/révision|en cours|évaluation/i);
  });
});
