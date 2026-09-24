// AUD-09 M12 (tanda 5, mezcla núcleo y mundos): una sola instancia de Manos a la
// Obra servía al núcleo y al hub de un mundo, sin `key`: "Ponerlas después",
// "Recalcular" y "cambiar modo" de un espacio aparecían en el otro. Cada espacio
// monta su propia instancia.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";

describe("cada espacio monta su propio Manos a la Obra", () => {
  it("la instancia lleva la llave de su espacio", () => {
    const f = readFileSync(path.join(__dirname, "IdeaView.tsx"), "utf8");
    expect(f).toMatch(/<ManosALaObra\s+key=\{espacioActivo\}/);
  });
});
