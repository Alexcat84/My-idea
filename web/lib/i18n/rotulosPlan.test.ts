/**
 * i18n F5 (DISENO §5): los MARCADORES NEUTROS del plan. Lo que se guarda lleva
 * siempre los rótulos de estructura en español ("## Etapa N:", "**Esta
 * semana:**", "_Plan completo_"...), porque eso es lo que leen checklist.ts y
 * planParser.ts. La pantalla y los documentos los pintan en el idioma de quien
 * lee. Si la IA los tradujo pese a la regla, se devuelven a su forma neutra
 * antes de guardar.
 */
import { describe, expect, it } from "vitest";
import { neutralizarRotulos, pintarRotulos, rotulosPlan } from "./rotulosPlan";
import { derivarChecklist } from "../engine/checklist";

const NEUTRO = [
  "_Plan completo_",
  "",
  "# 화분 판매 계획",
  "",
  "## Etapa 1: 수요 확인",
  "",
  "**Pasos:**",
  "1. 5명에게 물어보세요.",
  "",
  "**Entregable:** 명단",
  "",
  "**Esta semana:** 가격을 올리세요.",
  "",
  "## ¿Puede sostenerse tu idea? Los números en simple",
  "",
  "**El lunes que viene:** 표를 만드세요.",
  "",
  "## Lo que este plan aún no cubre",
  "- 고객 검증",
].join("\n");

describe("pintarRotulos: del neutro al idioma de quien lee", () => {
  it("en español no cambia nada", () => {
    expect(pintarRotulos(NEUTRO, "es")).toBe(NEUTRO);
  });

  it("en coreano pinta cada rótulo con el catálogo y deja el contenido intacto", () => {
    const esperado = [
      "_전체 계획_",
      "",
      "# 화분 판매 계획",
      "",
      "## 1단계: 수요 확인",
      "",
      "**진행 순서:**",
      "1. 5명에게 물어보세요.",
      "",
      "**결과물:** 명단",
      "",
      "**이번 주:** 가격을 올리세요.",
      "",
      "## 아이디어가 지속될 수 있을까요? 쉽게 보는 숫자",
      "",
      "**다음 월요일:** 표를 만드세요.",
      "",
      "## 이 계획이 아직 다루지 않는 것",
      "- 고객 검증",
    ].join("\n");
    expect(pintarRotulos(NEUTRO, "ko")).toBe(esperado);
  });

  it("en francés, con el espacio de no separación (U+00A0) antes de los dos puntos, como en sus catálogos", () => {
    const md = "## Etapa 2: Vérifie la demande\n\n**Esta semana:** appelle trois clients.";
    expect(pintarRotulos(md, "fr")).toBe("## Étape 2\u00a0: Vérifie la demande\n\n**Cette semaine\u00a0:** appelle trois clients.");
  });

  it("en japonés, con los dos puntos de ancho completo", () => {
    expect(pintarRotulos("## Etapa 3: 需要を確かめる", "ja")).toBe("## ステージ3：需要を確かめる");
  });

  it("una etiqueta de pasos con complemento (del español) se pinta como la de pasos", () => {
    expect(pintarRotulos("**Pasos para construir:**", "en")).toBe("**Steps:**");
  });
});

describe("neutralizarRotulos: si la IA tradujo los rótulos, vuelven al neutro", () => {
  it("coreano traducido → neutro", () => {
    expect(neutralizarRotulos(pintarRotulos(NEUTRO, "ko"))).toBe(NEUTRO);
  });

  it.each(["en", "pt", "fr", "de", "it", "ja", "zh", "ko", "ar", "hi"] as const)("%s: ida y vuelta sin pérdida", (l) => {
    expect(neutralizarRotulos(pintarRotulos(NEUTRO, l))).toBe(NEUTRO);
  });

  it("un rótulo en inglés escrito por la IA con otros dos puntos también vuelve", () => {
    expect(neutralizarRotulos("## Stage 1 — Find buyers\n**This week**: call them")).toBe(
      "## Etapa 1: Find buyers\n**Esta semana:** call them"
    );
  });

  it("el neutro queda igual", () => {
    expect(neutralizarRotulos(NEUTRO)).toBe(NEUTRO);
  });

  it("el checklist sale igual de un plan traducido una vez neutralizado", () => {
    const items = derivarChecklist(neutralizarRotulos(pintarRotulos(NEUTRO, "de")));
    expect(items.map((i) => i.texto)).toEqual(["5명에게 물어보세요.", "가격을 올리세요."]);
    expect(items[1].destacado).toBe(true);
  });
});

describe("rotulosPlan", () => {
  it("toma las palabras de los catálogos (una sola fuente)", () => {
    const en = rotulosPlan("en");
    expect(en.estaSemana).toBe("This week");
    expect(en.etiquetaCompleto).toBe("Full plan");
  });
});
