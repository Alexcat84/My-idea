/**
 * "MATERIAL" (decision del fundador, 9 oct 2026, REDACTOR_CON_RESPALDO.md punto 1). La ultima medicion sostuvo dos
 * procedencias: el redactor citaba su propio payload como fuente ("El material enseña que...", M3A-f015-1; "El material
 * de este plan no cubre...", M3A-f003-3). El payload y los prompts le llamaban "material" y el propio prompt le dictaba
 * "mi material es de negocio". Dos cambios: un nombre que no suena a fuente (temas_del_recorrido, temas_vecinos, "los
 * temas") y un filtro en el codigo que quita las frases que citan los temas como fuente, en los once idiomas.
 */
import { describe, expect, it } from "vitest";
import { cargarFamilies } from "../readiness";
import { cargarGrafo } from "./graph";
import { finalizarPlan, prepararPlan } from "./planRedactor";
import { quitarCitasDeFuente } from "./citasDeFuente";
import prompts from "../assets/prompts.json";
import { REGLA_SIN_FUENTES } from "../reglaSinFuentes";
import type { Locale } from "../i18n/config";

const graph = cargarGrafo();
const families = cargarFamilies();
const MATERIAL = /\bmaterial\b/i;

describe("el payload y los prompts no llaman 'material' a los temas", () => {
  it("el payload del redactor trae temas_del_recorrido y temas_vecinos, sin claves 'material'", () => {
    const prep = prepararPlan(["concierge_mvp", "punto_equilibrio_unidades"], graph, families, "mi idea", "perfil", null, false, null);
    const claves = Object.keys(prep.payload);
    expect(claves).toContain("temas_del_recorrido");
    expect(claves).toContain("temas_vecinos");
    expect(claves.filter((k) => k.includes("material"))).toEqual([]);
  });

  it.each(["SYSTEM_PLAN", "SYSTEM_INTERPRETE_MULTI", "SYSTEM_CAMINOS", "SYSTEM_DIAGNOSTICO_MUNDO", "SYSTEM_REPORTE", "SYSTEM_ORGANIZADOR"])(
    "%s no dice 'material' (los costos de materiales siguen siendo 'materiales')",
    (nombre) => {
      const p = (prompts as Record<string, string>)[nombre];
      expect(p).toBeTruthy();
      expect(p).not.toMatch(MATERIAL);
      expect(p).not.toMatch(/mi material|material_principal|material_de_apoyo/);
    }
  );

  it("la regla de toda llamada ya no le enseña la palabra: la prohíbe como fuente", () => {
    expect(REGLA_SIN_FUENTES).not.toMatch(/material que recibes/);
    expect(REGLA_SIN_FUENTES).toMatch(/'el material'/);
    expect(REGLA_SIN_FUENTES).toMatch(/la persona no sabe que existen/i);
  });
});

describe("quitarCitasDeFuente: el código quita los temas citados como fuente", () => {
  it("caso real M3A-f015-1: «El material enseña que X» queda como «X»", () => {
    const r = quitarCitasDeFuente(
      "El material enseña que la seguridad funciona cuando la gente participa, no cuando se le impone. Por eso empieza preguntándoles.",
      ["es"]
    );
    expect(r.texto).toBe("La seguridad funciona cuando la gente participa, no cuando se le impone. Por eso empieza preguntándoles.");
    expect(r.cambios).toBe(1);
  });

  it("caso real M3A-f003-3: la frase que solo habla de la fuente se quita entera", () => {
    const r = quitarCitasDeFuente(
      "Cambia la contraseña de tu correo. El material de este plan no cubre seguridad informática en detalle. Anota qué cuentas usas.",
      ["es"]
    );
    expect(r.texto).toBe("Cambia la contraseña de tu correo. Anota qué cuentas usas.");
  });

  it("«Según el material, X» queda como «X»", () => {
    expect(quitarCitasDeFuente("Según el material, conviene empezar por lo más barato.", ["es"]).texto).toBe(
      "Conviene empezar por lo más barato."
    );
  });

  it("el material físico no se toca (un taller de macetas habla de su material)", () => {
    for (const t of [
      "Si el material se agrieta al secar, anota la humedad del día.",
      "Tu material sale caro: anota cuánto gastas por tanda.",
      "Revisa que el material muestra grietas antes de pintar.",
    ]) {
      expect(quitarCitasDeFuente(t, ["es"])).toEqual({ texto: t, cambios: 0 });
    }
  });

  it("los temas citados como fuente tampoco pasan", () => {
    expect(quitarCitasDeFuente("Los temas de este plan recomiendan anotar cada venta. Anótala hoy.", ["es"]).texto).toBe(
      "Anótala hoy."
    );
  });

  const OTROS: Array<[Locale, string, string]> = [
    ["en", "The material teaches that safety works when people take part. Ask them first.", "Safety works when people take part. Ask them first."],
    ["fr", "Le contenu de ce plan ne couvre pas la sécurité informatique. Note tes comptes.", "Note tes comptes."],
    ["pt", "Segundo o material, convém começar pelo mais barato.", "Convém começar pelo mais barato."],
    ["de", "Das Material lehrt, dass Sicherheit mit Beteiligung funktioniert. Frag sie zuerst.", "Frag sie zuerst."],
    ["it", "Secondo il materiale, conviene partire dal più economico.", "Conviene partire dal più economico."],
    ["ja", "資料によると、安全は参加で機能します。まず聞いてください。", "まず聞いてください。"],
    ["zh", "根据资料，安全靠参与。先问问他们。", "先问问他们。"],
    ["ko", "자료에 따르면 안전은 참여로 작동합니다. 먼저 물어보세요.", "먼저 물어보세요."],
    ["ar", "وفقًا للمادة، تنجح السلامة بالمشاركة. اسألهم أولًا.", "اسألهم أولًا."],
    ["hi", "सामग्री के अनुसार सुरक्षा भागीदारी से चलती है। पहले उनसे पूछें।", "पहले उनसे पूछें।"],
  ];
  it.each(OTROS)("%s", (idioma, entrada, salida) => {
    expect(quitarCitasDeFuente(entrada, ["es", idioma]).texto).toBe(salida);
  });
});

describe("finalizarPlan pasa el filtro y deja el rastro", () => {
  it("el plan guardado no cita los temas como fuente", () => {
    const ruta = ["punto_equilibrio_unidades"];
    const prep = prepararPlan(ruta, graph, families, "mi idea", "perfil", null, false, null);
    const raw =
      "# Tu plan\n\n## Etapa 1: Ordena tus números\n\nEl material enseña que lo primero es medir. Anota tus costos.\n\n" +
      '===JSON===\n{"familias_tratadas": [], "etapas": {"1": ["punto_equilibrio_unidades"]}}';
    const eventos: Array<Record<string, unknown>> = [];
    const r = finalizarPlan(raw, prep, ruta, families, "mi idea", (e) => eventos.push(e));
    expect(r.markdown).not.toMatch(/el material/i);
    expect(r.markdown).toContain("Lo primero es medir. Anota tus costos.");
    expect(eventos.some((e) => e.tipo === "cita_de_fuente_interna")).toBe(true);
  });
});
