// AUD-09 (tanda 5): con la idea realizada, Manos a la Obra seguía ofreciendo el
// "Ciclo de profundización" (un seguimiento pagado) y "¿Tu idea ya es un
// proyecto?" (un segundo cierre). El mundo ya los ocultaba con !completado; el
// núcleo no. La ruta del follow ya lo rechaza; la pantalla no debe ofrecerlo.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";

const f = readFileSync(path.join(__dirname, "ManosALaObra.tsx"), "utf8");

describe("Manos a la Obra con la idea realizada", () => {
  it("deriva un estado de núcleo cerrado de realizadaAt", () => {
    expect(f).toMatch(/const nucleoCerrado = Boolean\(realizadaAt\)/);
  });
  it("el ciclo de profundización del núcleo (móvil y escritorio) y el acta se ocultan cerrada", () => {
    // (8 oct 2026: profundizar, replantear y cerrar abren su propio espacio; las
    // tarjetas ya no esperan a que el ritual esté cerrado, porque abierto el
    // ritual el hub ni se pinta. La ruta tampoco abre nada con la idea realizada:
    // accionEspacioPropio.test.tsx.)
    expect(f).toMatch(/core && cCore\.total > 0 && !nucleoCerrado && \(/);
    expect(f).toMatch(/\{!nucleoCerrado && \(\s*<div className="hidden lg:block">/);
    expect(f).toMatch(/cCore\.total > 0 && !nucleoCerrado && \(\s*<TarjetaAcceso\s+icono="realizar"/);
  });
});
