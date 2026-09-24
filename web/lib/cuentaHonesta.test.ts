// AUD-09 M01 (tanda 5, conteos): las tareas retiradas (no_aplica) contaban en el
// total del encabezado, de los chips de mundo y de /ideas, mientras Manos a la
// Obra y el servidor contaban solo las activas: "3/10" contra "3/9" para lo
// mismo. BANCO §5: "X de N activas". Una sola cuenta.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { cuentaHonesta } from "./dbContract";

describe("cuentaHonesta: el denominador son las activas", () => {
  it("10 tareas, 1 retirada, 3 hechas: 3 de 9 activas y 1 retirada", () => {
    // A MANO: activas = 10 − 1 = 9; hechas entre las activas = 3.
    const items = [
      ...Array.from({ length: 3 }, () => ({ estado: "hecho" })),
      ...Array.from({ length: 6 }, () => ({ estado: "pendiente" })),
      { estado: "no_aplica" },
    ];
    expect(cuentaHonesta(items)).toEqual({ hechos: 3, total: 9, retiradas: 1 });
  });
});

describe("las tres superficies cuentan igual", () => {
  const leer = (rel: string) => readFileSync(path.join(__dirname, "..", rel), "utf8");
  it("el encabezado y los chips de mundo de la página de la idea", () => {
    const f = leer("app/idea/[id]/IdeaView.tsx");
    expect(f).toMatch(/cuentaHonesta\(itemsCore\)/);
    expect(f).not.toMatch(/total: items\.length/);
  });
  it("/ideas", () => {
    expect(leer("lib/ideas.ts")).toMatch(/cuentaHonesta|esActivo/);
  });
  it("Manos a la Obra", () => {
    expect(leer("app/ui/ManosALaObra.tsx")).toMatch(/cuentaHonesta\(/);
  });
});
