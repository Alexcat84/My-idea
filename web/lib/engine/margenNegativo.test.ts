/**
 * MARGEN NEGATIVO (decision del fundador, 10 oct 2026, punto 2). Caso real de la tercera medicion final (fb027af0, f004,
 * contrario sostenido): «Con las cifras que me diste, tu costo de hacer una maceta, contando tu hora, es mayor que lo
 * que cobras. Hay un número que aún no sabes y es el que decide cuántas macetas necesitas vender cada mes.» Con margen
 * negativo no hay punto de equilibrio: vender mas agranda la perdida. La seccion la escribe la IA, asi que el codigo le
 * entrega la frase ya resuelta (calculosDelPlan): primero hay que corregir precio o costo, y nunca que los costos fijos
 * (ni otro dato que falte) deciden cuantas unidades vender.
 */
import { describe, expect, it } from "vitest";
import { calculosDelPlan } from "./numerosDeLaPersona";
import prompts from "../assets/prompts.json";

// Las cifras reales de fb027af0 (numeros_que_dio).
const FB027AF0 = {
  valor_hora: {
    valor: 17,
    unidad: "USD",
    texto_original: "Valoro mi hora de trabajo en unos 17",
  },
  horas_por_unidad: {
    valor: 2,
    unidad: "horas",
    texto_original: "le dedico un par de horas entre mezclar, moldear y pulir",
  },
  precio_tentativo: {
    valor: 85,
    unidad: "USD",
    texto_original:
      "Las vendo en 85 cada una, mas o menos, dependiendo del tamano.",
  },
  unidades_vendidas: {
    valor: 15,
    unidad: "ventas",
    texto_original: "ya tengo unas 15 ventas reales",
  },
  costo_materiales_unidad: {
    valor: 68,
    unidad: "USD",
    texto_original: "Cada maceta me cuesta como 68 en materiales",
  },
};

describe("calculosDelPlan con margen negativo", () => {
  it("caso real fb027af0: el punto de equilibrio no aplica y viaja la frase resuelta, sin pedir los costos fijos", () => {
    // A mano: costo = 68 + 2 × 17 = 102; margen = 85 − 102 = −17 (−17/85 = −20 % del precio). Faltan los costos fijos,
    // pero con margen negativo no deciden nada: no hay cantidad que cubra los gastos.
    const c = calculosDelPlan(FB027AF0);
    expect(c[0]).toMatchObject({
      que: "costo por unidad",
      estado: "calculado",
      valor: "102",
    });
    expect(c[1]).toMatchObject({
      que: "margen por unidad",
      estado: "calculado",
      valor: "-17 (-20 % del precio)",
    });
    const pe = c[2];
    expect(pe.que).toBe("punto de equilibrio");
    expect(pe.estado).toBe("no_aplica");
    expect(pe.falta).toBeUndefined();
    expect(pe.frase).toBe(
      "Hoy cada unidad te cuesta más de lo que cobras (pierdes 17 por unidad): vender más no cubre tus gastos, agranda la pérdida. Antes de calcular cuántas unidades vender, primero hay que subir el precio o bajar el costo por unidad.",
    );
  });

  it("con los costos fijos dados y margen cero, tampoco hay punto de equilibrio: la misma salida", () => {
    // A mano: costo = 50 + 1 × 30 = 80; margen = 80 − 80 = 0. Con margen 0 ninguna cantidad cubre 400 de fijos.
    const c = calculosDelPlan({
      costo_materiales_unidad: { valor: 50 },
      horas_por_unidad: { valor: 1 },
      valor_hora: { valor: 30 },
      precio_tentativo: { valor: 80 },
      costos_fijos_mensuales: { valor: 400 },
    });
    expect(c[2].estado).toBe("no_aplica");
    expect(c[2].frase).toBe(
      "Hoy cada unidad te deja 0 de margen: vender más no cubre tus gastos. Antes de calcular cuántas unidades vender, primero hay que subir el precio o bajar el costo por unidad.",
    );
  });

  it("con margen en rango que puede quedar en cero o negativo: la frase lo dice y pide asegurar el precio primero", () => {
    // A mano: costo = 60 + 1 × 20 = 80; precio de 70 a 100 → margen de 70 − 80 = −10 a 100 − 80 = 20.
    const c = calculosDelPlan({
      costo_materiales_unidad: { valor: 60 },
      horas_por_unidad: { valor: 1 },
      valor_hora: { valor: 20 },
      precio_tentativo: { valor: { min: 70, max: 100 } },
    });
    expect(c[1]).toMatchObject({ estado: "calculado" });
    expect(c[1].valor).toMatch(/^de -10 a 20/);
    expect(c[2].estado).toBe("no_aplica");
    expect(c[2].frase).toBe(
      "Con tus números, el margen por unidad va de -10 a 20: en el extremo bajo no te queda nada o pierdes. Antes de calcular cuántas unidades vender, primero hay que asegurar un precio por encima del costo por unidad.",
    );
  });

  it("con margen positivo, nada cambia: el punto de equilibrio sigue pendiente de los costos fijos", () => {
    // A mano: costo = 68 + 2 × 17 = 102; precio 150 → margen 48. Sin costos fijos, falta ese dato.
    const c = calculosDelPlan({
      ...FB027AF0,
      precio_tentativo: { valor: 150 },
    });
    expect(c[2]).toMatchObject({
      estado: "pendiente",
      falta: ["costos fijos del mes"],
    });
    expect(c[2].frase).toBeUndefined();
  });

  it("SYSTEM_PLAN 4-ter: un cálculo con frase se escribe tal cual, y si el equilibrio no aplica nunca deciden los costos fijos", () => {
    expect(prompts.SYSTEM_PLAN).toMatch(
      /un calculo con frase se escribe con esa frase, tal cual/,
    );
    expect(prompts.SYSTEM_PLAN).toMatch(/nunca digas que los costos fijos/);
  });
});
