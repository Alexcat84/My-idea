import { describe, expect, it, vi } from "vitest";
import { usoVacio } from "../costmeter";
import { cargarFamilies } from "../readiness";
import { cargarGrafo } from "./graph";
import {
  comprimirEstadoVivo,
  corregirCoherenciaCobertura,
  cosecharVecindario,
  ensamblarOffline,
  evaluacionDesdeAutodeclaracion,
  extraerTitulo,
  finalizarPlan,
  parsearAutodeclaracion,
  prepararPlan,
  SECCION_ECONOMICA_TITULO,
  type MaterialNodo,
} from "./planRedactor";

const graph = cargarGrafo();
const families = cargarFamilies();

describe("cosecharVecindario", () => {
  it("cosecha vecinos reales de la ruta, nunca nodos ya en la ruta", () => {
    const ruta = ["design_thinking_fundamentos"];
    const evaluacion = { tiene_accion_clientes: false, tiene_viabilidad_economica: false };
    const cosecha = cosecharVecindario(ruta, graph, families, evaluacion, "perfil de prueba", null, 10);
    expect(cosecha.length).toBeGreaterThan(0);
    for (const nid of cosecha) {
      expect(ruta).not.toContain(nid);
      expect(graph[nid]).toBeDefined();
    }
  });

  it("respeta el tope", () => {
    const ruta = ["design_thinking_fundamentos"];
    const evaluacion = { tiene_accion_clientes: true, tiene_viabilidad_economica: true };
    const cosecha = cosecharVecindario(ruta, graph, families, evaluacion, null, null, 2);
    expect(cosecha.length).toBeLessThanOrEqual(2);
  });

  it("reserva cupos para nodos afines a la prioridad_declarada antes del puntaje normal", () => {
    const ruta = ["design_thinking_fundamentos"];
    const vecino = graph["design_thinking_fundamentos"].nodos_siguientes?.[0];
    expect(vecino).toBeDefined();
    const tituloVecino = graph[vecino as string].titulo_concepto;
    const evaluacion = { tiene_accion_clientes: true, tiene_viabilidad_economica: true };
    const cosecha = cosecharVecindario(
      ruta,
      graph,
      families,
      evaluacion,
      null,
      { texto: tituloVecino, conteo: 2 },
      10
    );
    expect(cosecha[0]).toBe(vecino);
  });
});

describe("parsearAutodeclaracion", () => {
  it("separa el cuerpo del bloque ===JSON===", () => {
    const raw = '# Titulo\n\nCuerpo del plan.\n===JSON===\n{"familias_tratadas": ["accion_clientes"]}';
    const { cuerpo, autodeclaracion } = parsearAutodeclaracion(raw);
    expect(cuerpo).toBe("# Titulo\n\nCuerpo del plan.");
    expect(autodeclaracion?.familias_tratadas).toEqual(["accion_clientes"]);
  });

  it("sin el delimitador, devuelve el raw completo y autodeclaracion=null", () => {
    const raw = "# Titulo\n\nCuerpo sin bloque JSON.";
    const { cuerpo, autodeclaracion } = parsearAutodeclaracion(raw);
    expect(cuerpo).toBe(raw);
    expect(autodeclaracion).toBeNull();
  });

  it("con un bloque JSON invalido, devuelve el raw completo y autodeclaracion=null", () => {
    const raw = "# Titulo\n\nCuerpo.\n===JSON===\nesto no es json valido";
    const { cuerpo, autodeclaracion } = parsearAutodeclaracion(raw);
    expect(cuerpo).toBe(raw.trim());
    expect(autodeclaracion).toBeNull();
  });
});

describe("evaluacionDesdeAutodeclaracion", () => {
  it("es_completa solo si declara ambas familias tratadas", () => {
    expect(evaluacionDesdeAutodeclaracion({ familias_tratadas: ["accion_clientes", "viabilidad_economica"] }).es_completa).toBe(
      true
    );
    expect(evaluacionDesdeAutodeclaracion({ familias_tratadas: ["accion_clientes"] }).es_completa).toBe(false);
    expect(evaluacionDesdeAutodeclaracion(null).es_completa).toBe(false);
  });

  it("familias_faltantes lista solo lo no tratado", () => {
    const r = evaluacionDesdeAutodeclaracion({ familias_tratadas: ["accion_clientes"] });
    expect(r.familias_faltantes).toHaveLength(1);
    expect(r.tiene_accion_clientes).toBe(true);
    expect(r.tiene_viabilidad_economica).toBe(false);
  });
});

describe("corregirCoherenciaCobertura: 3a reincidencia del bug etiqueta/contenido (Motor v2.2)", () => {
  it("si la seccion economica esta presente en el cuerpo y hay material economico, corrige tiene_viabilidad_economica aunque el redactor haya autodeclarado lo contrario", () => {
    const cuerpo = `# Plan\n\n## ${SECCION_ECONOMICA_TITULO}\n\nTu margen es de $17 por pieza.`;
    const evaluacionMala = {
      es_completa: false,
      tiene_accion_clientes: true,
      tiene_viabilidad_economica: false,
      familias_faltantes: ["si tu idea puede sostenerse economicamente (costos, precios, punto de equilibrio)"],
    };
    const eventos: Record<string, unknown>[] = [];
    const corregida = corregirCoherenciaCobertura(evaluacionMala, cuerpo, true, (e) => eventos.push(e));
    expect(corregida.tiene_viabilidad_economica).toBe(true);
    expect(corregida.es_completa).toBe(true);
    expect(corregida.familias_faltantes).toHaveLength(0);
    expect(eventos).toHaveLength(1);
    expect(eventos[0].tipo).toBe("coherencia_cobertura_corregida");
  });

  it("no corrige si no hay material economico real (evita falsos positivos)", () => {
    const cuerpo = `# Plan\n\n## ${SECCION_ECONOMICA_TITULO}\n\nSeccion vacia de relleno.`;
    const evaluacion = {
      es_completa: false,
      tiene_accion_clientes: true,
      tiene_viabilidad_economica: false,
      familias_faltantes: ["algo"],
    };
    const corregida = corregirCoherenciaCobertura(evaluacion, cuerpo, false, undefined);
    expect(corregida).toEqual(evaluacion);
  });

  it("no corrige si la seccion no esta presente en el cuerpo", () => {
    const cuerpo = "# Plan\n\nSin seccion economica.";
    const evaluacion = {
      es_completa: false,
      tiene_accion_clientes: true,
      tiene_viabilidad_economica: false,
      familias_faltantes: ["algo"],
    };
    const corregida = corregirCoherenciaCobertura(evaluacion, cuerpo, true, undefined);
    expect(corregida).toEqual(evaluacion);
  });
});

