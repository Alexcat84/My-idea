// AUD-09 M11 (tanda 5, mezcla núcleo y mundos): el ritual de un mundo usaba la
// cadencia aprendida del NÚCLEO (su duración real por etapa). "Cero mezcla de
// medidas" (BANCO §7.1): cada espacio aprende de su propio ritmo.
import { readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { cadenciasPorEspacio } from "./fechasBase";

describe("cadenciasPorEspacio: cada espacio con la suya", () => {
  it("el núcleo y cada mundo aprenden de su propia duración por etapa", () => {
    // A MANO (cadencia = media de días por etapa / 7, redondeada, entre 1 y 6):
    //   núcleo: etapas de 21 y 21 días -> media 21 -> 3 semanas
    //   calidad: etapas de 7 días -> media 7 -> 1 semana
    const analytics = {
      universal: { duracionPorEtapa: [{ etapa: 1, dias: 21 }, { etapa: 2, dias: 21 }] },
      mundos: [{ dominio: "quality", universal: { duracionPorEtapa: [{ etapa: 1, dias: 7 }] } }],
    };
    expect(cadenciasPorEspacio(analytics)).toEqual({ core: 3, quality: 1 });
  });
});

describe("el ritual del mundo usa la cadencia del mundo", () => {
  it("Manos a la Obra pasa al panel del mundo la cadencia de SU espacio", () => {
    const f = readFileSync(path.join(__dirname, "..", "app", "ui", "ManosALaObra.tsx"), "utf8");
    expect(f).toMatch(/cadenciaSemanas=\{cadencias\[mundo\.dominio\] \?\? 1\}/);
  });
});
