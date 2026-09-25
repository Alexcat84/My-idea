// AUD-09 H12: la frase de la palanca de volumen podía decir "A null …",
// "unidads" y "— de ganancia". Una cifra que no existe no se escribe.
import { describe, expect, it } from "vitest";
import { pluralDe, textoPalanca } from "./TusNumeros";
import type { Palanca } from "@/lib/palancas";

const volumen = (meta: number | null, ganancia: number | null) =>
  ({ clave: "volumen", modo: "sano", bloqueada: false, meta, actual: null, gananciaResultante: ganancia, recomendada: true }) as unknown as Palanca;

describe("textoPalanca (volumen)", () => {
  it("el plural de la unidad es español: unidad -> unidades, pieza -> piezas", () => {
    expect(textoPalanca(volumen(44, 6300), "unidad")).toContain("44 unidades al mes");
    expect(textoPalanca(volumen(44, 6300), "pieza")).toContain("44 piezas al mes");
  });
  it("sin capacidad declarada no escribe 'null'", () => {
    const t = textoPalanca(volumen(null, null), "unidad");
    expect(t).not.toMatch(/null/);
    expect(t).toMatch(/por semana/);
  });
  it("sin gastos fijos no escribe '— de ganancia'", () => {
    const t = textoPalanca(volumen(44, null), "unidad");
    expect(t).not.toContain("—");
    expect(t).toContain("44 unidades al mes");
  });
});

// i18n F3: el plural de la unidad de venta sigue la regla de cada idioma (en
// F2 era solo la del español). Cada plural esperado está escrito a mano desde
// la gramática del idioma; los idiomas sin plural regular de sustantivo
// (de: "5 Stück", ja/zh/ko sin plural, ar/hi con plural irregular) dejan la
// unidad tal cual: mejor sin plural que con uno inventado.
describe("pluralDe por idioma (i18n F3)", () => {
  it("español, igual que antes (y el idioma por omisión)", () => {
    expect(pluralDe("vela")).toBe("velas");
    expect(pluralDe("lápiz", "es")).toBe("lápices");
    expect(pluralDe("pan", "es")).toBe("panes");
    expect(pluralDe("caja de velas", "es")).toBe("cajas de velas");
    expect(pluralDe("mes", "es")).toBe("mes");
  });
  it("inglés: +s, +es tras s/x/z/ch/sh, consonante+y -> ies; con 'of' la primera palabra, si no la última", () => {
    expect(pluralDe("candle", "en")).toBe("candles");
    expect(pluralDe("box", "en")).toBe("boxes");
    expect(pluralDe("batch", "en")).toBe("batches");
    expect(pluralDe("glass", "en")).toBe("glasses");
    expect(pluralDe("berry", "en")).toBe("berries");
    expect(pluralDe("day", "en")).toBe("days");
    expect(pluralDe("cup of coffee", "en")).toBe("cups of coffee");
    expect(pluralDe("candle kit", "en")).toBe("candle kits");
    expect(pluralDe("pants", "en")).toBe("pants");
  });
  it("portugués: +s, ão -> ões, m -> ns, l -> is, r/z -> es; la primera palabra", () => {
    expect(pluralDe("vela", "pt")).toBe("velas");
    expect(pluralDe("limão", "pt")).toBe("limões");
    expect(pluralDe("item", "pt")).toBe("itens");
    expect(pluralDe("jornal", "pt")).toBe("jornais");
    expect(pluralDe("colher", "pt")).toBe("colheres");
    expect(pluralDe("kit de velas", "pt")).toBe("kits de velas");
  });
  it("francés: +s, eau/au/eu -> +x, al -> aux, s/x/z sin cambio; la primera palabra", () => {
    expect(pluralDe("bougie", "fr")).toBe("bougies");
    expect(pluralDe("gâteau", "fr")).toBe("gâteaux");
    expect(pluralDe("journal", "fr")).toBe("journaux");
    expect(pluralDe("prix", "fr")).toBe("prix");
    expect(pluralDe("kit de bougies", "fr")).toBe("kits de bougies");
  });
  it("italiano: o -> i, a -> e (ca -> che, ga -> ghe), e -> i; las extranjeras sin cambio", () => {
    expect(pluralDe("vaso", "it")).toBe("vasi");
    expect(pluralDe("torta", "it")).toBe("torte");
    expect(pluralDe("barca", "it")).toBe("barche");
    expect(pluralDe("chiave", "it")).toBe("chiavi");
    expect(pluralDe("kit di candele", "it")).toBe("kit di candele");
  });
  it("alemán, japonés, chino, coreano, árabe e hindi: la unidad tal cual", () => {
    expect(pluralDe("Kerze", "de")).toBe("Kerze");
    expect(pluralDe("本", "ja")).toBe("本");
    expect(pluralDe("杯", "zh")).toBe("杯");
    expect(pluralDe("개", "ko")).toBe("개");
    expect(pluralDe("شمعة", "ar")).toBe("شمعة");
    expect(pluralDe("मोमबत्ती", "hi")).toBe("मोमबत्ती");
  });
});
