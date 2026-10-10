// Ciclo de replanteamiento, Fase 2 (decisiones del fundador, 27 sep 2026;
// docs/producto/CICLO_REPLANTEAMIENTO.md). Las piezas PURAS del flujo
// "Replantear mi camino" y de lo común a los dos ciclos. Cada valor esperado
// está escrito a mano a partir del escenario, no copiado de la salida.
import { describe, expect, it } from "vitest";
import {
  componerMensajeReplanteamiento,
  filasHeredadas,
  planAnteriorParaIA,
  relatoDeCiclo,
  validarCaminos,
  type TareaCiclo,
} from "./replanteamiento";
import prompts from "../assets/prompts.json";

const conserva: TareaCiclo[] = [
  { id: "t1", texto: "Hablar con 5 panaderías", nota: "dos dijeron que sí", completed_at: "2026-09-10T15:00:00.000Z", etapa: 1 },
  { id: "t2", texto: "Calcular el costo por pieza", nota: null, completed_at: "2026-09-12T15:00:00.000Z", etapa: 2 },
];
const suelta: TareaCiclo[] = [{ id: "t3", texto: "Rentar un local", nota: null, completed_at: "2026-09-14T15:00:00.000Z", etapa: 3 }];

describe("componerMensajeReplanteamiento: la historia primero, y la orden de no empezar de cero", () => {
  it("historia, lo que se conserva, lo que se suelta, lo pendiente y el bloque de realidad, en ese orden", () => {
    const msg = componerMensajeReplanteamiento({
      historia: "  El local se cayó y ahora vendo por encargo.  ",
      conserva,
      suelta,
      pendientes: [{ etapa: 3, texto: "Pintar el local", destacado: false, estado: "pendiente" }],
      bloqueRealidad: "Mi realidad medida: ciclo 2.",
    });
    expect(msg).toBe(
      [
        "Quiero replantear mi camino. Esto es lo que pasó:",
        "El local se cayó y ahora vendo por encargo.",
        "",
        "Lo que ya construí y ME SIGUE SIRVIENDO (2). No lo repitas, construye encima:",
        "- Hablar con 5 panaderías (nota: dos dijeron que sí)",
        "- Calcular el costo por pieza",
        "Lo que ya construí y YA NO APLICA (1). No lo vuelvas a proponer:",
        "- Rentar un local",
        "Lo que quedaba pendiente del plan anterior (1):",
        "- Pintar el local",
        "",
        "Mi realidad medida: ciclo 2.",
        "",
        "No empieces de cero: parte de lo que ya tengo.",
      ].join("\n")
    );
  });

  it("sin nada hecho ni pendiente, solo la historia y la orden final", () => {
    const msg = componerMensajeReplanteamiento({ historia: "Cambié de ciudad.", conserva: [], suelta: [], pendientes: [], bloqueRealidad: null });
    expect(msg).toBe(
      ["Quiero replantear mi camino. Esto es lo que pasó:", "Cambié de ciudad.", "", "No empieces de cero: parte de lo que ya tengo."].join("\n")
    );
  });
});

describe("validarCaminos: dos o tres, cada uno anclado a conceptos que el código ofreció", () => {
  const candidatos = ["n1", "n2", "n3", "n4", "n5", "n6"];

  it("filtra los conceptos inventados, quita repetidos, recorta a 5 y numera a, b, c", () => {
    const caminos = validarCaminos(
      {
        caminos: [
          { titulo: " Vender por encargo ", descripcion: "Sin local.", nodos: ["n1", "inventado", "n1", "n2"] },
          { titulo: "Feria", descripcion: "Un puesto.", nodos: ["n3", "n4", "n5", "n6", "n2", "n1"] },
          { titulo: "Sin conceptos", descripcion: "x", nodos: ["nada"] },
          { titulo: "", descripcion: "sin título", nodos: ["n1"] },
        ],
      },
      candidatos
    );
    // 1.º: n1, n2 (inventado fuera, n1 repetido fuera). 2.º: los primeros 5 de 6.
    // 3.º sin conceptos válidos y 4.º sin título: fuera.
    expect(caminos).toEqual([
      { id: "a", titulo: "Vender por encargo", descripcion: "Sin local.", nodos: ["n1", "n2"] },
      { id: "b", titulo: "Feria", descripcion: "Un puesto.", nodos: ["n3", "n4", "n5", "n6", "n2"] },
    ]);
  });

  it("nunca más de tres, y basura da lista vacía", () => {
    const uno = { titulo: "T", descripcion: "D", nodos: ["n1"] };
    expect(validarCaminos({ caminos: [uno, uno, uno, uno] }, candidatos).map((c) => c.id)).toEqual(["a", "b", "c"]);
    expect(validarCaminos(null, candidatos)).toEqual([]);
    expect(validarCaminos({ caminos: "no" }, candidatos)).toEqual([]);
  });
});

