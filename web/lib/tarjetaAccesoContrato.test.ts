// "Todo separado" (T5, D6): CONTRATO DE UNIFORMIDAD de las seis tarjetas
// hermanas. Ninguna tarjeta de aside —ni acceso (bitácora · calendario ·
// análisis · documentos) ni acción (realizar/cerrar · ciclo de profundización)—
// vive fuera del componente único TarjetaAcceso, en el núcleo o en el mundo.
//
// Se escanea el FUENTE de ManosALaObra: el formato de BOTÓN viejo de esas
// tarjetas (el botón de acceso con acento y el de realizar con `done`) no debe
// existir; todas pasan por el mismo componente. Si alguien vuelve a inline-ar
// una tarjeta con su propio botón, este test cae — es el lint que pidió D6.
import { readFileSync } from "node:fs";
import { describe, expect, it } from "vitest";

const fuente = readFileSync(new URL("../app/ui/ManosALaObra.tsx", import.meta.url), "utf8");

describe("TarjetaAcceso (T5, D6): las seis hermanas comparten UNA sola forma", () => {
  it("el componente único existe (icono + título + descripción, tarjeta entera)", () => {
    expect(fuente).toMatch(/function TarjetaAcceso\(/);
  });

  it("NINGUNA tarjeta de aside usa el formato de botón viejo (acento o done)", () => {
    // El botón de acceso viejo: `border border-accent/50 py-2.5 ... text-accent`.
    expect(fuente).not.toMatch(/border border-accent\/50 py-2\.5/);
    // El botón de "marcar realizada/completado" viejo: `border border-done/50 py-2.5`.
    expect(fuente).not.toMatch(/border border-done\/50 py-2\.5/);
  });

  it("los accesos y las acciones se declaran TODOS vía <TarjetaAcceso> (núcleo + mundo)", () => {
    const usos = (fuente.match(/<TarjetaAcceso/g) ?? []).length;
    // 4 accesos núcleo + realizar + ciclo(móvil) + ciclo(desktop) = 7;
    // 4 accesos mundo + ciclo + cerrar = 6. Total 13; el piso protege el contrato.
    expect(usos).toBeGreaterThanOrEqual(10);
  });
});
