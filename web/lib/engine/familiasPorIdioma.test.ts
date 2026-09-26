// i18n F6: el respaldo por encabezados (familiasDesdeEncabezados) en los once
// idiomas, y ruidoso donde no puede leer.
//
// Contexto (F5_INFORME, "Lo que queda para F6"): si el plan llega sin su
// autodeclaración (el JSON de cola se cortó), la cobertura se decide leyendo
// los encabezados del markdown con las palabras clave de readiness.ts, que
// solo estaban en español. Un plan en otro idioma perdía la familia de
// "acción con clientes" EN SILENCIO y salía etiquetado como incompleto.
//
// Los planes guardan sus rótulos de estructura en español (marcadores neutros
// de F5: "## Etapa N:", la sección económica); lo que va después de "Etapa N:"
// está en el idioma de la idea. Cada caso de abajo es un encabezado escrito a
// mano en su idioma, como lo escribiría la IA, y lo esperado se decide
// leyéndolo: "Etapa 1: Interview ten real customers" habla de entrevistar
// clientes → accion_clientes sí; "Etapa 2: Design your logo" no → no.
import { describe, expect, it, vi } from "vitest";
import { familiasDesdeEncabezados, SECCION_ECONOMICA_TITULO } from "./planRedactor";

// El cuerpo de cada etapa va en el idioma del plan, como lo escribe la IA.
const planCon = (cuerpo: string, ...etapas: string[]) =>
  ["# Plan", "", ...etapas.flatMap((e, i) => [`## Etapa ${i + 1}: ${e}`, "", cuerpo, ""])].join("\n");
const plan = (...etapas: string[]) => planCon("Texto de la etapa.", ...etapas);

describe("familiasDesdeEncabezados en los once idiomas: acción con clientes", () => {
  it.each([
    ["en", "Interview ten real customers"],
    ["en", "Build a simple prototype and show it"],
    ["fr", "Mène des entretiens avec tes premiers clients"],
    ["fr", "Construis un prototype simple"],
    ["ko", "첫 고객 다섯 명과 인터뷰하기"],
    ["ko", "간단한 프로토타입 만들기"],
    ["ar", "إجراء مقابلات مع أول عملائكم"],
    ["ar", "بناء نموذج أولي بسيط"],
    ["pt", "Faça entrevistas com seus primeiros clientes"],
    ["de", "Führe Interviews mit echten Kunden"],
    ["it", "Fai interviste ai tuoi primi clienti"],
    ["ja", "最初のお客様にインタビューする"],
    ["zh", "与前五位客户进行访谈"],
    ["hi", "पहले ग्राहकों का इंटरव्यू लें"],
  ] as const)("%s: «%s» cuenta como acción con clientes", (idioma, etapa) => {
    const r = familiasDesdeEncabezados(plan(etapa, "—"), idioma);
    expect(r.tiene_accion_clientes).toBe(true);
  });

  it.each([
    ["en", "Design your logo"],
    ["fr", "Choisis le nom de ton entreprise"],
    ["ko", "로고 디자인하기"],
    ["ar", "تصميم الشعار"],
  ] as const)("%s: «%s» NO cuenta como acción con clientes", (idioma, etapa) => {
    const r = familiasDesdeEncabezados(plan(etapa), idioma);
    expect(r.tiene_accion_clientes).toBe(false);
  });
});

describe("familiasDesdeEncabezados en los once idiomas: viabilidad económica", () => {
  it.each([
    ["en", "Find your break-even point"],
    ["fr", "Calcule ton seuil de rentabilité"],
    ["ko", "손익분기점 계산하기"],
    ["ar", "احسبوا نقطة التعادل"],
    ["de", "Berechne deine Gewinnschwelle"],
    ["ja", "損益分岐点を計算する"],
  ] as const)("%s: «%s» cuenta como viabilidad económica", (idioma, etapa) => {
    const r = familiasDesdeEncabezados(plan(etapa), idioma);
    expect(r.tiene_viabilidad_economica).toBe(true);
  });

  it("la sección económica neutra (en español en todo idioma) sigue bastando", () => {
    const md = `${plan("Design your logo")}\n## ${SECCION_ECONOMICA_TITULO} Los números en simple\n\nNumbers.`;
    expect(familiasDesdeEncabezados(md, "en").tiene_viabilidad_economica).toBe(true);
  });

  it("un plan en inglés con las dos familias es completo, sin faltantes", () => {
    const r = familiasDesdeEncabezados(plan("Interview ten real customers", "Find your break-even point"), "en");
    expect(r.es_completa).toBe(true);
    expect(r.familias_faltantes).toEqual([]);
  });
});

describe("el español no cambia", () => {
  it("«Entrevista a tus clientes reales» sigue contando; «Introducción» no", () => {
    expect(familiasDesdeEncabezados(plan("Entrevista a tus clientes reales")).tiene_accion_clientes).toBe(true);
    expect(familiasDesdeEncabezados("# Mi Plan\n\n## Introduccion\n\nNada.").tiene_accion_clientes).toBe(false);
  });
});

describe("fallar ruidoso: lo que no se puede leer se dice", () => {
  it("un plan en un idioma fuera de los once (ruso) deja un evento con su idioma", () => {
    const eventos: Array<Record<string, unknown>> = [];
    const aviso = vi.spyOn(console, "warn").mockImplementation(() => {});
    const md = planCon("Здесь вы начинаете работу.", "Проведите интервью с первыми клиентами", "Рассчитайте точку безубыточности");
    familiasDesdeEncabezados(md, "en", (e) => eventos.push(e));
    expect(eventos).toContainEqual({ tipo: "respaldo_familias_sin_palabras", idioma: "ru" });
    aviso.mockRestore();
  });

  it("en uno de los once no hay evento (sí sabe leer)", () => {
    const eventos: Array<Record<string, unknown>> = [];
    familiasDesdeEncabezados(plan("첫 고객 다섯 명과 인터뷰하기"), "ko", (e) => eventos.push(e));
    expect(eventos).toEqual([]);
  });

  it("aunque la plantilla caiga a otro idioma, el del texto manda: un plan en coreano con interfaz en español se lee en coreano", () => {
    const eventos: Array<Record<string, unknown>> = [];
    const r = familiasDesdeEncabezados(planCon("이번 단계에서 할 일을 정리해요.", "첫 고객 다섯 명과 인터뷰하기"), "es", (e) => eventos.push(e));
    expect(r.tiene_accion_clientes).toBe(true);
    expect(eventos).toEqual([]);
  });
});
