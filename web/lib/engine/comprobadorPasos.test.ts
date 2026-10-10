/**
 * COMPROBADOR PASO CONTRA NODO (decision del fundador, 10 oct 2026, punto 3). En la segunda medicion final quedaron tres
 * pasos que contradicen lo que enseña su tema (f001 8b7764c4: encargar la decision a otro como salida valida; f002
 * deb138a3: buscar un proveedor alterno cuando el tema enseña ir a uno solo y confiable; f016 fb027af0: moldes y empaques
 * como costos fijos cuando el tema clasifica los materiales como variables). Cada paso termina con la marca del tema del
 * que sale (⟦N:id⟧); el codigo la valida (solo que exista: un paso es una orden, no comparte palabras por fuerza) y la
 * guarda. Despues, una llamada compara cada paso solo con su tema: si lo contradice, el paso se quita, nunca se reescribe.
 * El codigo solo quita si las dos frases que chocan estan tal cual, la del tema en su tema y la del paso en el paso. Si la llamada falla, el plan
 * sale igual. Apagado salvo COMPROBADOR_PASOS=1.
 */
import { describe, expect, it } from "vitest";
import { validarCitas, type Respaldo } from "./citarOCallar";
import { comprobadorPasosActivo, comprobarPasos, quitarPasos, TOPE_QUITAR_PASOS } from "./comprobadorPasos";
import { usoVacio } from "../costmeter";
import prompts from "../assets/prompts.json";

const MEJORA = {
  id: "mejora_continua_del_proceso",
  etiqueta: "Mejora tu Proceso sin Pausa",
  pasos: ["Reducir progresivamente a un proveedor único por artículo mediante colaboración continua", "Medir cada mejora"],
  entregable: "Un proveedor confiable por artículo",
};
const RIESGOS = { id: "lista_riesgos", etiqueta: "Anota lo que Puede Salir Mal", pasos: ["Lista los riesgos", "Ordénalos por impacto"], entregable: "Una lista ordenada" };
const R: Respaldo = {
  respuestas: [{ id: "R1", texto: "Dependo de un solo proveedor de resina y no tengo colchón de dinero." }],
  nodos: [MEJORA, RIESGOS].map((m) => ({ id: m.id, textos: [m.etiqueta, ...m.pasos, m.entregable] })),
  cifras: [],
};

// Extracto real del plan deb138a3 (f002), con las marcas que pide ahora la regla 6-bis.
const PLAN = [
  "# Tu plan",
  "",
  "Tienes un solo proveedor de resina. ⟦R1⟧",
  "",
  "## Etapa 2: Decide cómo producir",
  "",
  "**Pasos:**",
  "1. Haz una lista de lo que podría salir mal en tu producción y ordénala por lo que más te dañaría. ⟦N:lista_riesgos⟧",
  "2. Busca un proveedor alterno de resina. ⟦N:mejora_continua_del_proceso⟧",
  "3. Define cuánto dinero necesitarías apartar si ese proveedor sube el precio. ⟦N:tema_inventado⟧",
  "",
  "**Entregable:** Una lista de riesgos.",
].join("\n");

describe("validarCitas: la marca final de un paso es su tema", () => {
  it("se valida solo que el tema exista (sin exigir palabras en común), se quita del texto y se guarda el par", () => {
    const r = validarCitas(PLAN, R);
    expect(r.texto).toContain("2. Busca un proveedor alterno de resina.");
    expect(r.texto).not.toMatch(/[⟦⟧]/);
    expect(r.pasosCitados).toEqual([
      { etapa: 2, numero: 1, nodos: ["lista_riesgos"] },
      { etapa: 2, numero: 2, nodos: ["mejora_continua_del_proceso"] },
    ]);
  });

  it("un tema que no vino en el material es una cita inventada: el paso sale como siempre (citar o callar), sin par", () => {
    const r = validarCitas(PLAN, R);
    expect(r.texto).not.toContain("Define cuánto dinero");
    expect(r.pasosCitados.some((p) => p.numero === 3)).toBe(false);
  });
});

describe("quitarPasos: quita la línea del paso y renumera su lista", () => {
  it("quita el 2.2 y el 3 pasa a ser 2", () => {
    const md = [
      "## Etapa 2: X",
      "",
      "**Pasos:**",
      "1. Haz una lista de lo que podría salir mal.",
      "2. Busca un proveedor alterno de resina.",
      "3. Define cuánto dinero necesitarías apartar.",
      "",
      "**Entregable:** Una lista.",
    ].join("\n");
    const out = quitarPasos(md, ["2.2"]);
    expect(out).not.toContain("proveedor alterno");
    expect(out).toContain("2. Define cuánto dinero necesitarías apartar");
    expect(out).toContain("1. Haz una lista de lo que podría salir mal");
  });
});

const clienteQueResponde = (texto: string, llamadas: unknown[] = []) =>
  ({
    messages: {
      create: async (req: unknown) => {
        llamadas.push(req);
        return { content: [{ type: "text", text: texto }], stop_reason: "end_turn", usage: { input_tokens: 1000, output_tokens: 100 } };
      },
    },
  }) as never;

