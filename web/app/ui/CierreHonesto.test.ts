// FASE B (canon 12) — el test del componente del cierre honesto. Protege las
// promesas: la pantalla NUNCA queda muda (ley 4.3 §2), el "porque" es la caja
// de vidrio (se pinta el motivo real cuando lo hay), el reembolso cuelga del
// ledger, las salidas core dependen del plan, y el payload viejo (solo cuerpo,
// sin titulo) no rompe nada (compat, amarre 1).
//
// Nota (docs/APK_READINESS.md §6): sin jsdom ni testing-library.
// renderToStaticMarkup basta para asertar que el texto y las salidas ESTAN;
// los clics los cubre el vuelo.
import { createElement } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it } from "vitest";
import { CierreHonesto } from "./CierreHonesto";

function pintar(props: Partial<Parameters<typeof CierreHonesto>[0]> = {}) {
  return renderToStaticMarkup(
    createElement(CierreHonesto, {
      tipo: "mundo",
      titulo: "Calidad y Confianza no es para esta idea, todavía.",
      cuerpo: "Exploré este mundo con lo que hay hoy y no encontré un subproyecto que te sume.",
      porque: null,
      hayPlan: true,
      onVolverAManos: () => {},
      onVolverAIdea: () => {},
      onExplorarOtroAngulo: () => {},
      onVerMundos: () => {},
      ...props,
    })
  );
}

describe("CierreHonesto (canon 12) — la pantalla jamás queda muda", () => {
  it("pinta el eyebrow, el título y el cuerpo del servidor", () => {
    const html = pintar();
    expect(html).toContain("Un alto honesto");
    expect(html).toContain("no es para esta idea, todav");
    expect(html).toContain("no encontré un subproyecto que te sume");
  });

  it("se anuncia a lectores de pantalla (aria-live)", () => {
    expect(pintar()).toContain('aria-live="polite"');
  });

  // Amarre 2: el "porque" es la caja de vidrio, el motivo REAL del intérprete.
  it("con motivo real, pinta la caja 'Por qué este mundo, no ahora' con ese texto", () => {
    const html = pintar({ tipo: "mundo", porque: "este mundo brilla cuando ya tienes clientes que vuelven" });
    expect(html).toContain("Por qué este mundo, no ahora");
    expect(html).toContain("este mundo brilla cuando ya tienes clientes que vuelven");
  });

  it("en el camino core, la caja se llama 'Lo que vi'", () => {
    const html = pintar({ tipo: "camino", porque: "no hay señal de demanda que sostenga las etapas" });
    expect(html).toContain("Lo que vi");
    expect(html).toContain("no hay señal de demanda que sostenga las etapas");
  });

  it("sin motivo (null), NO fabrica una caja de porqué", () => {
    const html = pintar({ porque: null });
    expect(html).not.toContain("Por qué este mundo");
    expect(html).not.toContain("Lo que vi");
  });

  // Salidas del canon: mundo vs camino, y el core condicionado al plan.
  it("mundo: ofrece Manos a la Obra y Ver los otros mundos", () => {
    const html = pintar({ tipo: "mundo" });
    expect(html).toContain("Volver a Manos a la Obra");
    expect(html).toContain("Ver los otros mundos");
    expect(html).toContain("Tu viaje principal sigue intacto");
  });

  it("camino CON plan: Volver a Manos a la Obra + Explorar otro ángulo", () => {
    const html = pintar({ tipo: "camino", hayPlan: true });
    expect(html).toContain("Volver a Manos a la Obra");
    expect(html).toContain("Explorar otro ángulo de la idea");
    expect(html).not.toContain("Volver a mi idea");
  });

  it("camino SIN plan (primera exploración): Volver a mi idea, no a Manos", () => {
    const html = pintar({ tipo: "camino", hayPlan: false });
    expect(html).toContain("Volver a mi idea");
    expect(html).not.toContain("Volver a Manos a la Obra");
  });

  // Amarre reembolso solo-con-ledger.
  it("con créditos DE VERDAD devueltos: chip + nota con el monto", () => {
    const html = pintar({ tipo: "mundo", creditosDevueltos: 3 });
    expect(html).toContain("Activación devuelta · 3 créditos");
    expect(html).toContain("Te devolvimos 3 créditos");
  });

  it("en beta (creditosDevueltos null) NO afirma ningún reembolso", () => {
    const html = pintar({ tipo: "mundo", creditosDevueltos: null });
    expect(html).not.toContain("Activación devuelta");
    expect(html).not.toContain("Te devolvimos");
  });

  it("0 créditos tampoco afirma nada (no hubo consumo)", () => {
    expect(pintar({ tipo: "mundo", creditosDevueltos: 0 })).not.toContain("Te devolvimos");
  });

  // Amarre 1: compat. Payload viejo/plano (solo cuerpo, sin título) no rompe.
  it("compat: sin título estructurado, pinta el cuerpo y no se queda mudo", () => {
    const html = pintar({ titulo: null, cuerpo: "Tu idea queda guardada tal como está: vuelve cuando quieras." });
    expect(html).toContain("Tu idea queda guardada tal como está");
    expect(html).toContain('aria-live="polite"');
  });
});
