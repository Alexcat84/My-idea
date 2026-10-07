// Auditoría final, promesas públicas M1 a M6 y B1 a B5 (informe del 1 oct 2026,
// docs/auditoria_final/informes/promesas_publicas.md), en la portada y en /nueva:
// el texto no promete lo que la app no hace. Lo gratis es ordenar la idea (la
// Claridad) y el diagnóstico de cada mundo; el plan usa créditos y solo se cobra
// si se entrega; rehacerlo es un ciclo que se pide; sin cuenta la idea no se
// guarda para siempre; el dictado depende del navegador; las preguntas salen de
// un banco que se adapta, no "sin plantillas"; y la app da método, no el resultado.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { PRECIOS } from "../precios";
import { LOCALES } from "./config";
import { NUEVA_IDEA } from "./mensajes/nuevaIdea";
import { PORTADA } from "./mensajes/portada";

/** Todas las cadenas de un catálogo de un idioma, con su ruta. */
function textos(x: unknown, ruta = ""): Array<[string, string]> {
  if (typeof x === "string") return [[ruta, x]];
  if (x && typeof x === "object") return Object.entries(x).flatMap(([k, v]) => textos(v, ruta ? `${ruta}.${k}` : k));
  return [];
}

const ambos = (l: (typeof LOCALES)[number]) => [...textos(PORTADA[l], "portada"), ...textos(NUEVA_IDEA[l], "nuevaIdea")];

// M3: las preguntas salen de un banco que se adapta (y con una plantilla neutral de
// salida segura), así que "sin plantillas" no se promete en ningún idioma.
const PLANTILLAS = /plantilla|template|modèle|modelo|Vorlage|modell[oi]|テンプレート|模板|템플릿|قالب|قوالب|टेम्पलेट/i;
// A3/M5: sin cuenta, la idea se borra a los 30 días sin actividad.
const PARA_SIEMPRE = /para siempre|forever|pour toujours|à jamais|para sempre|für immer|per sempre|永遠|永久|永远|영원|إلى الأبد|हमेशा के लिए/i;
// M2: BANCO §6 prohíbe "reemplaza a un consultor"; la portada tampoco se compara con uno.
const CONSULTOR = /consultor|consultant|Berater|consulente|コンサルタント|顾问|컨설턴트|مستشار|सलाहकार/i;
// B5: lo que se suma son mundos, no "módulos".
const MODULOS = /m[óo]dulo|module|modul|モジュール|模块|모듈|وحدات|मॉड्यूल/i;
// B4: el micrófono solo aparece si el navegador soporta la Web Speech API (CampoConVoz).
const NAVEGADOR = /navegador|browser|navigateur|ブラウザ|浏览器|브라우저|متصفّح|ब्राउज़र/i;

describe("la portada y /nueva no prometen lo que la app no hace (M1 a M6, B1 a B5)", () => {
  it("M3 y A3: ni 'plantillas' ni 'para siempre', en ningún idioma", () => {
    for (const l of LOCALES)
      for (const [ruta, t] of ambos(l)) {
        expect(t, `${l} ${ruta}`).not.toMatch(PLANTILLAS);
        expect(t, `${l} ${ruta}`).not.toMatch(PARA_SIEMPRE);
      }
  });

  it("M2 y B5: sin compararse con un consultor y sin 'módulos', en ningún idioma", () => {
    for (const l of LOCALES)
      for (const [ruta, t] of textos(PORTADA[l], "portada")) {
        expect(t, `${l} ${ruta}`).not.toMatch(CONSULTOR);
        expect(t, `${l} ${ruta}`).not.toMatch(MODULOS);
      }
  });

  it("M1 y B1: lo gratis es ordenar la idea, no 'comenzar' todo el viaje", () => {
    expect(PORTADA.es.comenzarGratis).toBe("Ordena tu idea gratis");
    expect(PORTADA.es.meta.descripcion).toMatch(/ordénala gratis/);
    expect(PORTADA.es.meta.descripcion).not.toMatch(/recibe tu plan y ejecútalo/);
  });

  it("B2: el plan dice su precio, que sale de precios.ts, y que solo se cobra si se entrega", () => {
    for (const l of LOCALES) expect(PORTADA[l].como.paso3.texto, l).toContain(String(PRECIOS.plan_completo));
    expect(PORTADA.es.como.paso3.texto).toBe(
      `Un plan detallado con etapas, experimentos y acciones concretas para ejecutarlo. Usa ${PRECIOS.plan_completo} créditos, que solo se cobran si lo recibes. Por ahora estamos en beta privada, por invitación.`
    );
    // Ninguna cifra de créditos escrita a mano en el catálogo (AGENTS.md): solo ${PLAN}.
    const fuente = readFileSync(path.join(__dirname, "mensajes", "portada.ts"), "utf8");
    expect(fuente).not.toMatch(/\d+\s*(?:créditos|credits|crédits|crediti|Punkte|ポイント|点|크레딧|من النقاط|क्रेडिट)/);
  });

  it("M4 y B3: rehacer el plan es un ciclo que se pide con créditos, sin 'pasos exactos'", () => {
    const { paso4 } = PORTADA.es.como;
    expect(paso4.demo).toBe("tu siguiente paso");
    expect(paso4.texto).toMatch(/nuevo ciclo con tus créditos/);
    for (const t of [paso4.demo, paso4.texto, PORTADA.es.acerca.parrafo2]) {
      expect(t).not.toMatch(/exact/);
      expect(t).not.toMatch(/recalcula/);
    }
    expect(PORTADA.en.como.paso4.demo).not.toMatch(/exact/i);
  });

  it("M5: volver cuando quieras es con tu cuenta", () => {
    expect(PORTADA.es.acerca.parrafo2).toMatch(/con tu cuenta, tu idea te espera tal como la dejaste/);
  });

  it("M6: la app acompaña hasta llevar la idea a la práctica, no promete verla funcionando", () => {
    expect(PORTADA.es.banda.texto).toMatch(/hasta llevarla a la práctica/);
    expect(PORTADA.es.banda.texto).not.toMatch(/funcionando/);
  });

  it("B4: todo texto que invita a dictar dice que depende del navegador, en los once idiomas", () => {
    for (const l of LOCALES)
      for (const [ruta, t] of [
        ["portada.como.paso1.texto", PORTADA[l].como.paso1.texto],
        ["portada.descargar.dictar", PORTADA[l].descargar.dictar],
        ["nuevaIdea.subtitulo", NUEVA_IDEA[l].subtitulo],
      ])
        expect(t, `${l} ${ruta}`).toMatch(NAVEGADOR);
    expect(NUEVA_IDEA.es.subtitulo).toBe(
      "Escríbela tal como la tienes en mente, o díctala si tu navegador lo permite. Ese es todo el requisito."
    );
  });
});
