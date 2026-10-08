// Decisión del fundador (8 oct 2026): un acceso directo para comprar y
// administrar los créditos (saldo, compras e historial). /creditos ya tenía el
// saldo y las recargas; aquí se prueba el historial: cómo se nombra cada
// movimiento del libro (credit_transactions), en los once idiomas, y que la
// página lo lea con el cliente de la persona (RLS: solo los suyos).
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { ACTIVE_LOCALES } from "./i18n/config";
import { CREDITOS } from "./i18n/mensajes/creditos";
import { etiquetaMovimiento, type Movimiento } from "./historialCreditos";
import { PRECIOS } from "./precios";

const t = CREDITOS.es.historial;
const mov = (over: Partial<Movimiento>): Movimiento => ({
  id: 1,
  delta: 0,
  saldo_resultante: 0,
  tipo: "consumo",
  concepto: null,
  origen: null,
  created_at: "2026-10-08T12:00:00Z",
  ...over,
});

describe("cómo se nombra cada movimiento", () => {
  it("una compra (grant de la tienda) es una compra de créditos", () => {
    expect(etiquetaMovimiento(mov({ tipo: "grant", origen: "revenuecat", delta: 30 }), t)).toBe(t.compra);
  });
  it("un grant sin tienda (cortesía, siembra de la beta) son créditos de regalo", () => {
    expect(etiquetaMovimiento(mov({ tipo: "grant", origen: "cortesia", delta: 20 }), t)).toBe(t.otorgados);
    expect(etiquetaMovimiento(mov({ tipo: "grant", origen: null, delta: 20 }), t)).toBe(t.otorgados);
  });
  it("un consumo se nombra por lo que pagó; uno desconocido, como uso", () => {
    expect(etiquetaMovimiento(mov({ concepto: "plan_completo", delta: -10 }), t)).toBe(t.conceptos.plan_completo);
    expect(etiquetaMovimiento(mov({ concepto: "mundo_replanteamiento", delta: -5 }), t)).toBe(t.conceptos.mundo_replanteamiento);
    expect(etiquetaMovimiento(mov({ concepto: "algo_raro", delta: -5 }), t)).toBe(t.consumo);
  });
  it("una devolución es una devolución", () => {
    expect(etiquetaMovimiento(mov({ tipo: "refund", concepto: "seguimiento", delta: 5 }), t)).toBe(t.devolucion);
  });
});

describe("en los once idiomas", () => {
  it.each([...ACTIVE_LOCALES])("%s: el historial tiene sus textos y un nombre para cada concepto de precios.ts", (idioma) => {
    const h = CREDITOS[idioma].historial;
    for (const k of ["titulo", "vacio", "noPudeLeer", "compra", "otorgados", "devolucion", "consumo", "saldoTras"] as const) {
      expect(h[k], `${idioma}.${k}`).toBeTruthy();
    }
    for (const c of Object.keys(PRECIOS)) expect((h.conceptos as Record<string, string>)[c], `${idioma}.${c}`).toBeTruthy();
  });
});

describe("la página /creditos", () => {
  const pagina = readFileSync(path.join(__dirname, "..", "app", "creditos", "page.tsx"), "utf8");
  it("lee el historial con el cliente de la persona y lo pinta con su ancla", () => {
    expect(pagina).toContain("leerHistorial(supabase");
    expect(pagina).toContain('id="historial"');
    expect(pagina).toContain("etiquetaMovimiento(");
  });
  it("si la lectura falla lo dice, en vez de pintar un historial vacío", () => {
    expect(pagina).toContain("th.noPudeLeer");
  });
});
