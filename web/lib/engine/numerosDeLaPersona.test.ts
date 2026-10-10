/**
 * NUMEROS POR CODIGO (decision del fundador, 9 oct 2026, REDACTOR_CON_RESPALDO.md punto 2). Las cifras de la persona
 * le llegaban al redactor en la prosa del perfil y la IA deducia que eran: "12 macetas al mes por Instagram" se leyo
 * como su venta total (M2A-f006-1, M2B-f002-2, M3A-f014-1) y un costo con su hora incluida como costo de materiales.
 * Ahora llegan en dos bloques armados por codigo: numeros_de_la_persona (cada cifra con lo que dijo, su alcance y lo
 * que NO es) y calculos (lo que la calculadora ya hizo y lo que falta). La IA no deduce cifras.
 *
 * Calculos a mano (regla de AGENTS.md: el valor esperado sale de aqui, no de la funcion):
 *   costo por unidad = materiales + horas x valor hora = 68 + 2 x 31 = 68 + 62 = 130
 *   margen por unidad = precio - costo = 250 - 130 = 120; porcentaje = 120 / 250 = 0,48 = 48 %
 *   punto de equilibrio: falta costos_fijos_mensuales -> pendiente
 *   con costos fijos de 1.000: 1.000 / 120 = 8,33 -> 9 unidades al mes (hacia arriba)
 */
import { describe, expect, it } from "vitest";
import { alcanceDe, calculosDelPlan, numerosDeLaPersona } from "./numerosDeLaPersona";
import { cargarFamilies } from "../readiness";
import { cargarGrafo } from "./graph";
import { prepararPlan } from "./planRedactor";
import prompts from "../assets/prompts.json";

const NUMEROS = {
  unidades_vendidas: { valor: 12, unidad: "macetas", texto_original: "Vendo unas 12 macetas al mes por Instagram" },
  costo_materiales_unidad: { valor: 68, unidad: null, texto_original: "Cada maceta le cuesta unos 68 en materiales (cemento, moldes y pintura)" },
  horas_por_unidad: { valor: 2, unidad: "horas", texto_original: "le lleva un par de horas entre mezclar, moldear y pulir" },
  valor_hora: { valor: 31, unidad: null, texto_original: "mi hora la valoro en 31" },
  precio_tentativo: { valor: 250, unidad: null, texto_original: "las vendo a 250" },
};

describe("alcanceDe: el alcance que dice la frase de la persona", () => {
  it("caso real: «Vendo unas 12 macetas al mes por Instagram» es de un canal y de un período", () => {
    expect(alcanceDe("Vendo unas 12 macetas al mes por Instagram")).toEqual({ canal: "Instagram", periodo: "al mes", tamano: null, incluyeTiempo: false });
  });
  it("un costo con su hora incluida (caso real aad2749d)", () => {
    expect(alcanceDe("ya sé mi costo real por pieza: 130 incluyendo mi hora a 50").incluyeTiempo).toBe(true);
  });
  it("tamaño y canal en la tienda", () => {
    const a = alcanceDe("las medianas las vendo a 300 en la tienda de plantas");
    expect(a.tamano).toBe("medianas");
    expect(a.canal).toBe("la tienda de plantas");
  });
  it("una frase sin alcance", () => {
    expect(alcanceDe("las vendo a 250")).toEqual({ canal: null, periodo: null, tamano: null, incluyeTiempo: false });
  });
});

