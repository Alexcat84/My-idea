// AUD-09 B05 (tanda 7B, confianza): la pantalla del límite decía "5 arranques
// al día" fijo, aunque el número real sale de LIMITE_ARRANQUES_DIA; y su botón
// "Ver planes" llevaba a la portada, donde no hay planes que ver. El mensaje
// dice el límite real y el botón lleva a las ideas guardadas.
import { readFileSync } from "node:fs";
import path from "node:path";
import { execSync } from "node:child_process";
import { describe, expect, it } from "vitest";
import { mensajeLimite } from "./rateLimit";

describe("el límite dice su número real (AUD-09 B05)", () => {
  it("con el número que corre, en singular y plural", () => {
    expect(mensajeLimite(3)).toBe(
      "Por hoy alcanzaste el límite de la beta (3 arranques al día). Tus ideas quedan guardadas. Vuelve mañana y seguimos donde quedamos."
    );
    expect(mensajeLimite(1)).toContain("(1 arranque al día)");
  });

  it("ninguna ruta usa el texto fijo", () => {
    const usos = execSync("git grep -l MENSAJE_LIMITE -- app lib || true", { cwd: path.join(__dirname, ".."), encoding: "utf8" })
      .split("\n")
      .filter((l) => l && !l.endsWith(".test.ts"));
    expect(usos).toEqual([]);
  });

  it("el botón de la pantalla del límite lleva a las ideas", () => {
    const nueva = readFileSync(path.join(__dirname, "..", "app", "nueva", "page.tsx"), "utf8");
    expect(nueva).not.toMatch(/Ver planes/);
    expect(nueva).toMatch(/router\.push\("\/ideas"\)[\s\S]{0,200}Ir a mis ideas/);
  });
});
