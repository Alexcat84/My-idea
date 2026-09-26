// "TU AVANCE" (decisión del fundador, 26 sep 2026): el punto animado de
// "estás aquí" se queda en el hito actual y la línea termina ahí; las etapas
// que faltan se ven en gris después, sin fecha y sin latido. La meta con la
// celebración sigue saliendo solo con el cierre real.
import { renderToStaticMarkup } from "react-dom/server";
import { describe, expect, it } from "vitest";
import { hitosDeEspacio } from "@/lib/hitosEspacio";
import { LineaAvance } from "./LineaAvance";

const html = (h: ReturnType<typeof hitosDeEspacio>) => renderToStaticMarkup(<LineaAvance hitos={h} />);

describe("LineaAvance muestra lo que falta en gris", () => {
  const soloChispa = hitosDeEspacio({ espacio: "core", chispaAt: "2026-01-01T00:00:00Z", claridadAt: null, planAt: null, realizadaAt: null });

  it("las tres etapas que faltan aparecen, marcadas como pendientes", () => {
    const s = html(soloChispa);
    for (const e of ["La Chispa", "Claridad", "Tu Plan", "El cierre"]) expect(s).toContain(e);
    expect(s.match(/data-pendiente="true"/g)?.length).toBe(3);
  });

  it("el latido queda en el hito actual (uno solo) y no en una pendiente", () => {
    const s = html(soloChispa);
    expect(s.match(/anima-halo-viva/g)?.length).toBe(1);
    const iLatido = s.indexOf("anima-halo-viva");
    const iPrimeraPendiente = s.indexOf('data-pendiente="true"');
    expect(iLatido).toBeLessThan(iPrimeraPendiente);
  });

  it("sin cierre real no hay celebración; con cierre real, sí, y nada pendiente", () => {
    expect(html(soloChispa)).not.toContain("🎉");
    const cerrado = hitosDeEspacio({ espacio: "core", chispaAt: "2026-01-01T00:00:00Z", claridadAt: "2026-01-02T00:00:00Z", planAt: "2026-01-03T00:00:00Z", realizadaAt: "2026-02-01T00:00:00Z" });
    const s = html(cerrado);
    expect(s).toContain("🎉");
    expect(s).not.toContain('data-pendiente="true"');
  });
});
