// I18N AL DÍA (encargo del fundador, 7 oct 2026), puntos 1 y 2. Prueba en rojo primero:
// - Los textos legales se sirven en el idioma de la persona si su traducción está publicada (el inglés, desde hoy;
//   las demás según las traduzcan), y si no, en español SIN aviso: el aviso "disponible en español y en francés"
//   (NAV.soloEsFr) se retira.
// - Preguntas frecuentes y Eliminar tu cuenta salen del catálogo en los once idiomas (no solo es, fr y en), con los
//   precios de precios.ts (regla P1) y el español sin cambiar de contenido.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { ACTIVE_LOCALES } from "@/lib/i18n/config";
import { PRECIOS } from "@/lib/precios";
import { CORREO_PRIVACIDAD, eliminarCuenta, idiomaLegal, navPublica, preguntasFrecuentes } from "./paginas";
import { TEXTOS_LEGALES, type DocumentoLegal } from "./textos";

const WEB = path.resolve(__dirname, "..", "..");
const leer = (rel: string) => readFileSync(path.join(WEB, rel), "utf-8");
const DOCUMENTOS: DocumentoLegal[] = ["privacidad", "terminos", "cookies"];

describe("los textos legales, en el idioma de la persona cuando su traducción existe", () => {
  it("el inglés lee el inglés en los tres documentos", () => {
    for (const doc of DOCUMENTOS) {
      expect(idiomaLegal("en", doc)).toBe("en");
      expect(TEXTOS_LEGALES[doc].en).toMatch(/^# My Idea /);
    }
  });

  it("el español y el francés siguen leyendo el suyo", () => {
    for (const doc of DOCUMENTOS) {
      expect(idiomaLegal("es", doc)).toBe("es");
      expect(idiomaLegal("fr", doc)).toBe("fr");
    }
  });

  it("cualquier otro idioma lee su traducción si está publicada y, si no, el español", () => {
    for (const doc of DOCUMENTOS)
      for (const idioma of ACTIVE_LOCALES)
        expect(idiomaLegal(idioma, doc)).toBe(TEXTOS_LEGALES[doc][idioma] !== undefined ? idioma : "es");
    expect(idiomaLegal("xx", "privacidad")).toBe("es");
  });

  it("el aviso «disponible en español y en francés» ya no existe en ninguna parte", () => {
    for (const rel of [
      "lib/legal/paginas.ts",
      "app/ui/PaginaPublica.tsx",
      "app/privacidad/page.tsx",
      "app/terminos/page.tsx",
      "app/cookies/page.tsx",
    ])
      expect(leer(rel)).not.toContain("soloEsFr");
  });
});

describe("Preguntas frecuentes y Eliminar tu cuenta, en los once idiomas", () => {
  it("las páginas toman el idioma de la persona, sin reducirlo a es, fr o en", () => {
    for (const rel of ["app/preguntas-frecuentes/page.tsx", "app/eliminar-cuenta/page.tsx", "app/ui/PaginaPublica.tsx"])
      expect(leer(rel)).not.toMatch(/idiomaDePagina|IdiomaPagina/);
  });

  it("en español, la respuesta del calendario dice una sola vía y cada varias horas", () => {
    const r = preguntasFrecuentes("es").items[8].r;
    expect(r).toMatch(/una sola vía/);
    expect(r).toMatch(/cada varias horas/);
    expect(r).toMatch(/Google Calendar/);
  });

  it("cada idioma tiene su texto propio y los precios salen de precios.ts", () => {
    const es = preguntasFrecuentes("es");
    for (const idioma of ACTIVE_LOCALES) {
      const p = preguntasFrecuentes(idioma);
      const e = eliminarCuenta(idioma);
      const todo = JSON.stringify([p, e, navPublica(idioma)]);
      expect(todo).not.toContain("{{");
      // 10 desde el 8 oct 2026: la respuesta del calendario (una sola vía y la
      // actualización cada varias horas de las apps que suscriben).
      expect(p.items).toHaveLength(10);
      expect(p.items[8].r, idioma).toMatch(/Google/);
      expect(p.items[2].r).toContain(String(PRECIOS.plan_completo));
      expect(p.items[2].r).toContain(String(PRECIOS.seguimiento));
      expect(e.sinAcceso).toContain(CORREO_PRIVACIDAD);
      expect(p.items[8].p.length, idioma).toBeGreaterThan(10);
      if (idioma !== "es") {
        expect(p.titulo).not.toBe(es.titulo);
        expect(e.titulo).not.toBe(eliminarCuenta("es").titulo);
      }
    }
  });

  it("el español no cambia de contenido", () => {
    // Las frases de antes del catálogo, copiadas de lib/legal/paginas.ts tal como estaban (con los precios de
    // precios.ts en su sitio, como las armaba el código de antes).
    const p = preguntasFrecuentes("es");
    expect(p.titulo).toBe("Preguntas frecuentes");
    expect(p.intro).toBe("Lo que más nos preguntan. Si no encuentras tu respuesta, escríbenos a support@myideaproject.com.");
    expect(p.items[2].r).toBe(
      `Tu plan usa ${PRECIOS.plan_completo} créditos; cada ciclo de seguimiento o de replanteamiento, ${PRECIOS.seguimiento}; el plan de un mundo, ${PRECIOS.mundo_activar}. Solo se cobran cuando recibes lo prometido; si algo falla, no se cobra o se reembolsa.`,
    );
    const e = eliminarCuenta("es");
    expect(e.titulo).toBe("Cómo eliminar tu cuenta de My Idea");
    expect(e.sinAcceso).toBe(
      "Escríbenos desde el correo de tu cuenta a privacy@myideaproject.com con el asunto «Eliminar mi cuenta». Comprobaremos que la cuenta es tuya y la eliminaremos en un plazo máximo de 30 días.",
    );
    expect(e.sinCuenta).toBe("Las ideas escritas sin cuenta se borran solas a los 30 días sin actividad.");
    expect(navPublica("es").eliminar).toBe("Eliminar tu cuenta");
  });
});
