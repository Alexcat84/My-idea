// AUD-09 M22 (tanda 7A, dinero): el ritual ("Ciclo de profundización") se abría
// sin consultar el saldo, y el 402 llegaba después de que el usuario escribía su
// "qué pasó". Contrato de fuente: toda puerta del ritual pasa por abrirRitual,
// que pregunta a GET follow antes de abrir el formulario.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";

const manos = readFileSync(path.join(__dirname, "ManosALaObra.tsx"), "utf8");

describe("el ritual consulta el saldo antes de abrirse (AUD-09 M22)", () => {
  it("ningún botón abre el ritual directo", () => {
    expect(manos).not.toMatch(/onClick=\{\(\) => setRitual\(true\)\}/);
    expect(manos).not.toMatch(/onClick=\{\(\) => setRitualMundo\(mundo\.dominio\)\}/);
  });

  it("abrirRitual pregunta a GET follow por el espacio y muestra el rechazo tal cual", () => {
    const fn = manos.match(/async function abrirRitual\([\s\S]*?\r?\n  \}\r?\n/)?.[0] ?? "";
    expect(fn).toMatch(/fetch\(`\/api\/project\/\$\{projectId\}\/follow\?dominio=\$\{encodeURIComponent\(dominio\)\}`\)/);
    expect(fn).toMatch(/leerRechazo\(res\)/);
  });
});