describe("comprobarPasos", () => {
  const entrada = () => {
    const v = validarCitas(PLAN, R);
    return { markdown: v.texto, pasosCitados: v.pasosCitados, nodos: [MEJORA, RIESGOS] };
  };

  it("caso real f002: el paso que contradice a su tema se quita, sin reescribir nada más", async () => {
    const llamadas: unknown[] = [];
    const cliente = clienteQueResponde(
      JSON.stringify({ contradicen: [{ clave: "2.2", nodo: "mejora_continua_del_proceso", el_tema_dice: "Reducir progresivamente a un proveedor único por artículo", el_paso_dice: "Busca un proveedor alterno de resina", motivo: "El tema enseña ir a un proveedor único." }] }),
      llamadas
    );
    const r = await comprobarPasos(cliente, entrada(), usoVacio(), { presupuestoUsd: 5 });
    expect(r.fallo).toBeNull();
    expect(r.quitados).toEqual(["2.2"]);
    expect(r.markdown).not.toContain("proveedor alterno");
    expect(r.markdown).toContain("1. Haz una lista de lo que podría salir mal");
    // Cada paso viaja solo con su tema; el paso sin tema valido no se juzga.
    const enviado = JSON.stringify(llamadas[0]);
    expect(enviado).toContain("Busca un proveedor alterno de resina");
    expect(enviado).not.toContain("Tienes un solo proveedor");
  });

  it("si la frase del tema que se da como prueba no está en el tema tal cual, no se quita nada", async () => {
    const cliente = clienteQueResponde(
      JSON.stringify({ contradicen: [{ clave: "2.2", nodo: "mejora_continua_del_proceso", el_tema_dice: "Nunca tengas dos proveedores", el_paso_dice: "Busca un proveedor alterno de resina", motivo: "x" }] })
    );
    const r = await comprobarPasos(cliente, entrada(), usoVacio(), { presupuestoUsd: 5 });
    expect(r.quitados).toEqual([]);
    expect(r.ignorados).toBe(1);
    expect(r.markdown).toContain("proveedor alterno");
  });

  it("si la frase del paso que se da como prueba no está en el paso tal cual, tampoco se quita", async () => {
    const cliente = clienteQueResponde(
      JSON.stringify({ contradicen: [{ clave: "2.2", nodo: "mejora_continua_del_proceso", el_tema_dice: "Reducir progresivamente a un proveedor único por artículo", el_paso_dice: "Ten siempre tres proveedores", motivo: "x" }] })
    );
    const r = await comprobarPasos(cliente, entrada(), usoVacio(), { presupuestoUsd: 5 });
    expect(r.quitados).toEqual([]);
    expect(r.ignorados).toBe(1);
  });

  it("si la llamada falla, el plan sale igual y el fallo queda registrado", async () => {
    const cliente = { messages: { create: async () => { throw new Error("529 overloaded"); } } } as never;
    const e = entrada();
    const r = await comprobarPasos(cliente, e, usoVacio(), { presupuestoUsd: 5 });
    expect(r.markdown).toBe(e.markdown);
    expect(r.fallo).toMatch(/529/);
  });

  it(`si propone quitar más del ${TOPE_QUITAR_PASOS * 100} % de los pasos juzgados, no aplica nada y queda para revisión`, async () => {
    const cliente = clienteQueResponde(
      JSON.stringify({
        contradicen: [
          { clave: "2.1", nodo: "lista_riesgos", el_tema_dice: "Lista los riesgos", el_paso_dice: "Haz una lista de lo que podría salir mal", motivo: "x" },
          { clave: "2.2", nodo: "mejora_continua_del_proceso", el_tema_dice: "Reducir progresivamente a un proveedor único por artículo", el_paso_dice: "Busca un proveedor alterno de resina", motivo: "x" },
        ],
      })
    );
    const e = entrada();
    const r = await comprobarPasos(cliente, e, usoVacio(), { presupuestoUsd: 5 });
    expect(r.revision).toBe(true);
    expect(r.markdown).toBe(e.markdown);
  });

  it("sin pasos con tema, no llama", async () => {
    const llamadas: unknown[] = [];
    const r = await comprobarPasos(clienteQueResponde("{}", llamadas), { markdown: "# x", pasosCitados: [], nodos: [] }, usoVacio(), { presupuestoUsd: 5 });
    expect(llamadas).toHaveLength(0);
    expect(r.quitados).toEqual([]);
  });
});

describe("el redactor marca el tema de cada paso y el comprobador está apagado por defecto", () => {
  it("SYSTEM_PLAN 6-bis: cada paso termina con la marca del tema del que sale", () => {
    expect(prompts.SYSTEM_PLAN).toMatch(/Cada paso termina con la marca del tema del que sale/);
  });

  it("comprobadorPasosActivo: solo con COMPROBADOR_PASOS=1", () => {
    const antes = process.env.COMPROBADOR_PASOS;
    delete process.env.COMPROBADOR_PASOS;
    expect(comprobadorPasosActivo()).toBe(false);
    process.env.COMPROBADOR_PASOS = "1";
    expect(comprobadorPasosActivo()).toBe(true);
    if (antes === undefined) delete process.env.COMPROBADOR_PASOS;
    else process.env.COMPROBADOR_PASOS = antes;
  });
});
