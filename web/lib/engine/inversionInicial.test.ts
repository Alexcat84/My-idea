/**
 * INVERSION INICIAL Y GASTO FIJO MENSUAL, SEPARADOS (decision del fundador, 10 oct 2026, noche, punto 2c). Caso real de
 * las mediciones (fb027af0, filas 23 y 28): la persona conto los moldes dentro de su costo de materiales por maceta
 * («Cada maceta me cuesta como 68 en materiales -- cemento, moldes, pintura») y el plan los paso a gasto fijo
 * («lo que pagas aunque no hagas ninguna: herramientas, moldes...»), contandolos dos veces. El bloque de numeros que
 * recibe el redactor separa ahora la inversion inicial (moldes, herramientas: lo que se compra una vez) del gasto fijo
 * mensual, y avisa cuando algo ya va dentro del costo por unidad.
 */
import { describe, expect, it } from "vitest";
import { calculosDelPlan, numerosDeLaPersona } from "./numerosDeLaPersona";

// Cifras reales de fb027af0, con un precio que deja margen positivo para que el equilibrio quede pendiente de los fijos.
const BASE = {
  valor_hora: {
    valor: 17,
    texto_original: "Valoro mi hora de trabajo en unos 17",
  },
  horas_por_unidad: {
    valor: 2,
    texto_original: "le dedico un par de horas entre mezclar, moldear y pulir",
  },
  costo_materiales_unidad: {
    valor: 68,
    texto_original:
      "Cada maceta me cuesta como 68 en materiales -- cemento, moldes, pintura",
  },
  precio_tentativo: { valor: 150, texto_original: "Las vendo en 150" },
};

describe("el bloque de números separa la inversión inicial del gasto fijo mensual", () => {
  it("la definición de los costos fijos del mes deja fuera la inversión inicial", () => {
    const f = numerosDeLaPersona({
      ...BASE,
      costos_fijos_mensuales: {
        valor: 400,
        texto_original: "pago 400 al mes de renta",
      },
    });
    const fijos = f.find((x) => x.campo === "costos_fijos_mensuales")!;
    expect(fijos.que_no_es).toContain(
      "no es la inversión inicial (moldes, herramientas, equipo que compras una vez): esa va aparte y no entra en el punto de equilibrio del mes",
    );
  });

  it("caso real fb027af0: los moldes que dijo dentro de sus materiales ya van en su costo por unidad", () => {
    const f = numerosDeLaPersona(BASE);
    const mat = f.find((x) => x.campo === "costo_materiales_unidad")!;
    expect(mat.que_no_es).toContain(
      "lo que nombró dentro (moldes) ya va en este costo por unidad: no lo cuentes otra vez como gasto fijo ni como inversión",
    );
  });

  it("caso real fb027af0: con el equilibrio pendiente de los costos fijos, viaja la frase que separa las dos cosas", () => {
    // A mano: costo = 68 + 2 × 17 = 102; margen = 150 − 102 = 48 > 0; faltan los costos fijos del mes.
    const pe = calculosDelPlan(BASE)[2];
    expect(pe).toMatchObject({
      estado: "pendiente",
      falta: ["costos fijos del mes"],
    });
    expect(pe.frase).toBe(
      "Para el punto de equilibrio falta saber tus gastos fijos del mes: lo que pagas cada mes aunque no vendas, como renta, servicios o suscripciones. Lo que compras una vez para empezar, como herramientas o equipo, es inversión inicial: va aparte y no entra en esa cuenta. Tus moldes ya van dentro de tu costo por unidad: no los sumes otra vez.",
    );
  });

  it("sin moldes en lo que dijo, la frase pone los moldes como ejemplo de inversión inicial", () => {
    const pe = calculosDelPlan({
      ...BASE,
      costo_materiales_unidad: {
        valor: 68,
        texto_original: "68 en materiales",
      },
    })[2];
    expect(pe.frase).toBe(
      "Para el punto de equilibrio falta saber tus gastos fijos del mes: lo que pagas cada mes aunque no vendas, como renta, servicios o suscripciones. Lo que compras una vez para empezar, como moldes, herramientas o equipo, es inversión inicial: va aparte y no entra en esa cuenta.",
    );
  });

  it("si falta otra cosa además de los costos fijos, no hay frase: se pide lo que falta como siempre", () => {
    const pe = calculosDelPlan({ costo_materiales_unidad: { valor: 68 } })[2];
    expect(pe.estado).toBe("pendiente");
    expect(pe.frase).toBeUndefined();
  });
});