describe("numerosDeLaPersona: cada cifra con lo que dijo, su alcance y lo que no es", () => {
  const filas = numerosDeLaPersona(NUMEROS);
  const de = (campo: string) => filas.find((f) => f.campo === campo)!;

  it("las 12 macetas son las de Instagram al mes, no su venta total", () => {
    const f = de("unidades_vendidas");
    expect(f.valor).toBe("12 macetas");
    expect(f.lo_que_dijo).toBe("Vendo unas 12 macetas al mes por Instagram");
    expect(f.alcance).toEqual(["canal: Instagram", "período: al mes"]);
    expect(f.que_no_es).toContain("no es su venta total por todos sus canales: es solo lo de Instagram");
  });

  it("el costo de materiales no incluye su tiempo", () => {
    expect(de("costo_materiales_unidad").que_no_es).toContain("no incluye su tiempo de trabajo");
  });

  it("un costo guardado como materiales pero que incluye su tiempo se dice tal cual", () => {
    const f = numerosDeLaPersona({ costo_materiales_unidad: { valor: 130, unidad: null, texto_original: "130 incluyendo mi hora a 50" } })[0];
    expect(f.alcance).toContain("incluye su tiempo");
    expect(f.que_no_es).toContain("no es solo materiales: según lo que dijo, incluye su tiempo");
  });

  it("un rango se escribe como rango", () => {
    expect(numerosDeLaPersona({ precio_tentativo: { valor: { min: 200, max: 250 }, unidad: null, texto_original: "entre 200 y 250" } })[0].valor).toBe(
      "de 200 a 250"
    );
  });

  it("sin números, lista vacía; los campos que no conoce no entran", () => {
    expect(numerosDeLaPersona(null)).toEqual([]);
    expect(numerosDeLaPersona({ otra_cosa: { valor: 3 } })).toEqual([]);
  });
});

describe("calculosDelPlan: lo que la calculadora ya hizo y lo que falta", () => {
  const c = calculosDelPlan(NUMEROS);
  const de = (que: string) => c.find((x) => x.que === que)!;

  it("costo por unidad: 68 + 2 x 31 = 130 (a mano, arriba)", () => {
    expect(de("costo por unidad")).toMatchObject({ estado: "calculado", valor: "130" });
  });
  it("margen por unidad: 250 - 130 = 120, el 48 % del precio", () => {
    expect(de("margen por unidad")).toMatchObject({ estado: "calculado", valor: "120 (48 % del precio)" });
  });
  it("punto de equilibrio: pendiente, falta el costo fijo del mes", () => {
    expect(de("punto de equilibrio")).toMatchObject({ estado: "pendiente", falta: ["costos fijos del mes"] });
  });
  it("con costos fijos de 1.000: 1.000 / 120 = 8,33, se necesitan 9 al mes", () => {
    const con = calculosDelPlan({ ...NUMEROS, costos_fijos_mensuales: { valor: 1000, unidad: null, texto_original: "pago 1000 al mes" } });
    expect(con.find((x) => x.que === "punto de equilibrio")).toMatchObject({ estado: "calculado", valor: "9 unidades al mes" });
  });
});

describe("el redactor recibe los dos bloques y la regla", () => {
  it("prepararPlan pone numeros_de_la_persona y calculos en el payload cuando hay números", () => {
    const prep = prepararPlan(["punto_equilibrio_unidades"], cargarGrafo(), cargarFamilies(), "idea", "perfil", null, false, null, null, {
      numeros: NUMEROS,
    });
    expect(prep.payload.numeros_de_la_persona?.find((f) => f.campo === "unidades_vendidas")?.alcance).toContain("canal: Instagram");
    expect(prep.payload.calculos?.length).toBe(3);
  });

  it("sin números, el payload no lleva los bloques", () => {
    const prep = prepararPlan(["punto_equilibrio_unidades"], cargarGrafo(), cargarFamilies(), "idea", "perfil", null, false, null);
    expect(prep.payload.numeros_de_la_persona).toBeUndefined();
    expect(prep.payload.calculos).toBeUndefined();
  });

  it("SYSTEM_PLAN: las cifras del negocio son las de los bloques, con su alcance, y no se deducen", () => {
    expect(prompts.SYSTEM_PLAN).toMatch(/numeros_de_la_persona/);
    expect(prompts.SYSTEM_PLAN).toMatch(/no la conviertas en un total/);
    expect(prompts.SYSTEM_PLAN).toMatch(/un calculo pendiente se escribe como lo que falta averiguar/i);
  });
});
