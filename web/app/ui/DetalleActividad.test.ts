// Fase 4.3.2 — "Explorar actividad". Se prueba lo que tiene lógica: el chip de
// cumplimiento en TONO ESPEJO (la tardía en ámbar `text-warn`, jamás rojo) y sus
// bordes, y que el detalle renderiza sus secciones sin depender de jsdom
// (renderToStaticMarkup de react-dom, ya dependencia — la misma decisión de
// CierreHonesto: no traer testing-library para asertar que un texto aparece).
import { createElement } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it } from "vitest";
import { DetalleActividad } from "./DetalleActividad";
import type { ItemChecklistUI } from "./ManosALaObra";

const base: ItemChecklistUI = {
  id: "i1",
  plan_id: "p1",
  dominio: "core",
  etapa: 2,
  orden: 1,
  texto: "Identifica un mercado donde haya personas que no te conocen y agenda tu primera aparición.",
  destacado: false,
  estado: "pendiente",
  nota: null,
  completed_at: null,
  no_aplica_motivo: null,
  fecha_base: null,
  fecha_base_origen: null,
  fecha_base_original: null,
  created_at: "2026-07-01T10:00:00Z",
  updated_at: "2026-07-01T10:00:00Z",
};

function pintar(over: Partial<ItemChecklistUI>) {
  return renderToStaticMarkup(
    createElement(DetalleActividad, {
      item: { ...base, ...over },
      tituloEtapa: "Consigue tu primera venta real",
      ocupado: false,
      onCambio: () => {},
      onCerrar: () => {},
    })
  );
}

describe("DetalleActividad — el chip de cumplimiento es espejo (Fase 4.3.2)", () => {
  it("hecho tarde → 'Tardía · N días' en ÁMBAR (text-warn), jamás rojo", () => {
    // base 10-jul, hecho 14-jul → +4 días tarde.
    const html = pintar({
      fecha_base: "2026-07-10T12:00:00Z",
      completed_at: "2026-07-14T12:00:00Z",
      estado: "hecho",
    });
    expect(html).toContain("Tardía · 4 días");
    expect(html).toContain("text-warn");
    expect(html).not.toContain("text-red");
    expect(html.toLowerCase()).not.toContain("rojo");
  });

  it("hecho antes → 'Adelantada · N días' en azul (piensa/planea)", () => {
    // base 20-jul, hecho 17-jul → 3 días antes.
    const html = pintar({
      fecha_base: "2026-07-20T12:00:00Z",
      completed_at: "2026-07-17T12:00:00Z",
      estado: "hecho",
    });
    expect(html).toContain("Adelantada · 3 días");
    expect(html).toContain("text-accent");
  });

  it("|dif| ≤ 1 día → 'A tiempo' en verde", () => {
    const html = pintar({
      fecha_base: "2026-07-10T12:00:00Z",
      completed_at: "2026-07-11T00:00:00Z",
      estado: "hecho",
    });
    expect(html).toContain("A tiempo");
    expect(html).toContain("text-done");
  });

  it("sin fecha planificada → sin chip y sin sección de fecha", () => {
    const html = pintar({ fecha_base: null });
    expect(html).not.toContain("A tiempo");
    expect(html).not.toContain("Tardía");
    expect(html).not.toContain("Mover fecha");
  });

  it("con fecha → aparece 'Mover fecha' y la promesa de conservar la original", () => {
    const html = pintar({ fecha_base: "2026-08-07T12:00:00Z" });
    expect(html).toContain("Mover fecha");
    expect(html).toContain("se conserva en tu historia");
  });

  it("ya movida → dice cuál era la original (la historia no se reescribe)", () => {
    const html = pintar({
      fecha_base: "2026-08-07T12:00:00Z",
      fecha_base_original: "2026-07-31T12:00:00Z",
    });
    expect(html).toContain("Ya la moviste");
    expect(html).toContain("31 de julio");
  });

  it("siempre muestra el detalle: etapa, texto, estado, nota, y una salida", () => {
    const html = pintar({});
    expect(html).toContain("Detalle de la actividad");
    expect(html).toContain("Consigue tu primera venta real"); // etapa
    expect(html).toContain("Identifica un mercado"); // texto
    expect(html).toContain("Tu nota");
    expect(html).toContain("Registrar tu nota es gratis");
    expect(html).toContain('role="dialog"');
  });
});