describe("planAnteriorParaIA: las etapas del plan anterior con sus tareas y su estado", () => {
  const md = ["# Pan", "", "## Etapa 1: Valida", "texto", "## Etapa 2: Cuenta", "texto", "## ¿Puede sostenerse tu idea?", "x"].join("\n");

  it("agrupa por etapa con el título del markdown, en orden", () => {
    const plan = planAnteriorParaIA(md, [
      { etapa: 2, texto: "Costo por pieza", estado: "pendiente", nota: null },
      { etapa: 1, texto: "Hablar con 5", estado: "hecho", nota: "dos sí" },
      { etapa: 1, texto: "Anotar objeciones", estado: "no_aplica", nota: null },
    ]);
    // REDACTOR_CON_RESPALDO punto 5 (visto del fundador, 9 oct 2026): de cada tarea viaja su estado y la nota de la
    // persona, nunca el texto de la tarea (era una frase del plan anterior, no un dato de la persona).
    expect(plan).toEqual({
      etapas: [
        {
          numero: 1,
          titulo: "Valida",
          tareas: [{ estado: "hecho", nota: "dos sí" }, { estado: "no_aplica" }],
        },
        { numero: 2, titulo: "Cuenta", tareas: [{ estado: "pendiente" }] },
      ],
    });
  });

  it("caso real (M2A-f007-2, M3A-f003-4): el texto de una tarea inventada no viaja al plan nuevo", () => {
    const plan = planAnteriorParaIA(md, [
      { etapa: 1, texto: "Anota si la feria local de agosto te sirve para probar el precio", estado: "pendiente", nota: null },
      { etapa: 1, texto: "Pregunta a tres compradores", estado: "hecho", nota: "Dos dijeron que lo pagarían" },
    ]);
    const enviado = JSON.stringify(plan);
    expect(enviado).not.toContain("feria");
    expect(enviado).not.toContain("Pregunta a tres compradores");
    expect(enviado).toContain("Dos dijeron que lo pagarían");
  });

  it("caso real (medición final, f003): de cada tarea hecha o retirada viaja el título del tema del que salió, nunca su texto", () => {
    // La persona retiró "multiplica tus horas por el valor de tu hora" y el seguimiento la volvió a proponer: sin el
    // texto, el redactor no sabía qué tema ya estaba hecho o retirado. Ahora recibe el título del nodo (decisión del
    // fundador, 10 oct 2026), resuelto con su etiqueta de árbol.
    const titulos: Record<string, string> = { hoja_estimacion_costos: "Calcula tu Costo Real", margen_bruto: "Mide tu Margen" };
    const plan = planAnteriorParaIA(
      md,
      [
        { etapa: 1, texto: "Multiplica tus horas por el valor de tu hora", estado: "no_aplica", nota: "ya lo tengo", nodos_origen: ["hoja_estimacion_costos"] },
        { etapa: 1, texto: "Calcula tu margen", estado: "hecho", nota: null, nodos_origen: ["margen_bruto"] },
        { etapa: 2, texto: "Anota la feria de agosto", estado: "pendiente", nota: null, nodos_origen: ["margen_bruto"] },
      ],
      (id) => titulos[id] ?? null
    );
    expect(plan!.etapas[0].tareas).toEqual([
      { estado: "no_aplica", nota: "ya lo tengo", temas: ["Calcula tu Costo Real"] },
      { estado: "hecho", temas: ["Mide tu Margen"] },
    ]);
    expect(plan!.etapas[1].tareas).toEqual([{ estado: "pendiente" }]);
    const enviado = JSON.stringify(plan);
    expect(enviado).not.toContain("Multiplica tus horas");
    expect(enviado).not.toContain("feria");
  });

  it("las reglas que leen el plan anterior lo describen así (el plan y los caminos del replanteo)", () => {
    for (const nombre of ["SYSTEM_PLAN", "SYSTEM_CAMINOS"] as const) {
      const p = (prompts as Record<string, string>)[nombre];
      expect(p).toMatch(/sin el texto de las tareas/);
      expect(p).toMatch(/nota de la persona/);
    }
  });

  it("sin plan anterior, null", () => {
    expect(planAnteriorParaIA(null, [])).toBeNull();
    expect(planAnteriorParaIA("", [])).toBeNull();
  });
});

describe("filasHeredadas: lo que me sigue sirviendo entra al plan nuevo como hecho", () => {
  it("etapa 1, antes que las tareas nuevas, hechas, con su fecha, su nota y el enlace a la original", () => {
    // Dos conservadas: órdenes -2 y -1, para ir antes del orden 0 de las nuevas.
    expect(filasHeredadas(conserva)).toEqual([
      {
        etapa: 1,
        orden: -2,
        texto: "Hablar con 5 panaderías",
        destacado: false,
        estado: "hecho",
        completed_at: "2026-09-10T15:00:00.000Z",
        nota: "dos dijeron que sí",
        heredado_de: "t1",
      },
      {
        etapa: 1,
        orden: -1,
        texto: "Calcular el costo por pieza",
        destacado: false,
        estado: "hecho",
        completed_at: "2026-09-12T15:00:00.000Z",
        nota: null,
        heredado_de: "t2",
      },
    ]);
  });
});

describe("relatoDeCiclo: lo que la persona escribió, para la bitácora, el Expediente y la Historia", () => {
  it("replantear: su historia; profundizar: lo que contó y hacia dónde; nada escrito: null", () => {
    expect(relatoDeCiclo({ tipo: "replantear", historia: " Se cayó el local. ", conserva: [], suelta: [], caminos: [], caminoElegido: null })).toBe(
      "Se cayó el local."
    );
    expect(relatoDeCiclo({ tipo: "profundizar", detalles: "Vendí 10.", enfoque: "precios" })).toBe("Vendí 10.\nprecios");
    expect(relatoDeCiclo({ tipo: "profundizar", detalles: null, enfoque: "  " })).toBeNull();
    expect(relatoDeCiclo(undefined)).toBeNull();
  });
});
