// Fase 4.3 §2 — el test del componente del cierre. Protege UNA promesa: cuando
// el motor sale, la pantalla NUNCA se queda muda.
//
// Nota de dependencias (docs/APK_READINESS.md §6, el freno): NO se añadió jsdom
// ni testing-library. `renderToStaticMarkup` viene de react-dom, que ya es
// dependencia, y alcanza de sobra para lo que hay que proteger: que el mensaje
// y las salidas ESTEN en la pantalla. Lo que no cubre (los clics) lo cubre el
// vuelo, que navega la UI de verdad. Una libreria nueva para asertar que un
// texto se renderiza habria sido justo la "conveniencia" que ese § prohibe.
import { createElement } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it } from "vitest";
import { CierreHonesto } from "./CierreHonesto";

const MENSAJE_MUNDO =
  "Calidad y Confianza está pensado para negocios con más estructura de la que tu proyecto " +
  "necesita hoy; te lo digo antes de hacerte perder tiempo.";

function pintar(props: Partial<Parameters<typeof CierreHonesto>[0]> = {}) {
  return renderToStaticMarkup(
    createElement(CierreHonesto, {
      mensaje: MENSAJE_MUNDO,
      hayPlan: true,
      onVolverAManos: () => {},
      onVerMundos: () => {},
      ...props,
    })
  );
}

describe("CierreHonesto — la pantalla jamás queda muda (Fase 4.3 §2)", () => {
  it("dice el mensaje del cierre, literal y completo", () => {
    expect(pintar()).toContain("está pensado para negocios con más estructura");
  });

  it("nunca es un cierre sin salidas: con plan, ofrece Manos a la Obra y los mundos", () => {
    const html = pintar({ hayPlan: true });
    expect(html).toContain("Volver a Manos a la Obra");
    expect(html).toContain("Ver los otros mundos");
  });

  it("sin plan todavía, la única salida honesta son los mundos", () => {
    const html = pintar({ hayPlan: false });
    expect(html).not.toContain("Volver a Manos a la Obra");
    expect(html).toContain("Ver los otros mundos");
  });

  // Fase 4.3.2 (regla de claims): la línea de reembolso cuelga de un evento del
  // ledger (creditosDevueltos), JAMÁS de un flag. Es una afirmación de dinero.
  it("con créditos DE VERDAD devueltos, lo dice con el monto", () => {
    expect(pintar({ creditosDevueltos: 3 })).toContain("Te devolvimos 3 créditos");
    expect(pintar({ creditosDevueltos: 1 })).toContain("Te devolvimos 1 crédito"); // singular
  });

  it("en beta (creditosDevueltos null) NO afirma ningún reembolso", () => {
    const html = pintar({ creditosDevueltos: null });
    expect(html).not.toContain("Te devolvimos");
    expect(html).not.toContain("crédito");
  });

  it("0 créditos tampoco afirma nada (no hubo consumo)", () => {
    expect(pintar({ creditosDevueltos: 0 })).not.toContain("Te devolvimos");
  });

  it("el cierre core también habla: el mensaje viene del servidor, no se inventa aquí", () => {
    const html = pintar({
      mensaje: "Tu idea queda guardada tal como está: vuelve cuando quieras y seguimos desde aquí.",
      creditosDevueltos: null,
    });
    expect(html).toContain("Tu idea queda guardada tal como está");
  });

  it("se anuncia a los lectores de pantalla (aria-live): un cierre no es decorado", () => {
    expect(pintar()).toContain('aria-live="polite"');
  });
});
