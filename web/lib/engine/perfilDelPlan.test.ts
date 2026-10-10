/**
 * El camino de produccion del perfil del plan, compartido por la ruta del plan y por el guion de medicion (decision del
 * fundador, 9 oct 2026: la proxima medicion usa el camino de produccion). Antes la ruta lo armaba en linea y el guion
 * lo imitaba a mano: la primera medicion sumo el estado vivo de HOY y la segunda no sumo ninguno.
 */
import { describe, expect, it } from "vitest";
import { estadoVivoDeLaFoto, textoContextoProyecto, memoriaDe } from "./memoria";
import { perfilConEstadoVivoActual } from "./perfilDelPlan";

describe("perfilConEstadoVivoActual (AUD-09 H05, el mismo de la ruta del plan)", () => {
  it("en un plan de mundo que no es seguimiento, suma el estado vivo actual al perfil", () => {
    expect(perfilConEstadoVivoActual("Hace macetas.", { dominio: "quality", esSeguimiento: false, estadoVivoActual: "Vende 12 al mes." })).toBe(
      "Hace macetas.\nEstado actual del proyecto, más reciente que la exploración: Vende 12 al mes."
    );
  });

  it("no lo suma en el núcleo, en un seguimiento, sin estado vivo o si el perfil ya lo trae", () => {
    expect(perfilConEstadoVivoActual("P", { dominio: "core", esSeguimiento: false, estadoVivoActual: "E" })).toBe("P");
    expect(perfilConEstadoVivoActual("P", { dominio: "quality", esSeguimiento: true, estadoVivoActual: "E" })).toBe("P");
    expect(perfilConEstadoVivoActual("P", { dominio: "quality", esSeguimiento: false, estadoVivoActual: null })).toBe("P");
    expect(perfilConEstadoVivoActual("P con E", { dominio: "quality", esSeguimiento: false, estadoVivoActual: "E" })).toBe("P con E");
  });
});

describe("estadoVivoDeLaFoto: el estado vivo que tenía el proyecto al abrir la sesión", () => {
  it("lo lee de la foto del contexto que arma textoContextoProyecto", () => {
    const foto = textoContextoProyecto(memoriaDe({}), { entradaOriginal: "Macetas", estadoVivo: "Vende 12 al mes por Instagram." });
    expect(estadoVivoDeLaFoto(foto)).toBe("Vende 12 al mes por Instagram.");
  });

  it("sin estado vivo o sin foto, null", () => {
    expect(estadoVivoDeLaFoto(textoContextoProyecto(memoriaDe({}), { entradaOriginal: "Macetas", estadoVivo: null }))).toBeNull();
    expect(estadoVivoDeLaFoto(null)).toBeNull();
  });
});
