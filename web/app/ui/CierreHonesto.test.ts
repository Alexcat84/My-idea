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

  it("si se devolvió la activación, lo DICE (el usuario pagó por ese mundo)", () => {
    expect(pintar({ unlockRevertido: true })).toContain("Tu activación quedó devuelta");
  });

  it("sin reembolso no promete uno", () => {
    expect(pintar({ unlockRevertido: false })).not.toContain("activación quedó devuelta");
  });

  it("el cierre core también habla: el mensaje viene del servidor, no se inventa aquí", () => {
    const html = pintar({
      mensaje: "Tu idea queda guardada tal como está: vuelve cuando quieras y seguimos desde aquí.",
      unlockRevertido: false,
    });
    expect(html).toContain("Tu idea queda guardada tal como está");
  });

  it("se anuncia a los lectores de pantalla (aria-live): un cierre no es decorado", () => {
    expect(pintar()).toContain('aria-live="polite"');
  });
});