describe("ensamblarOffline / extraerTitulo", () => {
  const material: MaterialNodo[] = [
    { concepto: "Fundamentos", pasos: ["paso uno", "paso dos"], entregable: "un documento", es_viabilidad_economica: false },
  ];

  it("arma un markdown con etapas y pasos numerados", () => {
    const md = ensamblarOffline(material, "perfil x", "mi idea original");
    expect(md).toContain("# Tu plan de accion");
    expect(md).toContain("Punto de partida: mi idea original");
    expect(md).toContain("## Etapa 1: Fundamentos");
    expect(md).toContain("1.1 paso uno");
    expect(md).toContain("Punto de control: un documento");
  });

  it("extraerTitulo toma la primera linea que empieza con '# '", () => {
    expect(extraerTitulo("_Plan completo_\n\n# Mi Plan Real\n\nresto")).toBe("Mi Plan Real");
    expect(extraerTitulo("sin ningun encabezado")).toBeNull();
  });
});

describe("prepararPlan + finalizarPlan: extremo a extremo con un texto de modelo simulado", () => {
  it("con autodeclaracion completa, etiqueta 'Plan completo' y sin seccion de faltantes", () => {
    const ruta = ["design_thinking_fundamentos"];
    const prep = prepararPlan(ruta, graph, families, "mi idea", "perfil", null, false, null);
    const rawModelo =
      `# Mi Plan\n\n## ${SECCION_ECONOMICA_TITULO}\n\nTexto economico real.\n\n` +
      '===JSON===\n{"familias_tratadas": ["accion_clientes", "viabilidad_economica"], "secciones": ["Intro"]}';

    const resultado = finalizarPlan(rawModelo, prep, ruta, families, "mi idea");
    expect(resultado.evaluacionCobertura.es_completa).toBe(true);
    expect(resultado.markdown).toContain("_Plan completo_");
    expect(resultado.markdown).not.toContain("Lo que este plan aun no cubre");
    expect(resultado.markdown).toContain("# Mi Plan");
  });

  it("con autodeclaracion incompleta, etiqueta 'Plan inicial' y lista lo que falta", () => {
    const ruta = ["design_thinking_fundamentos"];
    const prep = prepararPlan(ruta, graph, families, "mi idea", "perfil", null, false, null);
    const rawModelo = `# Mi Plan\n\nSolo cubre validacion.\n\n` + '===JSON===\n{"familias_tratadas": ["accion_clientes"]}';

    const resultado = finalizarPlan(rawModelo, prep, ruta, families, "mi idea");
    expect(resultado.evaluacionCobertura.es_completa).toBe(false);
    expect(resultado.markdown).toContain("_Plan inicial_");
    expect(resultado.markdown).toContain("Lo que este plan aun no cubre");
  });

  it("rawTextoModelo=null usa el respaldo offline con el material principal", () => {
    const ruta = ["design_thinking_fundamentos"];
    const prep = prepararPlan(ruta, graph, families, "mi idea", "perfil", null, false, null);
    const resultado = finalizarPlan(null, prep, ruta, families, "mi idea");
    expect(resultado.markdown).toContain("# Tu plan de accion");
  });
});

describe("comprimirEstadoVivo", () => {
  function respuestaClaudeTexto(texto: string) {
    return {
      content: [{ type: "text", text: texto }],
      usage: { input_tokens: 50, output_tokens: 10, cache_read_input_tokens: 0, cache_creation_input_tokens: 0 },
    };
  }

  it("usa el texto comprimido por Claude cuando la llamada tiene exito", async () => {
    const create = vi.fn(async () => respuestaClaudeTexto("estado vivo comprimido"));
    const cliente = { messages: { create } };
    const r = await comprimirEstadoVivo(cliente as never, "estado anterior", "perfil nuevo", ["Concepto A"], usoVacio());
    expect(r.estadoVivo).toBe("estado vivo comprimido");
  });

  it("si Claude falla, concatena estado_anterior + perfil_sesion_nueva sin comprimir", async () => {
    const create = vi.fn(async () => {
      throw new Error("fallo de red simulado");
    });
    const cliente = { messages: { create } };
    const r = await comprimirEstadoVivo(cliente as never, "estado anterior", "perfil nuevo", [], usoVacio());
    expect(r.estadoVivo).toBe("estado anterior\nperfil nuevo");
  });

  it("si no hay estado_anterior y Claude falla, devuelve solo perfil_sesion_nueva", async () => {
    const create = vi.fn(async () => {
      throw new Error("fallo de red simulado");
    });
    const cliente = { messages: { create } };
    const r = await comprimirEstadoVivo(cliente as never, null, "perfil nuevo", [], usoVacio());
    expect(r.estadoVivo).toBe("perfil nuevo");
  });
});
